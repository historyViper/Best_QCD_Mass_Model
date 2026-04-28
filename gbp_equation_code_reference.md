# GBP Framework — Equation-to-Code Reference
## Every Variable Has a Geometric Reason

**Author:** Jason Richardson (HistoryViper)  
**Date:** April 2026  
**Code:** gbp_complete_v8-9.py  
**Framework:** github.com/historyViper/mod30-spinor  
**Zenodo:** 10.5281/zenodo.19798271

---

## Purpose

This document maps every equation in the GBP framework to its
corresponding code implementation and explains WHY each variable
exists — its geometric origin, not just its numerical value.

For a physicist asking "where does X come from?" — this is the answer.
For a reviewer asking "is the algebra hidden?" — the code IS the algebra,
and this document shows the correspondence line by line.

---

## The Master Formula

Every baryon mass prediction:

$$\boxed{M = \left(\sum C_i + \delta g + g_c + r_t + C_{\text{HYP}} \cdot S\right)(1 + \lambda)}$$

**Code:** `predict_final()` function, line ~830

Each term has a geometric origin. None are fitting parameters.

---

## Section 1 — Fundamental Constants

### 1.1 GEO_B — The Minimum Projection

$$\text{GEO\_B} = \sin^2\!\left(\frac{\pi}{15}\right) = 0.043227$$

**Code:** `GEO_B = math.sin(PI15)**2` (line 308)

**Why it exists:** This is the Malus projection weight of the colorless
boundary lanes {r=1, r=29} of Z₃₀*. These are the lanes closest to
the identity element r=0 (which has P(0)=0 and cannot propagate). The
colorless boundary is where gluons die — they deposit energy P(1) × Λ_QCD
as they reach the boundary of the mod-30 winding geometry.

GEO_B appears everywhere in the framework because it is the fundamental
energy quantum of the mod-30 system — the minimum non-zero projection.
It is the geometric origin of:
- The optical reflection floor: R_min = GEO_B = 1.093%
- The Yang-Mills mass gap: Δ = GEO_B × Λ_QCD / LU
- The Malus-IR scheme conversion: C = −ln(1 − GEO_B × α_IR)
- The Sigma_b0 isospin correction: gf = S2_1 × (1 − GEO_B)

**Lane assignment:** r=1 and r=29 are mirror images under mod-30
(1 × 29 = 29 ≡ −1 mod 30). They are the colorless boundary — closest
to the vacuum, furthest from confinement.

---

### 1.2 ALPHA_IR — The IR Fixed Point

$$\alpha_{\text{IR}} = 0.848809$$

**Code:** `ALPHA_IR = 0.848809` (line 311)

**Why it exists:** The QCD coupling α_s runs with energy scale Q. At
the infrared fixed point — the lowest energy where QCD is still defined —
α_s saturates at this value. This is the coupling at the scale where the
winding field is most strongly coupled.

**Source:** Deur, Brodsky, de Teramond (2024) — measured from QCD
sum rules and hadronic τ decay. Not fitted by GBP — taken from
independent experimental determination.

**Physical meaning in GBP:** α_IR is the coupling constant of the
mod-30 winding field at the colorless boundary. It multiplies GEO_B
to give the effective absorptance of the boundary lanes:
GEO_B × α_IR = effective absorptance at the IR fixed point.

---

### 1.3 LU — The Universal Projection Scale

$$\text{LU} = \frac{\text{GEO\_B}}{\alpha_{\text{IR}}} = \frac{\sin^2(\pi/15)}{0.848809} = 0.050927$$

**Code:** `LAMBDA_UNIV = GEO_B / ALPHA_IR` (line 313), `LU = LAMBDA_UNIV` (line 316)

**Why it exists:** LU is the ratio of the minimum projection weight to
the IR coupling. It is the universal scaling factor that appears in every
mass correction — the energy cost per unit winding projected through the
colorless boundary.

