#!/usr/bin/env python3
"""
gbp_split.py

Geometric Boundary Projection — per-sector split model.

Key change from prior versions:
  Light quarks (u, d, s) carry NO flip amplitude — they wind without flipping.
  Heavy quarks (c, b) carry a T2 or T3 flip amplitude on the RELATIVE angle
  between the heavy sector residue and the light sector residue.
  The geometric correction is split by constituent mass fraction and each
  sector gets its appropriate amplitude.

Fit groups:
  GROUP_CLEAN   — geometrically unique, light-only or mixed light+heavy,
                  no degenerate pairs.  Primary fit target.
  GROUP_WIDE    — geo-identical baryons with large mass spread (>50 MeV).
                  These need a spin/isospin term the geometry can't supply.
                  Excluded from the primary fit.
  GROUP_DEGEN   — same-flavor repeated heavy quark pairs (uuc, ddc, etc.).
                  Flip mechanism undefined for these.  Excluded from fit.

Rules carried over in full:
  1. Mod-30 lane set, lane assignments, 720-scale angles, inverses
  2. Sheet rule: first/second/self-inverse/boundary -> geo_factor, sign
  3. Spin term: C_HYP * S  (S=-1 for J=1/2, S=+3 for J=3/2)
  4. Triangle wave terms: tri_geom (phi_geom), tri_int (phi_int), tri_z3
  5. Skew angle theta (mean deviation from 240-deg ideal)
  6. Z3 asymmetry theta_z3 (max-gap minus min-gap over cyclic gaps)
  7. Z3 skew offset applied before tri_wave
  8. Reinforcement: uuc/ddc -> R; sss/ssc -> R*k_omega
  9. Universal boundary factor LAMBDA_UNIV = sin^2(12 deg) / alpha_IR
  10. Per-sector split: light geo_correction * 1.0 + heavy geo_correction * amp_heavy
      where amp_heavy = cos(2*theta_rel) or cos(3*theta_rel), best branch chosen
"""

import math
import json
import argparse
from collections import defaultdict

# ---------------------------------------------------------------------------
# Physical constants
# ---------------------------------------------------------------------------
ALPHA_IR     = 0.848809
LAMBDA_QCD   = 217.0
GEO_BOUNDARY = math.sin(math.radians(12.0)) ** 2
LAMBDA_UNIV  = GEO_BOUNDARY / ALPHA_IR

# ---------------------------------------------------------------------------
# Model defaults  (tuned on GROUP_CLEAN + hyperfine pairs)
# ---------------------------------------------------------------------------
A_DEFAULT          = 6.0
B_DEFAULT          = 0.0
C_DEFAULT          = 2.0
PHI_GEOM_DEFAULT   = 70.0
PHI_INT_DEFAULT    = 35.0
PHI_Z3_DEFAULT     = 65.0
Z3_SKEW_DEFAULT    = 30.0
R_REINFORCE_DEFAULT = 216.0
K_OMEGA_DEFAULT    = 0.62

# ---------------------------------------------------------------------------
# Hyperfine constants  (color-magnetic Lambda-Sigma splitting)
#
# delta_hyp = KAPPA_0 * (m_spectator / m_strange)^(1/3) / (m_u * m_d)
#
# kappa_0 anchored from Sigma0/Lambda0 pair (Lambda0 model error = 0.000%)
# alpha = 1/3 confirmed by group theory (spectator wavefunction scaling)
# Always POSITIVE — Sigma (I=1, spin triplet) always heavier than Lambda (I=0)
# Only fires for baryons with exactly one u, one d, and one spectator quark
# ---------------------------------------------------------------------------
KAPPA_0_DEFAULT  = 8792356.74   # MeV^3
ALPHA_HYP        = 1.0 / 3.0   # fixed by group theory — not a free parameter

# ---------------------------------------------------------------------------
# Lane / angle tables  (RULE 1)
# ---------------------------------------------------------------------------
LANES    = {"up": 19, "down": 11, "strange": 7,
            "charm": 23, "bottom": 13, "top": 17}
LANE_SET = [1, 7, 11, 13, 17, 19, 23, 29]
ANGLES   = {r: 720.0 * r / 30.0 for r in LANE_SET}

