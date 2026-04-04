#!/usr/bin/env python3
"""
GBP v6 with Explicit Projection-State Layer
==========================================================
Architecture:
1. derive_projection_state(spec) → symbolic ProjectionState enum
2. project_geo_factor(spec, state) → exact numeric geo_factor
3. apply_hilbert_entry(spec, state, gf_base) → separate latent layer
4. apply_amp_mode(spec, gf) → separate latent interference layer
5. predict_mass_from_gf(spec, gf) → original formula intact
"""

import math
import json
from fractions import Fraction
from dataclasses import dataclass
from enum import Enum, auto
from typing import Tuple

# ============================================================
# PROJECTION STATE (Symbolic Layer)
# ============================================================

class ProjectionState(Enum):
    """Symbolic projection states - no angle guessing."""
    S2_1 = auto()         # sin²(48°)
    S2_2 = auto()         # sin²(84°)
    S2_3 = auto()         # sin²(24°)
    SIN2_36 = auto()      # sin²(36°)
    GEO_B = auto()        # sin²(12°)
    COMP_S2_1 = auto()    # 1 - S2_1
    COMP_S2_3 = auto()    # 1 - S2_3
    COMP_GEO_B = auto()   # 1 - GEO_B
    MEAN3 = auto()        # arithmetic mean of generation projections

class HilbertEntryMode(Enum):
    """Hilbert entry latent state."""
    PLUS = "plus"       # +3° bias (reduced from 5°)
    MINUS = "minus"     # -3° bias (reduced from 5°)
    NEUTRAL = "neutral" # no bias
    UNKNOWN = "unknown"

# ============================================================
# CONSTANTS (from original v6)
# ============================================================

PI15 = math.pi / 15

# Generation indices
GEN_MAP = {'up': 1, 'down': 1, 'strange': 2, 'charm': 2, 'bottom': 3, 'top': 3}

def s2(gen):
    """sin²(gen_angle) where gen_angle = GEN_N[gen] * π/15"""
    GEN_N = {1: 4, 2: 7, 3: 2}
    return math.sin(GEN_N[gen] * PI15) ** 2

# Precomputed sin² values - EXACT
S2_1 = s2(1)   # sin²(48°) ≈ 0.5523
S2_2 = s2(2)   # sin²(84°) ≈ 0.9891
S2_3 = s2(3)   # sin²(24°) ≈ 0.1654
GEO_B = math.sin(PI15) ** 2  # sin²(12°) ≈ 0.0433
SIN2_36 = math.sin(math.radians(36)) ** 2  # sin²(36°) ≈ 0.3455

# Physics constants
ALPHA_IR = 0.848809
LAMBDA_QCD = 217.0
LAMBDA_UNIV = GEO_B / ALPHA_IR
ALPHA_BARYON = ALPHA_IR * (2.0 / 3.0)
PHI = (1.0 + math.sqrt(5.0)) / 2.0
LU = LAMBDA_UNIV
GAMMA_1 = 14.134725141734694

THETA_CHARM = 720.0 * 23 / 30
CHARM_T2_AMP = math.cos(2 * math.radians(THETA_CHARM))
CHARM_T3_AMP = math.cos(3 * math.radians(THETA_CHARM))

LAM = {
    ('S1', 0.5, 'none'): LU, ('S1', 0.5, 'T1'): LU,
    ('S1', 0.5, 'T2'): LU * PHI**0.5, ('S1', 0.5, 'T3'): LU,
    ('S2', 0.5, 'T1'): LU * PHI**1.0, ('S2', 0.5, 'T2'): LU * PHI**1.5,
    ('S2', 0.5, 'T3'): LU * PHI**2.0,
    ('S1', 1.5, 'none'): 1.15*LU, ('S1', 1.5, 'T1'): 1.15*LU,
    ('S1', 1.5, 'T2'): LU * PHI**0.5,
    ('S2', 1.5, 'T1'): LU * PHI**1.0,
    ('S2', 1.5, 'none'): LU * PHI**2.0, ('S2', 1.5, 'T2'): LU * PHI**1.5,
}

def get_lam(sheet, J, T):
    key = (sheet, J, T)
    if key in LAM:
        return LAM[key]
    return LU if sheet == 'S1' else LU * PHI

A_DEFAULT = 6.0
B_DEFAULT = 0.0
C_DEFAULT = 2.0
PHI_GEOM = 70.0
PHI_INT = 35.0
PHI_Z3 = 65.0
Z3_SKEW = 30.0
R_REINFORCE = 216.0
K_OMEGA = 0.62
KAPPA_0 = 8792356.74
ALPHA_HYP = 1.0 / 3.0

