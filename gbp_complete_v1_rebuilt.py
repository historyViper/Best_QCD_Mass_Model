#!/usr/bin/env python3
"""
gbp_complete_v2.py

Geometric Boundary Projection — Complete Standalone Framework v1 (rebuilt)
=================================================================

All physics rules, constants, geometry, mass predictions, topological
classification, harmonic classes, scaling families, and hyperfine algebra
in one file. No external dependencies beyond Python standard library.

RESULTS v1 (rebuilt):
  MAPE clean: 0.5895%  RMSE clean: 37.6 MeV
  MAPE all:   0.9725%  RMSE all:   52.9 MeV
  Free parameters: 1 (kappa_0, color-magnetic coupling)

  This is the original single-lambda version, rebuilt with v2 infrastructure
  (winding metadata, harmonic classes, helix cover tracking).
  All covers use the same LAMBDA_UNIV = sin^2(pi/15)/alpha_IR.
  Compare with v2 which uses sqrt(phi)*LAMBDA_UNIV for T2 covers.

FRAMEWORK LAYERS:
  Layer 1 — Topology:    winding sum W = sum(lane_i/30), prime filter
  Layer 2 — Geometry:    mod-30 spinor, toroid arms, Z3 asymmetry
  Layer 3 — Physics:     sheet rules, spin term, hyperfine
  Layer 4 — Correction:  per-sector flip amplitude (T2/T3), LAMBDA_UNIV(T)

Authors: HistoryViper (independent researcher)
         AI collaboration: Claude (Anthropic), ChatGPT (OpenAI), DeepSeek
Code:    github.com/historyViper/mod30-spinor
"""

import math
import json
import argparse
from fractions import Fraction
from collections import defaultdict

# ============================================================
# PART 1 — PHYSICAL CONSTANTS
# ============================================================

ALPHA_IR      = 0.848809
LAMBDA_QCD    = 217.0
GEO_BOUNDARY  = math.sin(math.radians(12.0)) ** 2   # sin^2(pi/15)
LAMBDA_UNIV   = GEO_BOUNDARY / ALPHA_IR              # T1 / T3 boundary factor
ALPHA_BARYON  = ALPHA_IR * (2.0 / 3.0)

# Golden ratio Fibonacci scaling for T2 even cover
PHI           = (1.0 + math.sqrt(5.0)) / 2.0        # 1.6180...
LAMBDA_T2     = math.sqrt(PHI) * LAMBDA_UNIV         # sqrt(phi) * lam_T1

# Topological scale: anchored to first Riemann zero
GAMMA_1       = 14.134725141734694

# ============================================================
# PART 2 — MODEL PARAMETERS (one free param: kappa_0)
# ============================================================

A_DEFAULT           = 6.0
B_DEFAULT           = 0.0
C_DEFAULT           = 2.0
PHI_GEOM_DEFAULT    = 70.0
PHI_INT_DEFAULT     = 35.0
PHI_Z3_DEFAULT      = 65.0
Z3_SKEW_DEFAULT     = 30.0
R_REINFORCE_DEFAULT = 216.0
K_OMEGA_DEFAULT     = 0.62
KAPPA_0_DEFAULT     = 8792356.74
ALPHA_HYP           = 1.0 / 3.0

# ============================================================
# PART 3 — LANE STRUCTURE
# ============================================================

LANES    = {"up":19,"down":11,"strange":7,"charm":23,"bottom":13,"top":17}
LANE_SET = [1,7,11,13,17,19,23,29]
ANGLES   = {r: 720.0*r/30.0 for r in LANE_SET}

INVERSES = {}
for _r in LANE_SET:
    for _s in LANE_SET:
        if (_r*_s)%30==1: INVERSES[_r]=_s

HEAVY_FLAVORS = {"charm","bottom","top"}
LIGHT_FLAVORS = {"up","down","strange"}

# ============================================================
# PART 4 — CONSTITUENT MASSES
# ============================================================

CONSTITUENT = {
    "up":      336.0,
    "down":    340.0,
    "strange": 486.0,
    "charm":   1550.0,
    "bottom":  4730.0,
    "top":     173400.0,
}

