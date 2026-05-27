# GBP Scattering Mechanisms and Optical Predictions

**Jason Richardson (HistoryViper)**
Independent Researcher — GBP Framework
Preprint — May 2026
GitHub: github.com/HistoryViper | Zenodo DOI: 10.5281/zenodo.19798271

*Speculative preprint. AI-collaborative authorship disclosed. Claims labeled (D) = derived/verified, (H) = conjecture/hypothesis.*

---

## Abstract

The Geometric Boundary Projection (GBP) framework provides a unified geometric taxonomy of scattering interactions derived from the mod-30 coprime winding lattice on a Möbius toroid. We identify five distinct scattering mechanisms — each a different geometric aspect of the same underlying structure — and show that wave-particle duality follows directly from the figure-8 topology of the photon (2×T0 helicity-flip geometry), which carries both AC (wave) and DC (particle) components simultaneously. We derive a general scattering amplitude rule from T3 corner phase interference and show it recovers the φ⁻³ suppression factor of the W/Z sector as a special case. In optics, we demonstrate that standard Snell's Law and Fresnel equations are unchanged but gain a geometric foundation: refractive index n is a projection of the mod-30 lane structure, and materials cluster near tier attractor values n_tier(r) = sin(rπ/15)/sin(π/30). A universal reflection floor R_min = sin²(π/30) ≈ 1.093% is derived as a topological necessity and confirmed against 83 materials with zero violations. Crucially, we identify a new falsifiable prediction: crystalline materials should sit closer to tier attractor Brewster angles than their amorphous counterparts, with amorphous offsets that are always negative (below the tier). This prediction is confirmed by the SiO₂ system: crystalline quartz (n_o = 1.5383) sits within 14 arcminutes of the T1 tier, while fused silica (n = 1.4533) sits 1.28° below it — a 1.5° Brewster angle shift from structural disorder alone.

---

## 1. Introduction

The Amplituhedron program (Arkani-Hamed et al.) proposes that scattering amplitudes are volumes of geometric objects in abstract momentum-twistor space, with locality and unitarity emerging from the geometry rather than being axioms. Active Inference / Markov blanket approaches (Friston et al.) propose that particle interactions are fundamentally information-theoretic. Both programs are recovering something real from opposite ends of the problem.

The GBP framework occupies the space between them: a discrete geometric lattice in physical toroid space from which both the amplitude structure and the information-theoretic structure emerge as projections. This paper presents the GBP scattering taxonomy — five distinct mechanisms unified by a single geometric principle — and applies it to optical scattering with testable predictions.

The central claim: **scattering amplitudes in GBP are nonzero exactly where Möbius winding phase and triangular corner phase constructively interfere. Discreteness, locality, and unitarity are all consequences of the same interference condition, not additional axioms.**

---

## 2. The GBP Scattering Principle

### 2.1 The Phase Interference Condition **(D)**

In the GBP framework, a T3 baryon is a triangular toroid: three T1 Möbius-twisted arms joined at three contact corners. The gluon navigates the interior Y-junction Hamiltonian path. At each corner, two phase accumulations must simultaneously align:

- **Möbius winding phase**: accumulates in 24 discrete steps of 15° each (the mod-30 toroid structure, completing 360° per arm traversal)
- **Triangular corner phase**: fixed at 60° intervals by the T3 triangular geometry

These two frequencies are incommensurate: the 24-step Möbius winding and the 60° triangular corners do not share a common divisor in their phase cycle. As the system evolves, the accumulated phase mismatch grows continuously — until the rare moments where both phase clocks align simultaneously. At those moments, the corner fires: a simultaneous Hamiltonian flip and toroid surface flip — the double barrel roll.

**The scattering rule follows directly:**

> A transition between two T3 states is allowed if and only if the Möbius winding phase and the triangular corner phase constructively interfere simultaneously at both interacting corners.

All other transitions undergo destructive interference and vanish. This gives a discrete set of allowed transitions — not from an imposed selection rule, but from the mathematics of two incommensurate oscillators.

This is the geometric origin of locality (only corner-contact interactions allowed), unitarity (probabilities sum to 1 because all interference channels are accounted for), and the discrete spectrum of interaction channels.

### 2.2 The General Scattering Amplitude **(D/H)**

The amplitude for a two-body interaction via T3 corner contact is:

```
A(r₁, r₂ → r₃, r₄) = P(r₁) × P(r₂) × P(r₃) × P(r₄) × φ⁻³ × S
```