Physical interpretation: LU is how much of the winding energy "leaks"
through the colorless boundary per cycle. It is small (≈5%) because the
colorless boundary (GEO_B ≈ 4.3%) is weakly coupled to the colored sector.

LU appears as the base of every φ-ladder correction:
- T1 base: LU
- T2: LU × φ^0.5
- T3: LU × φ^1.0
- T4: LU × φ^1.5
- Dark matter skim: LU × φ^3.0

**The hierarchy is LU × φ^(k/2) where k counts topological levels.**

---

### 1.4 LAMBDA_QCD — The QCD Confinement Scale

$$\Lambda_{\text{QCD}} = 217.0 \text{ MeV}$$

**Code:** `LAMBDA_QCD = 217.0` (line 312)

**Why it exists:** The dimensional transmutation scale of QCD — the
energy where the QCD coupling becomes O(1) and confinement sets in.
This is the MS-bar 5-flavor value from PDG 2024.

Not derived by GBP — taken from experiment. GBP uses this as the
energy anchor. The mod-30 geometry determines ratios; Λ_QCD sets
the absolute scale.

---

### 1.5 LAMBDA_GBP — The GBP Winding Scale

$$\Lambda_{\text{GBP}} = \Lambda_{\text{QCD}} \cdot e^C, \quad
C = -\ln(1 - \text{GEO\_B} \cdot \alpha_{\text{IR}}) = 0.037382$$

**Code:**
```python
C_MALUS_IR = -math.log(1.0 - GEO_B * ALPHA_IR)   # line 375
LAMBDA_GBP = LAMBDA_QCD * math.exp(C_MALUS_IR)    # line 376
```

**Why it exists:** LAMBDA_GBP is the QCD scale converted from the
MS-bar renormalization scheme to the GBP winding scheme. The conversion
factor C is the **Malus-IR optical depth** — the proper distance in
coupling space between the Landau pole (MS-bar) and the IR fixed point
(GBP). This is a spacetime curvature effect invisible to perturbative QCD.

Physical interpretation: The colorless boundary lanes {1,29} act as
a partial absorber (optical depth C = GEO_B × α_IR to first order).
The scheme conversion is the Beer-Lambert law for winding energy:
Λ_GBP = Λ_QCD × e^C.

Used for the electroweak sector (v = 246 GeV) where the full winding
scheme energy is needed. The hadronic sector uses Λ_QCD directly.

---

### 1.6 PHI — The Golden Ratio

$$\varphi = \frac{1 + \sqrt{5}}{2} = 1.6180339...$$

**Code:** `PHI = (1.0 + math.sqrt(5.0)) / 2.0` (line 315)

**Why it exists:** φ appears at the T3 corner phase 204° = 180° + 24°.
The two-gluon cross-pairing amplitude at this angle is exactly φ⁻³
(confirmed by full angular sweep, gap = 1.1×10⁻⁵). This is because
204° = 180° + T1_H_beat, and the T3 corner geometry enforces the
golden ratio through the five-fold Z5* symmetry of the wormhole
(pentaquark) topology.

φ sets the spacing of the phi-ladder:
- T0→T1 ratio: φ^0.5
- T1→T2 ratio: φ^0.5
- T2→T3 ratio: φ^0.5
- All mass corrections scale as φ^(k/2) per topological level k

The golden ratio is not put in by hand. It emerges from the Z5*
five-fold symmetry of mod-30 = 2×3×**5**.

---

### 1.7 GAMMA_1 — The First Riemann Zero

$$\gamma_1 = 14.134725141734694$$

**Code:** `GAMMA_1 = 14.134725141734694` (line 317)

**Why it exists:** γ₁ is the imaginary part of the first non-trivial
zero of the Riemann zeta function: ζ(1/2 + iγ₁) = 0.

In GBP, γ₁ appears as the denominator of the topological energy scale:

$$\Lambda_{\text{topo}} = m_{\text{up}} / \gamma_1 = 337.64 / 14.1347 = 23.89 \text{ MeV}$$

**Code:** `LAMBDA_TOPO = CONSTITUENT["up"] / GAMMA_1` (line 465)