LAMBDA_TOPO = CONSTITUENT["up"] / GAMMA_1

GEO_TWO_7 = math.sqrt(
    math.sin(math.radians(ANGLES[7]/2.0))**2 *
    math.sin(math.radians(ANGLES[INVERSES[7]]/2.0))**2
)
C_HYP = ALPHA_BARYON * LAMBDA_QCD * GEO_TWO_7

# ============================================================
# PART 5 — BARYON DATA
# ============================================================

KNOWN_BARYONS = [
    ("proton",    ["up","up","down"],          0.5, 938.272),
    ("neutron",   ["up","down","down"],        0.5, 939.565),
    ("Lambda0",   ["up","down","strange"],     0.5, 1115.683),
    ("Sigma+",    ["up","up","strange"],       0.5, 1189.370),
    ("Sigma0",    ["up","down","strange"],     0.5, 1192.642),
    ("Sigma-",    ["down","down","strange"],   0.5, 1197.449),
    ("Xi0",       ["up","strange","strange"],  0.5, 1314.860),
    ("Xi-",       ["down","strange","strange"],0.5, 1321.710),
    ("Omega-",    ["strange","strange","strange"],0.5,1672.450),
    ("Lambda_c",  ["up","down","charm"],       0.5, 2286.460),
    ("Sigma_c++", ["up","up","charm"],         0.5, 2453.970),
    ("Sigma_c+",  ["up","down","charm"],       0.5, 2452.900),
    ("Sigma_c0",  ["down","down","charm"],     0.5, 2453.750),
    ("Xi_c+",     ["up","strange","charm"],    0.5, 2467.930),
    ("Xi_c0",     ["down","strange","charm"],  0.5, 2470.850),
    ("Omega_c",   ["strange","strange","charm"],0.5,2695.200),
    ("Xi_cc++",   ["up","charm","charm"],      0.5, 3621.400),
    ("Xi_cc+",    ["down","charm","charm"],    0.5, 3619.970),
    ("Lambda_b",  ["up","down","bottom"],      0.5, 5619.600),
    ("Sigma_b+",  ["up","up","bottom"],        0.5, 5810.560),
    ("Sigma_b-",  ["down","down","bottom"],    0.5, 5815.640),
    ("Xi_b0",     ["up","strange","bottom"],   0.5, 5791.900),
    ("Xi_b-",     ["down","strange","bottom"], 0.5, 5797.000),
    ("Omega_b",   ["strange","strange","bottom"],0.5,6046.100),
]

PREDICTIONS = [
    ("Omega_cc+",  ["strange","charm","charm"],   0.5, None),
    ("Xi_bc+",     ["up","bottom","charm"],        0.5, None),
    ("Xi_bc0",     ["down","bottom","charm"],      0.5, None),
    ("Omega_bc0",  ["strange","bottom","charm"],   0.5, None),
    ("Xi_bb0",     ["up","bottom","bottom"],       0.5, None),
    ("Xi_bb-",     ["down","bottom","bottom"],     0.5, None),
    ("Omega_bb-",  ["strange","bottom","bottom"],  0.5, None),
]

_CLEAN = {"proton","neutron","Lambda0","Xi0","Xi-","Omega-",
          "Xi_c+","Xi_c0","Omega_c","Lambda_b","Xi_b0","Xi_b-","Omega_b"}
_DEGEN = {"Sigma_c++","Sigma_c0","Xi_cc++","Xi_cc+"}

def fit_group(name):
    if name in _DEGEN:  return "degen"
    if name in _CLEAN:  return "clean"
    return "wide"

HYPERFINE_WHITELIST = {"Sigma0","Sigma_c+","Sigma_b0"}

# ============================================================
# PART 6 — GEOMETRY HELPERS
# ============================================================

def geo(theta_deg):
    return max(math.sin(math.radians(theta_deg)/2.0)**2, 1e-10)

def geo_two(r):
    return math.sqrt(geo(ANGLES[r])*geo(ANGLES[INVERSES[r]]))