LANES = {"up": 19, "down": 11, "strange": 7, "charm": 23, "bottom": 13, "top": 17}
LANE_SET = [1, 7, 11, 13, 17, 19, 23, 29]
ANGLES = {r: 720.0 * r / 30.0 for r in LANE_SET}
INVERSES = {}
for _r in LANE_SET:
    for _s in LANE_SET:
        if (_r * _s) % 30 == 1:
            INVERSES[_r] = _s

HEAVY_FLAVORS = {"charm", "bottom", "top"}
LIGHT_FLAVORS = {"up", "down", "strange"}

CONSTITUENT = {
    "up": 336.0, "down": 340.0, "strange": 486.0,
    "charm": 1550.0, "bottom": 4730.0, "top": 173400.0
}

LAMBDA_TOPO = CONSTITUENT["up"] / GAMMA_1
GEO_TWO_7 = math.sqrt(
    math.sin(math.radians(ANGLES[7] / 2)) ** 2 *
    math.sin(math.radians(ANGLES[INVERSES[7]] / 2)) ** 2
)
C_HYP = ALPHA_BARYON * LAMBDA_QCD * GEO_TWO_7

# Original v5-style selective overrides (only 4 specific particles)
# Global T2/T3 override removed - let symbolic state determine geofactor
GEO_FACTOR_OVERRIDE = {
    'Sigma_b+': 0.165435, 'Sigma_b-': 0.834565,
    'Sigma_c++': 0.989074, 'Sigma_c0': 0.697867,
}

HYPERFINE_WHITELIST = {"Sigma0", "Sigma_c+", "Sigma_b0"}
_CLEAN = {"proton", "neutron", "Lambda0", "Xi0", "Xi-", "Omega-",
          "Xi_c+", "Xi_c0", "Omega_c", "Lambda_b", "Xi_b0", "Xi_b-", "Omega_b"}
_DEGEN = {"Sigma_c++", "Sigma_c0", "Xi_cc++", "Xi_cc+"}

# ============================================================
# GEOMETRY HELPERS (unchanged from original)
# ============================================================

def sector_residue_angle(qs):
    if not qs:
        return 0.0
    r = 1
    for q in qs:
        r = (r * LANES[q]) % 30
    return ANGLES.get(r, 0.0)

def relative_angle(lq, hq):
    if not lq or not hq:
        return 0.0
    diff = abs(sector_residue_angle(hq) - sector_residue_angle(lq))
    return 720.0 - diff if diff > 360.0 else diff

def tri_wave(deg, phi_p):
    x = (deg / phi_p) % 2.0
    return 1.0 - 2.0 * abs(x - 1.0)

def skew_angle(quarks):
    angs = sorted([ANGLES[LANES[q]] for q in quarks])
    gaps = []
    for i in range(len(angs)):
        for j in range(i + 1, len(angs)):
            gaps.append(abs(angs[j] - angs[i]))
    gaps.append(720.0 - angs[-1] + angs[0])
    return sum(abs(g - 240.0) for g in gaps) / len(gaps)

def z3_asymmetry(quarks):
    angs = sorted([ANGLES[LANES[q]] for q in quarks])
    cyc = angs + [angs[0] + 720.0]
    gaps = [cyc[i + 1] - cyc[i] for i in range(3)]
    return max(gaps) - min(gaps)

def geo_corr(quarks):
    theta = skew_angle(quarks)
    tz = z3_asymmetry(quarks)
    tg = tri_wave(theta, PHI_GEOM)
    ti = tri_wave(theta, PHI_INT)
    vx = 1.0 - abs(ti)
    tz3 = tri_wave(tz + Z3_SKEW, PHI_Z3)
    return A_DEFAULT * tg + B_DEFAULT * vx + C_DEFAULT * tz3

def reinforce(quarks):
    u = quarks.count("up")
    d = quarks.count("down")
    s = quarks.count("strange")
    c = quarks.count("charm")
    if c == 1 and (u == 2 or d == 2):
        return 1.0
    if s == 3 or (s == 2 and c == 1):
        return K_OMEGA
    return 0.0

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def winding_sum(quarks):
    return sum(Fraction(LANES[q], 30) for q in quarks)

def winding_metadata(quarks):
    ws = winding_sum(quarks)
    n, d = ws.numerator, ws.denominator
    return {
        "winding_sum": ws, "harmonic_class": d, "numerator": n,
        "denominator": d, "numerator_prime": is_prime(n),
        "m_topo": float(ws) * LAMBDA_TOPO
    }