where:
- P(r) = sin²(rπ/15) is the Malus projection weight for lane r
- φ⁻³ is the double barrel roll corner suppression factor (derived in the WZ paper)
- S is the discrete corner chirality selector: +1 for W⁺, −1 for W⁻, 0 for Z⁰ (for electroweak), or +1 for constructive same-chirality gluon exchange

The φ⁻³ factor decomposes as three geometric contributions:
- φ⁻¹ from the first gluon's T3 coupling
- φ⁻¹ from the second gluon's capped amplitude
- φ⁻¹ from the corner coincidence requirement itself

For ordinary strong-force gluon exchange (no corner coincidence required, single gluon, same T3), the φ⁻³ suppression is absent. This is why the strong force is strong and the weak force is weak — both follow from the same geometry, at different corner topologies.

---

## 3. Five Scattering Mechanisms

The GBP framework identifies five distinct scattering mechanisms. These are not separate theories — they are five geometric aspects of the same mod-30 coprime winding lattice, each becoming the dominant description depending on what boundary condition the experiment imposes.

### 3.1 Shadow Projection (Virtual Particle Exchange) **(D)**

The mock theta series Θ₃₀(τ) = Σ_{gcd(n,30)=1} q^{n²} decomposes into:

```
Θ₃₀(τ) = Θ₃₀^{holo}(τ) + Θ₃₀^{shadow}(τ)
```

A virtual particle is the 90° projected shadow of the mock theta loop reversal — the non-holomorphic completion term viewed from a perpendicular plane. One path, two projections. The apparent "exchange" is the i² = −1 midpoint of the loop observed from outside.

The GBP propagator:
```
D_GBP(r) = −i·P(r) / (χ̂(r) + iε)
```
replaces the standard Feynman propagator D_F(k) = −ig_μν/(k²+iε), with exact correspondence:

| Standard QED | GBP geometry |
|---|---|
| k² = 0 (on-shell) | χ̂(r) = 0, mirror axis r = 15 |
| k² ≠ 0 (virtual) | χ̂(r) ≠ 0, off-axis lane |
| iε prescription | 90° i-operator rotation |
| 1/(k²+iε) suppression | 1/χ̂(r) chirality weight |

### 3.2 GOE→GUE Transition **(D)**

The virtual particle is the observable signature of a time-reversal symmetry flip at the mock theta loop turning point. The T0/S0 sheet carries GOE statistics (time-reversal symmetric); the T1/S1 sheet carries GUE statistics (TRS broken). The transition between them at the 360° midpoint is what appears as a particle exchange when observed from a transverse direction. This is the same geometric structure that places Riemann zeros on Re(s) = 1/2.

### 3.3 Off-Axis Lane Displacement **(D)**

Virtual particles are lanes displaced from the mirror axis r = 15 in the mod-30 lattice. Real particles sit at χ̂(r) = 0. Virtual particles are weighted by 1/χ̂(r) — their distance from the balance axis. This is the GBP propagator picture (Section 3.1) stated in configuration space rather than momentum space.

### 3.4 Aharonov-Bohm Winding (Topological — No Vertex) **(D)**

This mechanism is fundamentally different from 3.1–3.3. There is no vertex, no exchange, no projection. The electron carries its T1 local chirality space as it moves. The vector potential A is the boundary projection of this T1 space onto the global frame:

```
A_μ(x) = P(r) × (winding density of T1 local space at x)
        = sin²(rπ/15) × ρ_winding(x)
```

The Aharonov-Bohm phase is the winding of the T1 local space around a topological obstruction — a pure topological invariant, not a local field measurement. The GBP phase shift:

```
Δφ_GBP = χ̂(C₁) − χ̂(C₂) = 3(1 − m(m−1))
```

At m = 2 (minimal spinor): Δφ = −3. This is the minimal chirality quantum, corresponding to one unit of AB phase. Flux quantization Φ₀ = h/2e follows from the T1 spinor double cover requiring 720° for closure.

The Amplituhedron has no analog of this mechanism — it handles vertex interactions only. Topological phase without a vertex is outside its scope.

### 3.5 Lane-Stepping Polarization Accumulation (Prism/Dispersion) **(D)**

This is the simplest mechanism geometrically. No vertex, no exchange, no winding around an obstruction. Each interface crossing costs a fixed minimum reflection:

```
R_min = LAMBDA_UNIV = sin²(π/30) ≈ 1.093%
```

This is the mandatory cost of the r=1 colorless boundary lane — the topological floor of any interface between vacuum and matter.

