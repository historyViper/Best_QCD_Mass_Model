#!/usr/bin/env python3
"""
Geometric Boundary Projection — diagnostics / best-match explorer

Built from the user's standalone runner, with additions for:
- per-baryon detailed diagnostics
- parameter search for best match on a chosen baryon or all baryons
- explicit reporting of intermediate variables used in each prediction
- winding-style derived metrics based on theta / phi ratios
"""

import math
import json
import argparse
from itertools import product

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

BARYON_MAP = {name: {"name": name, "quarks": quarks, "J": J, "obs": obs} for name, quarks, J, obs in BARYONS}

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

def skew_angle_details(quarks):
    lane_angles = [ANGLES[LANES[q]] for q in quarks]
    lane_angles_sorted = sorted(lane_angles)
    pair_gaps = []
    n = len(lane_angles_sorted)
    for i in range(n):
        for j in range(i + 1, n):
            pair_gaps.append(abs(lane_angles_sorted[j] - lane_angles_sorted[i]))
    closure_gap = 720 - lane_angles_sorted[-1] + lane_angles_sorted[0]
    gaps_all = pair_gaps + [closure_gap]
    deviations = [abs(g - 240) for g in gaps_all]
    theta = sum(deviations) / len(deviations)
    return {
        "lane_angles": lane_angles,
        "lane_angles_sorted": lane_angles_sorted,
        "pair_gaps": pair_gaps,
        "closure_gap": closure_gap,
        "gaps_all": gaps_all,
        "deviations_from_240": deviations,
        "theta": theta,
    }

def tri_wave(theta_deg, phi):
    x = (theta_deg / phi) % 2.0
    return 1.0 - 2.0 * abs(x - 1.0)

def predict_base(quarks, J):
    r = baryon_residue(quarks)
    sum_c = sum(CONSTITUENT[q] for q in quarks)

    if r not in ANGLES:
        geo_branch = "boundary_fallback"
        geo_factor = geo(24.0)
        delta_geo = -ALPHA_BARYON * LAMBDA_QCD * geo_factor
    elif is_self_inverse(r):
        geo_branch = "self_inverse"
        geo_factor = geo(ANGLES[r])
        delta_geo = -ALPHA_BARYON * LAMBDA_QCD * geo_factor
    elif sheet(r) == "second":
        geo_branch = "second_sheet_geo_two"
        geo_factor = geo_two(r)
        delta_geo = -ALPHA_BARYON * LAMBDA_QCD * geo_factor
    else:
        geo_branch = "first_sheet_geo_two"
        geo_factor = geo_two(r)
        delta_geo = +ALPHA_BARYON * LAMBDA_QCD * geo_factor

    S = -1.0 if J == 0.5 else 3.0
    delta_spin = C_HYP * S
    base = sum_c + delta_geo + delta_spin

    return {
        "base": base,
        "residue": r,
        "sum_constituent": sum_c,
        "geo_branch": geo_branch,
        "geo_factor": geo_factor,
        "delta_geo": delta_geo,
        "spin_factor_S": S,
        "delta_spin": delta_spin,
    }

def pair_signature(quarks):
    counts = {q: quarks.count(q) for q in sorted(set(quarks))}
    return {
        "same_up_pair": quarks.count("up") == 2,
        "same_down_pair": quarks.count("down") == 2,
        "same_strange_pair": quarks.count("strange") == 2,
        "same_charm_pair": quarks.count("charm") == 2,
        "ud_pair": quarks.count("up") == 1 and quarks.count("down") == 1,
        "counts": counts,
    }