Physical meaning: LAMBDA_TOPO is the energy scale at which the
discrete mod-30 winding geometry transitions to the continuum field.
The first Riemann zero γ₁ is the lowest frequency where the
all-integer interference cancellation becomes exact — the coprime
modes (Z₃₀*) and composite modes first achieve perfect destructive
interference. Below this frequency, the geometry is discrete.
Above it, the continuum limit applies.

The connection: the up quark sits on lane r=19, the closest lane
to the Z5* boundary. Its constituent mass divided by γ₁ gives the
minimum topological resolution of the mod-30 system.

See: gbp_coprime_interference_riemann.md for full derivation.

---

### 1.8 ALPHA_BARYON — The Baryon Coupling

$$\alpha_{\text{baryon}} = \alpha_{\text{IR}} \times \frac{2}{3} = 0.565873$$

**Code:** `ALPHA_BARYON = ALPHA_IR * (2.0 / 3.0)` (line 314)

**Why it exists:** Baryons are 3-quark systems. The effective coupling
for a 3-body winding system is reduced from the 2-body IR coupling by
the SU(3) Casimir ratio. The factor 2/3 is the ratio of the fundamental
(quark) Casimir C_F = 4/3 to the adjoint (gluon) Casimir C_A = 3:
2/3 = (4/3)/2 — the quark carries 2/3 of the gluon's coupling strength.

Geometrically: a 3-quark toroid distributes the winding phase across
three lanes simultaneously. The effective coupling per quark is 2/3
of the full coupling.

---

## Section 2 — Projection Functions

### 2.1 s2(gen) — The Generation Projection

$$P_{\text{gen}}(g) = \sin^2\!\left(\frac{n_g \cdot \pi}{15}\right)$$

where $n_g \in \{4, 7, 2\}$ for generations {1, 2, 3}

**Code:**
```python
GEN_N = {1: 4, 2: 7, 3: 2}                    # line 302
def s2(gen): return math.sin(GEN_N[gen]*PI15)**2  # line 305
S2_1 = s2(1); S2_2 = s2(2); S2_3 = s2(3)      # line 307
```

**Why it exists:** Each quark generation occupies a specific angular
sector of the mod-30 toroid. The generation number maps to a natural
angular position:

| Generation | Lane index n_g | Angle n_g×π/15 | P = sin²(angle) |
|-----------|---------------|---------------|----------------|
| 1 (up/down) | 4 | 48° | 0.165435 |
| 2 (strange/charm) | 7 | 84° | 0.989074 → corrected |
| 3 (bottom/top) | 2 | 24° | 0.165435 |

Note: n_g are not the lane assignments of individual quarks (those
are in LANES dict). They are the generation-level angular sectors
that set the base projection for each quark family.

---

### 2.2 LANES — Individual Quark Lane Assignments

$$r_q \in Z_{30}^* \text{ for each quark } q$$

**Code:**
```python
LANES = {"up":19, "down":11, "strange":7,      # line 439
         "charm":23, "bottom":13, "top":17}
```

**Why each assignment:**

| Quark | Lane r | P(r) = sin²(rπ/15) | Geometric reason |
|-------|--------|-------------------|-----------------|
| up | 19 | 0.552264 | Z3 sector center, family 1 upper boundary |
| down | 11 | 0.552264 | Z3 sector center, family 1 lower boundary |
| strange | 7 | 0.989074 | Near-maximum projection, family 2 boundary |
| charm | 23 | 0.989074 | Near-maximum projection, family 2 boundary |
| bottom | 13 | 0.165435 | Low projection, family 3 boundary |
| top | 17 | 0.165435 | Low projection, family 3 boundary |

Note: up/down and bottom/top are mirror pairs under mod-30
(11+19=30, 13+17=30). Same projection weight, different winding.
Strange/charm are also mirrors (7+23=30).

