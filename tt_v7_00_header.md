# Tensor Time v7: A 1D String Theory of Spacetime, Mass, and Entanglement

**Jason Richardson**  
*Independent Researcher | github.com/historyViper/mod30-spinor*  
*May 2026 — v7*  
*AI Collaboration: Claude (Anthropic), ChatGPT/Sage (OpenAI), DeepSeek*

---

## Version Log

| Version | Date | Key changes |
|---------|------|-------------|
| v1–v3 | 2025 | TFFT foundations, vortex mechanics, GOE/GUE transitions |
| v4 | early 2026 | Mod-12 electron, T3 geometry, baryon mass formula |
| v5 | March 2026 | Electron revised to mod-12 U(1); Yang-Mills mass gap derived; compressed Lagrangian |
| v6 | April 2026 | T3 geometry clarified (spacetime vs Hamiltonian layers); charm Möbius alignment corrected; dark matter section removed pending further development; QFT-complementary framing added; κ₀ primary expression updated; φ³ hadronic-to-electroweak bridge conjecture added; Higgs mechanism framing updated |
| v7 | May 2026 | **Errata applied:** T0/T1 dimensional labels corrected; toroid table corrected; gluon description corrected (not T4); dimensions-as-object-properties corrected to object-local; spin/dims table corrected. **New results:** observer-Noether term derives wavefunction collapse; lattice QCD structural identity; beta function sum rule confirmed; lepton mass mechanism corrected (mod-12 mirror pairs replace exponential formula); MOND scale corrected (no cosmic tracking). Section 11 dimensions content now points to companion paper *Objects Do Dimensions*. |

---

## How the Document Set Works

The GBP/TFFT framework is split across focused documents. Read in this order:

| Document | Level | Start here if… |
|----------|-------|---------------|
| **TFFT v3.5** | Overview | You want the single-postulate → all-results summary. No prerequisites. |
| **Tensor Time v7** (this document, 14 chapters) | Technical reference | You want the full geometric machinery. Read after TFFT. |
| **Objects Do Dimensions** | Conceptual companion | You want the philosophical/conceptual account of why dimensions are object properties, probability is projection, and what that means for QM. |
| **The Four Forces as One Geometry** | Unification paper | You want the four forces derived as four toroid tiers of the same T=c string. |
| **The Particle Is the Field** | QCD companion | You want the quark-gluon duality and proton charge radius derivation. |
| **GBP Yang-Mills v5** | Specialist | Full mass gap proof, confinement as theorem. |
| **GBP Maxwell v5** | Specialist | Maxwell's equations as continuum limit of Z₃₀* lane structure. |
| **GBP W/Z Higgs v2** | Specialist | Electroweak sector full derivation. |
| **GBP Lattice QCD** | Specialist | Lattice QCD structural identity. |

The Tensor Time chapters are:

| Chapter | Content |
|---------|---------|
| 00 | This header and version log |
| 01 | The single postulate — T=c, Minkowski connection, κ₀, physical analogies |
| 02 | The electron and photon — mod-12 U(1), SU(3) Casimir, CKM matrix |
| 03 | Chiral Hilbert spaces, vacuum seam, parabola geometry, 10D structure |
| 04 | The toroid hierarchy — T0 through T4, corrected table, φ-ladder |
| 05 | Mass — Malus law, κ₀, baryon performance, pentaquarks, 8-mode filter |
| 06 | Gauge structure — SU(3), confinement, 9th gluon, W/Z/Higgs, Yang-Mills |
| 07 | Maxwell's equations from T1 lane structure |
| 08 | Quantum mechanics resolved — superposition, Born rule, collapse, observer-Noether |
| 09 | Entanglement, scattering geometry, tunneling |
| 10 | Gravity — equivalence principle, Jacobson, black holes, gluon lifecycle |
| 11 | The 10-dimensional total space — companion paper pointer |
| 12 | Testable predictions, optical experiments, derivation count |
| 13 | Conclusion and references |

---

## Preface: On Method