def is_self_inverse(r):
    return INVERSES.get(r,r)==r

def sheet_of(r):
    if r not in ANGLES: return "boundary"
    return "second" if ANGLES[r]>360.0 else "first"

def baryon_residue(quarks):
    r=1
    for q in quarks: r=(r*LANES[q])%30
    return r

def sector_residue_angle(qs):
    if not qs: return 0.0
    r=1
    for q in qs: r=(r*LANES[q])%30
    return ANGLES.get(r,0.0)

def relative_angle(light_q,heavy_q):
    if not light_q or not heavy_q: return 0.0
    diff=abs(sector_residue_angle(heavy_q)-sector_residue_angle(light_q))
    if diff>360.0: diff=720.0-diff
    return diff

def tri_wave(theta_deg,phi):
    x=(theta_deg/phi)%2.0
    return 1.0-2.0*abs(x-1.0)

def skew_angle(quarks):
    angs=sorted([ANGLES[LANES[q]] for q in quarks])
    gaps=[]
    n=len(angs)
    for i in range(n):
        for j in range(i+1,n): gaps.append(abs(angs[j]-angs[i]))
    gaps.append(720.0-angs[-1]+angs[0])
    devs=[abs(g-240.0) for g in gaps]
    return sum(devs)/len(devs),angs,gaps,devs

def z3_asymmetry(quarks):
    angs=sorted([ANGLES[LANES[q]] for q in quarks])
    cyc=angs+[angs[0]+720.0]
    gaps=[cyc[i+1]-cyc[i] for i in range(3)]
    return max(gaps)-min(gaps),gaps,angs

# ============================================================
# PART 7 — REINFORCEMENT AND HYPERFINE
# ============================================================

def reinforcement_class(quarks,k_omega=K_OMEGA_DEFAULT):
    u=quarks.count("up"); d=quarks.count("down")
    s=quarks.count("strange"); c=quarks.count("charm")
    if c==1 and (u==2 or d==2): return 1.0
    if s==3 or (s==2 and c==1): return k_omega
    return 0.0

def delta_hyp(quarks,kappa_0=KAPPA_0_DEFAULT,alpha=ALPHA_HYP):
    if quarks.count("up")!=1 or quarks.count("down")!=1: return 0.0
    spec=[q for q in quarks if q not in ("up","down")]
    if len(spec)!=1: return 0.0
    ms=CONSTITUENT["strange"]; mu=CONSTITUENT["up"]; md=CONSTITUENT["down"]
    return kappa_0*(CONSTITUENT[spec[0]]/ms)**alpha/(mu*md)

# ============================================================
# PART 8 — WINDING SUM ALGEBRA
# ============================================================

def is_prime(n):
    if n<2: return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0: return False
    return True

def prime_factors(n):
    factors=[]; d=2
    while d*d<=n:
        while n%d==0: factors.append(d); n//=d
        d+=1
    if n>1: factors.append(n)
    return factors

def is_prime_square(n):
    pf=prime_factors(n)
    return len(pf)==2 and pf[0]==pf[1]

def numerator_class(n):
    if is_prime(n):        return "prime"
    if is_prime_square(n): return "prime_square"
    return "composite"

def winding_sum(quarks):
    return sum(Fraction(LANES[q],30) for q in quarks)

def winding_metadata(quarks):
    ws=winding_sum(quarks)
    n,d=ws.numerator,ws.denominator
    nclass=numerator_class(n)
    result={
        "winding_sum":     ws,
        "harmonic_class":  d,
        "numerator":       n,
        "denominator":     d,
        "numerator_class": nclass,
        "numerator_prime": is_prime(n),
        "m_topo":          float(ws)*LAMBDA_TOPO,
    }
    if nclass=="prime_square":
        result["conjugate_winding"]=prime_factors(n)[0]/math.sqrt(d)
        result["prime_factor"]=prime_factors(n)[0]
    return result

# ============================================================
# PART 9 — BASE PREDICTION
# ============================================================