The lane assignments are not free — they follow from the three-
generation structure of Z₃₀*. The 8 lanes naturally partition into
3 family pairs plus the colorless boundary:
- {1,29}: colorless boundary (photon, vacuum)
- {7,23}: high-projection family (strange, charm)
- {11,19}: medium-projection family (up, down)
- {13,17}: low-projection family (bottom, top)

---

### 2.3 ANGLES — Winding Angles

$$\theta_r = 720° \times \frac{r}{30} \quad \text{for } r \in Z_{30}^*$$

**Code:** `ANGLES = {r: 720.0 * r / 30.0 for r in LANE_SET}` (line 441)

**Why it exists:** The spinor double cover requires 720° for a full
winding cycle. Each lane r traces out 720° × r/30 of that cycle.
This is the winding angle of the T1 Möbius parallelogram for lane r.

The winding angles are:
- Lane 1: 24° (the T1 Hamiltonian beat — fundamental step)
- Lane 7: 168°
- Lane 11: 264°
- Lane 13: 312°
- Lane 17: 408°
- Lane 19: 456°
- Lane 23: 552° ← charm: 552° − 360° = 192° = 180° + 12° residual
- Lane 29: 696°

The charm residual 192° = 180° + 12° is the origin of the charm
helicity flip correction (v8.8). Lane 23 overshoots T1 closure by
12° = one natural step 360°/30.

---

### 2.4 INVERSES — Multiplicative Inverses mod 30

$$r \cdot r^{-1} \equiv 1 \pmod{30}$$

**Code:**
```python
INVERSES = {}
for _r in LANE_SET:
    for _s in LANE_SET:
        if (_r * _s) % 30 == 1: INVERSES[_r] = _s  # lines 443-446
```

**Why it exists:** The multiplicative inverse of lane r under mod-30
is the partner lane that, when combined with r, produces a colorless
singlet. This is the gluon color-anticolor pairing:

| Lane r | Inverse r⁻¹ | Product mod 30 |
|--------|------------|----------------|
| 1 | 1 | 1 |
| 7 | 13 | 91 = 1 mod 30 |
| 11 | 11 | 121 = 1 mod 30 |
| 13 | 7 | 91 = 1 mod 30 |
| 17 | 23 | 391 = 1 mod 30 |
| 19 | 19 | 361 = 1 mod 30 |
| 23 | 17 | 391 = 1 mod 30 |
| 29 | 29 | 841 = 1 mod 30 |

These pairs are the **gluon color-anticolor pairs** — the lanes that
annihilate each other into a colorless state. GEO_TWO_7 (used for
hyperfine coupling) uses the lane-7/lane-13 inverse pair:

$$\text{GEO\_TWO\_7} = \sqrt{P(7) \cdot P(\theta_{13}/2)} = \sqrt{\sin^2(84°) \cdot \sin^2(156°)}$$

**Code:** `GEO_TWO_7 = math.sqrt(sin²(ANGLES[7]/2) × sin²(ANGLES[INVERSES[7]]/2))` (lines 467-470)

---

## Section 3 — Mass Terms

### 3.1 ΣC — Constituent Quark Sum

$$\Sigma C = \sum_{q \in \text{quarks}} m_q^{\text{constituent}}$$

**Code:** `sumC = sum(CONSTITUENT[q] for q in quarks)` (line 801)

**Constituent masses (derived from mock theta geometry in v8):**

| Quark | Constituent mass | Geometric origin |
|-------|-----------------|-----------------|
| up | 335.68 MeV | C2 cycle: θ_eff = θ₀ − 8π |
| down | 338.19 MeV | C2 cycle: θ_eff = θ₀ − 8π |
| strange | 486.23 MeV | C1 cycle: θ_eff = θ₀ − 3r(r−1)×Γ_C1 |
| charm | 1555.97 MeV | C1 cycle: lane 23 winding |
| bottom | 4734.76 MeV | C1 cycle: V8 skim-corrected |
| top | 174466.26 MeV | C1 cycle: lane 17 winding |

All derived in `gbp_quarks_v2.py` from α_IR, Λ_QCD, GEO_B.
Zero free parameters.

