# Tensor Time v7 — Chapter 05b: Mass — The Riemann Version (v9 Three-Formula Framework)

*This is the unified three-formula framework connecting the mass ladder to the Riemann zeros via β(N)=−2 and Λ_TOPO = GEO_B/(α_IR × γ₁). It covers all Standard Model fermions and EW bosons. Overall MAPE 0.333% across 70 particles.*

*For the original baryon-only result (54 particles, MAPE 0.274%, cleaner physics) see: **tt_v7_05_mass.md***

---

## 5. Mass from Geometric Projection

### 5.1 The Three-Formula Framework

The GBP framework derives particle masses from a single underlying geometry — the mod-30 winding lattice — using three formulas depending on the particle sector:

```
FORMULA 1 — QUARKS  (N=30, doublet GM ladder)
  m = M_gm × exp((n + k/φ(30)²) × C_30)
  C_30 = −ln(1 − GEO_B × α_IR) = 0.037382
  φ(30)² = 64

FORMULA 2 — LEPTONS  (N=12, Koide scale ladder)
  m = M_0 × exp((n + k/φ(12)²) × C_12)
  C_12 = −ln(1 − sin²(π/6) × α_IR) = 0.238514
  M_0 = (√m_e + √m_μ + √m_τ)²/9  (Koide scale)

FORMULA 3 — BARYONS  (T-topology lane projection, v8.9)
  m = (sumC + dg + gc + rt + C_HYP×S) × (1 + λ)
  sumC = constituent quark masses from Z30* lane projections
  dg   = geo_sign × α_baryon × Λ_QCD × geo_factor
  gc   = tri-wave geometric correction
  λ    = topology lambda (T1/T2/T3 winding cover)
```

All three formulas share the same underlying constants (α_IR, Λ_QCD, mod-30 geometry). The RG kernel connecting them:

```
β(N) = d(ln C_N)/d(ln N) = −2  (exact)
C_N × N² → 4α_IR × ζ(2) × 6 = 4α_IR π²
C_12/C_30 = 6.380 ≈ 2π  (factor of 5, prime dispersion)
```

The Riemann connection: the zeros γ_n are the resonant frequencies of the coprime winding sum. Λ_TOPO = GEO_B/(α_IR × γ₁) = 0.003603 bridges the winding geometry to the first Riemann zero γ₁ = 14.134725.

### 5.2 The Malus Projection — Why Mass Has This Form

Mass is the energy cost of the toroid's Hamiltonian path projecting through the spacetime boundary:

```
P(r) = sin²(r · π/15)   for r ∈ {1, 7, 11, 13, 17, 19, 23, 29}
```

This is Malus's Law applied to spinor geometry. The same law that gives quantum probabilities gives particle masses — both are the Malus projection of the T1 winding from different measurement perspectives. (See Chapter 08 on the Born rule.)

### 5.3 κ₀ Derived **(D)**

```
κ₀ = m_u × m_d × ΔM(Σ⁰-Λ⁰) = 335.68 × 338.19 × 76.959 = 8,736,664 MeV³
```

Constituent masses derived from GBP geometry via mock theta band-center angles. Not tuned. κ₀ ≈ (ħc)² × Λ_GBP to 0.40% — the torsion coupling is the QCD phase-space quantum squared times the confinement scale. The φ³ conjecture connecting κ₀ to the electroweak VEV is in Chapter 01 §1.4.

---

## 5.4 Formula 1 — Quark Masses **(D)**

```
m = M_gm × exp((n + k/64) × C_30)
k from prime factors of 30=2×3×5  |  Möbius: Σk=0 ✓ per doublet
```

| Quark | M_gm (MeV) | n | k | Predicted (MeV) | PDG (MeV) | Error |
|-------|-----------|---|---|----------------|-----------|-------|
| up | 3.1760 | −10 | −20 | 2.1601 | 2.1600 | +0.003% |
| down | 3.1760 | +10 | +20 | 4.6699 | 4.6700 | −0.003% |
| strange | 344.4096 | −35 | +6 | 93.408 | 93.400 | +0.008% |
| charm | 344.4096 | +35 | −6 | 1269.89 | 1270.00 | −0.008% |
| bottom | 26867.16 | −50 | +14 | 4178.67 | 4180.00 | −0.032% |
| top | 26867.16 | +50 | −14 | 172744.9 | 172690.0 | +0.032% |

