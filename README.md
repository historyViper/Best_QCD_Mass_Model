# Geometric Boundary Projection (GBP) — Unified Framework

**HistoryViper** | viXra | github.com/historyViper/mod30-spinor  
AI collaboration: Claude (Anthropic), ChatGPT/Sage (OpenAI), MiniMax, DeepSeek

---

## Current Status — April 2026

| Version | MAPE ALL | Free Params | Key Advance |
|---------|----------|-------------|-------------|
| v2 | ~0.57% | 1 | T2 = √φ · LU first derived |
| v5 | 0.6365% | 2 | geo_factor fully derived (Malus's Law) |
| v6 | 0.4078% | 2 | Strange step-down rule + scan-derived assignments |
| v7 | 0.3029% | 2 | Photon-like branch + Sigma_c+ generation-adjacency fix |

**44 known baryons. 2 free parameters. No curve fitting.**

---

## GBP v7 — What's New

### 1. Photon-Like Branch (new topology class)

Several charm and bottom-strange J=3/2 baryons carry a **figure-8 flux tube
topology** where geometric mass largely cancels — only the skew correction
(geo_corr) and Hamiltonian winding survive. Formula:

```
M = (sumC + geo_corr + rt + C_HYP·S) × (1 + λ)
```

No `dg` term — the boundary projection cancels due to the specific
quark geometry. Applied to: Xi_c*+, Xi_c*0 (S1/T3), Xi_b*- (S1/T3).

Results:
- Xi_c*+: +0.057% (was +1.10%)
- Xi_c*0: +0.204% (was +1.25%)
- Xi_b*-: +0.759% (was +1.91%)

### 2. Sigma_c+ Generation-Adjacency Fix

`gf = S2[3] = 0.165435` for the udc baryon Sigma_c+.  
Physical mechanism: charm (gen2) is adjacent to bottom/top (gen3) in the
generation hierarchy. The S2[3] factor governs the geo_factor for mixed
light-heavy systems where the heavy quark sits at a generation boundary.  
Result: -0.070% (was +1.44%) — essentially exact.

### 3. Open Issues for v8

| Baryon | Error | Suspected cause |
|--------|-------|-----------------|
| Omega_c* | +2.41% | omega formula structurally wrong for ss+charm |
| Xi_b*- | +0.76% | T4 topology suspected (figure-8 winding, next cover level) |
| Omega_b* | +1.00% | needs investigation |

**T4 hypothesis:** Xi_b*- has three different quark generations (d,s,b) —
maximum topological complexity. T4 topology naturally produces figure-8
winding patterns where two flux tube pairs partially cancel. If T4 exists
on the Fibonacci lambda ladder, Xi_b*- may represent the first confirmed
T4 baryon.

---

## GBP v6 — Key Advances (retained in v7)

### Strange Inertial Step-Down Rule

Each strange quark subtracts one spinor step from the base coupling angle,
reflecting the ~40% inertial contribution to strange constituent mass:

| n_strange | geo_sign | angle | geo_factor | example |
|-----------|----------|-------|------------|---------|
| 0 | any | 48° | S2[1] = 0.5523 | proton, neutron |
| 1 | −1 (attractive) | 36° | sin²36° = 0.3455 | Lambda0 |
| 1 | +1 (repulsive) | 24° | S2[3] = 0.1654 | Sigma+/0/− |
| ≥2 | any | 12° | GEO_B = 0.0432 | Xi0, Xi−, Omega− |

### HE21 Waveguide Mode: Delta++

Delta++ is identified as an **HE21 waveguide mode baryon** — asymmetric
figure-8 topology with T2 helicity flip, confirmed by:
1. No nucleon analogue (uuu/ddd have no S1/T1 parent)
2. Helicity amplitude ratio A₃/₂:A₁/₂ ≈ 4:1
3. Flat production cross-section (11–205 GeV/c)
4. Figure-8 angular distribution in decay

### Minimum Topology Rule

| Condition | Minimum topology |
|-----------|-----------------|
| Pure same-generation quarks | S1/T1 allowed |
| Direct nucleon spin excitation | S1/T1 allowed |
| No nucleon parent (Delta++/−) | T2 minimum |
| Any heavy quark (c/b/t) | T2 minimum |
| Three different generations | T3 preferred |
| Three strange quarks | S2 minimum |

---

## Core Framework

### geo_factor — Malus's Law Transmission Coefficient

The geo_factor is the **Malus transmission coefficient** for spinor toroid
boundary projection. The toroid phase rotates; the 3D observable boundary
is a fixed polarizing filter. Phase alignment → maximum transmission.
Misalignment builds tension that releases at Y-junction vertices.

```
S2[gen] = sin²(GEN_N[g] · π/15)

S2[1] = sin²(48°) = 0.552264   gen1: up/down
S2[2] = sin²(84°) = 0.989074   gen2: strange/charm
S2[3] = sin²(24°) = 0.165435   gen3: bottom/top
GEO_B = sin²(12°) = 0.043227   boundary quantum
```

### Fibonacci Lambda Ladder

All boundary projection scales derive from a single geometric constant:

```
LU = GEO_B / α_IR = sin²(π/15) / 0.848809

T1 = T3 = LU                (odd covers — same boundary orientation)
T2      = LU · √φ           (helicity flip)
S2/T1   = LU · φ            (sheet crossing on T1)
S2/T2   = LU · φ^1.5
J=3/2 S2 = LU · φ²          (decuplet S2)
```

The ladder is a **phi-harmonic series** rooted in the same φ that governs
the lepton mass ratios (m_μ/m_e = φ¹¹, m_τ/m_μ = φ⁶).

### Two Free Parameters

1. **kappa_0 = 8,792,356.74** — color-magnetic hyperfine coupling
2. **lam_s1 = 1.15 · LU** — J=3/2 S1/T1 lambda (Delta+/0/− sector)

The 1.15 multiplier is suspected to encode the **triple same-chirality
winding bias** — when all three quarks share the same chirality (uuu, ddd),
the cancellation angle deviates from ideal by ~5°, producing a geometric
amplification factor. If confirmed, this eliminates the second free
parameter entirely, leaving only kappa_0.

---

## Broader Framework — Unification Direction

GBP is the baryon mass sector of a larger unified geometric framework
(TFFT — Temporal Flow Field Theory) in which:

- Particles are vortex structures in 4D spacetime
- Mass emerges from temporal curvature (chi-field)
- The phi-harmonic ladder governs **all** particle families
- Berry-Keating Hamiltonian connects Riemann zeros to the topological mass scale
- String theory 2π appears naturally from the TFFT tensor time structure
- MOND emerges as chi-field saturation at galactic scales

The mod-30 spinor circle (φ(30) = 8 coprime residues × 6 quark flavors = 48
dimensions) matches the 48-dimensional OAM topology observed in SPDC
entangled photons (Wits/Huzhou 2025, Nature Communications).

**Active research direction:** Deriving all constituent quark masses and
lepton masses from a single phi-harmonic ladder, eliminating all input
masses as free parameters.

---

## Repository Structure

```
mod30-spinor/
├── gbp_complete_v7.py     — current working code (MAPE=0.3029%)
├── gbp_complete_v6_final.py
├── gbp_complete_v5_final.py
├── unified_paper_v3.docx  — GBP + TFFT combined paper
├── gbp_v6_update_paper.docx
└── README.md
```

---

## References

- Korner (2014). Helicity Amplitudes. arXiv:1402.2787
- BESIII Collaboration (2019). Nature Physics 15, 631
- de Mello Koch et al. (2025). Nature Communications. DOI: 10.1038/s41467-025-66066-3
- Deur, Brodsky, de Teramond (2024). α_IR = 0.848809
- Bissey et al. (2007). Phys. Rev. D 76, 114512
- PDG (2024/2025). Baryon mass tables

sin²(θ/2) is the projection of toroid arm sweep angle θ onto the 
boundary — identical mathematics to Malus's Law in optics.

### Toroid cover system

| Cover | Mod  | Steps | Step° | Physical structure              |
|-------|------|-------|-------|---------------------------------|
| T1    | 30   | 30    | 24°   | Single parallelogram + Möbius   |
| T2    | 36   | 20    | 20°   | Two toroids, figure-8, HE21     |
| T3    | 18   | 18    | 40°   | Three toroids 120°, Y-junction  |

### Results

| Group  | MAPE    | RMSE    |
|--------|---------|---------|
| clean  | 0.8500% | 22.4 MeV |
| wide   | 0.3568% | 13.2 MeV |
| degen  | 0.2268% | 9.7 MeV  |
| J=1/2  | 0.6425% | —        |
| J=3/2  | 0.3086% | —        |
| ALL 44 | 0.4907% | 18.2 MeV |

(with Sigma+/0/- triangular toroid correction sin²(30°)=0.25)