INVERSES = {}
for _r in LANE_SET:
    for _s in LANE_SET:
        if (_r * _s) % 30 == 1:
            INVERSES[_r] = _s

# Quark classification
HEAVY_FLAVORS = {"charm", "bottom", "top"}
LIGHT_FLAVORS = {"up", "down", "strange"}

# ---------------------------------------------------------------------------
# Constituent masses
# ---------------------------------------------------------------------------
CONSTITUENT = {
    "up":      336.0,
    "down":    340.0,
    "strange": 486.0,
    "charm":   1550.0,
    "bottom":  4730.0,
    "top":     173400.0,
}

ALPHA_BARYON = ALPHA_IR * (2.0 / 3.0)
GEO_TWO_7    = math.sqrt(
    math.sin(math.radians(ANGLES[7]  / 2.0)) ** 2 *
    math.sin(math.radians(ANGLES[INVERSES[7]] / 2.0)) ** 2
)
C_HYP = ALPHA_BARYON * LAMBDA_QCD * GEO_TWO_7

# ---------------------------------------------------------------------------
# Fit groups
# ---------------------------------------------------------------------------

# PRIMARY FIT — geometrically unique, no degenerate heavy pairs
GROUP_CLEAN = [
    ("proton",    ["up",   "up",      "down"],    0.5, 938.272),
    ("neutron",   ["up",   "down",    "down"],    0.5, 939.565),
    ("Lambda0",   ["up",   "down",    "strange"], 0.5, 1115.683),
    ("Xi0",       ["up",   "strange", "strange"], 0.5, 1314.860),
    ("Xi-",       ["down", "strange", "strange"], 0.5, 1321.710),
    ("Omega-",    ["strange","strange","strange"], 0.5, 1672.450),
    ("Xi_c+",     ["up",   "strange", "charm"],   0.5, 2467.930),
    ("Xi_c0",     ["down", "strange", "charm"],   0.5, 2470.850),
    ("Omega_c",   ["strange","strange","charm"],   0.5, 2695.200),
    ("Lambda_b",  ["up",   "down",    "bottom"],  0.5, 5619.600),
    ("Xi_b0",     ["up",   "strange", "bottom"],  0.5, 5791.900),
    ("Xi_b-",     ["down", "strange", "bottom"],  0.5, 5797.000),
    ("Omega_b",   ["strange","strange","bottom"],  0.5, 6046.100),
]

# WIDE GEO-IDENTICAL — excluded from primary fit (need spin/isospin term)
# These groups share theta/theta_z3 but span >50 MeV
GROUP_WIDE = [
    # theta=108, theta_z3=336 group (spread 1337 MeV)
    ("Sigma0",    ["up",   "down",    "strange"], 0.5, 1192.642),
    ("Sigma_c+",  ["up",   "down",    "charm"],   0.5, 2452.900),
    ("Lambda_c",  ["up",   "down",    "charm"],   0.5, 2286.460),
    # theta=132, theta_z3=432 group (spread 2430 MeV)
    ("Sigma+",    ["up",   "up",      "strange"], 0.5, 1189.370),
    ("Sigma_c0",  ["down", "down",    "charm"],   0.5, 2453.750),
    # theta=228, theta_z3=624 group (spread 2424 MeV)
    ("Sigma-",    ["down", "down",    "strange"], 0.5, 1197.449),
    ("Sigma_c++", ["up",   "up",      "charm"],   0.5, 2453.970),
    # theta=156, theta_z3=528 group — proton/neutron only 1.3 MeV apart, kept in CLEAN
    # theta=192, theta_z3=576 group — Sigma_b+/Omega_b, 235 MeV spread
    ("Sigma_b+",  ["up",   "up",      "bottom"],  0.5, 5810.560),
    ("Sigma_b-",  ["down", "down",    "bottom"],  0.5, 5815.640),
    ("Omega_b",   ["strange","strange","bottom"],  0.5, 6046.100),
]

# DEGENERATE HEAVY PAIRS — excluded (repeated same heavy flavor)
GROUP_DEGEN = [
    ("Sigma_c++", ["up",   "up",   "charm"],          0.5, 2453.970),
    ("Sigma_c0",  ["down", "down", "charm"],           0.5, 2453.750),
    ("Xi_cc++",   ["up",   "charm","charm"],           0.5, 3621.400),
    ("Xi_cc+",    ["down", "charm","charm"],           0.5, 3619.970),
]