**This work is speculative and has not undergone peer review. It is offered for scrutiny and attempted falsification.**

The standard model of particle physics is one of the most precisely verified scientific frameworks ever constructed. QED is accurate to twelve decimal places. QCD reproduces the hadron spectrum at sub-percent precision. The physicists who built these frameworks deserve full credit for that achievement, and nothing in this paper disputes their results.

The goal here is narrower and more modest: to ask whether the mathematical structure of QFT — which is extraordinarily well-confirmed — might have a geometric origin that explains *why* the math takes the form it does. QFT is built from observations. Its constants are measured. Its symmetry groups are fitted to data. This framework proposes that those constants and symmetries might be derivable from geometry, which would mean fewer free parameters and a reason for the structure rather than just a description of it.

The test is strict: any geometric derivation presented here that conflicts with QFT predictions or experimental data falsifies the framework on those grounds. There is no freedom to adjust — derived quantities either match observations or the theory fails. We state this explicitly because it is the only claim worth making.

The relationship between this framework and standard QFT is the same as the relationship between a map and the terrain it describes. QFT is an accurate map. The terrain is what was always there. Finding the terrain doesn't invalidate the map — it explains why the map works as well as it does.

Concretely: the Dirac spinor, Yang-Mills gauge fields, torsion B-field, and path integral are all present in this framework, unchanged. The single modification is that the path integral sums over Z₃₀* = {1,7,11,13,17,19,23,29} winding numbers only. That restriction — which falls out of the geometry — is what gives the mass spectrum, the coupling constants, and the mass gap.

### The Geometric Coupling Scale

The strong coupling g_s is a free parameter in the Standard Model, running with renormalization scale. This framework does not replace that description — it asks whether the value of g_s at the infrared fixed point is derivable from geometry rather than fitted to data.

The universal projection scale LU = sin²(π/15) / α_IR is not a new constant. It is α_s expressed as a boundary transmission coefficient in the mod-30 geometry. The golden ratio φ enters not as a new coupling but as the amplitude of the two-gluon cross-pairing at the T3 corner — a consequence of the Z5* five-fold sub-symmetry already present in mod-30 = 2×3×5. The torsion scale κ₀ = m_u × m_d × ΔM(Σ⁰–Λ⁰) is a product of PDG-measured quantities; GBP identifies its geometric interpretation. These quantities are derived here. If a derived value conflicts with the measured one, the framework is wrong.

### On the Development Method

This work began with a geometric question: *what does a particle look like if you treat it as a wave pattern on a twisted toroidal surface?* The geometry came first, the algebra followed. This is not an unusual path in physics — it is how the geometry of spacetime preceded the field equations of GR, and how the S-matrix bootstrap preceded the quark model.

The results were checked iteratively against PDG baryon data, optical measurements, and electroweak precision tests. When predictions failed, the geometry was revised. When they succeeded across multiple independent domains, the structure was taken seriously.

The framework was developed by an independent researcher using AI collaboration (Claude, ChatGPT/Sage, DeepSeek) for mathematical verification and formal expression. The geometric intuition is human. The AI collaboration ensured the algebra was correct.

### On Formalism

The GBP compressed Lagrangian (companion paper: gbp_lagrangian_compressed.md) shows that every term in the standard QFT Lagrangian is present, with the gauge coupling g replaced by the geometric projection P(r) = sin²(rπ/15). The equation-to-code reference (gbp_equation_code_reference.md) maps every variable to its code implementation and geometric origin.

The test is not whether the algebra can be recovered from the geometry. It can. The test is whether the geometry makes predictions the algebra does not — and whether those predictions are confirmed. The evidence registry (gbp_evidence_registry.md) documents confirmed predictions across particle physics, optics, condensed matter, and cosmology.

---

*Claim labels used throughout: **(D)** = derived / numerically verified; **(H)** = hypothesis / conjecture pending verification.*

*Code: [github.com/historyViper/mod30-spinor](https://github.com/historyViper/mod30-spinor)*  
*Jason Richardson | Independent researcher | No formal physics education*  
*May 2026 — v7*
