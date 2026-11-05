#!/usr/bin/env python3
"""Render maintenance/README.md from maintenance/consumables.yaml.

Usage: python3 maintenance/render.py [--today YYYY-MM-DD]

Computes the next due date / engine hours for each item from its latest history entry
and interval, and flags overdue or soon-due items. Requires PyYAML.
"""
import argparse
import calendar
import datetime as dt
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
SRC = HERE / "consumables.yaml"
OUT = HERE / "README.md"

SOON_DAYS = 30
SOON_HOURS = 50

SYSTEMS = [
    ("engine", "Pääkone CAT 3126B"),
    ("gearbox", "Vaihteisto Advance 300"),
    ("hydraulics", "Hydrauliikka"),
    ("bow_thruster", "Keulapotkuri Side-Power SH240-U11"),
    ("electrics", "Sähkö"),
    ("hull", "Runko ja potkuriakseli"),
    ("anchor_winch", "Ankkurivinssi"),
    ("heating", "Lämmitys"),
]
ACTIONS = {"replace": "vaihto", "inspect": "tarkistus", "spare": "varaosa"}
UNKNOWN = "**⚠ ei tiedossa**"


def num(x):
    """Format a number with a decimal comma."""
    if isinstance(x, float) and x.is_integer():
        x = int(x)
    return str(x).replace(".", ",")


def to_date(x):
    if x is None:
        return None
    if isinstance(x, dt.date):
        return x
    return dt.date.fromisoformat(str(x))


def add_months(d, months):
    m = d.month - 1 + months
    y, m = d.year + m // 12, m % 12 + 1
    return dt.date(y, m, min(d.day, calendar.monthrange(y, m)[1]))


def interval_text(it):
    parts = []
    if it.get("interval_h"):
        parts.append(f"{num(it['interval_h'])} h")
    if it.get("interval_months"):
        parts.append(f"{num(it['interval_months'])} kk")
    if parts:
        return " tai ".join(parts)
    return "–" if it.get("action") == "spare" else UNKNOWN


def last_text(last):
    if not last:
        return "–"
    bits = [str(to_date(last.get("date")) or "päivä ⚠ ei tiedossa")]
    if last.get("engine_h") is not None:
        bits.append(f"{num(last['engine_h'])} h")
    return ", ".join(bits)


def next_due(it, last, today, hours_now):
    """Return (text, status, sort_key). status: overdue | soon | ok | none."""
    if not last:
        return (it.get("due_note") or "ei kirjattua vaihtoa", "none", None)
    texts, status, key = [], "ok", None
    if it.get("interval_months") and last.get("date"):
        d = add_months(to_date(last["date"]), it["interval_months"])
        texts.append(str(d))
        key = d
        if today >= d:
            status = "overdue"
        elif (d - today).days <= SOON_DAYS:
            status = "soon"
    if it.get("interval_h") and last.get("engine_h") is not None:
        h = last["engine_h"] + it["interval_h"]
        texts.append(f"{num(h)} h")
        if hours_now is not None:
            if hours_now >= h:
                status = "overdue"
            elif h - hours_now <= SOON_HOURS and status != "overdue":
                status = "soon"
    if not texts:
        return (it.get("due_note") or UNKNOWN, "none", None)
    return (" tai ".join(texts), status, key)


ICON = {"overdue": "🔴 ", "soon": "🟡 ", "ok": "✅ ", "none": ""}


def cell(x):
    return "–" if x in (None, "") else str(x).replace("|", "\\|").replace("\n", " ").strip()