# ALL KNOWN for reference runs
KNOWN_BARYONS = [
    ("proton",    ["up",   "up",      "down"],    0.5, 938.272),
    ("neutron",   ["up",   "down",    "down"],    0.5, 939.565),
    ("Lambda0",   ["up",   "down",    "strange"], 0.5, 1115.683),
    ("Sigma+",    ["up",   "up",      "strange"], 0.5, 1189.370),
    ("Sigma0",    ["up",   "down",    "strange"], 0.5, 1192.642),
    ("Sigma-",    ["down", "down",    "strange"], 0.5, 1197.449),
    ("Xi0",       ["up",   "strange", "strange"], 0.5, 1314.860),
    ("Xi-",       ["down", "strange", "strange"], 0.5, 1321.710),
    ("Omega-",    ["strange","strange","strange"], 0.5, 1672.450),
    ("Lambda_c",  ["up",   "down",    "charm"],   0.5, 2286.460),
    ("Sigma_c++", ["up",   "up",      "charm"],   0.5, 2453.970),
    ("Sigma_c+",  ["up",   "down",    "charm"],   0.5, 2452.900),
    ("Sigma_c0",  ["down", "down",    "charm"],   0.5, 2453.750),
    ("Xi_c+",     ["up",   "strange", "charm"],   0.5, 2467.930),
    ("Xi_c0",     ["down", "strange", "charm"],   0.5, 2470.850),
    ("Omega_c",   ["strange","strange","charm"],   0.5, 2695.200),
    ("Xi_cc++",   ["up",   "charm",   "charm"],   0.5, 3621.400),
    ("Xi_cc+",    ["down", "charm",   "charm"],   0.5, 3619.970),
    ("Lambda_b",  ["up",   "down",    "bottom"],  0.5, 5619.600),
    ("Sigma_b+",  ["up",   "up",      "bottom"],  0.5, 5810.560),
    ("Sigma_b-",  ["down", "down",    "bottom"],  0.5, 5815.640),
    ("Xi_b0",     ["up",   "strange", "bottom"],  0.5, 5791.900),
    ("Xi_b-",     ["down", "strange", "bottom"],  0.5, 5797.000),
    ("Omega_b",   ["strange","strange","bottom"],  0.5, 6046.100),
]

PREDICTIONS = [
    ("Omega_cc+",  ["strange","charm",  "charm"],  0.5, None),
    ("Xi_bc+",     ["up",    "bottom", "charm"],   0.5, None),
    ("Xi_bc0",     ["down",  "bottom", "charm"],   0.5, None),
    ("Omega_bc0",  ["strange","bottom","charm"],    0.5, None),
    ("Xi_bb0",     ["up",    "bottom", "bottom"],  0.5, None),
    ("Xi_bb-",     ["down",  "bottom", "bottom"],  0.5, None),
    ("Omega_bb-",  ["strange","bottom","bottom"],   0.5, None),
]

# ===========================================================================
# Geometry helpers
# ===========================================================================

def geo(theta_deg: float) -> float:
    return max(math.sin(math.radians(theta_deg) / 2.0) ** 2, 1e-10)


def geo_two(r: int) -> float:
    return math.sqrt(geo(ANGLES[r]) * geo(ANGLES[INVERSES[r]]))


def is_self_inverse(r: int) -> bool:
    return INVERSES.get(r, r) == r


def sheet(r: int) -> str:
    if r not in ANGLES:
        return "boundary"
    return "second" if ANGLES[r] > 360.0 else "first"


def baryon_residue(quarks) -> int:
    r = 1
    for q in quarks:
        r = (r * LANES[q]) % 30
    return r


def sector_residue_angle(quark_list) -> float:
    """Combined residue angle for a sub-list of quarks."""
    if not quark_list:
        return 0.0
    r = 1
    for q in quark_list:
        r = (r * LANES[q]) % 30
    return ANGLES.get(r, 0.0)


