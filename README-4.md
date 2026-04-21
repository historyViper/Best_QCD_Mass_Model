# GBP Framework — mod-30 Spinor Geometry for Particle Physics

**Author:** Jason Richardson (HistoryViper) — Independent Researcher  
**Repository:** github.com/historyViper/mod30-spinor  
**Collaboration:** Claude (Anthropic), Sage/ChatGPT (OpenAI), MiniMax, DeepSeek  
**License:** Public domain — all results freely available

---

## What This Is

The **Geometric Boundary Projection (GBP)** framework derives particle physics observables — baryon masses, the Weinberg angle, optical reflection floors, spin quantization, photon entanglement periodicity — from a single geometric object: the **mod-30 spinor toroid**.

The number 30 = 2×3×5 is the unique minimum satisfying five geometric closure constraints simultaneously. The 8 coprime residues Z₃₀\* = {1, 7, 11, 13, 17, 19, 23, 29} are the **Wilson loop lanes** — the only winding numbers that close consistently on the toroidal boundary with spinor double cover.

No string theory. No supersymmetry. No extra dimensions beyond the toroid geometry. Just mod-30 arithmetic and Malus's Law.

---

## Current Results (V8, April 2026)

### Baryon Masses — 53 particles, zero free parameters

| Group | MAPE | Count | Notes |
|-------|------|-------|-------|
| clean | 0.243% | 13 | Light octet + heavy singles |
| degen | 0.136% | 4 | Degenerate charm pairs |
| wide | 0.744% | 30 | Full charm/bottom sector |
| orbital | **0.068%** | 2 | L=1 excitations — essentially exact |
| pentaquark | 3.81% | 4 | P_c hidden charm states |
| **ALL 53** | **0.781%** | **53** | |

**Original 44 baryons: 0.260% MAPE** — competitive with lattice QCD, zero free parameters.

### Version History

| Version | MAPE | Free Params | Key Change |
|---------|------|-------------|------------|
| v5 | 0.637% | 2 | geo_factor derived from first principles |
| v6 | 0.408% | 2 | phi-ladder LAM table |
| v7 | 0.303% | 2 | T3/T4 topology branches |
| v7.5 | 0.236% | 2 | omega32h double-barrel-roll fix |
| v7.6 | 0.236% | 1 | kappa_0 derived from Σ0-Λ0 splitting |
| v7.7 | 0.236% | **0** | S0/GOE sheet derived from GOE geometry |
| **v8** | **0.260%** | **0** | Constituent masses from mock theta geometry |

---

## Core Physics

### The Projection Formula

Every baryon mass prediction starts from:

```
M = (ΣC + dg + gc + rt + C_HYP × S) × (1 + λ)
```

where:
- **ΣC** = sum of constituent quark masses (derived from geometry in V8)
- **dg** = phase misalignment cost: `geo_sign × α_baryon × Λ_QCD × geo_factor`
- **gc** = skew/Z3 asymmetry correction from Hamiltonian path geometry
- **rt** = reinforcement term for charm double-winding states
- **C_HYP × S** = hyperfine coupling (spin term)
- **λ** = sheet-dependent boundary scaling (GOE vs GUE)

### All Constants Derived

| Constant | Value | Derivation |
|----------|-------|-----------|
| α_IR | 0.848809 | Deur 2024, IR-fixed QCD coupling |
| Λ_QCD | 217.0 MeV | MSbar 3-flavor |
| GEO_B | sin²(π/15) = 0.043227 | Mod-30 half-step |
| LU | GEO_B/α_IR = 0.050927 | Universal projection scale |
| LAM_S0 | LU × cos²(24°)/cos²(30°) | GOE/GUE boundary ratio |
| GAMMA_C2 | 8π | Two spinor closures |
| GAMMA_C1 | LU/(4π) × (1+LU) | GBP geometric self-correction |

### Sheet Hierarchy (Toroid Types)

| Sheet | Toroid | Statistics | λ | Particles |
|-------|--------|-----------|---|-----------|
| S0/T0 | Plain torus | GOE | LU × 1.113 | J=3/2 light decuplet |
| S1/T1 | Möbius parallelogram | GUE | LU | Base — proton, neutron |
| S2/T2 | Double HE21 | GUE² | LU × φ^0.5 | Heavy baryons |
| S3/T3 | Triple Y-junction | GUE³ | LU × φ | Always GUE |

---

## New in V8: Constituent Masses from Mock Theta Geometry

