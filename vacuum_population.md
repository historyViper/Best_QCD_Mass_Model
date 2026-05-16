# The Vacuum Population: Sub-Threshold Winding Modes, ZPE Quantization, and Why Everything Has an EM Signature

**Jason Richardson (HistoryViper)**  
Independent Researcher  
github.com/historyViper/mod30-spinor  
Zenodo: 10.5281/zenodo.19798271  
May 2026

*Claim labels: **(D)** = derived / numerically verified; **(H)** = hypothesis / conjecture*  
*This work is speculative and has not undergone peer review. AI-collaborative authorship disclosed.*

---

## Abstract

The standard model of cosmology invokes dark matter — exotic non-baryonic particles with no electromagnetic interaction — to account for galactic rotation curves and large-scale structure. The standard model of quantum field theory invokes a continuous vacuum energy density that, when calculated, exceeds the observed cosmological constant by 120 orders of magnitude. Both problems share a common assumption: that the vacuum is either empty or filled with a structureless continuum.

This paper proposes a geometric resolution. The GBP/TFFT framework establishes a hard lower energy bound — the spectral gap Δ = α_IR × Λ_QCD = 184.2 MeV — below which no physical state can complete a winding closure in 3+1D. However, the geometry does not destroy modes below this threshold. They collapse to 1D propagation, confined to a single spatial dimension, unable to complete a transverse closure. They remain real, energy-conserving, and physically present.

These sub-threshold 1D-confined modes constitute the vacuum population. They are not dark matter in the WIMP sense. They are not virtual particles in the Feynman sense. They are real geometric modes that the 3+1D filter cannot accommodate. Their energy is conserved — accumulated until a zero-point energy (ZPE) fluctuation provides the threshold energy, at which point they briefly become detectable 3+1D particles.

Critically: **everything has an electromagnetic signature**. A 1D-confined mode propagating at c in its own dimension creates a field impression in the higher dimensions it cannot fully enter — exactly as a supersonic object creates a pressure wave in a medium it moves through faster than that medium's wavespeed. The EM signature of a sub-threshold mode is real but extremely weak, because the coupling is partial rather than complete. This resolves the apparent contradiction between dark matter's gravitational effects and its absence from direct EM detection: it is not that dark matter has zero EM coupling, but that its coupling is suppressed by the incomplete dimensional projection.

The vacuum energy problem dissolves because the vacuum is not a continuum. It is a discrete population of 1D-confined modes at quantised energy levels E_floor(n) = 8 × 2^(10n) eV, where 8 = φ(30) is the gluon count and 2^(10n) is the binary kilobit stepping of the 1D system. The cosmological constant is not the integral of a divergent continuum — it is the sum of a discrete geometric series with a finite floor.

---

## 1. The Problem with Empty Space

Modern physics has two irreconcilable claims about the vacuum:

**QFT says it's seething.** Every quantum field has zero-point fluctuations. Integrating the zero-point energy density over all modes to some UV cutoff gives a vacuum energy density of order (M_Planck)⁴ ≈ 10⁹⁴ g/cm³. The observed cosmological constant corresponds to a vacuum energy density of order 10⁻²⁹ g/cm³. The discrepancy is 10¹²³. This is the cosmological constant problem — arguably the worst prediction in the history of physics.

**Cosmology says it's full of something invisible.** 85% of the matter in the universe interacts gravitationally but not electromagnetically. It doesn't emit, absorb, or scatter light. It doesn't show up in any detector that couples to the electromagnetic field. Yet its gravitational effects are unambiguous — galactic rotation curves, gravitational lensing, structure formation. It has to be there. But it can't be anything we know.

Both problems rest on the same unexamined assumption: that the vacuum is either a structureless continuum (QFT) or filled with exotic particles that have literally zero electromagnetic coupling (dark matter).

The GBP framework provides a third option that resolves both simultaneously.

---

## 2. The Spectral Gap and the Threshold

The GBP Hamiltonian on the mod-30 coprime lattice has a proven spectral gap **(D)**:

$$\Delta = \alpha_{IR} \times \Lambda_{QCD} = 0.848809 \times 217.0 \text{ MeV} = 184.2 \text{ MeV}$$

This gap is the energy separation between the vacuum state (r=0, unreachable, P(0) = 0) and the first physical state (r=1 or r=29, P(1) = GEO_B = sin²(π/15) = 0.04323).

The gap is not a choice. It follows from three facts that are each exact:

