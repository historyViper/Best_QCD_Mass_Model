#!/usr/bin/env python3
"""
geometric_boundary_projection_standalone.py

Standalone baryon runner with:
- embedded 24-baryon PDG-style ground-state list
- no external imports beyond Python stdlib
- no dependency on another local Python file
- dual-angle vortex correction with fitted defaults preserved
"""

import math
import json

ALPHA_IR = 0.848809
LAMBDA_QCD = 217.0
GEO_BOUNDARY = math.sin(math.radians(12.0)) ** 2
LAMBDA_UNIV = GEO_BOUNDARY / ALPHA_IR

A_DEFAULT = 20.0
B_DEFAULT = 2.0
PHI_GEOM_DEFAULT = 64.5
PHI_INT_DEFAULT = 55.0

LANES = {"up": 19, "down": 11, "strange": 7, "charm": 23, "bottom": 13, "top": 17}
LANE_SET = [1, 7, 11, 13, 17, 19, 23, 29]
ANGLES = {r: 720.0 * r / 30.0 for r in LANE_SET}

INVERSES = {}
for r in LANE_SET:
    for s in LANE_SET:
        if (r * s) % 30 == 1:
            INVERSES[r] = s

CONSTITUENT = {
    "up": 336.0, "down": 340.0, "strange": 486.0,
    "charm": 1550.0, "bottom": 4730.0, "top": 173400.0,
}

ALPHA_BARYON = ALPHA_IR * (2.0 / 3.0)
GEO_TWO_7 = math.sqrt((math.sin(math.radians(ANGLES[7] / 2.0)) ** 2) * (math.sin(math.radians(ANGLES[INVERSES[7]] / 2.0)) ** 2))
C_HYP = ALPHA_BARYON * LAMBDA_QCD * GEO_TWO_7

BARYONS = [
    ("proton",    ["up","up","down"],                0.5,  938.272),
    ("neutron",   ["up","down","down"],              0.5,  939.565),
    ("Lambda0",   ["up","down","strange"],           0.5, 1115.683),
    ("Sigma+",    ["up","up","strange"],             0.5, 1189.370),
    ("Sigma0",    ["up","down","strange"],           0.5, 1192.642),
    ("Sigma-",    ["down","down","strange"],         0.5, 1197.449),
    ("Xi0",       ["up","strange","strange"],        0.5, 1314.860),
    ("Xi-",       ["down","strange","strange"],      0.5, 1321.710),
    ("Omega-",    ["strange","strange","strange"],   0.5, 1672.450),

    ("Lambda_c",  ["up","down","charm"],             0.5, 2286.460),
    ("Sigma_c++", ["up","up","charm"],               0.5, 2453.970),
    ("Sigma_c+",  ["up","down","charm"],             0.5, 2452.900),
    ("Sigma_c0",  ["down","down","charm"],           0.5, 2453.750),
    ("Xi_c+",     ["up","strange","charm"],          0.5, 2467.930),
    ("Xi_c0",     ["down","strange","charm"],        0.5, 2470.850),
    ("Omega_c",   ["strange","strange","charm"],     0.5, 2695.200),
    ("Xi_cc++",   ["up","charm","charm"],            0.5, 3621.400),
    ("Xi_cc+",    ["down","charm","charm"],          0.5, 3619.970),

    ("Lambda_b",  ["up","down","bottom"],            0.5, 5619.600),
    ("Sigma_b+",  ["up","up","bottom"],              0.5, 5810.560),
    ("Sigma_b-",  ["down","down","bottom"],          0.5, 5815.640),
    ("Xi_b0",     ["up","strange","bottom"],         0.5, 5791.900),
    ("Xi_b-",     ["down","strange","bottom"],       0.5, 5797.000),
    ("Omega_b",   ["strange","strange","bottom"],    0.5, 6046.100),
]

def geo(theta_deg: float) -> float:
    return max(math.sin(math.radians(theta_deg) / 2.0) ** 2, 1e-10)

def geo_two(r: int) -> float:
    return math.sqrt(geo(ANGLES[r]) * geo(ANGLES[INVERSES[r]]))

def is_self_inverse(r: int) -> bool:
    return INVERSES.get(r, r) == r

def sheet(r: int) -> str:
    if r not in ANGLES:
        return "boundary"
    return "second" if ANGLES[r] > 360 else "first"

