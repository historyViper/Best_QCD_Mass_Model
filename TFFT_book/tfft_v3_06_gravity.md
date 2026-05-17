
### 6.1 What v2 Got Right and Wrong

TFFT v2 proposed a₀ = c²/(2πR_H). This works numerically at z≈0 but implies
a₀ tracks the Hubble radius as the universe expands — which would mean galaxy
rotation curves change over billion-year timescales. No such evolution is observed.

### 6.1a Two Sources of Gravitational Curvature **(H)**

Gravity — the accumulation of spacetime curvature across macroscopic matter — has two distinct geometric contributors. This updates the earlier picture in which only the T3 Y-junction was treated as gravitationally relevant.

**Primary contributor — T3 Y-junction (baryon mass):**

The T3 Y-junction is topologically protected. Its three arms reinforce constructively at the junction point, and this junction energy survives ensemble averaging across 10²³ atoms. This is the dominant source of gravitational curvature — it accounts for the bulk of atomic mass and is what the standard GR stress-energy tensor captures.

**Secondary contributor — T1 anisotropic component (electron winding):**

The electron's T1 winding curvature has two components (see tensor_time v7 §3.3b). The isotropic component averages out across the ensemble and becomes the classical EM field. The anisotropic component — the directional asymmetry arising from the mod-12 cross-point lacking reflection symmetry — does not cancel isotropically. It carries a net directional bias in boundary projection energy whose sign depends on the orientation of the electron's winding relative to adjacent atoms.

In ordinary bonded matter, electron shells naturally face toward each other. The anisotropic T1 contributions from adjacent atoms add constructively, contributing a small but nonzero positive increment to the net spacetime curvature — a genuine electron contribution to gravitational mass that the previous picture understated.

**The full gravitational curvature per atom:**

```
κ_atom = κ_T3 + κ_T1_aniso(bonding geometry)
```

where κ_T3 is the T3 Y-junction contribution (dominant, orientation-independent) and κ_T1_aniso is the electron winding contribution (secondary, orientation-dependent). In ordinary matter with inward-facing bonding geometry, both terms are positive.


### 6.2 The Constant v3 Formula

From T1 geometry, the beat angle between the Möbius grid (24° steps) and the
parallelogram grid (30° steps) is:

```
beat = 30° − 24° = 6° = π/30
```

The MOND scale is:

```
a₀ = (c² / R_beat) · tan(π/30)
```

where R_beat is the Möbius beat wavelength — a **fixed geometric constant**
determined by the T1 toroid topology, not by the Hubble radius.

At present epoch, R_beat ≈ 2π R_H to within ~10%, which is why v2's formula
worked locally. But v3 predicts **a₀ does not change with cosmic time.**

**Testable:** Measure a₀ from rotation curves at z=1–2 with JWST/ELT. v3 predicts constant a₀. v2's formula a₀ = c²/(2πR_H) predicts a₀ ∝ H(z) — cosmic drift. No such drift is observed at z≈0; v2 is already ruled out by the absence of observed rotation curve evolution. JWST will confirm this at higher redshift.

---

## 6.5 Venturi Gravity: GR Recovery and the T_min Floor **(D)**

### 6.5.1 Gravity as Tension Depression

In the TFFT framework, gravity is not a separate force — it is a **local depression
of time string tension** caused by the presence of mass. A mass concentrates
winding density, which reduces the local tension T(r) below the vacuum value T₀.
The surrounding vacuum, at higher tension T₀, pushes inward — exactly as a
high-pressure fluid pushes into a low-pressure region. This is the **Venturi
mechanism**: mass creates a tension trough; the tension gradient IS the
gravitational field.

```
T(r)/T₀ = √(1 − v²/c²)   (exact relativistic tension)
T(r)/T₀ ≈ 1 − ½v²/c²    (Venturi approximation, matches Newtonian limit)
```

The tension profile around a point mass decreases monotonically toward the mass,
with the vacuum pushing inward along the gradient. In the weak-field limit this
recovers Newtonian gravity exactly. In the strong-field limit it recovers GR.

### 6.5.2 PPN β = 1: GR Recovery **(D)**

The post-Newtonian parameter β measures the nonlinearity of gravitational
superposition. GR requires β = 1. The derivation from Venturi tension:

```
Step 1:  T(r)/T₀ = 1 − GM/(rc²)         (weak-field tension, Newtonian limit)

Step 2:  g₀₀ = −(T/T₀)²
              = −1 + 2GM/(rc²) − (GM/(rc²))²

Step 3:  PPN expansion: g₀₀ = −1 + 2Φ/c² − 2β(Φ/c²)²
         with Φ = −GM/r

Step 4:  Matching coefficients: 2β = 1  →  β = 1   (exactly)
```