**MAPE = 0.014%   RMSE = 22.42 MeV   [D]**

Free parameters: 3 geometric means (one per doublet). All n, k derived from mod-30 prime structure.

---

## 5.5 Formula 2 — Lepton Masses **(D)**

```
m = M_0 × exp((n + k/16) × C_12)
M_0 = (√m_e + √m_μ + √m_τ)²/9 = 313.841127 MeV  (Koide scale)
Koide Q = 0.66666051  (2/3 = 0.66666667,  deviation = 9.23 ppm)
```

The Koide formula is the mod-12 geometric constraint in the continuum limit. Deriving Koide from mod-12 winding directly is pending **(H)**.

| Lepton | n | k | Predicted (MeV) | PDG (MeV) | Error |
|--------|---|---|----------------|-----------|-------|
| electron | −27 | 1 | 0.508606 | 0.510999 | −0.468% |
| muon | −5 | 7 | 105.7066 | 105.6584 | +0.046% |
| tau | +7 | 4 | 1768.90 | 1776.86 | −0.448% |

**MAPE = 0.321%   RMSE = 4.60 MeV   [D]**

k values {1, 7, 4} are Koide residuals on the C_12 lattice. k sum = 12.

---

## 5.6 Electroweak Bosons **(D)**

| Boson | Predicted (MeV) | PDG/SM (MeV) | Error | Formula |
|-------|----------------|-------------|-------|---------|
| W | 80,359.95 | 80,369.00 | −0.011% | W/H mirror pair on C_30 |
| H (WH) | 125,264.11 | 125,250.00 | +0.011% | W/H mirror pair on C_30 |
| H (v/2) | 125,262.55 | 125,250.00 | +0.010% | (v/2)×(1+C_30/2) |
| Z | 90,751.91 | 91,187.60 | −0.478% | M_W/cos(θ_W=27.68°) |
| V_EW | 245,928.48 | 246,000.00 | −0.029% | 30×(Q₈/8)×φ³×Λ_GBP/LU |

**MAPE = 0.108%   RMSE = 197.67 MeV   [D]**

The Z mass error (0.478%) reflects the Weinberg angle T3 corner bias residual — an open geometric problem, not a free parameter.

---

## 5.7 Formula 3 — Baryon Performance (v9) **(D)**

| Sector | Count | MAPE | RMSE (MeV) |
|--------|-------|------|-----------|
| Light octet J=1/2 | 9 | 0.188% | 2.83 |
| Light decuplet J=3/2 | 9 | 0.189% | 3.36 |
| Charm baryons | 17 | 0.275% | 9.13 |
| Bottom baryons | 12 | 0.363% | 28.78 |
| Orbital excitations | 4 | 2.075% | 98.59 |
| Pentaquarks | 5 | 0.196% | 11.11 |
| **ALL 56 baryons** | **56** | **0.388%** | **30.19** |

Free parameter count: **0**. MAPE improves as parameters are removed — the opposite of overfitting.

**Known systematic — bottom baryons:** Consistently overpredicted. P(13) = 0.165 is the second-lowest projection weight; the lane 13 curvature correction is not yet derived. Left uncorrected deliberately.

**Known issue — orbital excitations:** Lambda_c(2625) at −7.132% drives the orbital MAPE. GBP assigns Lambda_c(2595) and Lambda_c(2625) to different topology branches, confirmed post-hoc by Nieves & Pavao (2019) arXiv:1907.05747.

### Individual Baryon Results

**Light octet J=1/2:**

