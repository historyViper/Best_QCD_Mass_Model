# Appendices

---

## Appendix A — For the Physicist: The Lagrangian Side by Side

The following presents the Standard Model Lagrangian and the GBP
Lagrangian term by term. The purpose is to show that every term
in the Standard Model is present and unchanged in the GBP framework.
The single modification is the substitution of the geometric
projection formula for the gauge coupling, and the restriction
of the path integral measure to the Z₃₀* winding sum.

### A.1 — The Gauge Sector

Standard Model:
  L_gauge = -¼ F^a_μν F^a^μν

GBP:
  L_gauge = -¼ F^a_μν F^a^μν × P(r)

where P(r) = sin²(rπ/15) for r ∈ Z₃₀* = {1,7,11,13,17,19,23,29}

The Yang-Mills field strength tensor F^a_μν is unchanged.
The projection formula P(r) replaces the gauge coupling g²
at each winding lane r. It is not a new parameter — it is
derived from the parabolic winding geometry of the time string.

### A.2 — The Fermion Sector

Standard Model:
  L_fermion = ψ̄ (iγ^μ D_μ - m) ψ

GBP:
  L_fermion = ψ̄ (iγ^μ D_μ - m) ψ

Unchanged. The Dirac spinor structure is exactly the standard
four-component form. The covariant derivative D_μ contains
the same gauge fields. The mass term m is the quantity
derived from the projection formula — not an input parameter
but a geometric output:

  m = κ₀ × P(r) × (geometric factors)

where κ₀ = m_u × m_d × ΔM(Σ⁰–Λ⁰) is the torsion coupling,
a product of three PDG-measured quantities, not a free parameter.

### A.3 — The Higgs Sector

Standard Model:
  L_Higgs = |D_μ φ|² - V(φ)   where V(φ) = -μ²|φ|² + λ|φ|⁴

GBP:
  The Higgs mass is derived from the T2→T3 geometric transition
  threshold, not from a fundamental scalar field. The Higgs
  mechanism is preserved — electroweak symmetry breaking occurs
  at the same scale — but the mass parameter μ is derived:

  m_H = 125.20 ± 0.11 GeV  (PDG)
  m_H (GBP) = 125.187 GeV  (0.010% error)

### A.4 — The Path Integral

Standard Model:
  Z = ∫ Dφ exp(iS[φ])

GBP:
  Z = Σ_{r ∈ Z₃₀*} ∫ Dφ_r exp(iS[φ_r])

The path integral sums over Z₃₀* winding numbers only.
Non-coprime winding numbers cancel by destructive interference
on the parabolic lattice — they are not excluded by hand
but by the same Fourier analysis that governs any compact
winding structure. The continuum limit (Riemann-Lebesgue)
recovers the standard Yang-Mills action exactly.

### A.5 — What Is Different

One substitution: g² → P(r) = sin²(rπ/15)
One restriction: path integral measure → Z₃₀* winding sum

Everything else: unchanged.

The claim of this framework is not that QFT is wrong.
It is that these two modifications — both derived from the
geometry of the parabolic time string — explain where the
Standard Model's structure comes from.

---

## Appendix B — The Full Particle Table

All particles computed by the GBP framework, compared to
PDG measured values. Sorted by percentage error so outliers
are immediately visible. The bottom baryon systematic
underprediction (~0.5%) is not patched.

**Overall MAPE: 0.2498% across 54 baryons and pentaquarks**
**Free parameters: zero (given Λ_QCD)**

### B.1 — Light Baryons (u, d, s quarks)

| Particle | Quarks | J | PDG (MeV) | GBP (MeV) | Error % |
|----------|--------|---|-----------|-----------|---------|
| p        | uud    | ½ | 938.272   | [computed]| [value] |
| n        | udd    | ½ | 939.565   | [computed]| [value] |
| Λ⁰       | uds    | ½ | 1115.683  | [computed]| [value] |
| Σ⁺       | uus    | ½ | 1189.370  | [computed]| [value] |
| Σ⁰       | uds    | ½ | 1192.642  | [computed]| [value] |
| Σ⁻       | dds    | ½ | 1197.449  | [computed]| [value] |
| Ξ⁰       | uss    | ½ | 1314.860  | [computed]| [value] |
| Ξ⁻       | dss    | ½ | 1321.710  | [computed]| [value] |
| Ω⁻       | sss    | 3/2| 1672.450 | [computed]| [value] |

*[Full numerical values to be extracted from gbp_complete_v89.py
and inserted here before final manuscript]*