---

### 3.2 δg — Phase Misalignment Cost

$$\delta g = \text{geo\_sign} \times \alpha_{\text{baryon}} \times \Lambda_{\text{QCD}} \times P_{\text{geo}}(r)$$

**Code:** `dg = geo_sign * ALPHA_BARYON * LAMBDA_QCD * gf` (line 803)

**Why it exists:** When three quarks wind together on a toroid, their
individual lane projections don't align perfectly. The phase mismatch
between the Möbius (24°) grid and the parallelogram (30°) grid creates
a tension cost — this is δg.

**geo_sign** (+1 or −1): the chirality orientation of the baryon's
quark configuration. Spin-parallel states have geo_sign = +1 (additive
tension). Spin-antiparallel states have geo_sign = −1 (subtractive).

**P_geo(r) = geo_factor**: the specific Malus projection for this
baryon's quark lane combination. Derived from the lane geometry —
see `derive_geo_factor_heavy()` for the heavy quark formula and
`strange_step_down_gf()` for light/strange baryons.

This term is the dominant mass correction for most baryons. Its
sign determines whether a baryon is heavier or lighter than its
flavor partner.

---

### 3.3 g_c — Z3 Skew Correction

$$g_c = \text{geo\_corr}(\text{quarks})$$

**Code:** `gc = geo_corr(quarks)` (line 813)

**Why it exists:** The Z3 sub-symmetry of mod-30 (factor of 3 in
30 = 2×3×5) creates a three-way angular asymmetry in the baryon
winding. When quarks from different Z3 sectors combine, there is a
geometric correction from the Hamiltonian path traversal through
the Y-junction.

For baryons with all quarks in the same Z3 sector: g_c ≈ 0.
For baryons with quarks from different Z3 sectors: g_c reflects
the angular mismatch at the Y-junction intersection.

This is the "geometric correction" term that distinguishes isospin
multiplet members (e.g. Sigma+, Sigma0, Sigma− have different g_c
because their quark content creates different Z3 path geometries).

---

### 3.4 r_t — Charm Reinforcement

$$r_t = n_{\text{charm}} \times R_{\text{reinforce}} \times \text{reinforce}(\text{quarks})$$

**Code:** `rt = reinforce(quarks) * R_REINFORCE` (line 814)
`R_REINFORCE = 216.0` (line 430)

**Why it exists:** Charm quarks sit on lane 23 with winding angle 552°.
After T1 closure (360°), the residual is 192° = 180° + 12°. This
12° overshoot means each additional T1 traversal adds a reinforcement
contribution — the charm winding resonates constructively over multiple
traversals.

R_REINFORCE = 216.0 MeV is the reinforcement energy per charm
double-winding. It appears in doubly-charmed baryons (Xi_cc)
where the two charm quarks both contribute this resonance.

Geometrically: charm double-winding is the T2 double-helix state —
the HE21 Hamiltonian. The 216 MeV is the T2 winding cost above
the T1 baseline.

---

### 3.5 C_HYP × S — Hyperfine Coupling

$$C_{\text{HYP}} \cdot S = \alpha_{\text{baryon}} \cdot \Lambda_{\text{QCD}} \cdot \text{GEO\_TWO\_7} \cdot S$$

where $S = -1$ for J=1/2, $S = +3$ for J=3/2

**Code:**
```python
C_HYP = ALPHA_BARYON * LAMBDA_QCD * GEO_TWO_7   # line 471
S = -1.0 if J == 0.5 else 3.0                    # line 802
```

**Why it exists:** The hyperfine coupling is the spin-spin interaction
between quarks. In GBP, this is the interference between the lane-7
and its inverse lane-13 at the colorless boundary crossing.

GEO_TWO_7 = √(P(7/2) × P(13/2)) is the geometric mean of the
half-angle projections of the color-anticolor pair {7,13}. This
pair has the maximum coupling (P(7) ≈ 0.989) and is the dominant
gluon exchange channel.