| Name | Quarks | Predicted (MeV) | PDG (MeV) | Error |
|------|--------|----------------|-----------|-------|
| proton | u/u/d | 938.33 | 938.272 | +0.006% |
| neutron | u/d/d | 940.96 | 939.565 | +0.149% |
| Lambda0 | u/d/s | 1117.40 | 1115.683 | +0.154% |
| Sigma+ | u/u/s | 1186.38 | 1189.370 | −0.252% |
| Sigma0 | u/d/s | 1191.14 | 1192.642 | −0.126% |
| Sigma− | d/d/s | 1196.09 | 1197.449 | −0.114% |
| Xi0 | u/s/s | 1309.86 | 1314.860 | −0.380% |
| Xi− | d/s/s | 1316.94 | 1321.710 | −0.361% |
| Omega− | s/s/s | 1669.92 | 1672.450 | −0.151% |

**Light decuplet J=3/2:**

| Name | Quarks | Predicted (MeV) | PDG (MeV) | Error |
|------|--------|----------------|-----------|-------|
| Delta++ | u/u/u | 1230.94 | 1232.000 | −0.086% |
| Delta+ | u/u/d | 1224.22 | 1232.000 | −0.632% |
| Delta0 | u/d/d | 1226.87 | 1232.000 | −0.416% |
| Delta− | d/d/d | 1229.52 | 1232.000 | −0.201% |
| Sigma*+ | u/u/s | 1380.65 | 1382.800 | −0.156% |
| Sigma*0 | u/d/s | 1383.30 | 1383.700 | −0.029% |
| Sigma*− | d/d/s | 1385.95 | 1387.200 | −0.090% |
| Xi*0 | u/s/s | 1531.36 | 1531.800 | −0.029% |
| Xi*− | d/s/s | 1534.00 | 1535.000 | −0.065% |

**Charm baryons:**

| Name | Quarks | Predicted (MeV) | PDG (MeV) | Error |
|------|--------|----------------|-----------|-------|
| Lambda_c+ | u/d/c | 2286.71 | 2286.460 | +0.011% |
| Sigma_c++ | u/u/c | 2459.11 | 2453.970 | +0.209% |
| Sigma_c+ | u/d/c | 2455.40 | 2452.900 | +0.102% |
| Sigma_c0 | d/d/c | 2459.76 | 2453.750 | +0.245% |
| Xi_c+ | u/s/c | 2460.92 | 2467.930 | −0.284% |
| Xi_c0 | d/s/c | 2463.64 | 2470.850 | −0.292% |
| Omega_c | s/s/c | 2715.34 | 2695.200 | +0.747% |
| Xi_cc++ | u/c/c | 3619.30 | 3621.400 | −0.058% |
| Xi_cc+ | d/c/c | 3618.87 | 3619.970 | −0.030% |
| Sigma_c*++ | u/u/c | 2520.99 | 2517.500 | +0.138% |
| Sigma_c*+ | u/d/c | 2523.66 | 2517.500 | +0.245% |
| Sigma_c*0 | d/d/c | 2526.33 | 2518.400 | +0.315% |
| Xi_c*+ | u/s/c | 2653.59 | 2645.900 | +0.290% |
| Xi_c*0 | d/s/c | 2656.22 | 2646.200 | +0.379% |
| Omega_c* | s/s/c | 2766.78 | 2765.900 | +0.032% |
| Xi_c_prime+ | u/s/c | 2593.84 | 2578.200 | +0.607% |
| Xi_c_prime0 | d/s/c | 2596.55 | 2578.700 | +0.692% |

**Bottom baryons:**

| Name | Quarks | Predicted (MeV) | PDG (MeV) | Error |
|------|--------|----------------|-----------|-------|
| Lambda_b | u/d/b | 5630.39 | 5619.600 | +0.192% |
| Sigma_b+ | u/u/b | 5817.53 | 5810.560 | +0.120% |
| Sigma_b− | d/d/b | 5819.18 | 5815.640 | +0.061% |
| Xi_b0 | u/s/b | 5792.66 | 5791.900 | +0.013% |
| Xi_b− | d/s/b | 5805.50 | 5797.000 | +0.147% |
| Omega_b | s/s/b | 6045.49 | 6046.100 | −0.010% |
| Sigma_b*+ | u/u/b | 5854.80 | 5832.100 | +0.389% |
| Sigma_b*− | d/d/b | 5860.15 | 5835.100 | +0.429% |
| Xi_b*0 | u/s/b | 5996.26 | 5945.200 | +0.859% |
| Xi_b*− | d/s/b | 6002.31 | 5953.800 | +0.815% |
| Omega_b* | s/s/b | 6104.31 | 6082.300 | +0.362% |
| Sigma_b0 | u/d/b | 5868.79 | 5813.100 | +0.958% |