def predict_final(quarks, J, A=A_DEFAULT, B=B_DEFAULT, phi_geom=PHI_GEOM_DEFAULT, phi_int=PHI_INT_DEFAULT):
    base_info = predict_base(quarks, J)
    skew = skew_angle_details(quarks)
    theta = skew["theta"]
    tri_geom = tri_wave(theta, phi_geom)
    tri_int = tri_wave(theta, phi_int)
    vortex = 1.0 - abs(tri_int)
    delta_geo_new = base_info["delta_geo"] + A * tri_geom + B * vortex
    pre_universal = base_info["base"] - base_info["delta_geo"] + delta_geo_new
    final = pre_universal * (1.0 + LAMBDA_UNIV)

    residue = base_info["residue"]
    residue_angle = ANGLES.get(residue)
    inverse_residue = INVERSES.get(residue)
    inverse_angle = ANGLES.get(inverse_residue) if inverse_residue is not None else None

    winding_geom = theta / phi_geom if phi_geom else float("inf")
    winding_int = theta / phi_int if phi_int else float("inf")

    return {
        **base_info,
        **skew,
        **pair_signature(quarks),
        "A": A,
        "B": B,
        "phi_geom": phi_geom,
        "phi_int": phi_int,
        "tri_geom": tri_geom,
        "tri_int": tri_int,
        "vortex": vortex,
        "delta_geo_new": delta_geo_new,
        "pre_universal": pre_universal,
        "lambda_univ": LAMBDA_UNIV,
        "final": final,
        "residue_angle": residue_angle,
        "inverse_residue": inverse_residue,
        "inverse_angle": inverse_angle,
        "sheet": sheet(residue),
        "winding_geom": winding_geom,
        "winding_int": winding_int,
        "winding_geom_floor": math.floor(winding_geom),
        "winding_int_floor": math.floor(winding_int),
        "winding_geom_frac": winding_geom - math.floor(winding_geom),
        "winding_int_frac": winding_int - math.floor(winding_int),
    }

def tag_name(name):
    if name == "Omega-":
        return "omega"
    if name.startswith(("Lambda_c","Sigma_c","Xi_c","Omega_c","Xi_cc")):
        return "charm"
    return "clean"

def evaluate_baryon(name, A=A_DEFAULT, B=B_DEFAULT, phi_geom=PHI_GEOM_DEFAULT, phi_int=PHI_INT_DEFAULT):
    item = BARYON_MAP[name]
    pred = predict_final(item["quarks"], item["J"], A=A, B=B, phi_geom=phi_geom, phi_int=phi_int)
    err = pred["final"] - item["obs"]
    err_pct = err / item["obs"] * 100.0
    return {
        "name": item["name"],
        "quarks": item["quarks"],
        "J": item["J"],
        "obs": item["obs"],
        "tag": tag_name(item["name"]),
        "err": err,
        "err_pct": err_pct,
        "abs_err": abs(err),
        "abs_err_pct": abs(err_pct),
        **pred,
    }

def run_model(A=A_DEFAULT, B=B_DEFAULT, phi_geom=PHI_GEOM_DEFAULT, phi_int=PHI_INT_DEFAULT):
    return [evaluate_baryon(name, A=A, B=B, phi_geom=phi_geom, phi_int=phi_int) for name in BARYON_MAP]

def mape(rows, mode="all"):
    if mode == "clean":
        rows = [r for r in rows if r["tag"] == "clean"]
    return sum(r["abs_err_pct"] for r in rows) / len(rows)

def frange(start, stop, step):
    vals = []
    x = start
    eps = step / 10.0
    while x <= stop + eps:
        vals.append(round(x, 10))
        x += step
    return vals

def best_match_for_baryon(name, A_values, B_values, phi_geom_values, phi_int_values):
    best = None
    for A, B, phi_geom, phi_int in product(A_values, B_values, phi_geom_values, phi_int_values):
        row = evaluate_baryon(name, A=A, B=B, phi_geom=phi_geom, phi_int=phi_int)
        if best is None or row["abs_err"] < best["abs_err"]:
            best = row
    return best

def best_match_all(A_values, B_values, phi_geom_values, phi_int_values):
    out = []
    for name in BARYON_MAP:
        out.append(best_match_for_baryon(name, A_values, B_values, phi_geom_values, phi_int_values))
    return out