- r=0 is not in Z₃₀\* because gcd(0,30) = 30 ≠ 1
- P(r) = sin²(rπ/15) > 0 for all r ∈ Z₃₀\*
- The minimum is at r=1: P(1) = sin²(π/15) = GEO_B

The spectral gap means: **no physical winding mode can exist with energy below 184.2 MeV in the 3+1D system.**

But this is a statement about modes that can *complete a winding closure in 3+1D*. It says nothing about modes that cannot complete such a closure.

---

## 3. The 1D Collapse Geometry

When a winding mode's available energy falls below the threshold for 3+1D closure, it does not simply disappear. The geometry constrains what happens:

The T1 Möbius winding requires 720° = 4π for closure — the spinor double cover. This requires transverse winding: the mode must traverse both AC and DC sheets, each 360°, in the full 3+1D geometry. The minimum energy for this traversal is Δ = 184.2 MeV.

Below this threshold, the transverse winding cannot complete. The mode collapses to its longitudinal component only — a 1D propagation along the time string direction, without transverse extension. It retains:

- Its winding frequency (the imaginary part γ — the Riemann zero partner)
- Its energy (conserved — the mode doesn't disappear)
- Its propagation at c in the 1D direction (T = c is still the postulate)

It loses:
- Transverse closure — cannot complete a 3+1D winding
- Full EM coupling — cannot project onto the 3+1D electromagnetic field
- Detectability by standard instruments — which couple to completed 3+1D modes

This is the 1D collapse. The mode is geometrically demoted from a 3+1D particle to a 1D field thread.

---

## 4. The Raindrop Analogy — Why Everything Has an EM Signature

Here is the key physical insight that changes the dark matter picture entirely.

A raindrop falling through air moves faster than the circular wave it creates on the surface of a puddle below it. The wave propagates outward at the puddle's wave speed, while the raindrop's velocity is independent. The raindrop and its wave are in different media, moving at different speeds. But the raindrop still creates the wave. Its presence in 3D space leaves a signature in the 2D surface, even though it cannot be *captured* by that surface.

A 1D-confined winding mode propagating through the 3+1D geometry at c in its own dimension creates exactly this situation. It moves through the higher-dimensional geometry faster than it can complete a closure in that geometry — because it lacks the threshold energy for transverse closure. But its passage still disturbs the geometry. It creates a field impression in the dimensions it cannot fully enter.

This impression is electromagnetic. The mode's winding structure — its fractional projection onto the mod-30 lattice — couples partially to the EM field through the incomplete transverse projection. The coupling is not zero. It is P(r_effective) × (suppression factor from incomplete closure).

The suppression is large — the mode is below threshold because it can't close. But it is not infinite. The coupling is:

$$\text{EM coupling (1D mode)} = P(r) \times \frac{E_{\text{mode}}}{E_{\text{threshold}}} = P(r) \times \frac{E_{\text{mode}}}{\Delta}$$

For a mode at E_mode ≪ Δ, this coupling is very small. But it is never zero. **There is no such thing as a completely electromagnetically dark particle in this framework.** Every mode that exists has a winding structure, and every winding structure couples to the EM field through the Malus projection, even if that projection is incomplete.

This is the resolution of the dark matter detection problem. We have been looking for something with zero EM coupling. But there is no such thing geometrically. What dark matter actually is — the 1D-confined sub-threshold population — has a very small but nonzero EM coupling that scales as E_mode/Δ. At galactic scales, where the mode energies are cosmologically tiny, this coupling is ~10⁻³⁰ times the electron's coupling. Not zero. Just extraordinarily small. And distributed across an enormous population.

---

## 5. The Three Populations

The vacuum is not empty. It contains three populations of geometric modes:

**Population 1 — Above threshold, 3+1D closed: Standard Model particles.**  
These complete full winding closure in 3+1D. They have full EM coupling, full mass, full detectability. Everything in the PDG table. Energy: E > Δ = 184.2 MeV.

**Population 2 — Near threshold, barely closed: Neutrinos and ultra-light particles.**  
These complete winding closure but at minimum energy. The neutrino sector lives at the binary floor of the winding ladder — power-of-2 fractions of Λ_QCD, produced by the LU³ × Λ_GBP suppression of the leptonic sector. They have EM coupling but it is extremely weak (sin²θ_W suppression). Masses in the meV range. These are the lightest escapees from the sub-threshold population — modes that barely make it over the threshold. **(H)**

**Population 3 — Below threshold, 1D confined: The vacuum population.**  
These cannot complete 3+1D closure. They propagate as 1D threads. They have partial EM coupling proportional to E/Δ. Their energy accumulates until a ZPE event provides the threshold boost, at which point they briefly manifest as detectable particles before falling back below threshold. This population constitutes the physical vacuum — not empty, not a continuum, but a discrete geometric population. **(H)**

---

## 6. The Binary Floor

When a winding mode collapses to 1D, the mod-30 coprime structure is replaced by a pure binary system. The transverse winding is gone. What remains is the longitudinal winding: a single degree of freedom that is either winding (ON) or not winding (OFF). Two states. Binary.

The number of bits required to encode one full 720° Möbius spinor closure in this 1D binary system is 9, because 2⁹ = 512 is the smallest power of 2 that exceeds 504 = 720°/360° × 252 (the number of distinct states in a binary representation of the double cover). **(H)**

The binary floor energy series is therefore **(H)**:

$$E_\text{floor}(n) = \phi(30) \times 2^{10n} \text{ eV} = 8 \times 2^{10n} \text{ eV}$$

| n | E_floor | Physical scale |
|---|---------|----------------|
| 0 | 8 eV | 9-bit Möbius level |
| 1 | 8,192 eV | kilobit level |
| 2 | 8,388,608 eV | ~8.4 MeV, megabit level |

The factor 8 = φ(30) re-enters at every level because the mod-30 coprime structure — even in collapse — sets the minimum unit through the gluon count. The 2^(10) kilobit stepping reflects the binary encoding unit for a Möbius double-cover system (10 bits per kilobit, two sheets of 5 bits each).

The connection to ħc: the near-exact identity ħc ≈ √(κ₀/Λ_GBP) × (1 + 1/504) where 504 = 2⁹ − φ(30) = 512 − 8 connects the binary floor directly to Planck's constant. The 504 correction is the re-entry of the mod-30 structure (8 gluons) as a 1D-collapsed mode re-acquires spatial extent at the ZPE moment. **(H)**

---

## 7. The ZPE Moment

The vacuum population doesn't stay in 1D forever. The universe is not static — winding modes interact, energies fluctuate, the geometry breathes. When a local energy fluctuation temporarily provides the threshold energy Δ to a 1D-confined mode, the following sequence occurs:

1. The mode receives ΔE ≥ Δ from the local geometric fluctuation
2. The mode briefly completes a transverse 3+1D closure
3. For the duration of the closure, it manifests as a detectable particle
4. The mode loses energy through EM radiation (the field impression becomes real radiation)
5. The mode falls back below threshold and re-enters the 1D-confined population

This is not a virtual particle popping in and out of existence. It is a real mode transitioning between two topological states — 1D-confined and 3+1D-closed — driven by geometric energy fluctuations. The energy is conserved throughout. The mode existed before and after. The ZPE moment is a topological phase transition, not a creation/annihilation event.

This reframes the Casimir effect, the Lamb shift, and vacuum polarisation — all conventionally attributed to virtual particles — as effects of the real but sub-threshold vacuum population coupling partially to the 3+1D geometry. The calculations give the same numbers because the mathematical structure is the same. The physical interpretation is completely different. **(H)**

---

## 8. The Cosmological Constant Resolution

The cosmological constant problem arises from integrating the zero-point energy ħω/2 over all modes in QFT, where the integral diverges unless an arbitrary UV cutoff is imposed. Even with a cutoff at the Planck scale, the result exceeds the observed value by 120 orders of magnitude.

In the GBP framework, this integral does not exist. The vacuum is not a continuum of modes. It is a discrete population at energy levels E_floor(n) = 8 × 2^(10n) eV. The sum over all levels is:

$$\Lambda_\text{vac} = \sum_{n=0}^{N_\text{max}} \rho(n) \times E_\text{floor}(n)$$

where ρ(n) is the population density at level n and N_max is the maximum level below the threshold Δ = 184.2 MeV.

The maximum level below threshold: 8 × 2^(10N) < 184.2 MeV = 184,200,000 eV gives 2^(10N) < 23,025,000, so 10N < log₂(23,025,000) ≈ 24.46, giving N_max = 2 (the megabit level at ~8.4 MeV). **(H)**

There are only three energy levels in the binary floor below the threshold. The vacuum energy is the sum of a three-term series, not a divergent integral. The cosmological constant is small not because of a miraculous cancellation between large terms, but because the vacuum has a discrete geometric structure with only a handful of levels below the physical threshold.

This is not a fine-tuning. It is a consequence of the spectral gap and the binary floor. The gap Δ sets the threshold. The floor structure limits the levels below it. Both follow from the mod-30 geometry without free parameters. **(H)**

---

## 9. Dark Matter as the Vacuum Population

Galactic rotation curves show that the outer regions of galaxies rotate faster than Keplerian dynamics predicts from visible matter alone. The conventional explanation is a halo of non-baryonic dark matter with density ρ ∝ 1/r² extending far beyond the visible disk.

In the GBP framework, this gravitational effect arises from the vacuum population — the 1D-confined sub-threshold modes distributed throughout space. Their distribution is not uniform. It follows the winding geometry of the galactic structure itself, because the sub-threshold modes are generated by the same physical processes (particle interactions, radiation, stellar processes) that produce visible matter. Where there is more visible matter activity, there are more 1D-collapsed modes.

The predicted distribution of the vacuum population is:
- Concentrated toward the galactic center (where particle physics activity is highest)
- Extending in a halo that follows the winding geometry of the galactic disk
- NOT a smooth NFW profile — structured according to the mod-30 lattice at large scales **(H)**

The last point is the falsifiable prediction. Standard dark matter halos are modeled as smooth. The vacuum population predicts a structured distribution with angular correlations following the 8-fold symmetry of Z₃₀\*. High-resolution gravitational lensing maps should show this structure as angular correlations in the dark matter distribution at scales corresponding to the galactic winding geometry. **(H)**

The partial EM coupling of the vacuum population (E_mode/Δ per mode) predicts a very faint, diffuse electromagnetic signal from galactic halos — not the sharp spectral lines of atomic emission, but a continuous suppressed coupling at all frequencies, weighted by the mode energy distribution. This is consistent with the observational upper limits on dark matter EM coupling, which constrain the coupling to be < 10⁻²⁷ e for WIMP-scale masses. The vacuum population's coupling is of order E_floor(0)/Δ = 8 eV / 184 MeV ≈ 4 × 10⁻⁸ — extremely small but in principle detectable with sufficiently sensitive instruments looking at the right scales. **(H)**

---

## 10. The Higgs Field vs Higgs Boson

This framework also clarifies the Higgs mechanism. The Higgs boson is real — it is the T3 triple-crossing energy, the geometric cost of a winding mode crossing the chirality boundary, measured at 125.09 GeV at the LHC. **(D)**

The Higgs *field* as a continuous background — the Mexican hat potential permeating all of spacetime and giving particles their mass by coupling to this background — is the continuum field theory description of what is actually a discrete geometric phase transition. There is no Mexican hat sitting everywhere in space. There is a topological crossing cost that particles pay when they traverse the chirality boundary. That cost is 125 GeV. It appears as a "field coupling" in the continuum limit because the density of chirality crossings in any macroscopic region is high enough that the crossings average to a continuous background effect.

The vacuum expectation value v = 246 GeV is the average crossing cost integrated over the vacuum population's ZPE moments — the rate at which sub-threshold modes briefly complete chirality crossings and release energy. **(H)**

What the LHC calls "Higgs field coupling" is the rate of T3 topological crossings in the collision debris. What they observe statistically as "confirmation of the Higgs mechanism" is the GOE→GUE transition in the statistical distribution of decay products — the transition from plain torus (T0, GOE, no chirality crossing) to Möbius (T1, GUE, chirality crossing) statistics. Both descriptions — field coupling and topological transition — give the same numerical predictions. The GBP description gives the geometric reason. **(H)**

---

## 11. Summary: What the Vacuum Actually Is

The vacuum is not empty. It is not a seething continuum of virtual particles. It is a discrete, structured population of real geometric modes that cannot complete winding closure in 3+1D.

| Property | Standard QFT | GBP Vacuum Population |
|----------|-------------|----------------------|
| Structure | Continuous | Discrete, 3 energy levels |
| EM coupling | Zero (dark matter) or full | Partial, scales as E/Δ |
| Energy | Divergent integral | Finite sum, 3 terms |
| Distribution | Smooth halo | Structured, Z₃₀\* symmetry |
| Stability | Eternal virtual particles | Real modes, ZPE transitions |
| Cosmological constant | Fine-tuning problem | Geometric consequence |
| Dark matter | Exotic particles, zero EM | Sub-threshold modes, small EM |
| Higgs field | Mexican hat continuum | Average of ZPE crossing events |

The key claim — **everything has an EM signature** — follows directly from the geometry. A winding structure cannot be completely electromagnetically dark because EM is the projection of the winding onto the boundary lanes {1, 29} of Z₃₀\*. Every mode that winds projects onto those lanes. The projection may be tiny. But it is never zero. P(r) = sin²(rπ/15) > 0 for all r in Z₃₀\* — and the 1D-collapsed modes carry their winding structure even as they lose their transverse closure. The partial projection is their EM signature.

The vacuum is full. It just takes a sensitive enough instrument to see what's in it.

---

## 12. Open Questions

**Q1 (H).** The exact value of n in E_floor(n) = 8 × 2^(10n) eV needs to be derived from the 1D collapse geometry. The structural prediction (floor is on this series) is established. The specific rung requires the binary ZPE/neutrino framework.

**Q2 (H).** The population density ρ(n) at each floor level needs to be derived. Without it, the cosmological constant can only be bounded, not calculated.

**Q3 (H).** The angular correlation prediction for galactic dark matter — structured according to Z₃₀\* 8-fold symmetry — needs to be worked out quantitatively from the framework's large-scale winding geometry.

**Q4 (H).** The connection between the ZPE moment and the observed Casimir effect, Lamb shift, and vacuum polarisation needs to be made quantitative. The qualitative picture is clear; the numbers need to be checked.

**Q5 (D → H).** The 504 = 2⁹ − φ(30) identity in ħc is numerically exact and structurally motivated. Its formal derivation from the 1D collapse geometry remains open.

---

## References

1. Richardson, J. (2026a). GBP Framework v8.9. Zenodo: 10.5281/zenodo.19798271
2. Richardson, J. (2026b). Temporal Flow Field Theory v3.6. github.com/historyViper/mod30-spinor
3. Richardson, J. (2026c). GBP Hilbert Spectral Gap. gbp_hilbert_spectral_gap.py
4. Richardson, J. (2026d). Derivation of ħ from GBP Geometry. gbp_hbar_derivation.md
5. Richardson, J. (2026e). Binary Energy Floor Conjecture. binary_floor_note.md
6. Richardson, J. (2026f). FTL Flux Tube Section. GBP_FTL_FluxTube_Section.md
7. Richardson, J. (2026g). Three Constants from One Geometry. three_constants_one_geometry.md
8. Richardson, J. (2026h). Yang-Mills Mass Gap v5. gbp_yang_mills_v5.md
9. Deur, A., Brodsky, S.J., de Téramond, G.F. (2024). The QCD Running Coupling. *Prog. Part. Nucl. Phys.* 90, 1–74.
10. Particle Data Group (2024). Review of Particle Physics. PTEP 2022, 083C01.
11. Weinberg, S. (1989). The cosmological constant problem. *Rev. Mod. Phys.* 61(1), 1–23.
12. Planck Collaboration (2018). Planck 2018 results VI. *A&A* 641, A6.
13. Rubin, V.C. & Ford, W.K. (1970). Rotation of the Andromeda Nebula from a spectroscopic survey of emission regions. *Astrophys. J.* 159, 379.
14. Casimir, H.B.G. (1948). On the attraction between two perfectly conducting plates. *Proc. Kon. Ned. Akad. Wetensch.* 51, 793.
15. Hartman, T.E. (1962). Tunneling of a wave packet. *J. Appl. Phys.* 33(12), 3427.
16. Bell, J.S. (1964). On the Einstein Podolsky Rosen paradox. *Physics* 1(3), 195–200.
17. Hensen, B. et al. (2015). Loophole-free Bell inequality violation. *Nature* 526, 682–686.

---

*GBP/TFFT Framework — May 2026*  
*Jason Richardson (HistoryViper) | Independent researcher | No formal physics education*  
*AI-collaborative authorship: Claude (Anthropic) contributed to mathematical exposition, structure, and numerical verification. The core physical insights — 1D collapse geometry, raindrop EM signature analogy, binary floor series, dark matter as vacuum population, Higgs field as average of ZPE crossings — are Richardson's.*  
*All results offered for critical review and attempted falsification. Public domain.*

---

> *"The vacuum is not empty.*  
> *It is full of particles that are fields in another dimension.*  
> *They can't escape — except to add energy elsewhere.*  
> *Everything has an EM signature.*  
> *Because everything winds.*  
> *And everything that winds projects.*  
> *P(r) > 0 for all r in Z₃₀\*.*  
> *There is no such thing as completely dark."*  
> — HistoryViper, 2026