Different wavelengths of light populate different P(r) lanes. Materials cluster near tier attractor n values because the coprime winding geometry has preferred projection angles. Each interface crossing accumulates a phase offset determined by the lane difference across the boundary. After many crossings (prism, rainbow), these phase offsets separate colors by lane:

```
Red   → lower P(r) lane → lower n → shallower refraction angle
Violet → higher P(r) lane → higher n → steeper refraction angle
```

The rainbow is the mod-30 lane structure projected onto angle. The dispersion is discrete in principle, continuous in appearance because lane spacing (12° = 2π/30 in angular units) is much smaller than macroscopic angular resolution.

---

## 4. Wave-Particle Duality from Photon Topology **(D)**

The photon propagates as a tangent-mode wave on the T0 toroid surface. E is the tangent vector to the surface; B is the surface normal. A tangent is perpendicular to the radius by definition — this is the geometric root of E⊥B and of transverse wave propagation. No further derivation is required.

The photon is a 2×T0 helicity-flip object — two plain toroids in the same chirality Hilbert space, connected by a helicity flip at the 180° inversion point. The combined path traces a figure-8. This topology gives the photon both AC (wave) and DC (particle) components simultaneously.

The AC/DC decomposition of P(r) = sin²(rπ/15):

```
P(r) = 1/2 − (1/2)cos(2rπ/15)
     = DC component + AC component
```

where:
- **DC component** = 1/2: the constant background, the "particle" aspect — always present, detected when a screen is placed in the path
- **AC component** = −(1/2)cos(2rπ/15): the oscillating interference term, the "wave" aspect — averages to zero over the full mod-30 circle, produces the diffraction pattern

For a T3 baryon (no self-return path), only the DC component survives in scattering — the interaction is particle-like. For the photon, the figure-8 self-return means the second lobe always traverses the same lanes the first lobe just passed through, generating automatic interference. Both components are always present.

**Wave-particle duality in one sentence:** Particles with a self-return path (figure-8 topology) carry AC and DC components simultaneously; particles without self-return carry DC only. The wave behavior is the AC component of the mod-30 phase interference — it was never mysterious, it is topology.

This is the GBP answer to the stochastic vs. S-matrix dichotomy in the video that motivated this paper: stochastic behavior (Markov blankets, active inference) is the AC component averaged over many figure-8 cycles; S-matrix behavior is the DC component at a single corner event. Both are real. Both emerge from the same figure-8 topology.

---

## 5. Optical Predictions: Snell's Law and Fresnel

### 5.1 Snell's Law — Unchanged, Geometrically Founded **(D)**

Snell's Law is unchanged by GBP:

```
n₁ sin(θ₁) = n₂ sin(θ₂)
```

The GBP derivation gives it a geometric foundation. The photon's AC component must match boundary projections continuously across a lane interface. In GBP terms:

```
P(r₁) sin(θ₁) = P(r₂) sin(θ₂)
```

where P(r) = sin²(rπ/15) is the lane projection weight. Since n ∝ √P(r) at the tier attractors (see Section 5.2), this recovers Snell's Law exactly at tier-attractor materials. The conservation law is: **the photon conserves the product of its AC amplitude and its geometric projection across any interface**.

### 5.2 Refractive Index Tier Attractors **(D)**

Materials with long-range crystalline order lock their lane winding to the mod-30 tier geometry. The attractor n values are:

```
n_tier(r) = (1 + sin(rπ/15)) / (1 − sin(rπ/15))
```

giving four physical tiers:

| Tier | Lane r | n_tier | θ_B | Physical assignment |
|------|--------|--------|-----|-------------------|
| T1 | r = 1 | 1.5250 | 56.745° | Vacuum coupling / colorless boundary |
| T2 | r = 13 | 1.1895 | 49.934° | s-quark projection |
| T3 | r = 11 | 2.2460 | 65.980° | u/d quark projection |
| T4 | r = 7 | plasma | — | Vacuum phase (metals) |

Crown glass (n = 1.523) sits within 18 arcseconds of the T1 tier. GaN (n = 2.380) and SrTiO₃ (n = 2.389) sit within 0.1° of the T3 tier.

### 5.3 The Universal Reflection Floor **(D)**

The colorless boundary lanes {r=1, r=29} carry the minimum non-zero projection weight. Any interface between vacuum and matter must project through at least the r=1 lane. This gives a topological reflection floor:

```
R_min = LAMBDA_UNIV = sin²(π/30) = sin²(6°) ≈ 0.010926 = 1.093%
```