def print_detail(row):
    print(f"Name: {row['name']}")
    print(f"Quarks: {row['quarks']}  J={row['J']}  tag={row['tag']}")
    print(f"Observed: {row['obs']:.6f}")
    print(f"Predicted final: {row['final']:.6f}")
    print(f"Absolute error: {row['abs_err']:.6f}")
    print(f"Percent error: {row['err_pct']:+.6f}%")
    print()
    print("Parameters")
    print(f"  A={row['A']}  B={row['B']}  phi_geom={row['phi_geom']}  phi_int={row['phi_int']}")
    print()
    print("Base terms")
    print(f"  sum_constituent={row['sum_constituent']:.6f}")
    print(f"  residue={row['residue']}  residue_angle={row['residue_angle']}")
    print(f"  inverse_residue={row['inverse_residue']}  inverse_angle={row['inverse_angle']}")
    print(f"  sheet={row['sheet']}  geo_branch={row['geo_branch']}")
    print(f"  geo_factor={row['geo_factor']:.12f}")
    print(f"  delta_geo={row['delta_geo']:.6f}")
    print(f"  spin_factor_S={row['spin_factor_S']:.6f}")
    print(f"  delta_spin={row['delta_spin']:.6f}")
    print(f"  base={row['base']:.6f}")
    print()
    print("Angular / skew terms")
    print(f"  lane_angles={row['lane_angles']}")
    print(f"  lane_angles_sorted={row['lane_angles_sorted']}")
    print(f"  pair_gaps={row['pair_gaps']}")
    print(f"  closure_gap={row['closure_gap']}")
    print(f"  gaps_all={row['gaps_all']}")
    print(f"  deviations_from_240={row['deviations_from_240']}")
    print(f"  theta={row['theta']:.6f}")
    print()
    print("Wave / vortex / winding")
    print(f"  tri_geom={row['tri_geom']:.12f}")
    print(f"  tri_int={row['tri_int']:.12f}")
    print(f"  vortex={row['vortex']:.12f}")
    print(f"  winding_geom={row['winding_geom']:.12f}  floor={row['winding_geom_floor']}  frac={row['winding_geom_frac']:.12f}")
    print(f"  winding_int={row['winding_int']:.12f}  floor={row['winding_int_floor']}  frac={row['winding_int_frac']:.12f}")
    print()
    print("Pair structure")
    print(f"  counts={row['counts']}")
    print(f"  same_up_pair={row['same_up_pair']}  same_down_pair={row['same_down_pair']}")
    print(f"  same_strange_pair={row['same_strange_pair']}  same_charm_pair={row['same_charm_pair']}")
    print(f"  ud_pair={row['ud_pair']}")
    print()
    print("Final assembly")
    print(f"  delta_geo_new={row['delta_geo_new']:.6f}")
    print(f"  pre_universal={row['pre_universal']:.6f}")
    print(f"  lambda_univ={row['lambda_univ']:.12f}")
    print(f"  final={row['final']:.6f}")

def build_parser():
    p = argparse.ArgumentParser(description="Geometric Boundary Projection diagnostics")
    p.add_argument("--name", help="Baryon name to inspect, e.g. Sigma_c++")
    p.add_argument("--A", type=float, default=A_DEFAULT)
    p.add_argument("--B", type=float, default=B_DEFAULT)
    p.add_argument("--phi-geom", type=float, default=PHI_GEOM_DEFAULT, dest="phi_geom")
    p.add_argument("--phi-int", type=float, default=PHI_INT_DEFAULT, dest="phi_int")
    p.add_argument("--detail", action="store_true", help="Print full variable breakdown")
    p.add_argument("--json", action="store_true", help="Emit JSON")
    p.add_argument("--table", action="store_true", help="Print table for all baryons at current parameters")
    p.add_argument("--search-best", action="store_true", help="Grid-search best match for selected --name or for all if --all-best")
    p.add_argument("--all-best", action="store_true", help="Grid-search best match for all baryons")
    p.add_argument("--A-min", type=float, default=18.0)
    p.add_argument("--A-max", type=float, default=22.0)
    p.add_argument("--A-step", type=float, default=0.5)
    p.add_argument("--B-min", type=float, default=0.0)
    p.add_argument("--B-max", type=float, default=4.0)
    p.add_argument("--B-step", type=float, default=0.5)
    p.add_argument("--phi-geom-min", type=float, default=50.0, dest="phi_geom_min")
    p.add_argument("--phi-geom-max", type=float, default=80.0, dest="phi_geom_max")
    p.add_argument("--phi-geom-step", type=float, default=0.5, dest="phi_geom_step")
    p.add_argument("--phi-int-min", type=float, default=45.0, dest="phi_int_min")
    p.add_argument("--phi-int-max", type=float, default=65.0, dest="phi_int_max")
    p.add_argument("--phi-int-step", type=float, default=0.5, dest="phi_int_step")
    return p