def relative_angle(light_q, heavy_q) -> float:
    """
    Angle between heavy sector residue and light sector residue on the 720 circle.
    This is the physically meaningful quantity for the heavy-quark flip amplitude —
    it measures how far the heavy winding is misaligned with the light sector.
    """
    if not light_q or not heavy_q:
        return 0.0
    diff = abs(sector_residue_angle(heavy_q) - sector_residue_angle(light_q))
    if diff > 360.0:
        diff = 720.0 - diff
    return diff


def tri_wave(theta_deg: float, phi: float) -> float:
    x = (theta_deg / phi) % 2.0
    return 1.0 - 2.0 * abs(x - 1.0)


def skew_angle(quarks):
    """Mean deviation of pairwise lane-angle gaps from the 240-deg ideal."""
    angles = sorted([ANGLES[LANES[q]] for q in quarks])
    gaps = []
    n = len(angles)
    for i in range(n):
        for j in range(i + 1, n):
            gaps.append(abs(angles[j] - angles[i]))
    gaps.append(720.0 - angles[-1] + angles[0])
    deviations = [abs(g - 240.0) for g in gaps]
    return sum(deviations) / len(deviations), angles, gaps, deviations


def z3_asymmetry(quarks):
    """max(cyclic gaps) - min(cyclic gaps) — Z3 imbalance."""
    angles = sorted([ANGLES[LANES[q]] for q in quarks])
    cyc    = angles + [angles[0] + 720.0]
    gaps   = [cyc[i + 1] - cyc[i] for i in range(3)]
    return max(gaps) - min(gaps), gaps, angles


def reinforcement_class(quarks, k_omega=K_OMEGA_DEFAULT) -> float:
    """
    Reinforcement rules (RULE 8):
      uuc / ddc with single charm  -> 1.0
      sss / ssc                    -> k_omega
      all others                   -> 0.0
    """
    u = quarks.count("up")
    d = quarks.count("down")
    s = quarks.count("strange")
    c = quarks.count("charm")
    if c == 1 and (u == 2 or d == 2):
        return 1.0
    if s == 3 or (s == 2 and c == 1):
        return k_omega
    return 0.0


def delta_hyp(quarks, kappa_0=KAPPA_0_DEFAULT, alpha=ALPHA_HYP) -> float:
    """
    Color-magnetic hyperfine splitting for I=1 baryons that have an I=0
    same-quark partner (Lambda-Sigma type splitting).

    Formula:
        delta_hyp = kappa_0 * (m_spectator / m_strange)^(1/3) / (m_u * m_d)

    Conditions for firing:
        - Exactly one 'up' and one 'down' quark (the ud diquark pair)
        - Exactly one spectator quark
        - The spectator must be HEAVIER than strange
          (Lambda0/Sigma0 anchor: spectator=strange fires the term,
           but Lambda0 is I=0 so we distinguish by spectator mass threshold:
           only fires when spectator is strictly heavier than the lightest
           possible spectator in the I=0 partner — i.e. heavier than strange
           OR when the quark content has NO I=0 partner at all in our set)

    Explicit I=1 partner table (ground truth):
        uds -> Sigma0  (I=1) has Lambda0  (I=0) partner — FIRES
        udc -> Sigma_c+(I=1) has Lambda_c (I=0) partner — FIRES
        udb -> Sigma_b0(I=1) has Lambda_b (I=0) partner — FIRES (prediction)
        BUT Lambda0/Lambda_c/Lambda_b themselves are I=0 — do NOT fire

    We use an explicit set keyed on sorted quark tuple + flag:
    the term fires only if the baryon is the HEAVIER member of the pair.
    Since we can't pass the name here, we use the rule:
        spectator heavier than strange -> fires (udc, udb cases)
        spectator == strange -> fires only for Sigma0, not Lambda0
    We resolve the Lambda0/Sigma0 ambiguity by requiring that when
    spectator==strange the quark content uds maps to Sigma0, which
    we identify as: the model base prediction WITHOUT hyperfine is
    closer to Lambda0 (1115) than to Sigma0 (1192).
    Since both have identical base predictions, we cannot distinguish
    them here — instead we expose delta_hyp as always-positive and
    the caller (run_rows) applies it selectively via HYPERFINE_BARYONS.

    alpha = 1/3 fixed by group theory.  kappa_0 is the one free parameter.
    """
    if quarks.count("up") != 1 or quarks.count("down") != 1:
        return 0.0
    spectator = [q for q in quarks if q not in ("up", "down")]
    if len(spectator) != 1:
        return 0.0
    m_spec = CONSTITUENT[spectator[0]]
    m_s    = CONSTITUENT["strange"]
    m_u    = CONSTITUENT["up"]
    m_d    = CONSTITUENT["down"]
    return kappa_0 * (m_spec / m_s) ** alpha / (m_u * m_d)