### B.2 — Charmed Baryons

| Particle   | Quarks  | J | PDG (MeV) | GBP (MeV) | Error % |
|------------|---------|---|-----------|-----------|---------|
| Λ_c⁺      | udc     | ½ | 2286.460  | [computed]| [value] |
| Σ_c⁺⁺     | uuc     | ½ | 2453.970  | [computed]| [value] |
| Ξ_cc⁺⁺    | ucc     | ½ | 3621.400  | [computed]| [value] |

*[Full table to be populated from Python output]*

### B.3 — Bottom Baryons
*Note: Systematic underprediction ~0.5% for all bottom baryons.
This is a known gap — the missing interior curvature correction
for lane r=13. Left unpatched deliberately as evidence against
overfitting. An overfitted model would correct this with a
free parameter. This framework does not.*

### B.4 — Pentaquarks

| Particle   | J^P   | PDG (MeV) | GBP (MeV) | Width    | Notes |
|------------|-------|-----------|-----------|----------|-------|
| Pc(4312)   | 1/2⁻  | 4311.9    | [computed]| Narrow   | Stable wormhole orbital |
| Pc(4440)   | 1/2⁻  | 4440.3    | [computed]| Narrow   | Stable wormhole orbital |
| Pc(4457)   | 1/2⁻  | 4457.3    | [computed]| Narrow   | Stable wormhole orbital |
| Pc(4380)   | 3/2⁻  | 4380      | [computed]| ~205 MeV | Wormhole reflection transient |

Pc(4380) falsification condition: if J^P is ever confirmed
as 1/2 or width confirmed narrow (<50 MeV), the wormhole
topology interpretation is wrong.

### B.5 — Gauge Bosons and Higgs

| Particle | PDG (GeV) | GBP (GeV) | Error % |
|----------|-----------|-----------|---------|
| W±       | 80.377    | [computed]| [value] |
| Z⁰       | 91.188    | [computed]| [value] |
| H⁰       | 125.20    | 125.187   | 0.010%  |

### B.6 — Regge Slope

| Quantity        | Observed      | GBP           | Error  |
|----------------|---------------|---------------|--------|
| α' (Regge slope)| 0.900 GeV⁻²  | 0.896 GeV⁻²  | 0.43%  |

---

## Appendix C — Derivation and Evidence Registry

Every quantitative claim in the book, labeled by status:

**D** = Derived and numerically verified against PDG or
        independent experimental data
**H** = Hypothesis or conjecture — mechanism identified
        but not yet numerically verified or confirmed
**P** = Prediction — specific falsifiable number not yet
        measured experimentally

| # | Claim | Status | Value | Source | Error |
|---|-------|--------|-------|--------|-------|
| 1 | φ(30) = 8 gluons | D | Exact | Algebraic identity | 0% |
| 2 | Q₈ = 7/2 | D | Exact | Cyclotomic identity | 0% |
| 3 | Q₈ = b₀(n_f=6)/2 → 6 quark flavors | D | n_f=6 | QCD beta function | 0% |
| 4 | Baryon MAPE | D | 0.2498% | 54 particles vs PDG | — |
| 5 | Higgs mass | D | 125.187 GeV | PDG 125.20 GeV | 0.010% |
| 6 | W mass | D | [value] | PDG 80.377 GeV | [value] |
| 7 | Z mass | D | [value] | PDG 91.188 GeV | [value] |
| 8 | Regge slope | D | 0.896 GeV⁻² | Observed 0.900 | 0.43% |
| 9 | α_IR fixed point | D | 0.848809 | Deur et al. 2024 | <0.1% |
| 10 | Flux quantization h/2e | D | Exact | Deaver & Fairbank 1961 | 0% |
| 11 | Optical floor R≥sin²(π/30) | D | 1.093% | 83 materials | 0 violations |
| 12 | Weinberg angle | D | [value] | PDG | [value] |
| 13 | CKM Vus | D | 0.23525 | PDG 0.2243 | ~4% |
| 14 | Λ_TOPO = m_up/γ₁ | D | 23.89 MeV | γ₁=14.1347 | — |
| 15 | GUE statistics in baryon masses | D | — | Montgomery kernel | — |
| 16 | Pc(4380) J^P = 3/2⁻ | D | 3/2⁻ | arXiv:1507.03717 | — |
| 17 | Charm CP violation mechanism | D | Tree-level | LHCb 2019 | 5.3σ |
| 18 | MOND a₀ constant | P | Fixed | JWST z=1-2 test | — |
| 19 | Ω_cc⁺ mass | P | 3645.60 MeV | HL-LHC 2030+ | — |
| 20 | Neutrino Σm_ν | P | ~58-62 meV | CMB-S4/Project 8 | — |
| 21 | Pc(4380) broad, J=3/2 always | P | J=3/2, ~205 MeV | LHCb Run 3 | — |
| 22 | Neutrino mass hierarchy | H | — | Mechanism: mod-12 beat | — |
| 23 | Lepton mass formula | H | — | Mechanism: mod-12 mirror | — |
| 24 | Bekenstein-Hawking entropy | H | Form correct | UV completion needed | — |
| 25 | RH proof from GBP | H | — | Conjecture only | — |
| 26 | Intermediate axis flip location | H | ~120°/240° | Charm companion paper | — |
| 27 | ΔACP from principal moments | H | Predicted | LHCb Run 3 | — |

