"""Generate the data-grounded and synthetic figures used in the sample PDF.

The script intentionally uses only Pillow and NumPy from the bundled runtime.
Official observations are transcribed in `draw_isiolo_profile`; actuarial outputs
are synthetic and reproducible from the fixed seed below.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "figures"
OUT.mkdir(parents=True, exist_ok=True)

NAVY = "#12324A"
BLUE = "#176B87"
TEAL = "#2A9D8F"
GOLD = "#E9A23B"
RED = "#C75146"
INK = "#263238"
MID = "#667681"
LIGHT = "#E8EFF2"
WHITE = "#FFFFFF"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = [
        Path("C:/Windows/Fonts/georgiab.ttf" if bold else "C:/Windows/Fonts/georgia.ttf"),
        Path("C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf"),
    ]
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size=size)
    return ImageFont.load_default()


def header(draw: ImageDraw.ImageDraw, title: str, subtitle: str) -> None:
    draw.text((95, 58), title, fill=NAVY, font=font(39, True))
    draw.text((95, 114), subtitle, fill=MID, font=font(23))
    draw.line((95, 158, 1505, 158), fill=TEAL, width=5)


def draw_evidence_map() -> None:
    img = Image.new("RGB", (1600, 1080), WHITE)
    d = ImageDraw.Draw(img)
    header(
        d,
        "Kenyan evidence geography used in the sample",
        "Reported or studied locations; orientation only, not a hazard boundary or pricing map",
    )

    # Simplified national outline in longitude/latitude. This is an orientation
    # silhouette rather than a cadastral or exposure boundary.
    outline = [
        (33.92, 4.22), (34.45, 4.62), (35.25, 4.60), (36.05, 4.18),
        (36.72, 4.45), (37.70, 4.35), (38.60, 3.72), (39.20, 3.38),
        (40.05, 3.05), (41.90, 3.98), (41.91, -1.65), (41.52, -1.95),
        (40.98, -2.70), (40.56, -3.45), (39.68, -4.67), (37.63, -3.48),
        (36.30, -2.10), (35.65, -1.35), (34.95, -1.05), (34.45, -0.62),
        (34.05, 0.20), (33.92, 1.00), (34.20, 2.30), (33.92, 4.22),
    ]
    left, top, width, height = 155, 205, 885, 755
    lon_min, lon_max, lat_min, lat_max = 33.7, 42.1, -4.9, 5.0

    def xy(lon: float, lat: float) -> tuple[float, float]:
        x = left + (lon - lon_min) / (lon_max - lon_min) * width
        y = top + (lat_max - lat) / (lat_max - lat_min) * height
        return x, y

    poly = [xy(lon, lat) for lon, lat in outline]
    d.polygon(poly, fill="#F2F6F4", outline=NAVY, width=5)
    for lon in range(34, 42):
        x, _ = xy(lon, 0)
        d.line((x, top, x, top + height), fill="#E3E9EC", width=1)
    for lat in range(-4, 5, 2):
        _, y = xy(34, lat)
        d.line((left, y, left + width, y), fill="#E3E9EC", width=1)
    d.polygon(poly, fill="#F2F6F4", outline=NAVY, width=5)

    places = [
        ("Lower Nzoia", 34.12, 0.50, BLUE, "Flood / river basin"),
        ("Isiolo", 37.58, 0.35, GOLD, "Drought bulletin"),
        ("Northern counties", 40.05, 1.75, RED, "Locust invasion"),
        ("Mount Kenya", 37.31, -0.15, TEAL, "Wildfire study"),
        ("West Pokot", 35.11, 1.24, NAVY, "Landslide evidence"),
        ("Mombasa / Tana River", 39.67, -4.04, "#7D5BA6", "Heat study"),
    ]
    label_offsets = {
        "Lower Nzoia": (-176, 18), "Isiolo": (18, 10),
        "Northern counties": (-35, -53), "Mount Kenya": (20, 4),
        "West Pokot": (-162, -38), "Mombasa / Tana River": (-245, 10),
    }
    for name, lon, lat, colour, _ in places:
        x, y = xy(lon, lat)
        d.ellipse((x - 11, y - 11, x + 11, y + 11), fill=colour, outline=WHITE, width=3)
        ox, oy = label_offsets[name]
        d.text((x + ox, y + oy), name, fill=INK, font=font(20, True))

    lx, ly = 1095, 225
    d.text((lx, ly), "Evidence lanes", fill=NAVY, font=font(27, True))
    for idx, (_, _, _, colour, meaning) in enumerate(places):
        y = ly + 58 + idx * 82
        d.rounded_rectangle((lx, y, 1140, y + 45), 8, fill=colour)
        d.text((1160, y + 7), meaning, fill=INK, font=font(21))
    d.rounded_rectangle((1080, 745, 1510, 938), 18, fill="#F7F2E8", outline=GOLD, width=3)
    d.text((1105, 770), "Interpretation boundary", fill=NAVY, font=font(24, True))
    note = [
        "Points locate evidence discussed in",
        "the manuscript. They do not assert",
        "event extent, policy exposure or",
        "comparative risk.",
    ]
    for i, line in enumerate(note):
        d.text((1105, 815 + i * 28), line, fill=INK, font=font(20))
    d.text((95, 1015), "Source: manuscript evidence register. Coordinates are approximate orientation points.", fill=MID, font=font(18))
    img.save(OUT / "kenya_evidence_geography.png", dpi=(200, 200))


def draw_isiolo_profile() -> None:
    img = Image.new("RGB", (1600, 1020), WHITE)
    d = ImageDraw.Draw(img)
    header(
        d,
        "Isiolo drought signal, January 2026",
        "Current indicator as a percentage of the bulletin reference; direction is shown explicitly",
    )
    supportive = [
        ("Rainfall", 3.8 / 12.2 * 100, "3.8 mm / 12.2 mm"),
        ("VCI-3 month", 22.8 / 34.8 * 100, "22.8 / 34.8"),
        ("Milk production", 1.40 / 1.70 * 100, "1.40 L / 1.70 L"),
        ("Food consumption score", 34.5 / 40.3 * 100, "34.5 / 40.3"),
    ]
    adverse = [
        ("Water-source distance", 2.2 / 2.2 * 100, "2.2 km / 2.2 km"),
        ("MUAC at-risk share", 10.5 / 9.2 * 100, "10.5% / 9.2%"),
    ]

    def panel(x0: int, y0: int, w: int, title: str, rows, colour: str, guidance: str):
        d.rounded_rectangle((x0, y0, x0 + w, y0 + 650), 20, fill="#F7F9FA", outline=LIGHT, width=3)
        d.text((x0 + 35, y0 + 28), title, fill=NAVY, font=font(27, True))
        d.text((x0 + 35, y0 + 71), guidance, fill=MID, font=font(19))
        axis0, axis1 = x0 + 240, x0 + w - 45
        for pct in (0, 50, 100, 150):
            x = axis0 + pct / 150 * (axis1 - axis0)
            d.line((x, y0 + 130, x, y0 + 585), fill="#DDE5E8", width=2)
            d.text((x - 15, y0 + 600), str(pct), fill=MID, font=font(17))
        tx = axis0 + 100 / 150 * (axis1 - axis0)
        d.line((tx, y0 + 118, tx, y0 + 585), fill=NAVY, width=4)
        for idx, (name, pct, raw) in enumerate(rows):
            y = y0 + 155 + idx * 102
            d.text((x0 + 35, y - 3), name, fill=INK, font=font(19, True))
            d.text((x0 + 35, y + 27), raw, fill=MID, font=font(16))
            x = axis0 + min(pct, 150) / 150 * (axis1 - axis0)
            d.line((axis0, y + 24, x, y + 24), fill=colour, width=18)
            d.ellipse((x - 10, y + 14, x + 10, y + 34), fill=colour)
            d.text((x + 14, y + 7), f"{pct:.0f}%", fill=INK, font=font(18, True))

    panel(80, 205, 930, "Availability / wellbeing indicators", supportive, TEAL, "Below 100% is less favourable")
    panel(1050, 205, 470, "Stress indicators", adverse, RED, "Above 100% is less favourable")
    d.rounded_rectangle((1050, 865, 470 + 1050, 946), 14, fill="#FFF6E5", outline=GOLD, width=2)
    d.text((1070, 881), "This is a signal profile, not an insured-loss estimate.", fill=INK, font=font(18, True))
    d.text((80, 970), "Source: NDMA Isiolo County Drought Early Warning Bulletin, January 2026.", fill=MID, font=font(18))
    img.save(OUT / "isiolo_drought_signal_jan_2026.png", dpi=(200, 200))


def simulate_actuarial_example() -> dict:
    rng = np.random.default_rng(20260828)
    segments = [
        {"name": "Dwellings", "count": 120, "value": 4.0, "affected": 0.60, "mdr": 0.18, "ded": 0.10, "limit": 2.50, "share": 1.00},
        {"name": "SMEs", "count": 80, "value": 8.0, "affected": 0.45, "mdr": 0.22, "ded": 0.25, "limit": 5.00, "share": 1.00},
        {"name": "Crop plots", "count": 300, "value": 0.30, "affected": 0.70, "mdr": 0.35, "ded": 0.03, "limit": 0.27, "share": 0.80},
        {"name": "Vehicles", "count": 50, "value": 2.0, "affected": 0.30, "mdr": 0.28, "ded": 0.10, "limit": 1.50, "share": 1.00},
    ]
    rows = []
    for s in segments:
        affected = round(s["count"] * s["affected"])
        gu = affected * s["value"] * s["mdr"]
        insured_each = s["share"] * min(max(s["value"] * s["mdr"] - s["ded"], 0), s["limit"])
        insured = affected * insured_each
        rows.append({**s, "affected_count": affected, "ground_up_m": gu, "insured_m": insured})

    n = 60000
    event_losses = np.zeros(n)
    for s in segments:
        # Beta distributions are parameterised to reproduce the stated means,
        # with broad uncertainty appropriate only for a demonstrator.
        a_f, b_f = s["affected"] * 35, (1 - s["affected"]) * 35
        a_m, b_m = s["mdr"] * 45, (1 - s["mdr"]) * 45
        affected_counts = rng.binomial(s["count"], rng.beta(a_f, b_f, n))
        mdr = rng.beta(a_m, b_m, n)
        insured_each = s["share"] * np.minimum(np.maximum(s["value"] * mdr - s["ded"], 0), s["limit"])
        event_losses += affected_counts * insured_each

    years = 100000
    counts = rng.poisson(0.65, years)
    annual = np.zeros(years)
    maximum = np.zeros(years)
    pool = rng.choice(event_losses, size=int(counts.sum()), replace=True)
    cursor = 0
    for i, count in enumerate(counts):
        if count:
            vals = pool[cursor: cursor + count]
            annual[i] = vals.sum()
            maximum[i] = vals.max()
            cursor += count

    # The 2-year aggregate quantile is zero because the Poisson event rate below
    # gives a probability of no annual event slightly above 50%. Starting at
    # three years keeps the visible curve informative without hiding that fact.
    return_periods = [3, 5, 10, 20, 50, 100, 200]
    aep = [float(np.quantile(annual, 1 - 1 / r)) for r in return_periods]
    oep = [float(np.quantile(maximum, 1 - 1 / r)) for r in return_periods]
    central = float(sum(row["insured_m"] for row in rows))
    recovery = min(max(central - 75.0, 0.0), 100.0)
    result = {
        "units": "KES million",
        "seed": 20260828,
        "segments": rows,
        "central_ground_up_m": float(sum(row["ground_up_m"] for row in rows)),
        "central_insured_m": central,
        "central_xol_recovery_m": recovery,
        "central_net_retained_m": central - recovery,
        "event_loss_quantiles_m": {str(q): float(np.quantile(event_losses, q)) for q in (0.1, 0.5, 0.9, 0.95)},
        "annual_average_loss_m": float(annual.mean()),
        "return_periods": return_periods,
        "aep_m": aep,
        "oep_m": oep,
    }
    return result


def draw_ep_curves(result: dict) -> None:
    img = Image.new("RGB", (1600, 1020), WHITE)
    d = ImageDraw.Draw(img)
    header(
        d,
        "Synthetic flood portfolio exceedance curves",
        "Reproducible demonstration - not a tariff, reserve, capital figure or Kenya market estimate",
    )
    x0, y0, x1, y1 = 170, 220, 1490, 850
    d.line((x0, y1, x1, y1), fill=NAVY, width=4)
    d.line((x0, y0, x0, y1), fill=NAVY, width=4)
    rps = result["return_periods"]
    series = [("AEP: annual aggregate", result["aep_m"], BLUE), ("OEP: largest event", result["oep_m"], GOLD)]
    ymax = math.ceil(max(max(result["aep_m"]), max(result["oep_m"])) / 50) * 50
    for val in range(0, ymax + 1, 50):
        y = y1 - val / ymax * (y1 - y0)
        d.line((x0, y, x1, y), fill="#E1E8EB", width=2)
        d.text((82, y - 12), str(val), fill=MID, font=font(18))
    log_min, log_max = math.log10(min(rps)), math.log10(max(rps))
    for rp in rps:
        x = x0 + (math.log10(rp) - log_min) / (log_max - log_min) * (x1 - x0)
        d.line((x, y0, x, y1), fill="#EEF2F3", width=1)
        d.text((x - 17, y1 + 18), str(rp), fill=MID, font=font(18))
    for label, values, colour in series:
        points = []
        for rp, val in zip(rps, values):
            x = x0 + (math.log10(rp) - log_min) / (log_max - log_min) * (x1 - x0)
            y = y1 - val / ymax * (y1 - y0)
            points.append((x, y))
        d.line(points, fill=colour, width=8, joint="curve")
        for x, y in points:
            d.ellipse((x - 9, y - 9, x + 9, y + 9), fill=colour, outline=WHITE, width=3)
    d.text((575, 920), "Return period (years, logarithmic axis)", fill=INK, font=font(23, True))
    d.text((170, 178), "Loss (KES m)", fill=INK, font=font(21, True))
    for idx, (label, _, colour) in enumerate(series):
        xx = 980 + idx * 0
        yy = 188 + idx * 37
        d.line((xx, yy, xx + 58, yy), fill=colour, width=8)
        d.text((xx + 75, yy - 14), label, fill=INK, font=font(20))
    d.text((170, 968), f"100,000 synthetic years; Poisson mean 0.65 events/year; fixed seed {result['seed']}.", fill=MID, font=font(18))
    img.save(OUT / "synthetic_flood_ep_curves.png", dpi=(200, 200))


if __name__ == "__main__":
    draw_evidence_map()
    draw_isiolo_profile()
    results = simulate_actuarial_example()
    draw_ep_curves(results)
    (OUT / "synthetic_flood_portfolio_results.json").write_text(
        json.dumps(results, indent=2), encoding="utf-8"
    )
    print(json.dumps(results, indent=2))