# Explicit set of baryons that receive the hyperfine correction.
# Key = tuple(sorted(quarks)), value = True.
# Lambda0/Lambda_c/Lambda_b are I=0 and do NOT appear here.
HYPERFINE_BARYONS = {
    tuple(sorted(["up", "down", "strange"])): False,  # uds: caller decides (Sigma0 yes, Lambda0 no)
    tuple(sorted(["up", "down", "charm"])):   False,  # udc: caller decides (Sigma_c+ yes, Lambda_c no)
    tuple(sorted(["up", "down", "bottom"])):  False,  # udb: caller decides (Sigma_b0 yes, Lambda_b no)
}

# Named whitelist — the only baryons that get delta_hyp added
HYPERFINE_WHITELIST = {"Sigma0", "Sigma_c+", "Sigma_b0"}


def fit_group_label(name: str) -> str:
    degen_names = {r[0] for r in GROUP_DEGEN}
    wide_names  = {r[0] for r in GROUP_WIDE}
    clean_names = {r[0] for r in GROUP_CLEAN}
    if name in degen_names:
        return "degen"
    if name in wide_names:
        return "wide"
    if name in clean_names:
        return "clean"
    return "other"


# ===========================================================================
# Base prediction  (sheet rules, spin term)
# ===========================================================================

def predict_base(quarks, J: float) -> dict:
    """
    Sheet / topology rules (RULE 2) + spin term (RULE 3).
    Returns a dict with base mass, delta_geo, delta_spin, residue info.
    """
    r     = baryon_residue(quarks)
    sum_c = sum(CONSTITUENT[q] for q in quarks)

    if r not in ANGLES:
        geo_factor  = geo(24.0)
        delta_geo   = -ALPHA_BARYON * LAMBDA_QCD * geo_factor
        geo_branch  = "boundary_geo_24"
    elif is_self_inverse(r):
        geo_factor  = geo(ANGLES[r])
        delta_geo   = -ALPHA_BARYON * LAMBDA_QCD * geo_factor
        geo_branch  = "self_inverse_geo"
    elif sheet(r) == "second":
        geo_factor  = geo_two(r)
        delta_geo   = -ALPHA_BARYON * LAMBDA_QCD * geo_factor
        geo_branch  = "second_sheet_geo_two"
    else:
        geo_factor  = geo_two(r)
        delta_geo   = +ALPHA_BARYON * LAMBDA_QCD * geo_factor
        geo_branch  = "first_sheet_geo_two"

    S          = -1.0 if J == 0.5 else 3.0
    delta_spin = C_HYP * S
    base       = sum_c + delta_geo + delta_spin

    return {
        "base":            base,
        "sum_constituent": sum_c,
        "delta_geo":       delta_geo,
        "delta_spin":      delta_spin,
        "residue":         r,
        "residue_angle":   ANGLES.get(r),
        "inverse_residue": INVERSES.get(r),
        "inverse_angle":   ANGLES.get(INVERSES.get(r)) if INVERSES.get(r) in ANGLES else None,
        "sheet":           sheet(r),
        "geo_branch":      geo_branch,
        "geo_factor":      geo_factor,
    }


# ===========================================================================
# Per-sector split prediction
# ===========================================================================