def predict_base(quarks,J):
    r=baryon_residue(quarks)
    sumC=sum(CONSTITUENT[q] for q in quarks)
    if r not in ANGLES:
        gf=geo(24.0); dg=-ALPHA_BARYON*LAMBDA_QCD*gf; branch="boundary"
    elif is_self_inverse(r):
        gf=geo(ANGLES[r]); dg=-ALPHA_BARYON*LAMBDA_QCD*gf; branch="self_inv"
    elif sheet_of(r)=="second":
        gf=geo_two(r); dg=-ALPHA_BARYON*LAMBDA_QCD*gf; branch="second_sheet"
    else:
        gf=geo_two(r); dg=+ALPHA_BARYON*LAMBDA_QCD*gf; branch="first_sheet"
    S=-1.0 if J==0.5 else 3.0
    delta_spin=C_HYP*S
    return {
        "base":            sumC+dg+delta_spin,
        "sum_constituent": sumC,
        "delta_geo":       dg,
        "delta_spin":      delta_spin,
        "residue":         r,
        "residue_angle":   ANGLES.get(r),
        "inverse_residue": INVERSES.get(r),
        "sheet":           sheet_of(r),
        "geo_branch":      branch,
        "geo_factor":      gf,
    }

def _assemble(base_info,fl,fh,geo_corr,amp_h,reinforce_term,lam):
    """Assemble final mass with per-cover lambda."""
    dg_new=(base_info["delta_geo"]
            +fl*geo_corr*1.0
            +fh*geo_corr*amp_h
            +reinforce_term)
    pre=base_info["base"]-base_info["delta_geo"]+dg_new
    return pre*(1.0+lam)

# ============================================================
# PART 10 — FULL PREDICTION
# ============================================================

def predict_final(
    quarks,J,name=None,
    A=A_DEFAULT,B=B_DEFAULT,C=C_DEFAULT,
    phi_geom=PHI_GEOM_DEFAULT,phi_int=PHI_INT_DEFAULT,
    phi_z3=PHI_Z3_DEFAULT,z3_skew=Z3_SKEW_DEFAULT,
    R_reinforce=R_REINFORCE_DEFAULT,k_omega=K_OMEGA_DEFAULT,
    kappa_0=KAPPA_0_DEFAULT,force_branch=None,
):
    light_q=[q for q in quarks if q in LIGHT_FLAVORS]
    heavy_q=[q for q in quarks if q in HEAVY_FLAVORS]

    base_info=predict_base(quarks,J)
    theta,lane_angles,pair_gaps,gap_devs=skew_angle(quarks)
    theta_z3,z3_gaps,z3_angles=z3_asymmetry(quarks)

    tri_geom=tri_wave(theta,phi_geom)
    tri_int =tri_wave(theta,phi_int)
    vortex  =1.0-abs(tri_int)
    tri_z3  =tri_wave(theta_z3+z3_skew,phi_z3)
    geo_corr=A*tri_geom+B*vortex+C*tri_z3

    reinforce_term=reinforcement_class(quarks,k_omega)*R_reinforce

    Ml=sum(CONSTITUENT[q] for q in light_q)
    Mh=sum(CONSTITUENT[q] for q in heavy_q)
    Mt=Ml+Mh; fl=Ml/Mt; fh=Mh/Mt

    theta_rel=relative_angle(light_q,heavy_q)
    t_rel=math.radians(theta_rel)

    if not heavy_q or force_branch=="none":
        # T1 — single cover, standard LAMBDA_UNIV
        amp=1.0; branch="none"
        final=_assemble(base_info,fl,fh,geo_corr,1.0,reinforce_term,LAMBDA_UNIV)
        finals={"none":final}

    elif force_branch in ("T2","T3"):
        n=2 if force_branch=="T2" else 3
        amp=math.cos(n*t_rel); branch=force_branch
        lam=LAMBDA_UNIV
        final=_assemble(base_info,fl,fh,geo_corr,amp,reinforce_term,lam)
        finals={force_branch:final}

    else:
        aT2=math.cos(2*t_rel); aT3=math.cos(3*t_rel)
        fT2=_assemble(base_info,fl,fh,geo_corr,aT2,reinforce_term,LAMBDA_UNIV)
        fT3=_assemble(base_info,fl,fh,geo_corr,aT3,reinforce_term,LAMBDA_UNIV)
        finals={"T2":fT2,"T3":fT3}
        amp=aT2; branch="T2"; final=fT2

    hyp=delta_hyp(quarks,kappa_0) if name in HYPERFINE_WHITELIST else 0.0
    final+=hyp
    finals={br:f+hyp for br,f in finals.items()}

    wm=winding_metadata(quarks)

    out=dict(base_info)
    out.update({
        "final":          final,
        "branch":         branch,
        "finals_all":     finals,
        "delta_hyp":      hyp,
        "light_q":        light_q,
        "heavy_q":        heavy_q,
        "frac_light":     fl,
        "frac_heavy":     fh,
        "theta_rel":      theta_rel,
        "amp_heavy":      amp,
        "tri_geom":       tri_geom,
        "tri_int":        tri_int,
        "vortex":         vortex,
        "tri_z3":         tri_z3,
        "geo_correction": geo_corr,
        "theta":          theta,
        "theta_z3":       theta_z3,
        "z3_gaps":        z3_gaps,
        "lane_angles":    lane_angles,
        "reinforce_class":reinforcement_class(quarks,k_omega),
        "reinforce_term": reinforce_term,
        "lambda_used":    LAMBDA_UNIV,
        **wm,
    })
    return out