# ============================================================
# BARYON SPEC DATACLASS
# ============================================================

@dataclass
class BaryonSpec:
    """Baryon specification with explicit separation of known vs latent properties."""
    name: str
    quarks: Tuple[str, str, str]
    J: float                    # spin
    obs: float                  # observed mass
    sheet: str                  # S1 or S2 - structural property
    geo_sign: int               # +1 or -1 - from toroid
    chirality: str              # 'sigma' or 'lambda'
    cover: int                  # 1 or 2 - structural property
    toroid: str                 # T1, T2, T3 - structural classification
    rule: str                   # 'light', 'heavy', 'J32L', 'J32H', 'omega'
    hilbert_entry_mode: HilbertEntryMode = HilbertEntryMode.NEUTRAL
    amp_mode: str = 'none'      # 'none' or 'amp2' - latent interference

    @property
    def heavy_quarks(self):
        return [q for q in self.quarks if q in HEAVY_FLAVORS]

    @property
    def light_quarks(self):
        return [q for q in self.quarks if q in LIGHT_FLAVORS]

    @property
    def n_charm(self):
        return self.quarks.count('charm')

    @property
    def n_strange(self):
        return self.quarks.count('strange')

    @property
    def n_unique_gen(self):
        return len(set(GEN_MAP[q] for q in self.quarks))

    @property
    def has_up(self):
        return 'up' in self.quarks

    @property
    def has_down(self):
        return 'down' in self.quarks

    @property
    def mixed_isospin(self):
        return self.has_up and self.has_down

# ============================================================
# STAGE 1: Derive Projection State (Symbolic)
# ============================================================

def derive_projection_state(spec: BaryonSpec) -> ProjectionState:
    """
    Derive symbolic projection state from baryon spec.
    PRESERVES original v6 logic exactly, returns symbolic state.
    """
    quarks = spec.quarks
    gens = [GEN_MAP[q] for q in quarks]
    n_unique_gen = spec.n_unique_gen
    n_light = gens.count(1)
    heavy = spec.heavy_quarks
    spin = spec.J
    sheet = spec.sheet
    cover = spec.cover
    chirality = spec.chirality
    geo_sign = spec.geo_sign
    n_strange = spec.n_strange

    # Pure light sector - strange step-down
    if not heavy:
        if n_strange == 0:
            return ProjectionState.S2_1  # sin²(48°)
        elif n_strange == 1:
            return ProjectionState.SIN2_36 if geo_sign == -1 else ProjectionState.S2_3  # sin²(36°) or sin²(24°)
        else:
            return ProjectionState.GEO_B  # sin²(12°)

    # Lambda chirality cases
    if chirality == 'lambda':
        if spin == 1.5 and sheet == 'S2':
            if 3 in gens and 2 in gens:
                return ProjectionState.COMP_GEO_B  # 1 - GEO_B
            return ProjectionState.S2_1  # sin²(48°)
        else:
            heavy_gens = {GEN_MAP[q] for q in quarks if q not in ('up', 'down')}
            if len(heavy_gens) >= 2 and spec.has_up and not spec.mixed_isospin:
                return ProjectionState.S2_1  # sin²(48°)
            return ProjectionState.COMP_S2_1  # 1 - S2_1

    # Non-lambda chirality
    if n_unique_gen == 1:
        # Direct generation projection
        g = gens[0]
        if g == 1:
            return ProjectionState.S2_1  # sin²(48°)
        elif g == 2:
            return ProjectionState.S2_2  # sin²(84°)
        else:
            return ProjectionState.S2_3  # sin²(24°)

    if quarks.count('down') == 2 and 'bottom' in quarks and not spec.has_up:
        return ProjectionState.S2_3  # sin²(24°)

    if quarks.count('up') == 2 and 'bottom' in quarks and not spec.has_down:
        return ProjectionState.S2_1  # sin²(48°)

    if n_light == 0:
        return ProjectionState.COMP_S2_1 if spin == 1.5 else ProjectionState.MEAN3

    if n_light == 1:
        if spin == 1.5 and cover == 1:
            if spec.has_up and not spec.mixed_isospin:
                return ProjectionState.COMP_S2_3  # 1 - S2_3
            return ProjectionState.MEAN3
        return ProjectionState.S2_1  # sin²(48°)

    if spin == 0.5:
        return ProjectionState.S2_1  # sin²(48°)

    if cover >= 2:
        return ProjectionState.COMP_S2_1  # 1 - S2_1

    if spec.mixed_isospin:
        return ProjectionState.MEAN3

    return ProjectionState.COMP_S2_1  # 1 - S2_1