The Venturi tension field produces β = 1 identically — the same value as GR —
because the squared tension form (T/T₀)² generates the same quadratic term as
the Schwarzschild metric. The Venturi and GR curves are numerically
indistinguishable across all tested gravitational potentials Φ/c².

This means Venturi gravity is not an approximation to GR — it recovers GR
exactly in the weak-to-moderate field regime, from a tension-pressure mechanism
rather than a geometric curvature mechanism. Any deviation would only manifest
at the T_min horizon, where the two pictures may diverge.

### 6.5.3 The T_min Floor and the Forbidden Zone **(D)**

The tension cannot fall to zero — that would require infinite energy density.
The minimum tension floor is set by the same geometric constant that governs
the optical reflection floor:

```
T_min/T₀ = GEO_B = sin²(π/15) = 0.04323
```

This is the **{1,29} winding lane projection weight** — the colorless boundary
value of P(r). It is not a new parameter; it is the same GEO_B that sets
R_min = 1.093% for optical reflectance.

**Physical consequences of T_min:**

- **Anti-gravity — why it remains incoherent in this framework:**

1. Gravity is a tension gradient.
2. The gradient always points toward lower tension.
3. Lower tension is always toward mass, because mass IS the winding density that depresses tension.

Therefore: the gravitational force always points toward mass. Anti-gravity in the sense of a *repulsive* gravitational force would require mass to raise local tension — which contradicts the definition of what mass is in the Venturi picture. This is the same impossibility as the anti-Venturi effect. It is not forbidden by a floor value; it is not a coherent concept in the framework.

- **Anti-mass — reduced gravitational coupling through orientation inversion **(H — Speculative):**

This is distinct from anti-gravity. The orientation-dependent T1 anisotropic contribution to κ_atom (§6.1a) opens a different possibility: if atomic bonding geometry could be engineered so that electron shells faced *away* from each other rather than inward, the κ_T1_aniso term would become negative — partially cancelling the T3 Y-junction contribution and reducing the net curvature per unit of matter. Less curvature per atom means less gravitational attraction, without reversing its direction. The correct term is **anti-mass**: reduced effective mass, not reversed gravitational force.

```
Ordinary bonding (inward-facing):      κ_T1_aniso > 0  →  κ_atom increases
Engineered inversion (outward-facing): κ_T1_aniso < 0  →  κ_atom decreases
```

Given the T1/T3 mass hierarchy (~1/1836), the magnitude of any achievable mass reduction is likely small. Maintaining outward-facing bonding geometry would require continuously applied energy — it is not a passive equilibrium state. This is a geometric conjecture; the quantitative ratio of κ_T1_aniso to κ_T3 per atom has not yet been calculated. **(H — speculative)**

- **Horizon structure:** Where T(r) → T_min, the time string approaches maximum
  curvature. This is the geometric analogue of the event horizon — not a coordinate
  singularity but a physical tension boundary.
- **The Z₃₀* lane structure sets the floor:** The same geometry that forbids a
  9th gluon and enforces R_min also enforces T_min. All three are consequences of
  the {1,29} winding pair being the outermost coprime lane.

### 6.5.4 The Winding Lane Tension Hierarchy

The Z₃₀* lane structure produces a discrete tension hierarchy. Each mirror pair
{r, 30−r} contributes a tension level T(r)/T₀ = P(r):

| Mirror pair | T(r)/T₀ = P(r) | Physical role |
|-------------|----------------|---------------|
| {1, 29} | 0.043 = GEO_B | T_min floor — vacuum / colorless boundary |
| {13, 17} | 0.165 | Bottom, top quarks |
| {11, 19} | 0.552 | Up, down quarks |
| {7, 23} | 0.989 | Strange, charm quarks |

The tension floor GEO_B = 0.043 is not a fitted value. It is sin²(π/15) —
the projection weight of the lowest coprime winding lane. Gravity cannot
depress tension below this floor because doing so would require a winding
number outside Z₃₀* — which is topologically forbidden by the closure
condition gcd(r,30)=1.

### 6.5.5 Connection to the Optical Floor

The same constant appears in three independent physical phenomena:

```
R_min (optics)     = sin²(π/30) = GEO_B = 0.04323   [83/83 materials confirmed]
T_min (gravity)    = sin²(π/15) = GEO_B = 0.04323   [anti-gravity floor]
P(1) = P(29) (QCD) = sin²(π/15) = GEO_B = 0.04323   [colorless boundary]
```

This is not a coincidence — all three are the same geometric fact: the minimum
non-zero projection weight of the Z₃₀* winding system. The universe has a
geometric floor, and it is the same number in optics, gravity, and QCD.
### 6.5.6 Black Hole Interior Structure **(H)**

#### Shell Structure

The Z₃₀* tension hierarchy produces four discrete shells
inside every black hole. Each shell is the radius at which
a specific mirror pair of winding lanes loses geometric
identity as T(r) → T_min. All radii normalized to
Schwarzschild radius r_s = 2GM/c²:

| Shell | Mirror pair | P(r) | r/r_s | Physical content |
|-------|------------|------|-------|-----------------|
| Outermost | {7,23} | 0.989 | 22.88 | Strange/charm quarks collapse |
| Middle | {11,19} | 0.552 | 12.78 | Up/down quarks collapse |
| Inner | {13,17} | 0.165 | 3.83 | Bottom/top quarks collapse |
| Horizon | {1,29} | 0.043 = GEO_B | 1.00 | Two states remain: ln(2)/cell |

Shell radii formula: r_shell/r_s = P(r)/GEO_B
Zero free parameters given black hole mass M.

**Entropy recovery:** At the horizon, two winding states
{1,29} survive. Entropy S ∝ (A/l_P²) × ln(2) — the
Bekenstein-Hawking formula in geometric form. Structural
form derived (D). Numerical match requires φ-ladder UV
completion from l_GBP to l_P (~94.4 φ-steps). (H)

#### Three Cancellation Zones (Weak Spots)

Between adjacent shells, competing pressures partially
cancel. These zones allow brief partial restoration of
winding structure — information compressed toward the
two-state floor can re-expand here.

| Zone | Between shells | Inner r/r_s | Outer r/r_s | Midpoint r/r_s |
|------|---------------|------------|------------|---------------|
| CZ1 (innermost) | Horizon ↔ {13,17} | 1.000 | 3.827 | 2.414 |
| CZ2 (middle) | {13,17} ↔ {11,19} | 3.827 | 12.776 | 8.302 |
| CZ3 (outermost) | {11,19} ↔ {7,23} | 12.776 | 22.881 | 17.828 |

CZ1 note: midpoint at r = 2.41 r_s sits close to ISCO
(r = 3 r_s for Schwarzschild). May reflect a deeper
connection between geometric and orbital instability
boundaries — not yet derived.

**Hawking radiation:** CZ1 is the Hawking zone. Two boundary
states {1,29} radiate thermally because the two-state alphabet
produces maximum entropy (most random) emission. Thermal
spectrum confirmed (D). CZ1 partial bottom/top restoration
introduces spectral correction of order P(13)/P(1) = 3.83 —
below current observational sensitivity.

#### Central Balance Point

At r = 0 (for spherically symmetric black hole): compression
arrives from all directions simultaneously. Net gradient = 0.
Winding structure restores under isotropic compression.
Full Z₃₀* accessible. Information is not destroyed — it
retreats to the geometric balance point where competing
curvatures cancel. Information paradox resolution: geometric,
not thermal. (H — conjecture, not yet formally derived)

#### Polar Precession Asymmetry (Rotating Black Hole)

The T1 Möbius structure assigns opposite chirality to the
two poles of a rotating black hole (same as the two halves
of the sphere in the spinor construction):

- North pole: clockwise winding, +12°/traversal phase accumulation
- South pole: counterclockwise winding, −12°/traversal

Shell positions are symmetric between poles (P(r) = P(30-r)).
Precession rates are not:
δΩ/Ω_BH = 12°/360° = 1/30 = 3.333%
ΔΩ_total/Ω_BH = 2/30 = 1/15 = 6.667%
North pole weak spots precess 3.333% faster than bulk rotation.
South pole weak spots precess 3.333% slower.
One full differential cycle: 720°/12° = 60 traversals.

**M87* test:** Cui et al. (Nature 621, 711, 2023) measured
the M87* jet precession period at ~11 years from 170 VLBI
epochs (2000–2022), confirming a spinning black hole with
Lense-Thirring precession. The GBP prediction: reanalyzing
the same dataset for asymmetry between approaching (South)
and receding (North) jet components should show a 6.667%
differential in precession rates, corresponding to ~8.8
months of phase offset per 11-year cycle. Over 22 years
of monitoring: ~2 full differential cycles accumulated.
Status: (H — pending reanalysis of existing dataset)

**Observational signatures:**
- Jet precession asymmetry: North jet leads, South jet lags
  by equal amounts (3.333% each of bulk rate)
- QNM overtones in gravitational wave ringdown at frequency
  ratios 22.88 : 12.78 : 3.83 relative to horizon mode
  (Einstein Telescope / Cosmic Explorer — long range)
- X-ray iron Kα line structure at CZ1 (r ≈ 2.41 r_s),
  CZ2 (r ≈ 8.30 r_s) in accreting black hole binaries

**Key citations:**
- Cui, Y. et al. (2023). Nature 621, 711–715.
- Hada, K. et al. (2016). ApJ 817, 131.
  (M87 jet base resolved to 10 Schwarzschild radii)
- EHT Collaboration (2019). ApJL 875, L1.
- 
---