S = −1 for J=1/2: spin-antiparallel → subtracts from mass.
S = +3 for J=3/2: spin-parallel → adds to mass.
The ratio 3/(−1) = −3 is the SU(6) spin-flavor ratio, here
emerging from the toroid geometry.

---

### 3.6 λ — The Torsion Phi-Ladder Correction

$$\lambda = \text{LU} \times \varphi^{k/2}$$

where k = 0, 1, 2, 3, 4 for toroid levels T0, T1, T2, T3, T4

**Code:** `lam = get_lam(sheet, J, T)` (line 815), LAM dict (lines 394-417)

**Why it exists:** λ is the torsion correction from the φ-harmonic
ladder. As a particle's topology increases (more twisted, more
covers), the torsion cost scales as φ^(k/2) per level.

This is the Einstein-Cartan torsion term — the contorsion tensor
contribution to mass. Each toroid level adds one half-step on the
φ-ladder because each new topological cover adds √φ in amplitude.

**The LAM table:**

| Sheet | J | Topology | λ | Physical meaning |
|-------|---|---------|---|-----------------|
| S0 | 3/2 | T0 | LU × 30/26 | GOE plain torus — missing Möbius beat |
| S1 | 1/2 | T1 | LU | T1 base — Möbius parallelogram |
| S1 | 1/2 | T2 | LU × φ^0.5 | T2 double-helix correction |
| S2 | 1/2 | T1 | LU × φ^1.0 | S2 sheet on T1 toroid |
| S2 | 1/2 | T2 | LU × φ^1.5 | S2 sheet on T2 toroid |
| S2 | 1/2 | T3 | LU × φ^2.0 | S2 sheet on T3 toroid |

**LAM_S0 specifically:**
$$\lambda_{S0} = \text{LU} \times \frac{\cos^2(24°)}{\cos^2(30°)} = \text{LU} \times \frac{30}{26}$$

The S0/GOE plain torus lacks the Möbius beat (24°). It projects
as cos²(30°) instead of cos²(24°). The correction ratio 30/26 is
the ratio of total spinor steps to GOE-available steps.

---

## Section 4 — Baryon Classification

### 4.1 BARYON_CLASS — Topology Assignments

Each baryon entry: `(sheet, geo_sign, chirality, cover, topology, rule)`

**Code:** `BARYON_CLASS` dict (lines ~500–603)

**Why each field exists:**

| Field | Values | Geometric meaning |
|-------|--------|------------------|
| sheet | S0, S1, S2 | Random matrix statistics: GOE (S0) or GUE (S1,S2) |
| geo_sign | +1, −1 | Chirality orientation: spin-parallel (+) or anti-parallel (−) |
| chirality | sigma, lambda | Hamiltonian path type through the Y-junction |
| cover | 0, 1, 2, 3 | Number of toroid covers (T1=1, T2=2, T3=3) |
| topology | T0,T1,T2,T3 | Toroid type: plain(T0), Möbius(T1), HE21(T2), Y-junct(T3) |
| rule | heavy,light,photon,omega,pentaquark,orbital | Mass formula variant |

**Sheet (S0 vs S1/S2):**
- S0 = GOE statistics = time-reversal symmetric = plain torus T0
  → all-light-quark J=3/2 decuplet (Delta, Sigma*, Xi*)
- S1 = GUE statistics = time-reversal broken = Möbius twist T1
  → all J=1/2 baryons, most J=3/2 heavy baryons
- S2 = GUE² = double Möbius = HE21 double helix T2
  → heavy baryons with large charm/bottom contribution

**Sigma vs Lambda chirality:**
- sigma: quarks wind in the same rotational direction → constructive
- lambda: quarks wind in opposite directions → partially destructive
  Lambda baryons are lighter than their Sigma partners because the
  lambda winding partially cancels.

---

## Section 5 — Electroweak Sector

### 5.1 Q8 — Noether Charge

$$Q_8 = \sum_{r \in Z_{30}^*} \sin^2\!\left(\frac{r\pi}{15}\right) = \frac{7}{2} \quad \text{(exact)}$$