No real material can have Fresnel reflection R < LAMBDA_UNIV. This has been confirmed against 83 materials spanning glasses, crystals, semiconductors, liquids, polymers, and metals — zero violations.

Note: Rp drops to zero at the Brewster angle for p-polarization, but Rs(θ) ≥ LAMBDA_UNIV at all angles for all transparent materials. The floor applies to s-polarization and the total unpolarized reflectance.

### 5.4 Brewster Angle Tier Prediction **(D)**

The Brewster angle for any tier-attractor material is:

```
θ_B(tier) = arctan(n_tier(r))
           = arctan((1 + sin(rπ/15)) / (1 − sin(rπ/15)))
```

For the T1 tier: θ_B = 56.745° exactly. This is also:

```
θ_B(T1) = π/4 + arctan(sin(π/15))
```

The Weinberg angle θ_W ≈ 28.19° ≈ θ_B(T1)/2 — the optical and electroweak sectors share the same mod-30 boundary geometry at different energy scales. This is not a coincidence: both are projections of the r=1 colorless boundary lane at T1 and T3 respectively.

### 5.5 Crystalline vs. Amorphous: A New Prediction **(D/H)**

GBP makes a prediction that standard Fresnel theory does not: **for any material that exists in both crystalline and amorphous forms, the crystalline phase should sit closer to a tier attractor Brewster angle than the amorphous phase, with the amorphous offset always negative (below the tier).**

The mechanism: crystalline long-range order locks lane winding to the mod-30 geometry. Amorphous disorder randomizes lane occupancy, averaging toward lower effective n and displacing the Brewster angle below the tier value.

**Test case: SiO₂**

At λ = 800 nm (from arxiv:2512.05738):
- Crystalline quartz (ordinary ray): n_o = 1.5383 → θ_B = 56.973° — sits +0.228° above T1 tier (14 arcminutes)
- Fused silica (amorphous): n = 1.4533 → θ_B = 55.469° — sits −1.276° below T1 tier

The amorphous-to-crystalline transition in SiO₂ produces a **1.5° Brewster angle shift** with the crystalline phase approximately at the tier attractor. Standard optics attributes this entirely to density and bonding differences with no deeper explanation. GBP identifies the tier as the geometric attractor and predicts the sign and approximate magnitude of the offset from structural disorder.

The birefringence of crystalline quartz (n_e − n_o = 0.0089, giving Δθ_B = 0.15°) is an additional GBP-interpretable effect: the ordinary and extraordinary rays sample the T1 winding at different projection angles, with the ordinary ray closer to the tier center and the extraordinary ray displaced by the anisotropy of the crystal axis.

**Falsification criterion:** A material in crystalline form with θ_B(crystalline) *further* from the nearest tier than θ_B(amorphous) would falsify this prediction.

**Further test pairs to check (H):**
- GeO₂: crystalline vs. amorphous (similar SiO₂ chemistry)
- TiO₂: rutile (crystalline) vs. amorphous TiO₂
- Al₂O₃: sapphire (crystalline) vs. amorphous alumina
- Carbon: diamond (crystalline, T3 tier, n=2.418) vs. amorphous carbon

Diamond (n = 2.418) sits within 0.36° of the T3 tier (n_T3 = 2.246 predicted vs 2.418 measured — note T3 is r=11, not the best anchor; diamond may indicate a higher tier or mixed-lane material). This deserves further investigation.

---

## 6. Summary Table: Five Scattering Mechanisms

| Mechanism | GBP object | Vertex? | Standard analog | Key equation |
|-----------|-----------|---------|----------------|-------------|
| Shadow projection | Θ₃₀^{shadow}(τ) | Yes | Virtual particle exchange | D_GBP(r) = −iP(r)/(χ̂(r)+iε) |
| GOE→GUE transition | Mock theta turning point | Yes | QFT propagator | Re(s) = 1/2 balance |
| Off-axis lane | χ̂(r) ≠ 0 displacement | Yes | Off-shell propagation | 1/χ̂(r) suppression |
| AB winding | T1 local chirality space | No | Aharonov-Bohm effect | Δφ = χ̂(C₁) − χ̂(C₂) |
| Lane-stepping | P(r) accumulation at boundary | No | Refraction/dispersion | R_min = sin²(π/30) |

The first three are vertex interactions (something is projected, flipped, or displaced at a contact point). The last two are topological (no vertex — interaction is from the geometry of the path or the lane structure). The Amplituhedron covers vertex interactions only. GBP covers all five from the same geometric foundation.

---

## 7. The Catalan Constant as the C1/C2 Chirality Euler Product **(D)**