---

## Appendix D — What Would Break This

These are explicit falsification conditions. If any of the
following are confirmed experimentally, the framework as
presented is wrong in a way that cannot be patched.

**D.1 — Optical floor violation**
Any transparent material confirmed to have reflectance
Rs(θ) < sin²(π/30) = 1.093% at any angle of incidence.
Currently: zero violations across 83 materials.
Test: measure reflectance of any transparent material
at near-normal incidence with calibrated spectrophotometer.

**D.2 — Baryon mass outlier**
Any baryon with confirmed PDG mass more than 2% from
GBP prediction, with no identified systematic reason
(the bottom systematic is known and documented).
Currently: maximum error [value]%, bottom baryons ~0.5%.

**D.3 — Pc(4380) spin-parity**
Pc(4380) confirmed with J^P = 1/2 (any parity).
Currently: independent QCD sum rules assigns 3/2⁻.
LHCb has not confirmed or refuted (insensitive to broad states).

**D.4 — Pc(4380) width**
Pc(4380) confirmed narrow (width < 50 MeV).
Currently: observed ~205 MeV broad. Framework predicts
this is irreducible — a wormhole collapse transient
cannot be narrow.

**D.5 — Ninth gluon**
A color-singlet gluon observed in experiment.
Currently: absent in all measurements.
Framework predicts it cannot exist: gcd(0,30) ≠ 1,
the singlet has zero Noether charge and cannot propagate.

**D.6 — Φ(30) mismatch**
If QCD were found to have any number of gluons other
than 8. Currently: 8 confirmed. φ(30) = 8 is an
algebraic identity — this would require the framework
to be wrong at its most fundamental level.

**D.7 — MOND a₀ tracking**
If JWST measurements at z=1-2 show a₀ varying with
cosmic epoch rather than remaining constant.
Framework predicts: a₀ = (c²/R_beat)·tan(π/30) is
a fixed geometric constant, not a cosmological tracker.

**D.8 — Charm CP violation**
If LHCb Run 3 confirms ΔACP consistent with Standard
Model penguin enhancement at the naive QCD level
(no order-of-magnitude enhancement required).
Framework predicts: the asymmetry is tree-level geometric,
not loop-suppressed, so it should remain anomalously large.

---

## Appendix E — Glossary

**α_IR (Alpha_IR):** The QCD infrared fixed point.
The value of the strong coupling constant at zero momentum
transfer — the point where the strong force stops getting
stronger as you zoom out. Value: 0.848809. Measured
independently by Deur et al. (2024). Appeared uninvited
in the GBP free-parameter fitting of quark masses.

**Bloch sphere:** The standard geometric representation
of a two-state quantum system. A sphere on which any
quantum superposition of two states can be represented
as a point. The four-quadrant structure of the GBP
toroid construction is a physical model of the Bloch sphere,
built from a question about magnet placement.

**CHARM_T2_AMP / CHARM_T3_AMP:** The charm helicity flip
amplitudes. CHARM_T2_AMP = cos(2 × 552°) = cos(24°).
CHARM_T3_AMP = cos(3 × 552°) = cos(216°). These encode
the three principal moments of the charm double helix and
implicitly contain the intermediate axis instability
(tennis racket theorem) that produces the torsion reversal.

**Double barrel roll:** The geometric shape found at the
three corners of the T3 triangular toroid when the
Hamiltonian phase and field phase are animated together.
The shape that corner phase-locking produces. The geometric
description of the three-gluon vertex in QCD.