def main():
    args = build_parser().parse_args()

    if args.search_best or args.all_best:
        A_values = frange(args.A_min, args.A_max, args.A_step)
        B_values = frange(args.B_min, args.B_max, args.B_step)
        phi_geom_values = frange(args.phi_geom_min, args.phi_geom_max, args.phi_geom_step)
        phi_int_values = frange(args.phi_int_min, args.phi_int_max, args.phi_int_step)

        if args.all_best:
            rows = best_match_all(A_values, B_values, phi_geom_values, phi_int_values)
            if args.json:
                print(json.dumps(rows, indent=2))
                return
            print(f"{'Baryon':<12} {'Obs':>10} {'Final':>10} {'err%':>9} {'A':>6} {'B':>6} {'phi_g':>8} {'phi_i':>8} {'wind_g':>8} {'wind_i':>8}")
            print("-" * 95)
            for r in rows:
                print(f"{r['name']:<12} {r['obs']:>10.3f} {r['final']:>10.3f} {r['err_pct']:>+9.3f} {r['A']:>6.2f} {r['B']:>6.2f} {r['phi_geom']:>8.2f} {r['phi_int']:>8.2f} {r['winding_geom']:>8.3f} {r['winding_int']:>8.3f}")
            return

        if not args.name:
            raise SystemExit("--search-best needs --name unless you use --all-best")
        row = best_match_for_baryon(args.name, A_values, B_values, phi_geom_values, phi_int_values)
        if args.json:
            print(json.dumps(row, indent=2))
        else:
            print_detail(row)
        return

    if args.table:
        rows = run_model(A=args.A, B=args.B, phi_geom=args.phi_geom, phi_int=args.phi_int)
        print(f"{'Baryon':<12} {'Obs':>10} {'Base':>10} {'Final':>10} {'err%':>9} {'theta':>9} {'wind_g':>8} {'wind_i':>8}")
        print("-" * 90)
        for r in rows:
            print(f"{r['name']:<12} {r['obs']:>10.3f} {r['base']:>10.3f} {r['final']:>10.3f} {r['err_pct']:>+9.3f} {r['theta']:>9.3f} {r['winding_geom']:>8.3f} {r['winding_int']:>8.3f}")
        print()
        print(json.dumps({
            "A": args.A,
            "B": args.B,
            "phi_geom": args.phi_geom,
            "phi_int": args.phi_int,
            "lambda_univ": LAMBDA_UNIV,
            "all_mape": mape(rows, "all"),
            "clean_mape": mape(rows, "clean"),
        }, indent=2))
        return

    if args.name:
        row = evaluate_baryon(args.name, A=args.A, B=args.B, phi_geom=args.phi_geom, phi_int=args.phi_int)
        if args.json:
            print(json.dumps(row, indent=2))
        elif args.detail:
            print_detail(row)
        else:
            print(f"{row['name']}: obs={row['obs']:.6f} final={row['final']:.6f} err={row['err']:+.6f} err_pct={row['err_pct']:+.6f}%")
        return

    rows = run_model(A=args.A, B=args.B, phi_geom=args.phi_geom, phi_int=args.phi_int)
    print("Geometric Boundary Projection — diagnostics")
    print(json.dumps({
        "A": args.A,
        "B": args.B,
        "phi_geom": args.phi_geom,
        "phi_int": args.phi_int,
        "lambda_univ": LAMBDA_UNIV,
        "all_mape": mape(rows, "all"),
        "clean_mape": mape(rows, "clean"),
    }, indent=2))

if __name__ == "__main__":
    main()