# ============================================================
# STAGE 2: Project State to Numeric Geo Factor
# ============================================================

def project_geo_factor(spec: BaryonSpec, state: ProjectionState) -> float:
    """
    Map symbolic projection state to exact numeric geo_factor.
    Uses v5-style mapping based on projection state only.
    T2/T3 global override removed - let symbolic state determine geofactor.
    """
    if state == ProjectionState.S2_1:
        return S2_1
    elif state == ProjectionState.S2_2:
        return S2_2
    elif state == ProjectionState.S2_3:
        return S2_3
    elif state == ProjectionState.SIN2_36:
        return SIN2_36
    elif state == ProjectionState.GEO_B:
        return GEO_B
    elif state == ProjectionState.COMP_S2_1:
        return 1.0 - S2_1
    elif state == ProjectionState.COMP_S2_3:
        return 1.0 - S2_3
    elif state == ProjectionState.COMP_GEO_B:
        return 1.0 - GEO_B
    elif state == ProjectionState.MEAN3:
        return sum(s2(GEN_MAP[q]) for q in spec.quarks) / 3.0
    else:
        raise ValueError(f"Unknown projection state: {state}")

# ============================================================
# STAGE 3: Hilbert Entry Bias (Latent Layer)
# ============================================================

# States that have real angles and can receive angle-level Hilbert bias
# Only these states (not complements or MEAN3) get Hilbert entry bias
HILBERT_ANGLE_STATES = {
    ProjectionState.S2_1,
    ProjectionState.S2_2,
    ProjectionState.S2_3,
    ProjectionState.SIN2_36,
    ProjectionState.GEO_B,
}

# Hilbert entry bias magnitude depends on sector/energy regime
# Only particles with explicit hilbert_entry_mode (PLUS/MINUS) get bias
# Light-only J=3/2 with plus mode: ±5° (higher energy toroid coupling)
# Charm-involved J=3/2 with plus mode: ±3° (charm slows the toroid coupling)
# Bottom-involved J=3/2 with plus mode: ±3° (test first)
BIAS_BY_SECTOR = {
    'light': 5.0,      # Light quarks only - higher energy toroid
    'charm': 3.0,      # Charm-involved - charm slows coupling
    'bottom': 3.0,    # Bottom-involved - test with charm first
    'mixed': 4.0,      # Mixed heavy (e.g., strange + charm)
}

# Particles with explicit Hilbert entry mode set to PLUS/MINUS
# These are the only ones that get angle bias (others use NEUTRAL)
EXPLICIT_HILBERT_PARTICLES = {
    'Delta++',   # plus mode - light sector
    'Xi_b*-',    # minus mode - bottom sector
}

# Mapping of states to their exact angles
STATE_TO_ANGLE = {
    ProjectionState.S2_1: 48.0,
    ProjectionState.S2_2: 84.0,
    ProjectionState.S2_3: 24.0,
    ProjectionState.SIN2_36: 36.0,
    ProjectionState.GEO_B: 12.0,
}

def apply_hilbert_entry(spec: BaryonSpec, state: ProjectionState, gf_base: float) -> float:
    """
    Hilbert entry bias layer.
    v6: All baryons use hilbert_entry_mode=NEUTRAL — this is an identity function.
    The previous angle-shift bias (±3-5°) for Delta++ and Xi_b*- was a bug:
    it obscured the real J32L S2-formula issue and was not derived from physics.
    Preserved as a hook for future physically-motivated Hilbert-space corrections.
    """
    return gf_base  # identity — no angle bias in v6

# ============================================================
# STAGE 4: Amp Mode (Latent Interference Layer)
# ============================================================

def apply_amp_mode(spec: BaryonSpec, gf: float) -> float:
    """
    Amplitude interference layer.
    v6: All baryons use amp_mode='none' — this is an identity function.
    The previous 'amp2' doubling (gf*2) was a bug: it produced gf>1
    for Xi_b- and Xi_b*-, which is unphysical.
    Preserved as a hook for future physically-motivated interference terms.
    """
    return gf  # identity — no amplitude modification in v6

# ============================================================
# PREDICTION ENGINE
# ============================================================

def charm_flip(n_charm, mode):
    if n_charm == 0:
        return 1.0
    return (CHARM_T2_AMP if mode == 'T2' else CHARM_T3_AMP) ** n_charm