def render(data, today):
    eh = data.get("engine_hours") or {}
    hours_now = eh.get("value_h")
    items = data.get("items") or []

    rows_by_sys, due_list = {}, []
    for it in items:
        hist = it.get("history") or []
        last = hist[0] if hist else None
        nxt, status, key = next_due(it, last, today, hours_now)
        it["_next"], it["_status"] = nxt, status
        rows_by_sys.setdefault(it["system"], []).append(it)
        if status in ("overdue", "soon"):
            due_list.append((status != "overdue", key or dt.date.max, it))

    out = []
    w = out.append
    w("# Vegan kulutus- ja vaihto-osat\n")
    w("> **Tämä tiedosto on generoitu** tiedostosta [consumables.yaml](consumables.yaml) komennolla")
    w("> `python3 maintenance/render.py`. Älä muokkaa taulukoita käsin: muuta YAML-tiedostoa ja aja")
    w(f"> komento uudelleen. Päivitetty {today}.\n")
    w("Lista kaikista kuluvista ja määräajoin vaihdettavista osista ja nesteistä järjestelmittäin:")
    w("malli, mitat, määrä, vaihtoväli, edellinen vaihto ja seuraava ajankohta. Tuntemattomat tiedot")
    w("on merkitty **⚠ ei tiedossa**, ja ne täydennetään veneellä tai huolto-ohjeista.\n")
    w("## Näin päivität\n")
    w("Kerro Claudelle, mitä teit, esimerkiksi:\n")
    w('- *"Vaihdoin moottoriöljyn ja suodattimen tänään, tuntimittari 1234 h."*')
    w('- *"Tuntimittari näyttää nyt 1310 h."*')
    w('- *"P1:n hihnat ovat Optibelt SPA 1250."*\n')
    w("Claude kirjaa vaihdon historiaan, laskee seuraavan ajankohdan ja päivittää tämän taulukon.")
    w("Seuraava vaihto lasketaan edellisestä vaihdosta: tunnit tuntimittarin lukemasta ja päivä")
    w("kalenterivälistä, ja kumpi tahansa täyttyy ensin.\n")
    if hours_now is not None:
        w(f"**Tuntimittari:** {num(hours_now)} h ({eh.get('date') or 'päivä ⚠ ei tiedossa'}).\n")
    else:
        w(f"**Tuntimittari:** {UNKNOWN}. Kirjaa lukema, jotta tunteihin sidotut vaihdot voidaan laskea.\n")
    w(f"Merkit: 🔴 myöhässä · 🟡 erääntyy {SOON_DAYS} vuorokauden tai {SOON_HOURS} tunnin sisällä · ✅ ajallaan.\n")

    w("## Seuraavaksi erääntyvät\n")
    if due_list:
        for _, _, it in sorted(due_list, key=lambda t: (t[0], t[1])):
            w(f"- {ICON[it['_status']]}**{cell(it['name'])}** (`{it['id']}`): {it['_next']}")
        w("")
    else:
        w("Ei myöhässä olevia eikä pian erääntyviä kohteita (kirjattujen vaihtojen perusteella).\n")

    for key, title in SYSTEMS:
        rows = rows_by_sys.pop(key, None)
        if not rows:
            continue
        w(f"## {title}\n")
        w("| Kohde | Työ | Tuote / osanumero | Mitat | Määrä | Väli | Edellinen | Seuraava | Lähde |")
        w("|---|---|---|---|---|---|---|---|---|")
        for it in rows:
            prod = cell(it.get("product")) if it.get("product") else ""
            if it.get("part_number"):
                prod = (prod + " " if prod else "") + f"`{it['part_number']}`"
            qty = []
            if it.get("volume_l") is not None:
                qty.append(f"{num(it['volume_l'])} l")
            if it.get("quantity"):
                qty.append(cell(it["quantity"]))
            if it.get("onboard_spares") is not None:
                qty.append(f"varalla {num(it['onboard_spares'])}")
            hist = it.get("history") or []
            w("| " + " | ".join([
                f"**{cell(it['name'])}** <br>`{it['id']}`",
                ACTIONS.get(it.get("action"), cell(it.get("action"))),
                prod or UNKNOWN,
                cell(it.get("size")),
                "; ".join(qty) or "–",
                interval_text(it),
                last_text(hist[0] if hist else None),
                ICON[it["_status"]] + cell(it["_next"]),
                cell(it.get("source")),
            ]) + " |")
        w("")
        notes = [it for it in rows if it.get("notes") or len(it.get("history") or []) > 1]
        if notes:
            w("**Huomiot**\n")
            for it in notes:
                line = f"- `{it['id']}`: {cell(it.get('notes'))}"
                older = (it.get("history") or [])[1:]
                if older:
                    line += " Aiemmat: " + "; ".join(
                        last_text(h) + (f" ({cell(h['note'])})" if h.get("note") else "") for h in older
                    ) + "."
                w(line)
            w("")
    if rows_by_sys:
        raise SystemExit(f"Unknown system(s) in consumables.yaml: {', '.join(rows_by_sys)}")
    return "\n".join(out).rstrip() + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--today", type=dt.date.fromisoformat, default=dt.date.today())
    args = ap.parse_args()
    data = yaml.safe_load(SRC.read_text(encoding="utf-8"))
    OUT.write_text(render(data, args.today), encoding="utf-8")
    print(f"Wrote {OUT.relative_to(HERE.parent)}")


if __name__ == "__main__":
    main()