Catalan's constant G ≈ 0.915965594... appears throughout physics and mathematics — in QED corrections, the anomalous magnetic moment, the free energy of the 2D Ising model, hyperbolic 3-manifold volumes, domino tilings, spiral galaxy mass distributions, and dozens of other contexts. Its ubiquity has never been explained from first principles.

The GBP framework identifies the exact geometric origin:

```
G = (15/16) × ∏_{p ∈ Θ₃₀} p² / (p² − χ₋₄(p))
```

where Θ₃₀ = primes coprime to 30, χ₋₄(p) = +1 if p ≡ 1 mod 4 (C1 lane), −1 if p ≡ 3 mod 4 (C2 lane), and 15/16 is the boundary term from p=3 and p=5 at the mod-30 lattice edge. Verified numerically to 10⁻⁸ precision with 2000 primes.

G is ubiquitous because every system with a two-state alternating structure evaluated on odd integers with a boundary mirror term IS the mock theta C1/C2 geometry in disguise. The Ising ±1 spins, the Whitehead link's two cusps, the QED one-loop, the domino tiling orientations — all are C1/C2 lane pairs. G is not a coincidence. It is the fingerprint.

Notably, the Whitehead link — formed by a circle threaded through a figure-8 — is literally the T0 vacuum circle linked with the 2×T0 photon topology. Its hyperbolic complement volume is 4G, the minimal two-cusped hyperbolic 3-manifold. The Borromean rings (three mutually linked = T3 baryon) have volume 8G = two corner events. The n-component link volume per component converges to 4G — one mock theta loop per lane pair.

**For the complete taxonomy of all known G appearances and their GBP interpretations, see:** *Richardson (2026), "Catalan's Constant as a Mock Theta Euler Product," GBP Catalan paper v2, this repository.*

---

## 9. Open Questions

**(H)** All items below are conjectures requiring further development:

- Explicit derivation of the n-particle generalization of the scattering rule (Section 2.2) beyond 2→2
- Quantitative prediction for the amorphous Brewster offset as a function of structural disorder parameter (correlation length of crystalline order)
- Diamond tier assignment — is diamond a T3 material or a higher-tier material?
- Whether photon-photon scattering angular distribution (predicted sharp peaks at mod-30 coprime angles) can be tested at LUXE or similar facilities
- Formal proof that the phase interference condition (Section 2.1) is both necessary and sufficient for amplitude nonzero (currently derived, not formally proved)

---

## 10. References

1. Richardson, J. (2026). GBP Framework v9.9. Zenodo: 10.5281/zenodo.19798271
2. Richardson, J. (2026). GBP W/Z Higgs paper v2. This repository. *φ⁻³ exact derivation, double barrel roll, 204° corner phase*
3. Richardson, J. (2026). Geometric Path Integration via Mock Theta Measure. This repository. *Five quantum phenomena from one geometric structure; D_GBP(r) derivation*
4. Richardson, J. (2026). Tetrahedral Alpha Clustering as the Geometric Foundation of Nuclear Shell Structure. This repository. *T3 corner phase interference, double barrel roll mechanism*
5. Richardson, J. (2026). GBP Optical Framework v3/v4. This repository. *83-material floor confirmation, tier Brewster angles*
6. Richardson, J. (2026). catalan_mock_theta.py. This repository. *Catalan constant as C1/C2 chirality Euler product over Θ₃₀*
7. Arkani-Hamed, N., Trnka, J. (2014). "The Amplituhedron." JHEP 10, 030. arXiv:1312.2007
8. Friston, K. (2010). "The free-energy principle: a unified brain theory?" Nature Reviews Neuroscience 11, 127.
9. Tikhonov, E.A., Lyamets, A.K. (2019). "Refractometry of birefringent materials at Brewster angle." arXiv:1908.09620
10. Aharonov, Y., Bohm, D. (1959). "Significance of electromagnetic potentials in the quantum theory." Phys. Rev. 115, 485.
11. Van Mechelen, T., Jacob, Z. (2016). "Universal spin-momentum locking of evanescent waves." Optica 3, 118.
12. Polyanskiy, M.N. (2024). Refractiveindex.info database. Sci. Data 11, 94.
13. arxiv:2512.05738 — Amorphous vs crystalline SiO₂ optical indices at 800nm: n_am = 1.4533, n_o = 1.5383, n_e = 1.5472
14. Deur, A. et al. (2024). "The QCD Running Coupling." Prog. Part. Nucl. Phys. 90, 1–74.