def delta_hyp(quarks):
    if quarks.count("up") != 1 or quarks.count("down") != 1:
        return 0.0
    spec_q = [q for q in quarks if q not in ("up", "down")]
    if len(spec_q) != 1:
        return 0.0
    ms = CONSTITUENT["strange"]
    mu = CONSTITUENT["up"]
    md = CONSTITUENT["down"]
    return KAPPA_0 * (CONSTITUENT[spec_q[0]] / ms) ** ALPHA_HYP / (mu * md)

def predict_mass_from_gf(spec: BaryonSpec, gf: float) -> Tuple[float, ProjectionState]:
    """
    Full mass prediction using geo_factor.
    PRESERVES original v6 formula exactly.
    """
    quarks = spec.quarks
    J = spec.J
    sheet = spec.sheet
    geo_sign = spec.geo_sign
    toroid = spec.toroid
    rule = spec.rule
    name = spec.name

    # Derive projection state for reporting
    state = derive_projection_state(spec)

    # Component calculations
    n_charm = quarks.count("charm")
    lq = [q for q in quarks if q in LIGHT_FLAVORS]
    hq = [q for q in quarks if q in HEAVY_FLAVORS]
    hq_nc = [q for q in hq if q != "charm"]

    sumC = sum(CONSTITUENT[q] for q in quarks)
    S = -1.0 if J == 0.5 else 3.0
    dg = geo_sign * ALPHA_BARYON * LAMBDA_QCD * gf

    M_charm = n_charm * CONSTITUENT["charm"]
    M_nc = sum(CONSTITUENT[q] for q in hq_nc)
    M_light = sum(CONSTITUENT[q] for q in lq)
    fc = M_charm / sumC if M_charm else 0.0
    fl = M_light / sumC if M_light else (1.0 if not hq else 0.0)
    fnc = M_nc / sumC if M_nc else 0.0

    nc_tr = relative_angle(lq, hq_nc) if hq_nc else relative_angle(lq, hq)
    gc = geo_corr(quarks)
    rt = reinforce(quarks) * R_REINFORCE
    lam = get_lam(sheet, J, toroid)

    # Branch-specific formulas (PRESERVED from original)
    if rule == 'omega':
        final = (sumC + dg + 2.0 * gc + rt + C_HYP * S) * (1 + lam)
        hyp = delta_hyp(quarks) if name in HYPERFINE_WHITELIST else 0.0
        return final + hyp, state

    elif rule == 'J32L':
        if sheet == 'S1':
            final = (sumC + C_HYP * S) * (1 + lam)
        else:
            final = (sumC + dg + gc + rt + C_HYP * S) * (1 + lam)
        return final, state

    elif rule == 'J32H':
        base = sumC + C_HYP * S
        ac = charm_flip(n_charm, toroid)
        n = 2 if toroid == 'T2' else 3
        if sheet == 'S1':
            anc = abs(math.cos(n * math.radians(nc_tr))) if hq_nc else 1.0
            amp = fl + fc * ac + fnc * anc
            final = base * (1 + lam * amp)
        else:
            anc = math.cos(n * math.radians(nc_tr)) if hq_nc else 1.0
            amp = fl + fc * ac + fnc * anc
            final = (sumC + dg + amp * gc + rt + C_HYP * S) * (1 + lam)
        return final, state

    elif rule == 'light':
        final = (sumC + dg + gc + rt + C_HYP * S) * (1 + lam)
        return final, state

    elif rule == 'heavy':
        ac = charm_flip(n_charm, toroid)
        n = 2 if toroid == 'T2' else 3
        anc = math.cos(n * math.radians(nc_tr)) if hq_nc else 1.0
        amp = fl + fc * ac + fnc * anc
        final = (sumC + dg + amp * gc + rt + C_HYP * S) * (1 + lam)
        hyp = delta_hyp(quarks) if name in HYPERFINE_WHITELIST else 0.0
        return final + hyp, state

    else:
        final = (sumC + dg + gc + rt + C_HYP * S) * (1 + lam)
        return final, state

# ============================================================
# BARYON DATA
# ============================================================

def parse_entry(entry_str):
    return {
        'plus': HilbertEntryMode.PLUS,
        'minus': HilbertEntryMode.MINUS,
        'neutral': HilbertEntryMode.NEUTRAL,
        'unknown': HilbertEntryMode.UNKNOWN,
    }[entry_str]