def baryon_residue(quarks):
    r = 1
    for q in quarks:
        r = (r * LANES[q]) % 30
    return r

def predict_base(quarks, J):
    r = baryon_residue(quarks)
    sum_c = sum(CONSTITUENT[q] for q in quarks)

    if r not in ANGLES:
        delta_geo = -ALPHA_BARYON * LAMBDA_QCD * geo(24.0)
    elif is_self_inverse(r):
        delta_geo = -ALPHA_BARYON * LAMBDA_QCD * geo(ANGLES[r])
    elif sheet(r) == "second":
        delta_geo = -ALPHA_BARYON * LAMBDA_QCD * geo_two(r)
    else:
        delta_geo = +ALPHA_BARYON * LAMBDA_QCD * geo_two(r)

    S = -1.0 if J == 0.5 else 3.0
    delta_spin = C_HYP * S
    return sum_c + delta_geo + delta_spin, delta_geo, delta_spin, r

def skew_angle(quarks):
    angles = sorted([ANGLES[LANES[q]] for q in quarks])
    gaps = []
    n = len(angles)
    for i in range(n):
        for j in range(i + 1, n):
            gaps.append(abs(angles[j] - angles[i]))
    gaps.append(720 - angles[-1] + angles[0])
    deviations = [abs(g - 240) for g in gaps]
    return sum(deviations) / len(deviations)

def tri_wave(theta_deg, phi):
    x = (theta_deg / phi) % 2.0
    return 1.0 - 2.0 * abs(x - 1.0)

def predict_final(quarks, J, A=A_DEFAULT, B=B_DEFAULT, phi_geom=PHI_GEOM_DEFAULT, phi_int=PHI_INT_DEFAULT):
    base, delta_geo, delta_spin, residue = predict_base(quarks, J)
    theta = skew_angle(quarks)
    tri_geom = tri_wave(theta, phi_geom)
    vortex = 1.0 - abs(tri_wave(theta, phi_int))
    delta_geo_new = delta_geo + A * tri_geom + B * vortex
    final = (base - delta_geo + delta_geo_new) * (1.0 + LAMBDA_UNIV)
    return {
        "base": base,
        "final": final,
        "delta_geo": delta_geo,
        "delta_spin": delta_spin,
        "delta_geo_new": delta_geo_new,
        "theta": theta,
        "tri_geom": tri_geom,
        "vortex": vortex,
        "residue": residue,
    }

def tag_name(name):
    if name == "Omega-":
        return "omega"
    if name.startswith(("Lambda_c","Sigma_c","Xi_c","Omega_c","Xi_cc")):
        return "charm"
    return "clean"

def run_model(A=A_DEFAULT, B=B_DEFAULT, phi_geom=PHI_GEOM_DEFAULT, phi_int=PHI_INT_DEFAULT):
    rows = []
    for name, quarks, J, obs in BARYONS:
        pred = predict_final(quarks, J, A=A, B=B, phi_geom=phi_geom, phi_int=phi_int)
        err = (pred["final"] - obs) / obs * 100.0
        rows.append({
            "name": name, "quarks": quarks, "obs": obs, "tag": tag_name(name),
            "err_pct": err, "abs_err_pct": abs(err), **pred
        })
    return rows

def mape(rows, mode="all"):
    if mode == "clean":
        rows = [r for r in rows if r["tag"] == "clean"]
    return sum(r["abs_err_pct"] for r in rows) / len(rows)

def main():
    rows = run_model()
    summary = {
        "A": A_DEFAULT,
        "B": B_DEFAULT,
        "phi_geom": PHI_GEOM_DEFAULT,
        "phi_int": PHI_INT_DEFAULT,
        "lambda_univ": LAMBDA_UNIV,
        "all_mape": mape(rows, "all"),
        "clean_mape": mape(rows, "clean"),
    }

    print("Geometric Boundary Projection — Standalone")
    print(json.dumps(summary, indent=2))
    print()
    print(f"{'Baryon':<10} {'Obs':>10} {'Base':>10} {'Final':>10} {'err%':>8} {'tag':>8}")
    print("-" * 64)
    for r in rows:
        print(f"{r['name']:<10} {r['obs']:>10.3f} {r['base']:>10.3f} {r['final']:>10.3f} {r['err_pct']:>+8.3f} {r['tag']:>8}")

if __name__ == "__main__":
    main()