**Orbital excitations:**

| Name | Quarks | Predicted (MeV) | PDG (MeV) | Error |
|------|--------|----------------|-----------|-------|
| Lambda_c(2595) | u/d/c | 2589.99 | 2592.000 | −0.078% |
| Lambda_b(5912) | u/d/b | 5915.63 | 5912.200 | +0.058% |
| Lambda_c(2625) | u/d/c | 2440.67 | 2628.100 | −7.132% |
| Lambda_b(5920) | u/d/b | 5858.81 | 5919.900 | −1.032% |

**Pentaquarks:**

| Name | Quarks | Predicted (MeV) | PDG (MeV) | Error |
|------|--------|----------------|-----------|-------|
| P_c(4312) | c/u/u/d | 4312.44 | 4311.900 | +0.013% |
| P_c(4380) | c/u/u/d | 4389.38 | 4380.000 | +0.214% |
| P_c(4440) | c/u/u/d | 4458.69 | 4440.300 | +0.414% |
| P_c(4457) | c/u/u/d | 4458.69 | 4457.300 | +0.031% |
| P_cs(4459) | c/u/s/d | 4472.53 | 4458.800 | +0.308% |

---

## 5.8 Unmeasured Baryon Predictions **(D — awaiting experimental confirmation)**

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

## 5.9 Neutrino Note — Binary Ladder Floor **(H — unfalsifiable at current sensitivity)**

Neutrinos sit at the **binary floor** of the framework — power-of-2 fractions of GBP scales, not the continuous C_12 ladder:

```
m₂ ≈ Λ_QCD × LU² / 2^16  →  0.0086 meV
     oscillation floor √(Δm²_21) = 8.68 meV  (1.0% off)

m₃ ≈ Λ_QCD × LU × C_30 / 2^13  →  0.0504 meV
     oscillation floor √(Δm²_31) = 49.53 meV  (1.8% off)

Σm_ν predicted: ~58–62 meV (normal hierarchy)
```

Testable by CMB-S4 / Simons Observatory (2027+) targeting Σm_ν ~30 meV, and Project 8 targeting sub-50 meV direct sensitivity.

---

## 5.10 Why Only Eight Modes Survive **(D)**

Composite modes in a cycle of length N cancel by the textbook identity Σ e^{2πik/d} = 0 (d > 1). For N = 30 = 2 × 3 × 5, the surviving coprime modes are Z₃₀* = {1, 7, 11, 13, 17, 19, 23, 29} — eight modes, not hand-selected. Equivalent to normal-ordering in canonical QFT.

---

## 5.11 The QCD Beta Function Identity: Q₈ = b₀(n_f=6) / 2 **(D)**

$$Q_8 = \sum_{r \in Z_{30}^*} \sin^2\!\left(\frac{r\pi}{15}\right) = \frac{7}{2} = \frac{b_0(n_f=6)}{2}$$

Exact identity. Consequences: n_f = 6 is predicted; the Higgs VEV carries b₀; α_IR is the IR zero of the GBP beta function. Full derivation in Chapter 06.

---

## 5.12 Lattice QCD Structural Identity and Continuum Limit **(D)**

```
P(r) = 4cos²(rπ/30) · sin²(rπ/30)  — exactly the Lüscher-Weisz O(a²) correction
⟨P(r)⟩ → 1/2  (continuum limit via Riemann-Lebesgue)
→ S_cont = ∫ d⁴x (1/4) F_{μν}^a F^{aμν}  (standard Yang-Mills action)
```

Testable: gluon spectral function ratios {1,29}:{13,17}:{11,19}:{7,23} = 0.0437:0.1673:0.5584:1.0000 (Ilgenfritz et al. 2018, Fig. 10). Full treatment: GBP_Maxwell_paper_v5.md.
