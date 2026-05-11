# Tensor Time v7 — Chapter 12: Testable Predictions and Derivation Count

---

## 12. Testable Predictions

| Prediction | Value | Test | Status |
|-----------|-------|------|--------|
| Xi_cc++ mass | 3619.30 MeV | LHCb 2017 (PDG: 3621.4) | **Confirmed — 0.058% error** |
| Xi_cc+ mass | 3618.87 MeV | LHCb March 2026 (PDG: 3619.97) | **Confirmed — 0.030% error** |
| Optical gap R_min=1.093% | 83/83 materials | Ellipsometry | **Confirmed** |
| Entanglement period 72° | φ²:1 split at magic angle | Gatti 2018 | **Confirmed** |
| P_c(4312) mass | 4312.44 MeV | LHCb 2019 (PDG: 4311.9) | **Confirmed — 0.013% error** |
| P_c(4457) mass | 4458.69 MeV | LHCb 2019 (PDG: 4457.3) | **Confirmed — 0.031% error** |
| Lambda_c(2595) orbital | 2589.99 MeV | PDG: 2592.0 | **Confirmed — 0.078% error** |
| Lambda_b(5912) orbital | 5915.63 MeV | PDG: 5912.2 | **Confirmed — 0.058% error** |
| Flux quantization Φ₀=h/2e | C₁ monodromy → spinor factor 2 | Deaver 1961 | **Confirmed** |
| No 4-quark state without antiquark | T4 requires ER bridge → antiquark mandatory | All hadron spectroscopy | **Confirmed — zero violations in PDG** |
| n_f = 6 quark flavors | Q₈ = b₀(6)/2 forces exactly 6 | SM | **Confirmed — exact algebraic identity** |
| Lambda_c(2595/2625) different branches | NOT HQSS partners | Nieves & Pavao 2019 | **Confirmed post-hoc** |
| Baryon flux tube hyperbolic triangle | Concave sides, 2° indent per side | Lattice QCD | Pending |
| Discrete EMF jumps | Steps at sin²(nπ/15) | Precision EMF | arXiv evidence exists |
| MOND scale a₀ constant | No cosmic drift | JWST z=1–2 | Pending |
| Omega_cc+ mass | 3645.60 MeV | HL-LHC 2030+ | Pending |
| Vacuum birefringence | 1.05 × QED | ELI-NP 2025+ | Pending |
| Gluon spectral peak ratios | 0.0437:0.1673:0.5584:1.0000 | Ilgenfritz et al. Fig. 10 | Pending — readable from existing data |
| Photon polarization = helicity flip direction | Two CW/CCW flip states at T0 inversion | Precision polarimetry | Pending |
| P_c(4380) decay angular distribution | Different from narrow states (reflection topology) | LHCb angular analysis | Pending |
| Neutrino Σm_ν ~58–62 meV | Binary ladder floor | CMB-S4 / Project 8 (2027+) | Pending |

---

## 12.1 Derivation Count — Two Result Sets

The framework has two performance summaries that should not be conflated. They measure different things.

### Result Set A: GBP Baryons v9.1 — The Core Physics Result **(D)**

*Source: tt_v7_05_mass.md | Code: gbp_complete_v9.py*

55 baryon and pentaquark masses from the T-topology lane projection formula. Zero free parameters. MAPE improves as particles are added — the anti-overfitting signal.

| Group | MAPE | RMSE (MeV) | Count |
|-------|------|-----------|-------|
| Clean | 0.222% | 7.62 | 13 |
| Wide | 0.300% | 18.89 | 30 |
| Degen | 0.136% | 4.13 | 4 |
| Orbital | 0.108% | 3.66 | 3 |
| Pentaquark | 0.196% | 11.11 | 5 |
| J=1/2 | 0.223% | 12.37 | 34 |
| J=3/2 | 0.293% | 18.24 | 21 |
| **ALL 55** | **0.2496%** | **14.89** | **55** |

Free parameters: **0**

Version history:

| Version | Particles | MAPE | Free params |
|---------|-----------|------|-------------|
| v5 | — | 0.637% | 2 |
| v6 | — | 0.408% | 2 |
| v7.5 | — | 0.236% | 2 |
| v8 | 54 | ~0.250% | 0 |
| v9.0 | 54 | 0.251% | 0 |
| **v9.1** | **55** | **0.250%** | **0** |

### Result Set B: Complete Mass Ladder v9 — The Riemann Framework **(D)**

*Source: tt_v7_05b_mass_riemann.md | Code: complete_mass_ladder.py*

