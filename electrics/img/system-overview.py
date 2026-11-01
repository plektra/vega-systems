# Vegan sähköjärjestelmän periaatekuva (electrics/img/system-overview.svg).
# Aja: python3 electrics/img/system-overview.py electrics/img/system-overview.svg
# Koodi MIT, kuva CC BY 4.0. Päivitä tätä ja aja uudelleen, kun suunnitelma muuttuu.
import sys

W, H = 1720, 1200
out = []
a = out.append

RED = "#d7261e"
BLK = "#222222"
BLUE = "#1d5fae"
CANC = "#1d5fae"
ORG = "#e07b00"
ACC = "#7a4a1d"
GREY = "#f2f4f7"


def rect(x, y, w, h, fill="#fff", stroke="#555", sw=1.5, rx=6, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    a(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>')


def text(x, y, s, size=13, fill="#222", weight="normal", anchor="start"):
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    a(f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" font-weight="{weight}" text-anchor="{anchor}">{s}</text>')


def lines(x, y, rows, size=12, fill="#222", lh=16, anchor="start", first_bold=False):
    for i, r in enumerate(rows):
        text(x, y + i * lh, r, size, fill, "bold" if (first_bold and i == 0) else "normal", anchor)


def path(pts, color, sw=5, dash=None, halo=False):
    d = "M " + " L ".join(f"{px} {py}" for px, py in pts)
    if halo:
        a(f'<path d="{d}" fill="none" stroke="#fff" stroke-width="{sw + 8}" stroke-linejoin="round"/>')
    ds = f' stroke-dasharray="{dash}"' if dash else ""
    a(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linejoin="round" stroke-linecap="round"{ds}/>')


def device(x, y, w, h, title, rows, color=BLUE):
    rect(x, y, w, h, fill=color, stroke="#0d3b73" if color == BLUE else "#555", sw=1.5, rx=8)
    fg = "#fff" if color in (BLUE, "#3a3f47") else "#222"
    text(x + 12, y + 24, title, 15, fg, "bold")
    lines(x + 12, y + 44, rows, 12, fg)


def fuse_v(x, y, label, color=RED, side="right"):
    # vertical fuse centred on (x, y)
    rect(x - 8, y - 18, 16, 36, fill="#fff", stroke=color, sw=2, rx=2)
    a(f'<line x1="{x}" y1="{y - 18}" x2="{x}" y2="{y + 18}" stroke="{color}" stroke-width="1.2"/>')
    if side == "right":
        text(x + 14, y + 4, label, 11, "#333")
    else:
        text(x - 14, y + 4, label, 11, "#333", anchor="end")


def fuse_h(x, y, label):
    rect(x - 18, y - 8, 36, 16, fill="#fff", stroke=RED, sw=2, rx=2)
    a(f'<line x1="{x - 18}" y1="{y}" x2="{x + 18}" y2="{y}" stroke="{RED}" stroke-width="1.2"/>')
    text(x, y - 14, label, 11, "#333", anchor="middle")


def switch_v(x, y, label, side="right", color=RED):
    # break in vertical line from y-14 to y+14 with lever
    a(f'<rect x="{x - 6}" y="{y - 16}" width="12" height="32" fill="#fff"/>')
    a(f'<circle cx="{x}" cy="{y + 14}" r="3.5" fill="#fff" stroke="{color}" stroke-width="2"/>')
    a(f'<circle cx="{x}" cy="{y - 14}" r="3.5" fill="#fff" stroke="{color}" stroke-width="2"/>')
    a(f'<line x1="{x}" y1="{y + 11}" x2="{x + 13}" y2="{y - 12}" stroke="{color}" stroke-width="2.5"/>')
    if side == "right":
        text(x + 18, y + 4, label, 11, "#333")
    else:
        text(x - 12, y + 4, label, 11, "#333", anchor="end")


def ground(x, y, label):
    a(f'<line x1="{x}" y1="{y}" x2="{x}" y2="{y + 12}" stroke="{BLK}" stroke-width="2"/>')
    for i, wdt in enumerate((22, 14, 6)):
        yy = y + 12 + i * 5
        a(f'<line x1="{x - wdt / 2}" y1="{yy}" x2="{x + wdt / 2}" y2="{yy}" stroke="{BLK}" stroke-width="2"/>')
    lines(x + 18, y + 18, label, 11, "#333", 14)


a(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="Helvetica, Arial, sans-serif">')
a(f'<rect x="0" y="0" width="{W}" height="{H}" fill="#ffffff"/>')

# Title
text(40, 44, "Vega – sähköjärjestelmän periaatekuva (24 V DC ja 230 V AC)", 22, "#111", "bold")
text(40, 68, "Periaatekuva 2026-11-01, ei asennuskuva. Sulakkeet ja kaapelit: electrics/design/circuit-list.md. "
     "Tarkastetaan pätevällä sähköasentajalla ennen rakentamista.", 12, "#555")

# ---------------- AC side ----------------
rect(40, 110, 180, 64, fill=GREY, stroke="#777")
lines(52, 134, ["Maasähkö", "230 V, kotilaituri 15 A"], 12, first_bold=True)
rect(40, 196, 180, 82, fill=GREY, stroke="#777")
lines(52, 220, ["Timco SS2200i", "1,8 kW, varalataus", "vain avokannella"], 12, first_bold=True)
# AC lines to inlet and transformer
path([(220, 142), (250, 142), (250, 180), (290, 180)], ACC, 4)
path([(220, 237), (250, 237), (250, 180)], ACC, 4, dash="10 6")
a(f'<circle cx="250" cy="180" r="5" fill="{ACC}"/>')
text(290, 250, "aggregaatti kytketään maasähköpistokkeeseen", 10, "#555")
device(290, 130, 170, 100, "Erotusmuuntaja", ["Airlink WM5002", "230/230 V, 5 kVA", "(olemassa)"], color="#ffffff")
path([(460, 180), (520, 180)], ACC, 4)
text(468, 172, "AC in", 11, "#555")
device(520, 110, 230, 180, "MultiPlus-II", ["24/5000/120-50, 230 V", "invertteri 4 kW", "laturi 120 A", "PowerAssist", "tulovirta: laituri 14 A,", "aggregaatti noin 7 A"])
path([(750, 180), (820, 180)], ACC, 4)
text(756, 172, "AC out", 11, "#555")
rect(820, 110, 270, 200, fill="#fff", stroke="#777")
lines(832, 134, ["230 V -keskus (AC)", "vikavirtasuoja 30 mA", "AC-01 Sähkökiuas 2,3 kW", "AC-02 Jääkaappi", "AC-03 Mikro- ja sähköuuni",
                 "AC-04 Keittiön pistorasiat", "AC-05 Muut pistorasiat", "AC-06 Ilmanvaihto, liesituuletin", "AC-07 Lämmityksen poltin",
                 "AC-08 Vedenlämmitin (vain maasähkö)"], 12, lh=17, first_bold=True)
device(1160, 110, 200, 90, "Cerbo GX", ["DVCC: BMS ohjaa latausta", "ja purkua"])
rect(1160, 222, 200, 56, fill=GREY, stroke="#777")
lines(1172, 245, ["Signal K / VRM", "valvonta ja hälytykset"], 12, first_bold=True)
path([(1260, 200), (1260, 222)], CANC, 2.5, dash="7 5")
# VE.Bus MultiPlus <-> Cerbo
path([(640, 110), (640, 92), (1260, 92), (1260, 110)], CANC, 2.5, dash="7 5")
text(950, 86, "VE.Bus", 11, CANC, anchor="middle")

# ---------------- DC busbars ----------------
PLUS_Y, MINUS_Y = 470, 545
# MultiPlus DC connections (drawn before bars, minus crosses plus bar)
path([(585, 290), (585, PLUS_Y)], RED, 6)
fuse_v(585, 380, "PJ-01  ≈ 180 A", side="left")
path([(690, 290), (690, MINUS_Y)], BLK, 6, halo=True)

rect(330, PLUS_Y - 8, 990, 16, fill=RED, stroke="#8a1410", rx=3)
text(340, PLUS_Y - 14, "Pääjakelu PJ, plus-kisko (+)", 12, RED, "bold")
rect(330, MINUS_Y - 8, 990, 16, fill=BLK, stroke="#000", rx=3)
text(1130, MINUS_Y + 26, "Miinuskisko (−)", 12, BLK, "bold")
path([(690, 290), (690, PLUS_Y - 12)], BLK, 6)  # redraw above bar part

# ---------------- house batteries ----------------
BY = 790
for i, bx in enumerate((440, 740)):
    rect(bx, BY, 250, 170, fill="#e8f1fb", stroke=BLUE, sw=2, rx=8)
    lines(bx + 14, BY + 36, [f"Käyttöakku {i + 1}", "8 × EVE MB31, 8S", "25,6 V, 314 Ah, ≈ 8 kWh"], 13, first_bold=True)
    rect(bx + 14, BY + 100, 222, 52, fill=BLUE, stroke="#0d3b73", rx=5)
    lines(bx + 24, BY + 121, ["JK-PB2A16S20P (BMS)", "CAN · 2 kuivakosketinta"], 12, "#fff")
    # terminals
    px, mx = bx + 50, bx + 200
    rect(px - 9, BY - 10, 18, 12, fill=RED, stroke="#8a1410", rx=2)
    rect(mx - 9, BY - 10, 18, 12, fill=BLK, stroke="#000", rx=2)
    # minus up to minus bar
    path([(mx, BY - 10), (mx, MINUS_Y + 8)], BLK, 6)
    # plus up through Class T and switch to plus bar (crosses minus bar)
    path([(px, BY - 10), (px, PLUS_Y + 8)], RED, 6, halo=True)
    path([(px, MINUS_Y - 14), (px, PLUS_Y + 8)], RED, 6)
    fuse_v(px, 735, "Class T")
    switch_v(px, 655, "pääkytkin")
    text(bx + 125, BY + 190, "", 11)

# third battery (option)
rect(1040, BY, 250, 170, fill="#fff", stroke="#999", sw=1.5, rx=8, dash="8 6")
lines(1054, BY + 36, ["Käyttöakku 3 (optio)", "tila ja lähtö PJ-07 varataan", "noin 24 kWh yhteensä"], 13, "#777", first_bold=True)
path([(1090, BY - 10), (1090, PLUS_Y + 8)], "#d99", 4, dash="8 6", halo=True)
text(1082, 700, "PJ-07", 11, "#777", anchor="end")

# BMS-CAN from Cerbo to both BMS
path([(1160, 180), (1110, 180), (1110, 770), (965, 770), (965, BY + 100)], CANC, 2.5, dash="7 5")
path([(665, 770), (965, 770)], CANC, 2.5, dash="7 5")
path([(665, 770), (665, BY + 100)], CANC, 2.5, dash="7 5")
text(1030, 764, "BMS-CAN", 11, CANC, anchor="middle")

# ---------------- engine & start batteries (left) ----------------
rect(40, 330, 270, 210, fill=GREY, stroke="#777", rx=8)
text(52, 352, "Pääkone CAT 3126B", 14, "#222", "bold")
rect(52, 366, 120, 46, fill="#fff", stroke="#777")
lines(62, 386, ["Laturi 65 A", "(olemassa)"], 11)
rect(182, 366, 116, 46, fill="#fff", stroke="#777")
lines(192, 386, ["Käynnistin,", "ohjausyksikkö"], 11)
rect(52, 430, 120, 56, fill="#3a3f47", stroke="#222", rx=5)
lines(62, 450, ["Alpha Pro III", "säädin"], 11, "#fff")
rect(182, 430, 116, 56, fill="#fff", stroke="#777")
lines(192, 450, ["Toinen laturi", "24 V, 150–175 A", "(tuleva)"], 11)
text(52, 512, "Kenttäohjaus säätimeltä laturille", 10, "#555")
path([(172, 456), (182, 456)], "#555", 2)
# second alternator to PJ via PJ-03
path([(298, 470), (330, 470)], RED, 6)
text(296, 500, "PJ-03 + APD24", 11, "#333")

# P3
rect(150, 600, 160, 66, fill="#fff", stroke="#777", rx=6)
lines(160, 622, ["P3 ohjauksen", "varapumppu 2,5 kW", "≈ 100 A (keskim. 40–50 A)"], 11)

# start batteries
rect(40, 790, 250, 170, fill="#f7efe6", stroke="#9a6b34", sw=2, rx=8)
lines(54, 826, ["Käynnistysakut", "2 × 12 V lyijy, 24 V", "(tyyppi ⚠ tarkistettava)"], 13, first_bold=True)
rect(70, 780, 18, 12, fill=RED, stroke="#8a1410", rx=2)
rect(240, 780, 18, 12, fill=BLK, stroke="#000", rx=2)
# start + up to engine (KA-01/02)
path([(79, 780), (79, 540)], RED, 6)
fuse_v(79, 730, "KA-02", side="left")
text(88, 580, "KA-01", 11, "#333")
# start + to P3 (KA-05)
path([(79, 700), (130, 700), (130, 633), (150, 633)], RED, 5)
fuse_v(130, 670, "KA-05", side="left")
# start minus to minus bar
path([(249, 780), (249, 720), (345, 720), (345, MINUS_Y + 8)], BLK, 5)
ground(345, 600, [])
lines(338, 682, ["Yksi yhteys-", "piste runkoon", "⚠ mitataan"], 11, "#333", 14, anchor="end")
# emergency parallel switch KA-04: start + -> plus bar
path([(130, 700), (130, 760), (420, 760), (420, PLUS_Y + 8)], RED, 4, halo=True)
path([(420, MINUS_Y - 14), (420, PLUS_Y + 8)], RED, 4)
switch_v(420, 705, "", side="right")
lines(432, 700, ["KA-04", "hätäkytkin", "(auki)"], 11, "#333", 14)

# KA-03 to Argo FET 2 (route along bottom)
path([(165, 960), (165, 1020), (1440, 1020), (1440, 735)], RED, 4)
fuse_v(165, 998, "KA-03", side="right")

# ---------------- sub panels (right) ----------------
rect(1430, 300, 260, 104, fill="#fff", stroke="#777")
lines(1442, 322, ["KS komentosilta", "KS-01…14, ESP32-PDM", "valot, hakuvalo (rele),", "navigointi, pyyhkijät"], 12, first_bold=True)
rect(1430, 420, 260, 104, fill="#fff", stroke="#777")
lines(1442, 442, ["KH konehuone", "KH-01…11, ESP32-PDM", "pumput, WC, valaistus", "KH-20…22 jatkuvat (Signal K)"], 12, first_bold=True)
rect(1500, 600, 190, 210, fill="#fff5f5", stroke=RED, sw=2)
lines(1512, 622, ["TK tärkeät kuormat", "ei PDM:ää, ei pääkytkintä", "TK-01…03 pilssipumput", "TK-04 kulkuvalot", "TK-05 ankkurivalo",
                  "TK-06 VHF", "TK-07 ylävesihälytin", "TK-08 kaasuhälytin (ehd.)"], 12, lh=18, first_bold=True)

# PJ-04 to KS
path([(1290, PLUS_Y), (1290, 352), (1430, 352)], RED, 5)
fuse_v(1290, 410, "PJ-04 60 A", side="left")
# PJ-05 to KH
path([(1320, PLUS_Y), (1395, PLUS_Y), (1395, 472), (1430, 472)], RED, 5)
fuse_h(1360, PLUS_Y, "PJ-05 40 A")
# PJ-06 via Argo FET 1 to TK
path([(1250, PLUS_Y), (1250, 650), (1395, 650)], RED, 4, halo=True)
path([(1250, MINUS_Y - 14), (1250, 650)], RED, 4)
fuse_v(1250, 610, "PJ-06 50 A", side="left")
path([(1320, 650), (1395, 650)], RED, 4, halo=True)
rect(1395, 632, 90, 40, fill=BLUE, stroke="#0d3b73", rx=5)
lines(1403, 650, ["Argo FET", "100-2"], 10, "#fff", lh=13)
path([(1485, 652), (1500, 652)], RED, 4)
rect(1395, 715, 90, 40, fill=BLUE, stroke="#0d3b73", rx=5)
lines(1403, 733, ["Argo FET", "100-2"], 10, "#fff", lh=13)
path([(1440, 755), (1440, 735)], RED, 4)
path([(1485, 735), (1500, 735)], RED, 4)
# minus to sub panels
path([(1320, MINUS_Y), (1415, MINUS_Y), (1415, 395), (1430, 395)], BLK, 3)
path([(1415, 515), (1430, 515)], BLK, 3)
path([(1320, MINUS_Y), (1335, MINUS_Y), (1335, 795), (1500, 795)], BLK, 3)

# dry contacts to Alpha Pro III Reg on
path([(615, BY + 152), (615, 975), (915, 975), (915, BY + 152)], ORG, 2.5, dash="4 4")
path([(615, 975), (25, 975), (25, 458), (52, 458)], ORG, 2.5, dash="4 4")
text(620, 991, "Kuivakoskettimet sarjassa → Alpha Pro III Reg on (vika tai suojaus pysäyttää laturin)", 11, ORG)

# ---------------- legend ----------------
LX, LY = 40, 1060
rect(LX, LY, 1650, 110, fill="#fafafa", stroke="#bbb", rx=6)
text(LX + 14, LY + 24, "Merkinnät", 13, "#222", "bold")
items = [
    (RED, 6, None, "+ DC (24 V)"),
    (BLK, 6, None, "− DC"),
    (ACC, 4, None, "230 V AC"),
    (CANC, 2.5, "7 5", "VE.Bus / CAN-väylä"),
    (ORG, 2.5, "4 4", "Ohjausjohdin (kuivakosketin)"),
]
for i, (c, sw, ds, lab) in enumerate(items):
    x0 = LX + 20 + i * 250
    y0 = LY + 52
    path([(x0, y0), (x0 + 50, y0)], c, sw, dash=ds)
    text(x0 + 60, y0 + 4, lab, 12)
fuse_v(LX + 30, LY + 88, "sulake (tunnus ja koko piirilistassa)")
switch_v(LX + 330, LY + 88, "kytkin")
lines(LX + 470, LY + 84, ["Sininen laatikko = Victron / JK -laite. Katkoviiva = optio tai tuleva. BMS-CAN: Victron 500 kbit/s, JK:n asetus tarkistettava.",
                          "Tunnukset (PJ, KA, TK, KS, KH, AC) vastaavat piirilistaa."], 12, "#333", 16)

a("</svg>")
open(sys.argv[1], "w", encoding="utf-8").write("\n".join(out))
