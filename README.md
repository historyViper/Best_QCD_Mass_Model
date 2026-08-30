# Best QCD Mass Model — GBP Framework (Phase 4Q Directed LIM)

**Jason Richardson (HistoryViper) — Independent Researcher**  
**Current checkpoint: Phase 4Q Directed LIM — August 30, 2026**

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19798271.svg)](https://doi.org/10.5281/zenodo.19798271)

> **Status note:** Geometric Baryon Physics (GBP) is an independent speculative framework under active development. The numerical mass benchmarks below are real outputs of the current code, but the proposed geometric interpretation is not established QCD. Claims such as toroidal transport, internal "wormhole" geometry, or a geometric Yang–Mills gap are GBP hypotheses unless explicitly identified as standard physics.

---

## Current Result

The current mass checkpoint is **Phase 4Q Directed LIM**.

It evaluates **55 known baryon / pentaquark states** with one common geometric mass engine built around the mod-30 coprime lanes

`Z30* = {1, 7, 11, 13, 17, 19, 23, 29}`.

| Metric | Phase 4Q |
|---|---:|
| States | **55** |
| MAPE | **0.119790284%** |
| RMSE | **5.727586506 MeV** |
| MAE | **3.704227571 MeV** |
| Maximum absolute residual | **20.204315413 MeV** |
| New fitted coefficients added by Phase 4Q | **0** |
| Geometry override table | **empty** |
| Hyperfine whitelist | **empty** |

The previous clean checkpoint, Phase 4P, gave:

| Metric | Phase 4P | Phase 4Q | Relative improvement |
|---|---:|---:|---:|
| MAPE | 0.131064757% | **0.119790284%** | **8.60%** |
| RMSE | 7.354613953 MeV | **5.727586506 MeV** | **22.12%** |
| MAE | 4.323830707 MeV | **3.704227571 MeV** | **14.33%** |
| Max error | 34.181189425 MeV | **20.204315413 MeV** | **40.89%** |

Phase 4Q changed only the states selected by the already-existing **mixed-UD heavy boundary** rule. No baryon-name correction and no newly fitted scale were introduced.

---

## The New Result: Directed LIM

The May 2026 README treated the quantity

`Q8 = 7/2`

as a separately declared exact constant.

That is no longer necessary.

For each mod-30 lane,

`P(r) = sin²(rπ/15)`.

The eight coprime lanes satisfy

`Σ P(r) = 7/2`.

The new directed Lane Interaction Matrix keeps the phase information that scalar Malus projection discards:

`C_rs = √(P_r P_s) exp[i(φ_r − φ_s)]`

with

`φ_r = 2πr/30`.

The old real LIM is simply

`Re(C_rs)`.

For the eight coprime lanes:

| Quantity | Exact / numerical result |
|---|---:|
| `ΣP` | **7/2 = 3.5** |
| Directed complex LIM rank | **1** |
| Non-zero directed LIM eigenvalue | **7/2** |
| Real LIM non-zero eigenvalues | **21/8, 7/8** |
| `21/8 + 7/8` | **7/2** |

Therefore the current code treats

`Q8 ≡ ΣP ≡ λ_LIM = 7/2`

as a **derived LIM quantity**, not as an independently declared model constant.

### Phase 4Q boundary scalarization

For a three-quark state, the tested Phase 4Q rule is

`g_LIM = |mean_{i<j}(C_ij)|`.

It is currently applied only where the pre-existing model already identifies the state as a mixed-UD heavy Malus boundary.

That changes two known-state predictions:

| State | Phase 4P residual | Phase 4Q residual |
|---|---:|---:|
| `Sigma_c+` | +2.353 MeV | **+0.916 MeV** |
| `Sigma_b0` | +34.181 MeV | **−1.540 MeV** |

The important structural point is that the model now performs the **coherent directed combination first** and scalarizes afterward.

That is different from squaring away direction at the beginning.

---

## Current Sector Performance

| Sector | States | MAPE | RMSE |
|---|---:|---:|---:|
| Light / strange | 18 | 0.144211% | 2.218 MeV |
| Charm | 19 | **0.086153%** | 2.783 MeV |
| Bottom | 13 | 0.131613% | 9.961 MeV |
| Exotics | 5 | 0.128960% | 7.467 MeV |

The bottom sector remains the largest contributor to the all-state RMSE and is a major target for the unfinished tangent / decay-transport work.

---

## Version History

| Version / checkpoint | MAPE | Main change |
|---|---:|---|
| v8.8 | 0.547% | Early charm / Malus corrections |
| v9.9 | 0.2427% | Hyperfine whitelist removed |
| v10.6 | ~0.1950% | Geometry cleanup + PDG refresh |
| Phase 4N | ~0.13593% | Xi transport / hinge-era clean checkpoint |
| Phase 4P | **0.131064757%** | Linear-energy scalar-phi interpolation; zero geo overrides |
| **Phase 4Q** | **0.119790284%** | **Directed LIM replaces scalar mixed-UD heavy boundary** |

The naming changed after v10.x because later work was developed as frozen experimental phases rather than continuously mutating one version number.

---

## Model Hygiene and Fitting Status

The old README used the phrase **"zero free parameters."** That is too broad for the current project and has been replaced with more precise language.

The current status is:

- Phase 4Q adds **zero new fitted continuous coefficients**.
- `Q8 = 3.5` is no longer independently declared; it is derived from the LIM.
- `GEO_FACTOR_OVERRIDE` is empty in the clean mass checkpoint.
- The old hyperfine whitelist is empty.
- No observed mass is used to choose a particle-specific phi position.
- The model still contains inherited physical / phenomenological inputs such as constituent masses, `Lambda_QCD`, and `alpha_IR`.
- Structural rules have been developed while examining known baryon residuals, so the 55-state result must **not** be described as a fully blind out-of-sample prediction set.
- The tangent sector is not yet globally incorporated and no universal tangent strength has yet been fitted.

This distinction matters: **few fitted numerical coefficients** is not the same claim as **no data-informed model development**.

---

## Core Mod-30 Geometry

The basic projection law remains

```python
import math

Z30_star = [1, 7, 11, 13, 17, 19, 23, 29]

def P(r):
    return math.sin(r * math.pi / 15.0) ** 2
```

Current lane assignments are

| Quark | Lane |
|---|---:|
| up | 19 |
| down | 11 |
| strange | 7 |
| charm | 23 |
| bottom | 13 |
| top | 17 |

The physical top-view lane angle is

`theta_q = 12° × r`

and the full spinor-cover phase used in the geometric construction is

`Theta_r = 24° × r`.

Mirror pairs are

`(1,29), (7,23), (11,19), (13,17)`.

Scalar Malus projection gives identical magnitudes to mirror partners. The directed LIM keeps the relative phase / orientation that survives before squaring.

---

## Toroid Cover vs. Path Shape

A major terminology cleanup since the old README is that **cover class and path shape are not the same thing**.

`T_n` now means only the closure / cover class.

A separate `path_shape` should describe the actual route, for example:

`HE21`, `wingnut`, `figure-8`, `Y-junction`, etc.

A `T2` state is therefore **not automatically a figure-8**.

This prevents old shorthand from being mistaken for a derived geometric statement.

---

## 720° Frame Transport

The intended GBP spinor construction is

`360° orbital closure + 360° accumulated frame transport = 720° total frame return`.

This is meant to model the familiar spin-1/2 `4π` return structure.

It should not be confused with a textbook Möbius strip having a single 180° half-twist.

For formal writing, the preferred language is a **framed toroidal loop / full-twist toroidal annulus with accumulated frame holonomy**.

Recovering the standard SU(2) spinor transformation quantitatively remains a required consistency test.

---

## Mass-Scale Chain

The current Phase 4P / 4Q mass engine uses the following scale chain:

`GEO_B = sin²(π/15)`

`LU = GEO_B / alpha_IR`

`C_Malus_IR = -ln(1 - GEO_B × alpha_IR)`

`Lambda_GBP = Lambda_QCD × exp(C_Malus_IR)`

with the current inputs

`alpha_IR = 0.848809`

`Lambda_QCD = 217.0 MeV`.

Using the LIM-derived

`Q8 = 7/2`

the electroweak-scale relation currently gives

`V_EW = 245.928476 GeV`.

The proximity to the Standard Model Higgs VEV is a GBP model result; it is not by itself evidence that the proposed geometric mechanism is the Standard Model origin of electroweak symmetry breaking.

---

## Selected Current Mass Results

These values come from the Phase 4Q snapshot, not the old v9.9 table.

| State | GBP Phase 4Q | Reference used by snapshot | Absolute % error |
|---|---:|---:|---:|
| `Lambda_c+` | 2285.551 MeV | 2286.460 MeV | **0.0398%** |
| `Xi_cc++` | 3619.269 MeV | 3621.400 MeV | **0.0588%** |
| `Xi_cc+` | 3616.830 MeV | 3619.970 MeV | 0.0867% |
| `P_c(4312)` | 4309.015 MeV | 4311.900 MeV | 0.0669% |
| `P_c(4380)` | 4385.951 MeV | 4380.000 MeV | 0.1359% |
| `P_c(4440)` | 4455.263 MeV | 4440.300 MeV | 0.3370% |
| `P_c(4457)` | 4455.263 MeV | 4457.300 MeV | **0.0457%** |
| `P_cs(4459)` | 4456.154 MeV | 4458.800 MeV | **0.0593%** |

The current snapshot also preserves **12 legacy unobserved / comparison predictions** so later measurements can be compared against a frozen numerical record.

---

## A Recent Three-Body Quark-Model Benchmark

A useful recent comparison is:

**J. Baek et al., "Three-body forces in the quark model," arXiv:2608.18949 (2026).**

Their calculation is a conventional few-body treatment using a meson-calibrated two-body Hamiltonian, Gaussian Expansion Method / generalized eigenvalue machinery, and three fitted three-body couplings `A`, `B`, and `C`.

Their final mass-scaled Yukawa three-body model reports

`RMSE = 3.13 MeV`

on its nine-state baryon calibration set.

Using corresponding isospin / charge representatives, Phase 4Q gives approximately

`RMSE ≈ 2.58 MeV`

on the analogous nine-state comparison.

This is an interesting numerical benchmark, but it is **not a blind-prediction victory**: the Baek et al. paper performs genuine fixed-parameter omitted-state tests, while GBP's structural development has repeatedly inspected known baryon residuals.

The comparison is therefore best read as:

**current same-spectrum descriptive accuracy**, not a universal ranking of QCD models.

---

## The Tangent Sector — Next Major Checkpoint

Phase 4Q is deliberately frozen **before** the global tangent update.

The remaining program is to determine the tangent contribution from geometry rather than particle-by-particle residuals.

The intended workflow is:

1. enumerate every geometrically allowed tangent / escape contact;
2. preserve direction and odd-quark side ordering;
3. derive the tangent sign and angle from the path;
4. if a scale must be calibrated, use one universal tangent strength rather than baryon-specific values;
5. preferably calibrate against decay widths and then test the corresponding mass shifts;
6. freeze the rule and rerun all 55 states without individual corrections.

In standard resonance language, a common self-energy has

`Re Sigma -> mass shift`

and

`-2 Im Sigma -> width`.

If GBP's tangent geometry is genuinely describing an open decay channel, one geometric rule should eventually constrain both sides.

**No global tangent improvement is included in the 0.119790% MAPE quoted above.**

---

## Pentaquark Spin / "Wormhole" Claim — Historical Status

The May 2026 README advertised a particularly strong claim that `P_c(4380)` must have

`J^P = 3/2-`

because of a reflection at a proposed internal wormhole boundary.

That statement is **not carried forward as a Phase 4Q mass-model result**.

The current Phase 4Q snapshot does not encode that historical spin/parity assignment; its pentaquark mass records are currently mass-branch entries with parity unset. The old rarity estimate and detailed reflection narrative therefore require a separate re-audit before being advertised as current predictions.

In current GBP terminology, "wormhole" should be read as an **internal state-space / gauge-geometry connection**, not an experimentally established spacetime wormhole.

---

## Yang–Mills Gap Claim — Current Wording

The mod-30 construction contains the exact algebraic identity

`P(0) = 0`

while all eight coprime physical lanes have positive Malus weight.

The framework has explored the energy scale

`Delta = alpha_IR × Lambda_QCD ≈ 184.2 MeV`

as a possible geometric mass-gap mechanism.

This remains a **GBP conjectural mechanism**.

It is not a mathematical proof of the Yang–Mills existence and mass-gap problem, and the identity `P(0)=0` alone does not establish the full non-perturbative Yang–Mills theorem required by the Clay problem.

---

## Current Runnable Checkpoint

The current development artifacts are:

```text
gbp_app_phase4Q_directed_LIM.html
GBP_Mass_Snapshot_Phase4Q_Directed_LIM_2026-08-30.json
gbp_phase4Q_directed_LIM_boundary_test.py
gbp_phase4P_NO_GEO_OVERRIDES_STANDALONE_android_2026_08_27.py
```

Current Phase 4Q source SHA-256:

`009acbfd25b99846c6d3e144d5dfa010711493faac0dcce0706a928eb4a3cc42`

When publishing a result, include the checkpoint name and hash so later geometry changes cannot silently rewrite an earlier benchmark.

---

## App

The all-in-one GBP app now contains the **Phase 4Q Directed LIM** mass workspace.

It includes:

- individual state calculator;
- all 55 known-state predictions;
- mass decomposition;
- sector accuracy;
- predictions / unobserved-state snapshot;
- splittings;
- method / audit notes;
- the LIM-derived `Q8 = 7/2`;
- the frozen pre-tangent checkpoint.

Current app file:

`gbp_app_phase4Q_directed_LIM.html`

---

## Repository Guidance

The old README listed many historical files as if they were all part of the active mass engine. Going forward, the repository should distinguish three categories clearly:

| Category | Meaning |
|---|---|
| `current/` or release root | Files needed to reproduce the current Phase 4Q result |
| `papers/` | Derivations, conjectures, and framework papers |
| `legacy/` | v8.x, v9.x, v10.x and superseded experimental branches |

Do not delete the old checkpoints. They are useful for documenting how numerical corrections were removed, replaced, or falsified.

---

## Reproducibility Standard

A mass-model result should be considered reproducible only when it includes:

`checkpoint + source hash + state list + reference masses + predicted masses + residual metrics`.

For Phase 4Q those are frozen in

`GBP_Mass_Snapshot_Phase4Q_Directed_LIM_2026-08-30.json`.

This makes future tangent, decay, or path-shape changes directly auditable against the current pre-tangent baseline.

---

## What Would Falsify the Current Direction?

The strongest tests are not "does another correction improve MAPE?"

They are structural transfer tests.

A proposed LIM / tangent / transport rule should fail if it requires a different sign, scale, or exception for each baryon once the geometry has been fixed.

The directed LIM becomes much more compelling if the exact same matrix rule continues to improve new structural classes without residual-based selectors.

The tangent hypothesis becomes much more compelling if one frozen geometry and one universal scale simultaneously improves decay widths and mass shifts.

Failure of those transfer tests should be treated as evidence against the proposed geometric interpretation, not patched away.

---

## Contact / Collaboration

Independent researcher. Open to collaboration, peer review, replication, and criticism.

**Zenodo DOI:** 10.5281/zenodo.19798271  
**GitHub:** https://github.com/historyViper/Best_QCD_Mass_Model

---

*"The donut is allowed to be weird. The numbers still have to survive the audit."*

— GBP development note, 2026