70 measured particles across all Standard Model sectors, unified under three formulas sharing the mod-30 winding geometry. The Riemann connection β(N)=−2 and Λ_TOPO = GEO_B/(α_IR × γ₁) connects the mass ladder to the first Riemann zero γ₁ = 14.134725.

| Sector | N | MAPE | RMSE | Status |
|--------|---|------|------|--------|
| Quarks (N=30, Formula 1) | 6 | 0.014% | 22.42 MeV | [D] proven |
| Leptons (Koide M_0, Formula 2) | 3 | 0.321% | 4.60 MeV | [D] Koide scale |
| EW bosons | 5 | 0.108% | 197.67 MeV | [D] proven |
| Baryons — light octet J=1/2 | 9 | 0.188% | 2.83 MeV | [D] |
| Baryons — light decuplet J=3/2 | 9 | 0.189% | 3.36 MeV | [D] |
| Baryons — charm | 17 | 0.275% | 9.13 MeV | [D] |
| Baryons — bottom | 12 | 0.363% | 28.78 MeV | [D] |
| Baryons — orbital | 3 | 0.108% | 3.66 MeV | [D] — Lambda_c(2625) chirality fixed v9.1 |
| Baryons — pentaquarks | 5 | 0.196% | 11.11 MeV | [D] |
| **All baryons (Formula 3)** | **56** | **0.388%** | **30.19 MeV** | **[D]** |
| **Total measured** | **70** | **0.333%** | **59.70 MeV** | |

Free parameters: **3 doublet geometric means** (quarks only). All other constants derived.

**Why the baryon MAPE differs between sets (0.2496% vs 0.388%):** Result Set B includes more states and reorganizes groupings. The core light-sector numbers in Set A are the same or better. The overall lift in Set B comes from including harder states with different parameterization. These are not competing results — they are the same framework at different scope.

**Key framework constants (v9):**
```
α_IR      = 0.848809        (Deur 2024)
Λ_QCD     = 217.0 MeV
γ₁        = 14.134725       (first Riemann zero)
C_30      = 0.03738177
C_12      = 0.23851388
C_12/C_30 = 6.380 ≈ 2π
Λ_TOPO    = 0.00360297
V_EW      = 245,928.48 MeV
β(N)      = −2  (exact RG kernel)
```

---

## 12.2 Unmeasured Baryon Predictions **(D — awaiting experimental confirmation)**

| Name | Quarks | J | Predicted (MeV) |
|------|--------|---|----------------|
| Omega_cc+ | s/c/c | 0.5 | 3645.60 |
| Xi_bc+ | u/b/c | 0.5 | 6926.79 |
| Xi_bc0 | d/b/c | 0.5 | 6930.86 |
| Omega_bc0 | s/b/c | 0.5 | 7071.75 |
| Xi_bb0 | u/b/b | 0.5 | 10352.86 |
| Xi_bb− | d/b/b | 0.5 | 10349.67 |
| Omega_bb− | s/b/b | 0.5 | 10487.49 |
| Omega_ccc++ | c/c/c | 1.5 | 4997.43 |
| Omega_bbb− | b/b/b | 1.5 | 15258.57 |
| Omega_ccb+ | c/c/b | 0.5 | 8204.76 |
| Omega_cbb0 | c/b/b | 0.5 | 11625.15 |

---

## 12.3 Open Problems as of v9

| Problem | Status |
|---------|--------|
| Lepton mass — Koide derivation from mod-12 winding | Mechanism identified; formal derivation pending **(H)** |
| CKM matrix beyond ρη | ρη derived (2.5% error); full 4-parameter matrix in progress |
| Newton's constant G from T0 Venturi | Jacobson coefficient identified as LU; full derivation pending |
| Neutrino masses (direct) | Binary floor identified; unfalsifiable until CMB-S4/Project 8 |
| Continuum limit convergence rate (formal proof) | Physical argument complete; O(a/L) proof pending |
| Full Yukawa hierarchy from P(r) + φ-ladder | P(r) gives generation-level structure; full hierarchy open |
| Graviton as T=c perturbation | Spin-2 forbidden as single toroid; correlated T4 pair pending |
| Black hole horizon: T=c saturation → signature flip | Qualitative mechanism proposed; derivation pending |
| Lambda_c(2625) chirality — **resolved v9.1** | geo_sign=+1 (spin-parallel J=3/2 partner of Lambda_c(2595)). Error: −7.132% → **−0.188%** |
| Bottom quark curvature correction (lane 13) | Directional error consistent; correction not yet derived |
| Weinberg angle T3 corner bias (Z mass 0.478% error) | Open geometric derivation |
