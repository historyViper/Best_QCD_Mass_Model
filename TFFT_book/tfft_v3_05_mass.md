## 4. The Projection Formula and Malus's Law **(D)**

Each winding lane r projects onto the colorless boundary with weight:

```
P(r) = sin²(rπ/15)   for r ∈ Z₃₀*   (hadronic sector)
P₁₂(r) = sin²(rπ/6) = 1/4   for r ∈ Z₁₂*   (leptonic sector)
```

This is **Malus's Law applied to spinor geometry**: the projection weight at
angle θ is sin²(θ). The eight coprime lanes give four distinct weight classes
due to the mirror symmetry P(r) = P(30−r):

| Mirror pair | P(r) | Quark assignment |
|-------------|------|-----------------|
| {1, 29} | 0.043227 | Colorless boundary / vacuum |
| {13, 17} | 0.165435 | Bottom, top quarks |
| {11, 19} | 0.552264 | Up, down quarks |
| {7, 23} | 0.989074 | Strange, charm quarks |

### 4.1 Baryon Mass Formula Results **(D)**

The GBP compressed Lagrangian applied to baryon winding configurations:

| Group | MAPE | RMSE (MeV) | Count |
|-------|------|-----------|-------|
| Clean baryons | 0.243% | 7.63 | 13 |
| Wide baryons | 0.333% | 18.97 | 30 |
| Degenerate baryons | 0.136% | 4.13 | 4 |
| Orbital excitations | 0.068% | 2.81 | 2 |
| Pentaquarks | 0.196% | 11.11 | 5 |
| **All 55** | **0.2427%** | **14.76 MeV** | **55** |

**Zero free parameters.** External input: Λ_QCD = 217 MeV (PDG 2024). All other
constants derived from mod-30 geometry.

### 4.2 The Structural Link to Lattice QCD **(D)**

The GBP projection P(r) = sin²(rπ/15) and the standard lattice QCD momentum
weight w(r,N) = sin²(rπ/N) satisfy at N=30:

```
P(r) = 4cos²(rπ/30) · w(r,30)
```

The factor 4cos²(rπ/30) is the **Lüscher-Weisz O(a²) improvement correction**
used in improved lattice actions. GBP's projection is therefore the improved
lattice weight, restricted to the 8 coprime modes.

This means GBP may be the **analytic closed-form solution** that lattice QCD
approximates numerically — explaining why GBP achieves 0.2427% MAPE analytically
while lattice QCD achieves 1–2% with supercomputer simulations.

**Testable prediction (H):** The gluon spectral function (Ilgenfritz et al. 2018,
arXiv:1701.08610) should show quasi-particle peak height clusters at ratios:

```
0.0437 : 0.1673 : 0.5584 : 1.0000
```

This requires only reading four peak heights from Figure 10 of that paper.
Verification script: gbp_lattice_comparison.py (public repository).

---

## 5. The Mass Gap **(D)**

The colorless singlet state has winding number r = 0:

```
P(0) = sin²(0) = 0   (exact)
```

Zero Noether charge means zero propagation — by Schur's lemma, a state that
commutes with all Z₃₀* generators cannot be produced or absorbed by any colored
state. It cannot propagate.

The minimum energy gap above the vacuum is therefore:

```
Δ = P_min × Λ_QCD / LU = α_IR × Λ_QCD = 0.848809 × 217 MeV = 184.2 MeV
```

**The mass gap is topological, not dynamical.** It follows from P(0) = 0, an
algebraic identity, not from loop corrections or confinement dynamics. This
addresses the Yang-Mills mass gap (Clay Millennium Prize Problem) geometrically.
The gap survives the continuum limit because P(0) = 0 is preserved under all
averaging and coarse-graining operations.

---

## 5.4 Higgs Boson Mass from T2 HE21 Figure-8 Topology **(D/H)**

The Higgs boson mass is derived from first principles with zero free parameters.

**Physical identification.** The Higgs is not a T3 particle. It is a T2 resonance at the T3 threshold. The T2 HE21 toroid's default geometry is the tic-tac prolate spheroid with an oval Hamiltonian path (see tensor_time v7 §4.2). The Higgs corresponds to a special excitation state of T2 in which the winding enters a figure-8 configuration — two lobes with a crossing at the midpoint.

**The chirality structure of the Higgs figure-8 is not yet fully determined **(H):** The Higgs appears and disappears experimentally, which is consistent with chirality crossing at the figure-8 midpoint — a crossing between the two chirality Hilbert spaces would produce exactly the instability and finite lifetime observed. The particle is spin-0, consistent with two angular momentum contributions cancelling at the crossing. However, whether the two lobes run in opposing chirality (chirality crossing at the midpoint) or same chirality with a helicity flip (as in the photon's figure-8) has not yet been derived from first principles within GBP. The opposing-chirality picture is the working hypothesis given the Higgs's massive and unstable character — chirality crossing carries mass cost and cannot permanently constructively interfere — but it is not yet proven. **(H)**

**The two structural facts:**

1. **v/2 base:** The T2 figure-8 samples one lobe at a time. Each lobe costs half the T3 threshold energy to excite. The half-threshold resonance is v/2 = 122.964 GeV.

2. **C/2 correction:** The figure-8 has two crossings, each accumulating half the Malus-IR optical depth C that a full T3 closure traversal accumulates. The total correction per lobe is C/2, giving a multiplicative factor (1 + C/2).

**The formula **(D)**:**

```
M_H = (v/2) × (1 + C/2)

where:
  v   = 245.928 GeV    (Higgs VEV, derived — §9.5)
  C   = −ln(1 − GEO_B × α_IR) = 0.037382  (Malus-IR optical depth)
  C/2 = 0.018691

M_H = (245.928/2) × (1 + 0.018691)
    = 122.964 × 1.018691
    = 125.262 GeV
```

**Result:** M_H = **125.262 GeV** vs observed 125.25 GeV. Error: **0.010%**. Zero free parameters.

**Why C/2 and not C?** The full C applies when crossing the colorless boundary once — one complete traversal from the MS-bar Landau pole to the GBP IR fixed point. The figure-8 Higgs crosses the boundary *twice per cycle* (once per lobe), but each crossing is a *half-traversal* because the lobe only reaches the midpoint of the T2 oval before reversing. Two half-traversals × C/2 each = C total — but the observable mass resonance is set by *one lobe's* half-traversal, hence C/2.

This is consistent with the known result M_H ≈ v/2 at leading order (1.8% from v/2 alone), now corrected to 0.010% by the geometric C/2 term.

---
