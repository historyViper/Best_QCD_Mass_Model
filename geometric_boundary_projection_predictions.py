#!/usr/bin/env python3
"""
geometric_boundary_projection_predictions.py

Standalone baryon mass runner with:
- embedded known baryon table
- current double-triangle model
- phi_int = 55
- outer Star-of-David / Z3 wave at 60 degrees
- upcoming doubly-heavy prediction states included
- no external imports beyond Python stdlib
"""

import math
import json
import argparse

ALPHA_IR = 0.848809
LAMBDA_QCD = 217.0
GEO_BOUNDARY = math.sin(math.radians(12.0)) ** 2
LAMBDA_UNIV = GEO_BOUNDARY / ALPHA_IR

A_DEFAULT = 20.0
B_DEFAULT = 2.0
C_DEFAULT = 8.0
PHI_GEOM_DEFAULT = 64.5
PHI_INT_DEFAULT = 55.0
PHI_Z3_DEFAULT = 60.0

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
GEO_TWO_7 = math.sqrt(
    (math.sin(math.radians(ANGLES[7] / 2.0)) ** 2)
    * (math.sin(math.radians(ANGLES[INVERSES[7]] / 2.0)) ** 2)
)
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

PREDICTIONS = [
    ("Omega_cc+", ["strange", "charm", "charm"], 0.5),
    ("Xi_bc+",    ["up", "bottom", "charm"],     0.5),
    ("Xi_bc0",    ["down", "bottom", "charm"],   0.5),
    ("Omega_bc0", ["strange", "bottom", "charm"],0.5),
    ("Xi_bb0",    ["up", "bottom", "bottom"],    0.5),
    ("Xi_bb-",    ["down", "bottom", "bottom"],  0.5),
    ("Omega_bb-", ["strange", "bottom", "bottom"],0.5),
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
        geo_branch = "boundary_geo_24"
        geo_factor = geo(24.0)
    elif is_self_inverse(r):
        delta_geo = -ALPHA_BARYON * LAMBDA_QCD * geo(ANGLES[r])
        geo_branch = "self_inverse_geo"
        geo_factor = geo(ANGLES[r])
    elif sheet(r) == "second":
        delta_geo = -ALPHA_BARYON * LAMBDA_QCD * geo_two(r)
        geo_branch = "second_sheet_geo_two"
        geo_factor = geo_two(r)
    else:
        delta_geo = +ALPHA_BARYON * LAMBDA_QCD * geo_two(r)
        geo_branch = "first_sheet_geo_two"
        geo_factor = geo_two(r)

    S = -1.0 if J == 0.5 else 3.0
    delta_spin = C_HYP * S
    base = sum_c + delta_geo + delta_spin
    return {
        "sum_constituent": sum_c,
        "base": base,
        "delta_geo": delta_geo,
        "delta_spin": delta_spin,
        "residue": r,
        "residue_angle": ANGLES.get(r),
        "inverse_residue": INVERSES.get(r),
        "inverse_angle": ANGLES.get(INVERSES.get(r)),
        "sheet": sheet(r),
        "geo_branch": geo_branch,
        "geo_factor": geo_factor,
    }


def skew_angle(quarks):
    lane_angles = [ANGLES[LANES[q]] for q in quarks]
    angles = sorted(lane_angles)
    gaps = []
    n = len(angles)
    for i in range(n):
        for j in range(i + 1, n):
            gaps.append(abs(angles[j] - angles[i]))
    closure_gap = 720 - angles[-1] + angles[0]
    deviations = [abs(g - 240.0) for g in gaps + [closure_gap]]
    theta = sum(deviations) / len(deviations)
    return theta, lane_angles, gaps, closure_gap


def tri_wave(theta_deg, phi):
    x = (theta_deg / phi) % 2.0
    return 1.0 - 2.0 * abs(x - 1.0)


def z3_phase(quarks):
    angles = sorted([ANGLES[LANES[q]] for q in quarks])
    cyc = angles + [angles[0] + 720.0]
    ordered_gaps = [cyc[i + 1] - cyc[i] for i in range(3)]
    theta_z3 = max(ordered_gaps) - min(ordered_gaps)
    return theta_z3, ordered_gaps


def predict_final(quarks, J, A=A_DEFAULT, B=B_DEFAULT, C=C_DEFAULT,
                  phi_geom=PHI_GEOM_DEFAULT, phi_int=PHI_INT_DEFAULT, phi_z3=PHI_Z3_DEFAULT):
    base_info = predict_base(quarks, J)
    theta, lane_angles, pair_gaps, closure_gap = skew_angle(quarks)
    theta_z3, ordered_z3_gaps = z3_phase(quarks)

    tri_geom = tri_wave(theta, phi_geom)
    tri_int = tri_wave(theta, phi_int)
    vortex = 1.0 - abs(tri_int)
    tri_z3 = tri_wave(theta_z3, phi_z3)

    delta_geo_new = base_info["delta_geo"] + A * tri_geom + B * vortex + C * tri_z3
    pre_universal = base_info["base"] - base_info["delta_geo"] + delta_geo_new
    final = pre_universal * (1.0 + LAMBDA_UNIV)

    return {
        **base_info,
        "final": final,
        "delta_geo_new": delta_geo_new,
        "pre_universal": pre_universal,
        "theta": theta,
        "theta_z3": theta_z3,
        "lane_angles": lane_angles,
        "pair_gaps": pair_gaps,
        "closure_gap": closure_gap,
        "ordered_z3_gaps": ordered_z3_gaps,
        "tri_geom": tri_geom,
        "tri_int": tri_int,
        "tri_z3": tri_z3,
        "vortex": vortex,
        "winding_geom": theta / phi_geom,
        "winding_int": theta / phi_int,
        "winding_z3": theta_z3 / phi_z3,
        "lambda_univ": LAMBDA_UNIV,
        "A": A,
        "B": B,
        "C": C,
        "phi_geom": phi_geom,
        "phi_int": phi_int,
        "phi_z3": phi_z3,
    }


def run_known(A=A_DEFAULT, B=B_DEFAULT, C=C_DEFAULT,
              phi_geom=PHI_GEOM_DEFAULT, phi_int=PHI_INT_DEFAULT, phi_z3=PHI_Z3_DEFAULT):
    rows = []
    for name, quarks, J, obs in BARYONS:
        pred = predict_final(quarks, J, A=A, B=B, C=C, phi_geom=phi_geom, phi_int=phi_int, phi_z3=phi_z3)
        err = (pred["final"] - obs) / obs * 100.0
        row = {
            "name": name,
            "quarks": quarks,
            "obs": obs,
            "err_pct": err,
            "abs_err_pct": abs(err),
            **pred,
        }
        rows.append(row)
    return rows


def run_predictions(A=A_DEFAULT, B=B_DEFAULT, C=C_DEFAULT,
                    phi_geom=PHI_GEOM_DEFAULT, phi_int=PHI_INT_DEFAULT, phi_z3=PHI_Z3_DEFAULT):
    rows = []
    for name, quarks, J in PREDICTIONS:
        pred = predict_final(quarks, J, A=A, B=B, C=C, phi_geom=phi_geom, phi_int=phi_int, phi_z3=phi_z3)
        row = {
            "name": name,
            "quarks": quarks,
            **pred,
        }
        rows.append(row)
    return rows


def mape(rows, names=None):
    if names is not None:
        rows = [r for r in rows if r["name"] in names]
    return sum(r["abs_err_pct"] for r in rows) / len(rows)


def print_known(rows):
    print(f"{'Baryon':<10} {'Obs':>10} {'Final':>10} {'err%':>8}")
    print("-" * 44)
    for r in rows:
        print(f"{r['name']:<10} {r['obs']:>10.3f} {r['final']:>10.3f} {r['err_pct']:>+8.3f}")


def print_predictions(rows):
    print(f"{'Predicted state':<12} {'Quarks':<20} {'Mass (MeV)':>12}")
    print("-" * 48)
    for r in rows:
        q = " ".join(r["quarks"])
        print(f"{r['name']:<12} {q:<20} {r['final']:>12.3f}")


def print_detail(row, observed=None):
    print(json.dumps({
        "name": row["name"],
        "quarks": row["quarks"],
        **({"obs": observed} if observed is not None else {}),
        **{k: v for k, v in row.items() if k not in {"name", "quarks", "obs", "err_pct", "abs_err_pct"}}
    }, indent=2))
    if observed is not None:
        err = (row["final"] - observed) / observed * 100.0
        print(f"\nerror_pct = {err:+.6f}")


def main():
    parser = argparse.ArgumentParser(description="Geometric Boundary Projection with doubly-heavy predictions")
    parser.add_argument("--known", action="store_true", help="Print known baryon validation table")
    parser.add_argument("--predictions", action="store_true", help="Print prediction table")
    parser.add_argument("--all", action="store_true", help="Print both known table and predictions")
    parser.add_argument("--json", action="store_true", help="Print JSON payload for all output")
    parser.add_argument("--name", type=str, help="Print detail for a specific known or predicted state")
    args = parser.parse_args()

    known_rows = run_known()
    prediction_rows = run_predictions()

    if args.name:
        for r in known_rows:
            if r["name"].lower() == args.name.lower():
                print_detail(r, observed=r["obs"])
                return
        for r in prediction_rows:
            if r["name"].lower() == args.name.lower():
                print_detail(r)
                return
        raise SystemExit(f"State not found: {args.name}")

    if args.json:
        payload = {
            "parameters": {
                "A": A_DEFAULT,
                "B": B_DEFAULT,
                "C": C_DEFAULT,
                "phi_geom": PHI_GEOM_DEFAULT,
                "phi_int": PHI_INT_DEFAULT,
                "phi_z3": PHI_Z3_DEFAULT,
                "lambda_univ": LAMBDA_UNIV,
                "alpha_ir": ALPHA_IR,
                "lambda_qcd": LAMBDA_QCD,
            },
            "validation_summary": {
                "all_mape": mape(known_rows),
                "bottom_mape": mape(known_rows, names={"Lambda_b","Sigma_b+","Sigma_b-","Xi_b0","Xi_b-","Omega_b"}),
                "double_pair_mape": mape(known_rows, names={"Xi_cc++","Xi_cc+"}),
            },
            "known": known_rows,
            "predictions": prediction_rows,
        }
        print(json.dumps(payload, indent=2))
        return

    if args.all or (not args.known and not args.predictions):
        print("Geometric Boundary Projection — Double Triangle + Predictions")
        print(json.dumps({
            "A": A_DEFAULT,
            "B": B_DEFAULT,
            "C": C_DEFAULT,
            "phi_geom": PHI_GEOM_DEFAULT,
            "phi_int": PHI_INT_DEFAULT,
            "phi_z3": PHI_Z3_DEFAULT,
            "lambda_univ": LAMBDA_UNIV,
            "all_mape": mape(known_rows),
            "bottom_mape": mape(known_rows, names={"Lambda_b","Sigma_b+","Sigma_b-","Xi_b0","Xi_b-","Omega_b"}),
            "double_pair_mape": mape(known_rows, names={"Xi_cc++","Xi_cc+"}),
        }, indent=2))
        print()
        print("Known baryon validation")
        print_known(known_rows)
        print()
        print("Predictions")
        print_predictions(prediction_rows)
        return

    if args.known:
        print_known(known_rows)
    if args.predictions:
        if args.known:
            print()
        print_predictions(prediction_rows)


if __name__ == "__main__":
    main()