**ER bridge:** Einstein-Rosen bridge. A wormhole — a
topological connection between two regions of space through
an interior shortcut. In GBP, the cc̄ figure-8 structure
of the J/ψ meson forms an ER bridge between the two
chirality spaces. This bridge is required by the framework
for hidden-charm pentaquarks.

**GEO_B:** sin²(π/15) = 0.043227. The projection amplitude
at the lowest surviving winding lane (r=1). The minimum
reflection floor for any real transparent material.
The charm Möbius 12° alignment amplitude. Appears in
multiple independent contexts throughout the framework.

**Hopf fibration:** A mathematical map between spheres
discovered by Heinz Hopf in 1931. Describes how the
3-sphere (a sphere in four dimensions) can be decomposed
into circles that fit together without touching. Underlies
the spinor double cover — the reason the electron needs
720° to return to its original state. Identified as the
name for the GBP toroid geometry when the construction
was described to an AI.

**HE21 modes:** Hybrid electromagnetic modes in fiber optics
and waveguide theory. Characterized by a specific angular
relationship: 30° when viewed straight-on, 60° when viewed
from above. Found in the T1 toroid geometry when the wave
structure was described to an AI without knowing the name.

**Intermediate axis theorem (tennis racket theorem /
Dzhanibekov effect):** A result from classical mechanics
stating that rotation around the intermediate principal
axis of a rigid body is unstable. The rotation spontaneously
flips at a point determined by the mass distribution.
Observed as a wing nut tumbling in space. In GBP, the charm
quark's double helix has three distinct winding axes with
unequal effective moments — making the intermediate axis
unstable and producing the torsion reversal that generates
CP violation.

**κ₀ (Kappa_0):** The torsion coupling constant.
κ₀ = m_u × m_d × ΔM(Σ⁰–Λ⁰). A product of three
PDG-measured quantities. Not a free parameter. The bridge
between the geometric winding structure and particle masses
in MeV.

**Λ_GBP (Lambda_GBP):** The GBP energy scale.
Λ_GBP = 225.27 MeV. Derived from α_IR and the mod-30
winding structure. Related to but not identical to
the standard QCD scale Λ_QCD.

**Λ_TOPO (Lambda_TOPO):** The topological energy scale.
Λ_TOPO = m_up / γ₁ = 23.89 MeV, where γ₁ = 14.1347...
is the imaginary part of the first Riemann zeta zero.
The bridge between the particle mass spectrum and the
Riemann zero structure.

**LU (Lambda_Universal):** LU = GEO_B / α_IR = 0.050927.
The natural orbital energy unit of the framework.
Appears as the missing coefficient in Jacobson's
thermodynamic derivation of general relativity.
Derived, not fitted.

**Mod-30 lattice / Z₃₀*:** The set of integers from 1 to 30
that share no common factor with 30:
{1, 7, 11, 13, 17, 19, 23, 29}. Eight elements.
These are the eight surviving winding lanes — the eight
gluons of QCD. The modular structure is forced by five
QCD consistency conditions and independently confirmed
by the parabolic winding geometry, the lattice QCD
Lüscher-Weisz formula, the Aharonov-Bohm flux
quantization, and the T3 corner count.

**Möbius twist:** A half-twist that makes a surface
non-orientable — the property of a Möbius strip.
In GBP, the T1 toroid has a Möbius twist built into
its winding structure, which is why the electron needs
720° to return to its original state.

**P(r) (Projection formula):** P(r) = sin²(rπ/15).
The projection amplitude at winding lane r. Derived from
the parabolic winding structure. Identical to the
Lüscher-Weisz O(a²) improved action coefficient in
lattice QCD. The physical meaning: the probability that
a winding path at lane r survives the interference
filter of the parabolic lattice. Also the gauge coupling
constant — not an input but a geometric output.

**Q₈:** The Noether charge of the Z₃₀* system.
Q₈ = Σ sin²(rπ/15) for r ∈ {1,7,11,13,17,19,23,29} = 7/2.
An exact algebraic identity from cyclotomic polynomial
theory. Q₈ = b₀(n_f=6)/2, which forces exactly six quark
flavors. Zero free parameters.

**T0 through T4:** The toroid hierarchy. Each tier
is a spatial dimension emerging from the time string:
T0 = time (photon, massless), T1 = first spatial
dimension (electron, leptons), T2 = second spatial
dimension (quarks, gluons), T3 = third spatial dimension
(baryons, confinement), T4 = chirality flip to antimatter
(entangled pairs, the second half of the sphere).