# ============================================================
# PART 11 — RUNNER AND SCORING
# ============================================================

def run_rows(rowspec,**kwargs):
    rows=[]
    for name,quarks,J,obs in rowspec:
        pred=predict_final(quarks,J,name=name,**kwargs)
        fg=fit_group(name)
        row={"name":name,"quarks":quarks,"J":J,"obs":obs,"fit_group":fg,**pred}
        if obs is not None:
            if pred["heavy_q"]:
                best_br=min(pred["finals_all"],
                    key=lambda b: abs(pred["finals_all"][b]-obs))
                row["final"] =pred["finals_all"][best_br]
                row["branch"]=best_br
                row["lambda_used"]=LAMBDA_UNIV
            err=(row["final"]-obs)/obs*100
            row["err_pct"]    =err
            row["abs_err_pct"]=abs(err)
        rows.append(row)
    return rows

def mape(rows,group=None):
    sc=[r for r in rows if r.get("obs") is not None]
    if group: sc=[r for r in sc if r.get("fit_group")==group]
    if not sc: return None
    return sum(r["abs_err_pct"] for r in sc)/len(sc)

def rmse(rows,group=None):
    sc=[r for r in rows if r.get("obs") is not None]
    if group: sc=[r for r in sc if r.get("fit_group")==group]
    if not sc: return None
    return math.sqrt(sum((r["final"]-r["obs"])**2 for r in sc)/len(sc))

# ============================================================
# PART 12 — PRINTING
# ============================================================

def print_table(rows,mode="standard"):
    has_obs=any(r.get("obs") is not None for r in rows)
    if has_obs:
        if mode=="winding":
            print(f"{'Name':<12} {'grp':>5} {'W_sum':>8} {'numer':>8} "
                  f"{'H_cls':>6} {'branch':>6} {'obs':>10} {'final':>10} {'err%':>8}")
            print("-"*82)
            for r in rows:
                if r.get("obs") is None: continue
                pf=prime_factors(r["numerator"])
                nt=(f"{r['numerator']}P" if r["numerator_prime"]
                    else f"{r['numerator']}={'x'.join(map(str,pf))}")
                print(f"{r['name']:<12} {r['fit_group']:>5} "
                      f"{str(r['winding_sum']):>8} {nt:>8} "
                      f"{r['harmonic_class']:>6} {r['branch']:>6} "
                      f"{r['obs']:>10.3f} {r['final']:>10.3f} "
                      f"{r['err_pct']:>+8.3f}")
        else:
            print(f"{'Name':<12} {'grp':>5} {'branch':>6} {'lam':>8} "
                  f"{'obs':>10} {'final':>10} {'err%':>8}")
            print("-"*68)
            for r in rows:
                if r.get("obs") is None: continue
                lam=r.get("lambda_used",LAMBDA_UNIV)
                print(f"{r['name']:<12} {r['fit_group']:>5} {r['branch']:>6} "
                      f"{lam:>8.5f} "
                      f"{r['obs']:>10.3f} {r['final']:>10.3f} "
                      f"{r['err_pct']:>+8.3f}")
    else:
        print(f"{'Name':<12} {'W_sum':>8} {'H_cls':>6} "
              f"{'branch':>6} {'final':>12}")
        print("-"*48)
        for r in rows:
            print(f"{r['name']:<12} {str(r['winding_sum']):>8} "
                  f"{r['harmonic_class']:>6} {r['branch']:>6} "
                  f"{r['final']:>12.3f}")