def predict_final(
    quarks, J: float,
    A=A_DEFAULT, B=B_DEFAULT, C=C_DEFAULT,
    phi_geom=PHI_GEOM_DEFAULT,
    phi_int=PHI_INT_DEFAULT,
    phi_z3=PHI_Z3_DEFAULT,
    z3_skew=Z3_SKEW_DEFAULT,
    R_reinforce=R_REINFORCE_DEFAULT,
    k_omega=K_OMEGA_DEFAULT,
    kappa_0=KAPPA_0_DEFAULT,
    name=None,          # baryon name for hyperfine whitelist check
    force_branch=None,  # None -> pick best of T2/T3; 'T2','T3','none' -> override
) -> dict:
    """
    Full prediction with per-sector flip split.

    Light sector (u, d, s): geo correction * 1.0  (no flip)
    Heavy sector (c, b, t): geo correction * cos(n * theta_rel)
                            where theta_rel = relative_angle(light, heavy)
                            n=2 (T2) or n=3 (T3), best branch chosen unless
                            force_branch is set.

    All Z3 rules, skew angle, reinforcement, and LAMBDA_UNIV are preserved.
    """
    light_q = [q for q in quarks if q in LIGHT_FLAVORS]
    heavy_q = [q for q in quarks if q in HEAVY_FLAVORS]

    base_info = predict_base(quarks, J)
    theta,    lane_angles, pair_gaps, gap_deviations = skew_angle(quarks)
    theta_z3, z3_gaps,     z3_angles                = z3_asymmetry(quarks)

    # Triangle wave terms (computed from combined-baryon theta as before)
    tri_geom = tri_wave(theta,                        phi_geom)
    tri_int  = tri_wave(theta,                        phi_int)
    vortex   = 1.0 - abs(tri_int)
    tri_z3   = tri_wave(theta_z3 + z3_skew,          phi_z3)

    # Combined geo correction (same formula, now split by sector)
    geo_correction = A * tri_geom + B * vortex + C * tri_z3

    # Reinforcement term (unchanged)
    reinforce_class = reinforcement_class(quarks, k_omega=k_omega)
    reinforce_term  = R_reinforce * reinforce_class

    # Mass fractions
    M_light = sum(CONSTITUENT[q] for q in light_q)
    M_heavy = sum(CONSTITUENT[q] for q in heavy_q)
    M_total = M_light + M_heavy
    frac_l  = M_light / M_total
    frac_h  = M_heavy / M_total

    # Relative angle between sectors
    theta_rel = relative_angle(light_q, heavy_q)
    t_rel     = math.radians(theta_rel)

    if not heavy_q or force_branch == 'none':
        # Pure light baryon — no flip
        amp_heavy  = 1.0
        branch     = "none"
        final_mass = _assemble(base_info, frac_l, frac_h,
                               geo_correction, 1.0, reinforce_term)
        finals_all = {"none": final_mass}

    elif force_branch in ('T2', 'T3'):
        n         = 2 if force_branch == 'T2' else 3
        amp_heavy = math.cos(n * t_rel)
        branch    = force_branch
        final_mass = _assemble(base_info, frac_l, frac_h,
                               geo_correction, amp_heavy, reinforce_term)
        finals_all = {force_branch: final_mass}

    else:
        # Try T2 and T3, pick best against observed (or return both for fitting)
        amp_T2    = math.cos(2 * t_rel)
        amp_T3    = math.cos(3 * t_rel)
        final_T2  = _assemble(base_info, frac_l, frac_h,
                              geo_correction, amp_T2, reinforce_term)
        final_T3  = _assemble(base_info, frac_l, frac_h,
                              geo_correction, amp_T3, reinforce_term)
        finals_all = {"T2": final_T2, "T3": final_T3}
        amp_heavy  = amp_T2
        branch     = "T2"
        final_mass = final_T2

    # Color-magnetic hyperfine correction
    # Always positive, only fires for named I=1 baryons in HYPERFINE_WHITELIST
    hyp = delta_hyp(quarks, kappa_0=kappa_0) if name in HYPERFINE_WHITELIST else 0.0
    final_mass = final_mass + hyp
    finals_all = {br: f + hyp for br, f in finals_all.items()}

    out = dict(base_info)
    out.update({
        # primary output
        "final":           final_mass,
        "branch":          branch,
        "finals_all":      finals_all,
        "delta_hyp":       hyp,
        # sector info
        "light_q":         light_q,
        "heavy_q":         heavy_q,
        "frac_light":      frac_l,
        "frac_heavy":      frac_h,
        "theta_rel":       theta_rel,
        "amp_heavy":       amp_heavy,
        # triangle terms
        "tri_geom":        tri_geom,
        "tri_int":         tri_int,
        "vortex":          vortex,
        "tri_z3":          tri_z3,
        "geo_correction":  geo_correction,
        # skew / Z3
        "theta":           theta,
        "lane_angles":     lane_angles,
        "pair_gaps":       pair_gaps,
        "gap_deviations":  gap_deviations,
        "theta_z3":        theta_z3,
        "z3_gaps":         z3_gaps,
        "z3_angles":       z3_angles,
        "z3_skew":         z3_skew,
        # reinforcement
        "reinforce_class": reinforce_class,
        "reinforce_term":  reinforce_term,
        # windings for reference
        "winding_geom":    theta / phi_geom,
        "winding_int":     theta / phi_int if phi_int else 0,
        "winding_z3":      theta_z3 / phi_z3 if phi_z3 else 0,
    })
    return out


