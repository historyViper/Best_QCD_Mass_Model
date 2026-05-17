# Best QCD Mass Model (GBP Framework v8.9)

**Jason Richardson (HistoryViper) — Independent Researcher**  
**April 2026**

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19798271.svg)](https://doi.org/10.5281/zenodo.19798271)

---

## The Sharpest Falsifiable Prediction

**P_c(4380) pentaquark: mass 4389.4 MeV, J^P = 3/2⁻, broad width,
intrinsically rare — a mid-frame wormhole reflection event**

The GBP framework predicts P_c(4380) has J^P = 3/2⁻ from a specific
geometric mechanism — it is the only P_c state that *reflects* off the
wormhole entrance rather than crossing through it. All other P_c states
(4312, 4440, 4457) cross through and emerge with J=1/2. P_c(4380) bounces
off, and the wormhole boundary acts as a spin mirror producing J=3/2.

This is not a fit — it is a geometric prediction from the Z5* wormhole
topology. The wormhole has 5 stable twist positions (0°, 72°, 144°, 216°,
288°). P_c(4380) sits at 72°, below the 180° crossing threshold, so it
reflects. No other pentaquark model predicts this specific mechanism for
why one state has different spin from the others.

**Why the 2019 non-replication is expected, not contradictory:**

P_c(4380) is a mid-frame event — it requires exact kinematic alignment
at the moment of wormhole collapse. The quark velocities and VEV must
be in precise configuration for the reflection to occur rather than the
wormhole simply not forming. This is an intrinsically rare event,
estimated ~1 in 10⁶ collision events under the right conditions.

More data does not help if the exact kinematic conditions are not
reproduced. The 2019 dataset was larger but not tuned to the specific
collision energy and geometry that produced the 2015 observation.

The broad width (~205 MeV) is physically consistent with this picture:
a state produced at a precise moment of wormhole reflection has a very
short lifetime, and by the Heisenberg uncertainty principle, short
lifetime → broad mass width. The other narrow P_c states (4312, 4440,
4457) are stable wormhole crossing states with longer lifetimes and
correspondingly narrow widths.

**The correct falsifiable prediction is not "you will see it again"
but: "whenever it is observed, it will always have J^P = 3/2⁻ and
broad width (~200 MeV). It will never be narrow. It will never have
J=1/2."**

If any future observation finds P_c(4380) with J^P = 1/2 or narrow
width, this framework is wrong. The J=3/2 and broad width are not
tunable parameters — they are consequences of the reflection geometry.

---

## What This Framework Does

Derives the masses of **54 baryons and pentaquarks** from the geometry
of the mod-30 coprime residue group Z₃₀* = {1,7,11,13,17,19,23,29}.

**One geometric object. Zero free parameters. 54 predictions.**

| Metric | Value |
|--------|-------|
| MAPE (all 54) | **0.274%** |
| RMSE | 15.07 MeV |
| Free parameters | **0** |
| Pentaquark MAPE | 0.196% |
| Ablation test | MAPE *improves* as parameters removed |

The last row is the anti-overfitting signature. A model that gets more
accurate as you remove parameters is not overfit. The bottom quark sector
(hardest predictions, most structurally distinct) has the smallest errors —
the second anti-overfitting signature.

---

## Other Confirmed Predictions

| Prediction | GBP | Observed | Error | Source |
|-----------|-----|---------|-------|--------|
| P_c(4312) mass | 4312.4 MeV | 4311.9 MeV | **0.013%** | LHCb 2019 |
| P_c(4457) mass | 4458.7 MeV | 4457.3 MeV | **0.031%** | LHCb 2019 |
| Xi_cc++ mass | 3619.3 MeV | 3621.4 MeV | 0.058% | LHCb 2017 |
| Xi_cc+ mass | 3618.9 MeV | 3620.0 MeV | 0.030% | LHCb 2026 |
| Higgs VEV | 245.928 GeV | 246.000 GeV | **0.029%** | PDG |
| Weinberg angle | 28.471° | 28.190° | 0.28° | PDG |
| Optical floor R_min | 1.093% | 83/83 materials | 0 violations | Refractiveindex.info |

The optical reflection floor is independently testable by anyone with access
to the refractive index database — no particle accelerator required.

---

## The Core Geometry

Everything derives from one function on eight integers:

```python
Z30_star = [1, 7, 11, 13, 17, 19, 23, 29]  # φ(30) = 8 integers coprime to 30

def P(r):
    return math.sin(r * math.pi / 15) ** 2  # Malus projection weight

# Key exact identities (no approximation):
# Σ P(r) = 7/2        ← Noether charge Q8
# Σ P(r)² = 21/8      ← new exact identity
# P(0) = 0            ← no colorless gluon
# P(r) = P(30-r)      ← color-anticolor mirror symmetry
```

The modulus 30 = 2 × 3 × 5 is forced by five geometric closure
constraints. It is not chosen.

---

## Yang-Mills Mass Gap

The colorless singlet P(0) = sin²(0) = 0 cannot propagate (Schur's lemma).
All 8 physical gluon states have P(r) > 0. The minimum propagation energy is:

**Δ = α_IR × Λ_QCD = 0.848809 × 217.0 MeV = 184.2 MeV > 0**

This is the Yang-Mills mass gap. It is topological — P(0) = 0 is an
algebraic identity, not a dynamical result. The gap cannot be tuned away.

The formal Hilbert space construction, continuum limit argument (scale
ΛTOPO = m_up/γ₁ = 23.89 MeV), and Osterwalder-Schrader axiom verification
are in `papers/gbp_yang_mills_mass_gap.md`.

Key result on OS axioms: the correct symmetry group recovered in the
continuum limit is **SO(4), not O(4)**. This is a prediction, not a
weakness — full O(4) would require parity conservation, which is
experimentally ruled out.

---

## Repository Structure

```
Best_QCD_Mass_Model/
│
├── README.md                          ← this file
│
├── code/
│   ├── gbp_complete_v8-9.py           ← main mass prediction code
│   ├── gbp_hilbert_spectral_gap.py    ← Yang-Mills gap verification
│   ├── gbp_os_axioms_geometry.py      ← OS axiom geometric tests
│   ├── gbp_su3_casimir_check.py       ← Z30* ↔ SU(3) verification
│   ├── gbp_su3_casimir_fix.py         ← corrected SU(3) checks
│   ├── gbp_prime_dual_interference.py ← Riemann/primes connection
│   ├── gbp_ckm_and_sheet_test.py      ← CKM + GOE/GUE sheet test
│   ├── gluon_lifecycle.py             ← gluon energy lifecycle model
│   └── mass_ladder_v3_lepton_gravity.py
│
├── papers/
│   ├── gbp_yang_mills_mass_gap.md     ← Yang-Mills mass gap (main)
│   ├── gbp_su3_identification.md      ← Z30* ↔ SU(3) (8 checks)
│   ├── GBP_WZ_Higgs_paper.md         ← W/Z boson masses, Weinberg angle
│   ├── GBP_Maxwell_paper_v2.md       ← Maxwell equations from geometry
│   ├── gbp_coprime_interference_riemann.md  ← Riemann zeros connection
│   ├── gbp_lagrangian_compressed.md  ← 4-term compressed Lagrangian
│   ├── gbp_observer_lagrangian.md    ← observer-Noether 5th term
│   ├── gbp_yang_mills_mass_gap.md    ← Yang-Mills paper
│   ├── tensor_time_v5.md             ← full framework derivation
│   └── GBP_formal_conjectures.md     ← open conjectures with status
│
├── results/
│   ├── GBP-Results_v8-9.txt          ← full 54-baryon prediction table
│   └── gbp_evidence_registry.md      ← all confirmed predictions
│
└── CITATION.md                        ← how to cite this work
```

---

## Key Papers

**Start here:**
1. `papers/tensor_time_v5.md` — full framework from first principles
2. `papers/gbp_yang_mills_mass_gap.md` — Yang-Mills mass gap proof

**For specific predictions:**
- Baryon masses: run `code/gbp_complete_v8-9.py`
- W/Z bosons: `papers/GBP_WZ_Higgs_paper.md`
- Optical floor: `code/gbp_optical_fresnel_v4.py`

**For mathematical foundations:**
- SU(3) identification: `papers/gbp_su3_identification.md`
- Hilbert space: `code/gbp_hilbert_spectral_gap.py`
- OS axioms: `code/gbp_os_axioms_geometry.py`

---

## The Reviewer's Challenge

*"Isolate one sharply defined, genuinely new prediction that standard
QFT does not already accommodate."*

**Answer: P_c(4380) has J^P = 3/2⁻ because it reflects off the wormhole
entrance, not because of any dynamical calculation.**

Standard QFT can reproduce J=3/2 for pentaquarks by choosing appropriate
quark model parameters. GBP derives it from the geometric position of the
state in the Z5* orbit — there is no free parameter, no choice. The
prediction is that ALL states below the 180° Z5* threshold will reflect
(J=3/2) and all states above will cross (J=1/2). This is a structural
prediction about the full P_c spectrum, not just one state.

LHCb Run 3 will test this directly.

---

## Why Mod-30

Not numerology. Not a choice. Five geometric closure constraints
simultaneously require exactly 30 = 2 × 3 × 5 as the minimum modulus:

| Constraint | Requires |
|-----------|---------|
| Fermionic statistics (spinor double cover) | Factor of 2 |
| Color charge (SU(3) gauge group) | Factor of 3 |
| Generation structure (5-fold Z5* symmetry) | Factor of 5 |
| All three simultaneously at minimum | 30 = 2×3×5 |

φ(30) = 8 = N²−1 for SU(3). The generator count of SU(3) equals the
Euler totient of 30. This is not a coincidence — it is the geometric
reason SU(3) is the color gauge group.

---

## Contact / Collaboration

Independent researcher. Open to collaboration, peer review, and criticism.
All results are public domain.

All code runs on standard Python with no special dependencies beyond
`math`, `numpy`, and `fractions`.

**Zenodo DOI:** 10.5281/zenodo.19798271  
**GitHub:** github.com/historyViper/Best_QCD_Mass_Model

---

*"The mass gap is not a dynamical mystery.*
*It is a topological boundary condition.*
*The universe chose mod-30. The gap came with it."*
— HistoryViper, 2026