**Tent map:** A dynamical systems map with a characteristic
sawtooth/folding structure. Found in the pentaquark
wormhole geometry when the toroid structure was
described to an AI. The Pc(4380) wormhole topology
maps onto the tent map's folding behavior.

**THETA_CHARM:** 720° × 23/30 = 552°. The full winding
angle of the charm quark at lane r=23. After one full
360° closure: 192° residual. Decomposed as approximately
(torsion reversal point) + 12°, where the reversal
sits near 120°-240° due to the intermediate axis
instability, and 12° = one natural mod-30 step.

**720° spinor:** The property of spin-½ particles
requiring two full rotations (720°) rather than one
(360°) to return to their original state. Found
physically by placing four macaroni noodles on a
half-sphere — each noodle covering six of the 24
steps in the Möbius twist — and discovering the
loop closed at 720°, not 360°.

**Z₃₀*:** See Mod-30 lattice.

---

## Appendix F — Papers Still Needed Before Final Manuscript

The following companion papers are required before the
book manuscript is submitted. Each is flagged because
the book references results that exist only in
conversation records, Python code, or working notes —
not in citable form.

### F.1 — PRIORITY: The Charm Double Helix Paper
**Status:** No standalone paper exists.
**Content needed:**
- Lane r=23 winding arithmetic: THETA_CHARM = 552°
- Three principal moments of T2 double helix:
  I₁ (longitudinal, 12° step),
  I₂ (transverse, CHARM_T2_AMP = cos(24°)),
  I₃ (twist, CHARM_T3_AMP = cos(216°))
- Identification of I₂ as intermediate axis
- Derivation of torsion reversal location (~120°-240°)
  from principal moment ratios
- Connection to intermediate axis theorem / Dzhanibekov effect
- Prediction: specific ΔACP from geometric principal moments
- Comparison to LHCb 2019: ΔACP = −15.4 × 10⁻⁴
- Prediction for LHCb Run 3 measurements
- Gluon-gluon fusion at torsion reversal as dominant
  production mechanism (confirmed at LHC)
**Source material:** gbp_complete_v89.py lines 403-405,
793-800; conversation records May 2026
**Estimated length:** 15-20 pages

### F.2 — PRIORITY: The Pc(4380) Wormhole Paper
**Status:** Notes exist in gbp_boundary_cosmology_notes.md.
No formal paper.
**Content needed:**
- ER bridge topology requirement from T4 chirality flip
  applied to cc̄ pair creation
- Five Z₅* twist positions and four observed Pc states
- Why Pc(4380) reflects off the wormhole boundary:
  below the 180° crossing threshold
- Angular momentum acquisition at spin mirror: J=3/2
- Comparison to arXiv:1507.03717 (independent J^P = 3/2⁻)
- LHCb 2019 insensitivity to broad states as confirmation
- The tent map topology of the Pc(4380) state
- Falsification conditions
**Source material:** gbp_boundary_cosmology_notes.md;
gbp_complete_v89.py pentaquark section; conversation
records May 2026
**Estimated length:** 20-25 pages

### F.3 — Update All Existing Papers to MAPE = 0.2498%
**Status:** Some papers cite older MAPE values.
**Action needed:** Systematic update of MAPE figure
in all papers that cite the baryon mass results.
Papers affected: [to be listed after audit]
**Note:** Do not adjust any predictions or calculations —
only update the summary MAPE statistic and any
tables that showed the old value.

### F.4 — Objects Do Dimensions Companion Paper
**Status:** Referenced in tt_v7_00_header.md.
No standalone paper in project.
**Content needed:**
- The philosophical and physical argument that particles
  do dimensions rather than inhabiting global spacetime
- The FTL resolution: local geometry spreading across
  a frame as a flux tube
- The observer insight: time dilation is personal,
  not global
- The time machine argument: the past is a particle
  configuration, not a place
- Connection to T0-T4 toroid hierarchy as local
  dimensions, not global background
**Estimated length:** 10-15 pages

### F.5 — The T3 Geometry Paper
**Status:** No standalone paper exists.
This is the most important missing paper because
the double barrel roll at the corners — the geometric
description of the three-gluon vertex — exists
nowhere in the literature.
**Content needed:**
- Three phase-matched 720° spinors assembled into
  triangular toroid
- UUD vs UDD phase cancellation determining proton
  vs neutron
- Hyperbolic concave walls from ring pressure +
  Möbius twist
- The cutting problem: equilateral triangles fail,
  30° invariant specifies the cut