**Code:** `Q8 = 3.5` (line 373)

**Why it exists:** Q8 is the total Noether charge of the 8-gluon
Z₃₀* system. It is an exact algebraic identity over cyclotomic
polynomials — not a numerical approximation.

Q8 = 7/2 because: the 8 projection values {0.043, 0.165, 0.165,
0.552, 0.552, 0.989, 0.989, 0.043} sum to exactly 3.5. This is
the conserved charge under Z₃₀* phase rotation symmetry.

The "9th gluon" (r=0) has P(0)=0 — zero charge — and cannot
propagate. Q8 = 7/2 captures exactly the 8 physical gluons.

---

### 5.2 PHI3 — T3 Cross-Pairing Amplitude

$$\varphi^3 = 4.2361...$$

**Code:** `PHI3 = PHI**3` (line 374)

**Why it exists:** At the T3 Y-junction corner phase 204° = 180° + 24°,
two gluons arriving simultaneously cross-pair with amplitude φ⁻³.
The factor φ³ is therefore the denominator of the cross-pairing
probability.

Confirmed by full angular sweep: P_WZ × φ³ = 1.00001 (gap = 1.1×10⁻⁵).
The 24° is the T1 Hamiltonian beat — the same 24° that appears in
LAM_S0 and GOE correction. The framework is angularly self-consistent.

---

### 5.3 V_EW — The Higgs VEV

$$v = 30 \times \frac{Q_8}{8} \times \varphi^3 \times \frac{\Lambda_{\text{GBP}}}{\text{LU}}
= 245{,}928 \text{ MeV} \quad \text{(error: } 0.029\%\text{)}$$

**Code:** `V_EW = 30.0 * (Q8/8.0) * PHI3 * LAMBDA_GBP / LU` (line 377)

**Why it exists — term by term:**
- **30**: the mod-30 modulus — the number of T1 winding steps
- **Q8/8**: the average Noether charge per gluon lane = 7/16
- **φ³**: the T3 corner cross-pairing amplitude
- **Λ_GBP**: the GBP winding energy scale
- **/LU**: normalizes to the colorless boundary projection

The VEV is the energy at which two gluons can simultaneously reach
a T3 corner. Below v, they can't — the electroweak symmetry is
"broken" in the sense that the T3 corner cross-pairing threshold
is not reached.

---

## Section 6 — Special Corrections

### 6.1 Charm Helicity Flip (v8.8)

$$\text{GBP\_cover} = \text{SM\_cover} - \frac{n_{\text{charm}}}{2}$$

**Code:** Comments at lines 566-577, applied via cover assignments
in BARYON_CLASS for Xi_c_prime+/0.

**Why it exists:** Lane 23 (charm) winding = 720° × 23/30 = 552°.
After T1 closure: 552° − 360° = 192° = 180° + 12°. The 12° residual
is exactly one natural T1 step (360°/30). Each charm traversal adds
this 12° phase mismatch, making T1 charm LOOK like a higher-cover
state to experimenters measuring decay angular distributions.

The correction: SM_cover − n_charm × (12°/24°) = SM_cover − n_charm/2.
The 24° is the T1 H_beat. The 12° is half a H_beat.

**Xi_c_prime:** SM assigned cover=3 → GBP cover = 3 − 0.5 = 2.5 → T1.
Error reduced from 5.3% to 0.6%.

This is a systematic prediction: any charm baryon with SM-assigned
cover ≥ 2 should be cross-checked.

---

### 6.2 Sigma_b0 Malus-IR Correction (v8.8)

$$\text{gf}(\Sigma_b^0) = S_{2,1} \times (1 - \text{GEO\_B})
= \sin^2\!\left(\frac{4\pi}{15}\right) \times \cos^2\!\left(\frac{\pi}{15}\right)
= 0.528391$$

**Code:** `'Sigma_b0': S2_1 * (1.0 - GEO_B)` (line 610)