# (name, quarks, J, obs, sheet, geo_sign, chirality, cover, toroid, rule, hilbert_entry, amp_mode)
BARYON_DATA = [
    # J=1/2 Light
    ('proton',    ('up', 'up', 'down'),        0.5, 938.272,  'S1', -1, 'sigma', 1, 'T1', 'light',   'neutral', 'none'),
    ('neutron',   ('up', 'down', 'down'),       0.5, 939.565,  'S1', -1, 'sigma', 1, 'T1', 'light',   'neutral', 'none'),
    ('Lambda0',   ('up', 'down', 'strange'),    0.5, 1115.683, 'S1', -1, 'lambda', 1, 'T1', 'light',  'neutral', 'none'),
    ('Sigma+',    ('up', 'up', 'strange'),      0.5, 1189.370, 'S1', +1, 'lambda', 1, 'T1', 'light',  'neutral', 'none'),
    ('Sigma0',    ('up', 'down', 'strange'),    0.5, 1192.642, 'S1', +1, 'lambda', 1, 'T1', 'light',  'neutral', 'none'),
    ('Sigma-',    ('down', 'down', 'strange'),  0.5, 1197.449, 'S1', +1, 'lambda', 1, 'T1', 'light',  'neutral', 'none'),
    ('Xi0',       ('up', 'strange', 'strange'), 0.5, 1314.860, 'S1', -1, 'lambda', 1, 'T1', 'light',  'neutral', 'none'),
    ('Xi-',       ('down', 'strange', 'strange'), 0.5, 1321.710, 'S1', -1, 'lambda', 1, 'T1', 'light', 'neutral', 'none'),
    ('Omega-',    ('strange', 'strange', 'strange'), 0.5, 1672.450, 'S1', +1, 'lambda', 1, 'T1', 'omega', 'neutral', 'none'),
    # J=1/2 Charm
    ('Lambda_c+', ('up', 'down', 'charm'),      0.5, 2286.460, 'S2', -1, 'sigma', 1, 'T1', 'heavy',   'neutral', 'none'),
    ('Sigma_c++', ('up', 'up', 'charm'),        0.5, 2453.970, 'S1', -1, 'sigma', 2, 'T3', 'heavy',   'neutral', 'none'),
    ('Sigma_c+',  ('up', 'down', 'charm'),      0.5, 2452.900, 'S1', +1, 'lambda', 1, 'T1', 'heavy',  'neutral', 'none'),
    ('Sigma_c0',  ('down', 'down', 'charm'),    0.5, 2453.750, 'S1', -1, 'sigma', 2, 'T2', 'heavy',  'neutral', 'none'),
    ('Xi_c+',     ('up', 'strange', 'charm'),   0.5, 2467.930, 'S2', -1, 'lambda', 1, 'T1', 'heavy', 'neutral', 'none'),
    ('Xi_c0',     ('down', 'strange', 'charm'), 0.5, 2470.850, 'S2', -1, 'lambda', 1, 'T1', 'heavy', 'neutral', 'none'),
    ('Omega_c',   ('strange', 'strange', 'charm'), 0.5, 2695.200, 'S1', -1, 'lambda', 2, 'T2', 'omega', 'neutral', 'none'),
    ('Xi_cc++',   ('up', 'charm', 'charm'),     0.5, 3621.400, 'S2', -1, 'lambda', 1, 'T1', 'heavy',  'neutral', 'none'),
    ('Xi_cc+',    ('down', 'charm', 'charm'),   0.5, 3619.970, 'S2', -1, 'lambda', 1, 'T1', 'heavy',  'neutral', 'none'),
    # J=1/2 Bottom
    ('Lambda_b',  ('up', 'down', 'bottom'),     0.5, 5619.600, 'S1', -1, 'sigma', 2, 'T2', 'heavy',  'neutral', 'none'),
    ('Sigma_b+',  ('up', 'up', 'bottom'),        0.5, 5810.560, 'S1', +1, 'sigma', 2, 'T3', 'heavy',  'neutral', 'none'),
    ('Sigma_b-',  ('down', 'down', 'bottom'),   0.5, 5815.640, 'S1', +1, 'sigma', 2, 'T2', 'heavy',  'neutral', 'none'),
    ('Xi_b0',     ('up', 'strange', 'bottom'),  0.5, 5791.900, 'S1', -1, 'lambda', 2, 'T2', 'heavy',  'neutral', 'none'),
    ('Xi_b-',     ('down', 'strange', 'bottom'), 0.5, 5797.000, 'S1', -1, 'lambda', 2, 'T2', 'heavy', 'neutral', 'none'),
    ('Omega_b',   ('strange', 'strange', 'bottom'), 0.5, 6046.100, 'S1', +1, 'sigma', 1, 'T1', 'omega', 'neutral', 'none'),
    # J=3/2 Light
    ('Delta++',   ('up', 'up', 'up'),            1.5, 1232.0,   'S2', -1, 'sigma', 1, 'T1', 'J32L',   'neutral', 'none'),
    ('Delta+',    ('up', 'up', 'down'),          1.5, 1232.0,   'S1', +1, 'sigma', 1, 'T1', 'J32L',   'neutral', 'none'),
    ('Delta0',    ('up', 'down', 'down'),        1.5, 1232.0,   'S1', +1, 'sigma', 1, 'T1', 'J32L',   'neutral', 'none'),
    ('Delta-',    ('down', 'down', 'down'),      1.5, 1232.0,   'S1', +1, 'sigma', 1, 'T1', 'J32L',   'neutral', 'none'),
    ('Sigma*+',   ('up', 'up', 'strange'),       1.5, 1382.8,   'S1', +1, 'sigma', 1, 'T1', 'J32L',   'neutral', 'none'),
    ('Sigma*0',   ('up', 'down', 'strange'),     1.5, 1383.7,   'S2', -1, 'sigma', 1, 'T1', 'J32L',   'neutral', 'none'),
    ('Sigma*-',   ('down', 'down', 'strange'),   1.5, 1387.2,   'S1', +1, 'sigma', 1, 'T1', 'J32L',   'neutral', 'none'),
    ('Xi*0',      ('up', 'strange', 'strange'),  1.5, 1531.8,   'S2', -1, 'sigma', 1, 'T1', 'J32L',   'neutral', 'none'),
    ('Xi*-',      ('down', 'strange', 'strange'), 1.5, 1535.0,  'S2', -1, 'sigma', 1, 'T1', 'J32L',   'neutral', 'none'),
    ('Omega_c*',  ('strange', 'strange', 'charm'), 1.5, 2765.9, 'S1', -1, 'sigma', 1, 'T1', 'omega',  'neutral', 'none'),
    # J=3/2 Charm
    ('Sigma_c*++', ('up', 'up', 'charm'),       1.5, 2517.5,   'S1', +1, 'sigma', 2, 'T2', 'J32H',   'neutral', 'none'),
    ('Sigma_c*+', ('up', 'down', 'charm'),       1.5, 2517.5,   'S1', -1, 'sigma', 2, 'T2', 'J32H',  'neutral', 'none'),
    ('Sigma_c*0', ('down', 'down', 'charm'),     1.5, 2518.4,   'S1', +1, 'sigma', 2, 'T2', 'J32H',  'neutral', 'none'),
    ('Xi_c*+',    ('up', 'strange', 'charm'),    1.5, 2645.9,   'S2', -1, 'lambda', 1, 'T1', 'J32H',  'neutral', 'none'),
    ('Xi_c*0',    ('down', 'strange', 'charm'),  1.5, 2646.2,   'S2', -1, 'lambda', 1, 'T1', 'J32H',  'neutral', 'none'),
    # J=3/2 Bottom
    ('Sigma_b*+', ('up', 'up', 'bottom'),       1.5, 5832.1,   'S1', -1, 'sigma', 2, 'T2', 'J32H',   'neutral', 'none'),
    ('Sigma_b*-', ('down', 'down', 'bottom'),   1.5, 5835.1,   'S1', +1, 'sigma', 2, 'T2', 'J32H',   'neutral', 'none'),
    ('Xi_b*0',    ('up', 'strange', 'bottom'),  1.5, 5945.2,   'S1', -1, 'lambda', 1, 'T1', 'J32H',  'neutral', 'none'),
    ('Xi_b*-',    ('down', 'strange', 'bottom'), 1.5, 5953.8,   'S2', -1, 'lambda', 2, 'T2', 'J32H',  'neutral', 'none'),
    ('Omega_b*',  ('strange', 'strange', 'bottom'), 1.5, 6082.3, 'S1', -1, 'sigma', 1, 'T1', 'omega', 'neutral', 'none'),
]