- 12 pieces per side, corner overlap correction,
  36 - 6 = 30 pieces total
- Hamiltonian placed in center (path of least resistance)
- EMF vs EF: field alone vs field + Hamiltonian
- Phase mismatch along walls, lock at corners
- The double barrel roll as corner phase-locking shape
- Three corners = three color charges (not assigned,
  found geometrically)
- Color confinement as the closed hyperbolic interior
**Estimated length:** 25-30 pages
**Note:** This paper is essentially Chapter 5 of the
book in formal mathematical language. Draft the
chapter first, then formalize.

---

## Appendix G — Key Citations by Chapter

*[To be populated as chapters are finalized]*

### Chapter 2 — The Tradeoff
- Noether, E. (1915). Invariante Variationsprobleme.
  Nachrichten der Königlichen Gesellschaft der
  Wissenschaften zu Göttingen, 235–257.
- Einstein, A. (1905). Zur Elektrodynamik bewegter Körper.
  Annalen der Physik, 17, 891–921.
- Hafele, J.C. & Keating, R.E. (1972). Around-the-world
  atomic clocks. Science, 177, 166–170.

### Chapter 3 — Why 30?
- Lüscher, M. & Weisz, P. (1985). On-shell improved
  lattice gauge theories. Communications in Mathematical
  Physics, 97, 59–77.
- Deaver, B.S. & Fairbank, W.M. (1961). Experimental
  evidence for quantized flux in superconducting
  cylinders. Phys. Rev. Lett. 7, 43.
- Aharonov, Y. & Bohm, D. (1959). Significance of
  electromagnetic potentials in the quantum theory.
  Physical Review, 115, 485.

### Chapter 8 — Charm and Wormhole
- LHCb Collaboration (2019). Observation of CP violation
  in charm decays. arXiv:1903.08726.
- CERN (2019). LHCb sees a new flavour of
  matter-antimatter asymmetry. Press release.
- Szczurek et al. (2025). Production of open and hidden
  charm in fixed-target experiments at the LHC.
  arXiv:2503.23961.
- [arXiv:1507.03717] Independent QCD sum rules:
  J^P = 3/2⁻ for Pc(4380).
- LHCb Collaboration (2015). Observation of J/ψp
  resonances consistent with pentaquark states.
  arXiv:1507.03414.
- LHCb Collaboration (2019). Observation of narrow
  pentaquark states. arXiv:1904.03947.

### FTL Chapter (Chapter 12)
- Hartman, T.E. (1962). Tunneling of a wave packet.
  Journal of Applied Physics, 33(12), 3427.
- Enders, P. & Nimtz, G. (1992). Phys. Rev. E 48, 632.
- Steinberg, A.M., Kwiat, P.G., & Chiao, R.Y. (1993).
  Phys. Rev. Lett. 71, 708.
- Nimtz, G. (2011). Foundations of Physics, 41, 1193.
- Aspect, A., Dalibard, J., & Roger, G. (1982).
  Phys. Rev. Lett. 49, 1804.
- Weihs, G. et al. (1998). Phys. Rev. Lett. 81, 5039.
- Hensen, B. et al. (2015). Nature, 526, 682–686.
- Giustina, M. et al. (2015). Phys. Rev. Lett. 115, 250401.
- Shalm, L.K. et al. (2015). Phys. Rev. Lett. 115, 250402.
- Bennett, C.H. et al. (1993). Phys. Rev. Lett. 70, 1895.
- Bouwmeester, D. et al. (1997). Nature, 390, 575–579.
- Ren, J.-G. et al. (2017). Nature, 549, 70–73.
- Bardeen, J., Cooper, L.N., & Schrieffer, J.R. (1957).
  Physical Review, 108, 1175.
- Josephson, B.D. (1962). Physics Letters, 1(7), 251–253.
- Anderson, P.W. & Rowell, J.M. (1963).
  Phys. Rev. Lett. 10, 230.
- Arute, F. et al. / Google AI (2019).
  Quantum supremacy. Nature, 574, 505–510.

---

*End of Appendices — First Draft*

---

**Notes for revision:**
- Appendix B numerical values marked [computed] need
  to be populated by running gbp_complete_v89.py
  and extracting the full output table
- Appendix C error values marked [value] need the
  same treatment
- Appendix G needs to be extended as remaining
  chapters are drafted
- Consider adding Appendix H: Timeline of Discovery —
  a chronological record of when each major result
  was found, to support the "discovered not constructed"
  narrative of the preface