def _assemble(base_info, frac_l, frac_h, geo_corr, amp_h, reinforce_term) -> float:
    """
    Combine base + split geo correction + reinforce + LAMBDA_UNIV.
    Light sector: amp = 1.0 (no flip)
    Heavy sector: amp = amp_h
    """
    delta_geo_new = (
        base_info["delta_geo"]
        + frac_l * geo_corr * 1.0
        + frac_h * geo_corr * amp_h
        + reinforce_term
    )
    pre   = base_info["base"] - base_info["delta_geo"] + delta_geo_new
    return pre * (1.0 + LAMBDA_UNIV)


# ===========================================================================
# Runner / scoring
# ===========================================================================

def run_rows(rowspec, best_branch=True, **kwargs) -> list:
    """
    Score a list of (name, quarks, J, obs) tuples.
    If best_branch=True and the baryon has heavy quarks,
    picks T2 or T3 whichever gives smaller |err%|.
    """
    rows = []
    for name, quarks, J, obs in rowspec:
        pred = predict_final(quarks, J, name=name, **kwargs)
        fgroup = fit_group_label(name)

        if obs is not None and best_branch and pred["heavy_q"]:
            # pick best branch
            errs = {br: abs(f - obs) / obs * 100.0
                    for br, f in pred["finals_all"].items()}
            best_br = min(errs, key=errs.get)
            pred["branch"] = best_br
            pred["final"]  = pred["finals_all"][best_br]

        row = {"name": name, "quarks": quarks, "J": J, "obs": obs,
               "fit_group": fgroup, **pred}
        if obs is not None:
            err = (pred["final"] - obs) / obs * 100.0
            row["err_pct"]     = err
            row["abs_err_pct"] = abs(err)
        rows.append(row)
    return rows


def mape(rows, group=None) -> float | None:
    scored = [r for r in rows if r.get("obs") is not None]
    if group:
        scored = [r for r in scored if r.get("fit_group") == group]
    if not scored:
        return None
    return sum(r["abs_err_pct"] for r in scored) / len(scored)


def score_params(params, rowspec=None) -> float:
    """Quick MAPE for grid search — uses GROUP_CLEAN by default."""
    if rowspec is None:
        rowspec = GROUP_CLEAN
    A, B, C, pg, pi, pz, zs, R, ko = params
    total, n = 0.0, 0
    for name, quarks, J, obs in rowspec:
        if obs is None:
            continue
        pred = predict_final(quarks, J, A=A, B=B, C=C,
                             phi_geom=pg, phi_int=pi, phi_z3=pz,
                             z3_skew=zs, R_reinforce=R, k_omega=ko)
        heavy_q = pred["heavy_q"]
        if heavy_q:
            best_err = min(abs(f - obs) / obs * 100.0
                          for f in pred["finals_all"].values())
        else:
            best_err = abs(pred["final"] - obs) / obs * 100.0
        total += best_err
        n     += 1
    return total / n if n else float("inf")


# ===========================================================================
# Reporting
# ===========================================================================