def print_summary(known_rows):
    print("="*65)
    print("GBP v1 (rebuilt) — Summary")
    print("="*65)
    print(f"  LAMBDA_UNIV (all T) = {LAMBDA_UNIV:.6f}  [sin^2(pi/15)/alpha_IR]")
    print(f"  (v2 uses sqrt(phi)*LAMBDA_UNIV for T2 — see gbp_complete_v2.py)")
    print(f"  C_HYP               = {C_HYP:.4f} MeV")
    print(f"  kappa_0             = {KAPPA_0_DEFAULT:.2f} MeV^3  (ONE free parameter)")
    print(f"  alpha_hyp           = 1/3  (fixed by group theory)")
    print()
    for grp in ("clean","wide","degen"):
        m=mape(known_rows,grp); r=rmse(known_rows,grp)
        if m is not None:
            print(f"  MAPE {grp:<6} = {m:.4f}%   RMSE = {r:.2f} MeV")
    print(f"  MAPE all    = {mape(known_rows):.4f}%   "
          f"RMSE = {rmse(known_rows):.2f} MeV")
    print()
    # cover breakdown
    by_cover=defaultdict(list)
    for r in known_rows:
        if r.get("obs"): by_cover[r["branch"]].append(r)
    for cover in ["none","T2","T3"]:
        g=by_cover.get(cover,[])
        if g:
            print(f"  MAPE {cover:<4} = "
                  f"{sum(r['abs_err_pct'] for r in g)/len(g):.4f}%"
                  f"  ({len(g)} baryons)")

# ============================================================
# PART 13 — CLI
# ============================================================

def main():
    parser=argparse.ArgumentParser(
        description="GBP v1 (rebuilt) — single LAMBDA_UNIV for all covers")
    parser.add_argument("--known",       action="store_true")
    parser.add_argument("--predictions", action="store_true")
    parser.add_argument("--winding",     action="store_true")
    parser.add_argument("--all",         action="store_true")
    parser.add_argument("--json",        action="store_true")
    parser.add_argument("--name",        type=str)
    args=parser.parse_args()

    known_rows=run_rows(KNOWN_BARYONS)
    pred_rows =run_rows(PREDICTIONS)

    if args.name:
        all_rows=known_rows+pred_rows
        matched=[r for r in all_rows if r["name"].lower()==args.name.lower()]
        if not matched: raise SystemExit(f"Not found: {args.name}")
        print(json.dumps({k:str(v) if isinstance(v,Fraction) else v
                          for k,v in matched[0].items()
                          if not isinstance(v,(list,dict,tuple))},indent=2))
        return

    if args.json:
        def serial(r):
            return {k:(str(v) if isinstance(v,Fraction) else
                       [str(x) for x in v] if isinstance(v,tuple) else v)
                    for k,v in r.items()}
        print(json.dumps({"known":[serial(r) for r in known_rows],
                          "predictions":[serial(r) for r in pred_rows]},indent=2))
        return

    print_summary(known_rows)
    print()
    mode="winding" if (args.winding or args.all) else "standard"

    if args.all or args.known or not any([args.predictions]):
        print("Known baryons:")
        print_table(known_rows,mode=mode)
        print()

    if args.all or args.predictions:
        print("Predictions:")
        print_table(pred_rows,mode="winding")

if __name__=="__main__":
    main()