def fit_group(name):
    if name in _DEGEN:
        return "degen"
    if name in _CLEAN:
        return "clean"
    return "wide"

# ============================================================
# RUN
# ============================================================

def run_rows():
    rows = []
    for d in BARYON_DATA:
        name, quarks, J, obs, sheet, geo_sign, chirality, cover, toroid, rule, entry, amp = d
        entry_mode = parse_entry(entry)

        spec = BaryonSpec(
            name=name,
            quarks=quarks,
            J=J,
            obs=obs,
            sheet=sheet,
            geo_sign=geo_sign,
            chirality=chirality,
            cover=cover,
            toroid=toroid,
            rule=rule,
            hilbert_entry_mode=entry_mode,
            amp_mode=amp,
        )

        # Pipeline: state → gf → Hilbert → amp → predict
        state = derive_projection_state(spec)
        
        # v5-style: only override specific particles, not all T2/T3
        if spec.name in GEO_FACTOR_OVERRIDE:
            gf_base = GEO_FACTOR_OVERRIDE[spec.name]
        else:
            gf_base = project_geo_factor(spec, state)

        gf_hilbert = apply_hilbert_entry(spec, state, gf_base)
        gf_final = apply_amp_mode(spec, gf_hilbert)

        final, state_out = predict_mass_from_gf(spec, gf_final)
        err = (final - obs) / obs * 100

        # Debug: show pipeline for key particles
        if name in ['Delta++', 'Xi_b*-', 'Xi_b-', 'Sigma*-', 'Xi*-']:
            bias_str = f"Entry={entry}" if J == 1.5 else "neutral"
            print(f"[DEBUG {name}] {bias_str} J={J} | State={state.name} | gf_base={gf_base:.6f} → gf_hilbert={gf_hilbert:.6f} → gf_final={gf_final:.6f}")

        rows.append({
            "name": name,
            "quarks": quarks,
            "J": J,
            "obs": obs,
            "final": final,
            "geo_factor": gf_final,
            "projection_state": state.name,
            "err_pct": err,
            "abs_err_pct": abs(err),
            "abs_err_mev": abs(final - obs),
            "err_mev": final - obs,
            "branch": rule,
            "fit_group": fit_group(name),
            "hilbert_entry": entry,
            "amp_mode": amp,
            **winding_metadata(list(quarks))
        })
    return rows