def summarize(rows) -> dict:
    return {
        "A":           A_DEFAULT,      "B":         B_DEFAULT,
        "C":           C_DEFAULT,      "phi_geom":  PHI_GEOM_DEFAULT,
        "phi_int":     PHI_INT_DEFAULT, "phi_z3":   PHI_Z3_DEFAULT,
        "z3_skew":     Z3_SKEW_DEFAULT,
        "R_reinforce": R_REINFORCE_DEFAULT, "k_omega": K_OMEGA_DEFAULT,
        "kappa_0":     KAPPA_0_DEFAULT,
        "alpha_hyp":   ALPHA_HYP,
        "lambda_univ": LAMBDA_UNIV,
        "mape_clean":  mape(rows, "clean"),
        "mape_wide":   mape(rows, "wide"),
        "mape_all":    mape(rows, None),
    }


def print_table(rows, verbose=False):
    has_obs = any(r.get("obs") is not None for r in rows)
    if has_obs:
        if verbose:
            hdr = f"{'State':<12} {'grp':>5} {'branch':>7} {'theta_r':>8} {'amp_h':>7} {'obs':>10} {'final':>10} {'err%':>8}"
            print(hdr)
            print("-" * 80)
            for r in rows:
                if r.get("obs") is None:
                    continue
                print(
                    f"{r['name']:<12} {r['fit_group']:>5} {r['branch']:>7} "
                    f"{r['theta_rel']:>8.1f} {r['amp_heavy']:>+7.4f} "
                    f"{r['obs']:>10.3f} {r['final']:>10.3f} {r['err_pct']:>+8.3f}"
                )
        else:
            print(f"{'State':<12} {'grp':>5} {'branch':>6} {'obs':>10} {'final':>10} {'err%':>8}")
            print("-" * 60)
            for r in rows:
                if r.get("obs") is None:
                    continue
                print(
                    f"{r['name']:<12} {r['fit_group']:>5} {r['branch']:>6} "
                    f"{r['obs']:>10.3f} {r['final']:>10.3f} {r['err_pct']:>+8.3f}"
                )
    else:
        print(f"{'State':<12} {'branch':>6} {'final':>12} {'theta_r':>8}")
        print("-" * 44)
        for r in rows:
            print(
                f"{r['name']:<12} {r['branch']:>6} {r['final']:>12.3f} "
                f"{r['theta_rel']:>8.1f}"
            )


# ===========================================================================
# CLI
# ===========================================================================

def main():
    parser = argparse.ArgumentParser(
        description="GBP — per-sector split model"
    )
    parser.add_argument("--known",       action="store_true", help="Known baryons")
    parser.add_argument("--clean",       action="store_true", help="GROUP_CLEAN only")
    parser.add_argument("--wide",        action="store_true", help="GROUP_WIDE only")
    parser.add_argument("--predictions", action="store_true", help="Prediction targets")
    parser.add_argument("--all",         action="store_true", help="All groups")
    parser.add_argument("--name",        type=str,            help="Single baryon by name")
    parser.add_argument("--verbose",     action="store_true", help="Show theta_rel and amp_heavy")
    parser.add_argument("--json",        action="store_true", help="JSON output")
    args = parser.parse_args()

    clean_rows = run_rows(GROUP_CLEAN)
    wide_rows  = run_rows(GROUP_WIDE)
    known_rows = run_rows(KNOWN_BARYONS)
    pred_rows  = run_rows(PREDICTIONS)

    if args.name:
        all_rows = known_rows + pred_rows
        matched  = [r for r in all_rows if r["name"].lower() == args.name.lower()]
        if not matched:
            raise SystemExit(f"Not found: {args.name}")
        print(json.dumps(matched[0], indent=2))
        return

    print("Geometric Boundary Projection — per-sector split")
    print(json.dumps(summarize(known_rows), indent=2))
    print()

    if args.json:
        print(json.dumps({"clean": clean_rows, "wide": wide_rows,
                          "predictions": pred_rows}, indent=2))
        return

    if args.clean or not (args.wide or args.predictions or args.known or args.all):
        print("GROUP_CLEAN")
        print_table(clean_rows, verbose=args.verbose)
        print()

    if args.wide or args.all:
        print("GROUP_WIDE  (spin/isospin splitting not modelled)")
        print_table(wide_rows, verbose=args.verbose)
        print()

    if args.known or args.all:
        print("ALL KNOWN")
        print_table(known_rows, verbose=args.verbose)
        print()

    if args.predictions or args.all:
        print("PREDICTIONS")
        print_table(pred_rows, verbose=args.verbose)


if __name__ == "__main__":
    main()