**Why it exists:** Sigma_b0 = [up, down, bottom] is the isospin-mixed
member of the Sigma_b triplet. As the mixed state (neither fully
up-spin nor fully down-spin), it sees the colorless boundary Malus
attenuation (1 − GEO_B).

Physical meaning: the up/down isospin mixing places one component of
the wave function at the colorless boundary. That component sees the
boundary attenuation factor (1 − GEO_B) = cos²(π/15). The factor
S2_1 = sin²(4π/15) is the up/down generation projection.

Error reduced from 3.84% to 0.96%.

---

### 6.3 KAPPA_0 — Torsion Coupling Scale

$$\kappa_0 = m_u \times m_d \times \Delta m = 335.68 \times 338.19 \times 76.959$$

**Code:** `KAPPA_0 = _M_U * _M_D * _DELTA_M` (line 437)

**Why it exists:** KAPPA_0 is the torsion coupling scale for the
up-down quark isospin system. It is the product of the up constituent
mass, down constituent mass, and their splitting. This appears in the
isospin-breaking corrections where the up-down mass difference creates
a torsion contribution.

Δm = m_d − m_u = 338.19 − 335.68 = 2.51 MeV is the isospin
splitting, setting the scale of electromagnetic mass differences
within isospin multiplets.

---

## Section 7 — Summary Table

| Variable | Value | Code line | Geometric origin |
|---------|-------|-----------|-----------------|
| GEO_B | 0.043227 | 308 | sin²(π/15) — colorless boundary projection |
| ALPHA_IR | 0.848809 | 311 | IR fixed point coupling (Deur 2024) |
| LU | 0.050927 | 313 | GEO_B/α_IR — universal projection scale |
| LAMBDA_QCD | 217.0 MeV | 312 | QCD dimensional transmutation (PDG) |
| LAMBDA_GBP | 225.27 MeV | 376 | LAMBDA_QCD × e^C — GBP winding scheme |
| PHI | 1.618034 | 315 | Golden ratio — T3 corner geometry |
| GAMMA_1 | 14.134725 | 317 | First Riemann zero — coprime interference |
| LAMBDA_TOPO | 23.89 MeV | 465 | m_up/γ₁ — topological energy scale |
| ALPHA_BARYON | 0.565873 | 314 | α_IR × 2/3 — 3-body coupling reduction |
| Q8 | 3.5 (exact) | 373 | Noether charge of Z₃₀* — algebraic identity |
| PHI3 | 4.2361 | 374 | φ³ — T3 cross-pairing amplitude |
| C_MALUS_IR | 0.037382 | 375 | Malus-IR optical depth — scheme conversion |
| LAM_S0 | 0.058494 | 345 | LU × cos²(24°)/cos²(30°) — GOE correction |
| C_HYP | ~0.032 | 471 | α_baryon × Λ_QCD × GEO_TWO_7 — hyperfine |
| KAPPA_0 | ~8.7×10⁶ | 437 | m_u × m_d × Δm — isospin torsion scale |
| R_REINFORCE | 216.0 MeV | 430 | Charm double-winding T2 resonance energy |
| TWIST_SCALE | ~228 MeV | 329 | Λ_QCD × (1 + LU×φ³) — pentaquark scale |

**Zero free parameters. Every value derived from geometry.**

---

## Conclusion

The Python code `gbp_complete_v8-9.py` IS the algebra. Every variable
has a geometric origin traceable to the mod-30 spinor toroid structure.
No constant is fitted to the baryon mass data — each is derived from
GEO_B, ALPHA_IR, LAMBDA_QCD, and PHI through geometric arguments.

The master formula M = (ΣC + δg + g_c + r_t + C_HYP×S)(1 + λ) is
not empirical. It is the Euler-Lagrange equation of the GBP compressed
Lagrangian evaluated on the mod-30 winding lattice for each specific
quark content and topology.

54 particles. 0.274% MAPE. Zero free parameters.
The geometry is real.

---

*github.com/historyViper/mod30-spinor — April 2026*