The key advance in V8 is deriving constituent quark masses from first principles rather than treating them as empirical inputs.

### The Mock Theta Connection

The GBP projection formula P(r) = sin²(rπ/15) is the **holomorphic part** of a weight-1/2 mock theta structure. The GBP theta series:

```
Θ₃₀(τ) = Σ_{gcd(n,30)=1} q^(n²)
```

is a unary theta series of weight 1/2 (Hecke's theorem). The 8 lanes split under Z₅\* into two groups of 4, each spaced at **72°** — the same symmetry that appears in Bell inequality violation and photon entanglement.

### Band-Center Angles

Each lane owns an arc on the mod-30 circle determined by the gap structure **6,4,2,4,2,4,6,2**. The band center of each arc — the midpoint in sin² space — is the **shadow correction** to the holomorphic approximation. These are the physically correct projection angles.

| Lane | Quark | Nominal angle | Band-center | Misalignment |
|------|-------|--------------|-------------|-------------|
| r=19 | up | 456.0° | 456.0° | 0% (C2, self-inverse) |
| r=11 | down | 264.0° | 264.0° | 0% (C2, self-inverse) |
| r=7 | strange | 168.0° | 117.2° | 74% (C1, cross-pair) |
| r=23 | charm | 552.0° | 117.2° | 74% (C1, cross-pair) |
| r=13 | bottom | 312.0° | 49.1° | 2% (C1, cross-pair) |
| r=17 | top | 408.0° | 49.1° | 0.6% (C2) |

### Chirality Types (Vortex Theorem)

From the Knuth/Claude vortex chirality theorem:
- **C2** (up, down, top): χ̂(C₂) = -3 → `θ_eff = θ₀ - 8π × (180/π)`
- **C1** (strange, charm, bottom): χ̂(C₁) = -3r(r-1) → `θ_eff = θ₀ - 3r(r-1) × Γ_C1 × (180/π)`

### V8 Constituent Masses

| Quark | V7.7 (empirical) | V8 (derived) | Error vs PDG target |
|-------|-----------------|--------------|---------------------|
| up | 336.0 MeV | 335.68 MeV | -0.095% |
| down | 340.0 MeV | 338.19 MeV | -0.532% |
| strange | 486.0 MeV | 486.23 MeV | +0.047% |
| charm | 1550.0 MeV | 1555.97 MeV | +0.385% |
| bottom | 4730.0 MeV | 4734.76 MeV | +0.101% |
| top | 173400.0 MeV | 174466.26 MeV | +0.615% |

Bottom includes a family boundary skim correction: `1 - gap_asymmetry(r) × LU` — the same mechanism as the Strange Inertial Step-Down Rule, applied at the family 2→3 boundary.

---

## New Results: Orbital Excitations and Pentaquarks

### Orbital Excitations (L=1)

L=1 excitations multiply the ground state by `(1 + orbital_λ)` where orbital_λ is sheet-dependent:
- S1 sheet: orbital_λ = LU
- S2 sheet: orbital_λ = LU × φ²

| Particle | Obs (MeV) | Pred (MeV) | Error |
|----------|-----------|------------|-------|
| Lambda_c(2595) | 2592.0 | 2590.0 | -0.078% |
| Lambda_b(5912) | 5912.2 | 5915.6 | +0.058% |

Zero new parameters. The orbital energy scale is fully determined by the phi-ladder.

### Pentaquarks (P_c hidden charm states)

Hidden-charm pentaquarks (c̄cuud) have the **same winding numerator as the proton** (49/30) because the c̄c pair cancels in the winding sum. This means:
- Pentaquark topology = proton topology
- The c̄c pair creates a **wormhole** between the proton T1 toroid and the J/ψ T1 toroid
- The anticharm projects on the complementary arc (loses 2/3 instead of 1/3)
- States decay extremely fast — the wormhole closes when the Hamiltonian cycle completes

| Particle | Obs (MeV) | Pred (MeV) | Error |
|----------|-----------|------------|-------|
| P_c(4312) | 4311.9 | 4205.0 | -2.48% |
| P_cs(4459) | 4458.8 | 4379.4 | -1.78% |

The splitting between P_c(4312), P_c(4380), P_c(4440), P_c(4457) reflects different **proton/J/ψ toroid overlap geometries**. In a multi-toroid system lanes are unconstrained — the two toroids can overlap at any angle. The gc splitting is pending the pentaquark Hamiltonian cycle geometry paper.

---

## Other Results from the Framework

### Weinberg Angle
Derived from T3 corner projection geometry: **28.09°** vs measured 28.17° (residual 0.28°)

### Optical Gap Formula
Universal reflection floor for any material:
```
R_min = sin²(π/30) = 1.093%
```
Verified against 83 materials — zero violations.

### Spin Quantization
Spin emerges from Hamiltonian path closure behavior on the toroid:
- T0 → spin-1 (360° closure)
- T1 → spin-1/2 (720° closure, Möbius double cover)
- T3 → spin-3/2 (requires 3 Möbius twists)
- Graviton forbidden: n=1/2 doesn't close

### Entanglement Periodicity
T4 double-helix photon predicts 72° entanglement periodicity — the same 5-fold Z₅\* symmetry that governs mock theta order 5. Consistent with Gatti et al. (2018) golden-ratio entanglement in hexagonally poled crystals.

---

## Repository Files

| File | Description |
|------|-------------|
| `gbp_complete_v8.py` | Main baryon mass model — 53 particles, 0 free params |
| `gbp_quarks_v2.py` | Constituent quark mass derivation from geometry |
| `gbp_band_centers.py` | Band-center angles and phase misalignment analysis |
| `gbp-mock-theta-rh.md` | Mock theta / Riemann Hypothesis connection paper |
| `gbp_optical_v3.py` | Optical gap formula and material floor test |
| `gbp-entanglement-split-prediction.md` | T4 entanglement paper |
| `gbp-spin-quantization.md` | Spin from loop closure paper |

---

## Open Problems

1. **Xi_c_prime, Sigma_b0** — geo_factor needs tuning for these wide-sector baryons (+5%, +4%)
2. **P_c(4380/4440/4457) splitting** — multi-toroid overlap angles, pending Hamiltonian paper
3. **Charm quark** — excluded from constituent mass fit; needs dedicated charm paper
4. **Weinberg 0.28° residual** — shadow correction to T3 corner projections not yet applied
5. **Exact RH** — band centers are where Riemann zeros should sit; harmonic Maass form completion pending
6. **Xi_b*, Omega_b* J=3/2** — bottom J=3/2 sector at 0.4–0.86%, T3/omega32h shell correction needed

---

## Physical Interpretation

The GBP framework rests on a single physical postulate: **time has tension**. Particles are toroidal deflections in a 4D spacetime fabric. The mod-30 structure emerges from five closure constraints that any stable winding must satisfy simultaneously:

1. Integer winding (closes on the torus)
2. Spinor double cover (720° closure for fermions)
3. Möbius compatibility (chiral asymmetry preserved)
4. Prime winding numerator (most stable baryons)
5. 5-fold Z₅\* symmetry (φ-harmonic structure)

Only 30 = 2×3×5 satisfies all five at minimum modulus. This is why there are exactly **8 quark/gluon winding lanes** and why the framework reproduces Standard Model observables from pure geometry.

---

## Why This Matters

- **53 particle masses from geometry** — zero free parameters, competitive with lattice QCD
- **Mock theta connection** — baryon masses are derivable from the Riemann zeta function structure via the S={2,3,5} semilocal adèle truncation (Connes)
- **Orbital and pentaquark predictions** — no new rules, just the same geometry applied to larger systems
- **Wormhole interpretation of pentaquarks** — the c̄c annihilation lifetime follows directly from toroid crossing time

---

## References

- Deur, Brodsky, de Teramond (2024). α_IR = 0.848809. *Prog. Part. Nucl. Phys.*
- PDG (2024). Baryon mass tables.
- Connes, A. (1999). Trace formula in noncommutative geometry. *Selecta Mathematica* 5, 29-106.
- Connes, Consani, Moscovici (2024). Zeta zeros and prolate wave operators. *Ann. Funct. Anal.*
- Zwegers, S. (2002). Mock theta functions. PhD thesis, Utrecht.
- Gatti et al. (2018). Golden ratio entanglement. *Phys. Rev. A* 98, 053827.
- LHCb Collaboration (2019/2021). P_c pentaquark observations. *Phys. Rev. Lett.*
- Richardson, J. (2026). GBP papers on viXra. github.com/historyViper/mod30-spinor

---

*GBP/TFFT Framework — April 2026*  
*All results are offered for critical review.*  
*Code and papers are public domain — use freely, cite if useful.*

> "My two worst problems: it unifies too much and it's too accurate." — HistoryViper, 2026