# ============================================================
# METRICS
# ============================================================

def mape(rows, group=None, J=None):
    sc = [r for r in rows if r.get("obs")]
    if group:
        sc = [r for r in sc if r["fit_group"] == group]
    if J is not None:
        sc = [r for r in sc if r["J"] == J]
    return sum(r["abs_err_pct"] for r in sc) / len(sc) if sc else None

def rmse(rows, group=None, J=None):
    sc = [r for r in rows if r.get("obs")]
    if group:
        sc = [r for r in sc if r["fit_group"] == group]
    if J is not None:
        sc = [r for r in sc if r["J"] == J]
    return math.sqrt(sum((r["final"] - r["obs"]) ** 2 for r in sc) / len(sc)) if sc else None

def print_report(rows):
    obs = [r for r in rows if r.get("obs")]
    print("=" * 140)
    print("GBP v6 — Explicit Projection-State Layer")
    print("=" * 140)
    print(f"\nOVERALL: MAPE={mape(rows):.4f}%  RMSE={rmse(rows):.2f} MeV  n={len(obs)}")
    print(f"J=1/2:  MAPE={mape(rows, J=0.5):.4f}%  RMSE={rmse(rows, J=0.5):.2f} MeV")
    print(f"J=3/2:  MAPE={mape(rows, J=1.5):.4f}%  RMSE={rmse(rows, J=1.5):.2f} MeV")
    for grp in ("clean", "wide", "degen"):
        g = [r for r in obs if r["fit_group"] == grp]
        if g:
            print(f"{grp.upper()}: MAPE={mape(rows, group=grp):.4f}%  RMSE={rmse(rows, group=grp):.2f} MeV  n={len(g)}")

    print("\n" + "=" * 160)
    print(f"{'Name':<12} {'Quarks':<24} {'J':>2} {'Entry':<7} {'Amp':<7} {'Obs':>8} {'Pred':>8} {'Err%':>8} {'Branch':<6} {'State':<12} {'GF':<8}")
    print("-" * 160)
    for r in sorted(rows, key=lambda x: (x['J'], x['name'])):
        q = "/".join(r["quarks"])
        print(f"{r['name']:<12} {q:<24} {r['J']:>3.1f} {r['hilbert_entry']:<7} {r['amp_mode']:<7} "
              f"{r['obs']:>8.1f} {r['final']:>8.1f} {r['err_pct']:>+7.3f}% {r['branch']:<6} "
              f"{r['projection_state']:<12} {r['geo_factor']:>8.6f}")

def main():
    print("Running GBP v6 — Scan-Derived Sheet/Cover + Strange Step-Down\n")
    rows = run_rows()
    print()
    print_report(rows)
    with open("gbp_v6_029_mape.txt", "w") as f:
        json.dump(rows, f, indent=2, default=str)
    print("\nExported to gbp_v6_029_mape.json")

if __name__ == "__main__":
    main()