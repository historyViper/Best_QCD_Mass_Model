# GBP Framework — The Compressed Lagrangian
## One Expression Capturing All Sectors

**Author:** Jason Richardson (HistoryViper)  
**Date:** April 2026  
**Code:** github.com/historyViper/mod30-spinor  
**Zenodo:** 10.5281/zenodo.19798271

---

## The Core Insight — Two Trips at c

Every particle makes two trips per cycle:

- **Trip 1 (mod-30):** The field of the particle — Hilbert space side.
  Winding numbers Z₃₀* = {1,7,11,13,17,19,23,29}. Eight lanes.
- **Trip 2 (mod-24):** The particle's wave — observable spacetime side.
  Winding numbers Z₂₄* = {1,5,7,11,13,17,19,23}. Eight lanes.

At relativistic speeds both trips run at c. They add and subtract —
that is the wavefunction. The interference between the two trips IS
quantum mechanics.

Note: mod-30 + mod-24 = **54** (the number of predicted baryons).
Note: mod-30 - mod-24 = **6** = half the natural angular step.
The two trips are geometrically locked. This is not a coincidence.

The Dirac spinor already knows this. Its four components are:

| Component | Trip | Sector | Chirality |
|-----------|------|--------|-----------|
| ψ_L (large, +) | Trip 1 | Hilbert (mod-30) | Left |
| ψ_L (large, −) | Trip 1 | Hilbert (mod-30) | Right |
| ψ_S (small, +) | Trip 2 | Spacetime (mod-24) | Left |
| ψ_S (small, −) | Trip 2 | Spacetime (mod-24) | Right |

The "large" and "small" components of the Dirac spinor are the
Hilbert space and spacetime trips respectively. No extra machinery needed.

---

## The Compressed Lagrangian

$$\boxed{
\mathcal{L}_{\text{GBP}} =
\underbrace{\bar{\Psi}\, i\gamma^\mu \hat{D}_\mu \Psi}_{\text{two-trip kinetic}}
- \underbrace{M_{\text{Malus}}(\hat{r})\, \bar{\Psi}\Psi}_{\text{8-lane mass}}
+ \underbrace{\mathcal{L}_{\text{torsion}}}_{\text{strange/charm}}
- \underbrace{\frac{1}{4}F_{\mu\nu}^{(r)}F^{(r)\mu\nu}}_{\text{lane gauge field}}
}$$

**That's it. Four terms.** Everything else is a consequence.

---

## Term 1: Two-Trip Kinetic (Dirac + Malus Connection)

$$\bar{\Psi}\, i\gamma^\mu \hat{D}_\mu \Psi$$

The covariant derivative with Malus projection built in:

$$\hat{D}_\mu = \partial_\mu + i \sum_{r \in Z_{30}^*} P(r)\, A_\mu^{(r)}$$

where:
$$P(r) = \sin^2\!\left(\frac{r\pi}{15}\right), \quad r \in Z_{30}^* = \{1,7,11,13,17,19,23,29\}$$

**This puts all 8 lanes into the covariant derivative.** Malus's Law
is the lane-dependent coupling — exactly analogous to the gauge coupling
$g$ in QCD, but here it is not a free parameter. It is fixed by geometry:
$P(r) = \sin^2(r\pi/15)$.

The Dirac spinor $\Psi$ is a standard 4-component spinor. Its two large
components (Trip 1) live on the mod-30 Hilbert space grid. Its two small
components (Trip 2) live on the mod-24 spacetime grid. The $\gamma^\mu$
matrices handle the mixing between trips — this is exactly what they
were always doing, now with a geometric interpretation.

**The ± structure** (Hilbert space vs observable spacetime) is automatic:
positive-energy solutions are Trip 2 (spacetime, what we measure),
negative-energy solutions are Trip 1 (Hilbert space, the field).
At speed c they are degenerate — that is the interference.

---

## Term 2: The 8-Lane Mass (Malus Mass Operator)

$$M_{\text{Malus}}(\hat{r})\, \bar{\Psi}\Psi$$

The mass is not a single number. It is a **lane-dependent operator**:

$$M_{\text{Malus}}(\hat{r}) = \Lambda_{\text{GBP}} \cdot P(\hat{r}) \cdot (1 + \lambda_k)$$

where:
- $\hat{r}$ = winding number operator (eigenvalue $r \in Z_{30}^*$)
- $\Lambda_{\text{GBP}} = \Lambda_{\text{QCD}} \cdot e^C$ = GBP energy scale
- $C = -\ln(1 - \text{GEO\_B} \cdot \alpha_{\text{IR}})$ = Malus-IR optical depth
- $\lambda_k = \text{LU} \cdot \varphi^{k/2}$ = torsion level correction
  ($k$ = 0, 0.5, 1, 1.5 for T1, T2, T3, T4)

**This is Malus's Law as a mass term.** The mass of a particle is
the projection of the time string tension onto its winding lane.
Heavy particles are on high-projection lanes (r=7,23: P≈0.989).
Light particles are on low-projection lanes (r=1,29: P≈0.043).

The colorless boundary lanes {1,29} have $P(1) = P(29) = \sin^2(\pi/15)$
= GEO_B = the minimum projection. This is why the photon is massless —
it rides the colorless boundary, and in the massless limit GEO_B → 0.

---

## Term 3: Torsion Term (Strange and Charm)

$$\mathcal{L}_{\text{torsion}} = -\frac{1}{12} H_{\mu\nu\rho} H^{\mu\nu\rho} + \mathcal{L}_{\text{charm-flip}}$$

**Strange quark** (lane 11, $P(11) = \sin^2(11\pi/15) = 0.5523$):

Strange needs one extra Malus correction because it sits at the
midpoint of the lane projection range — exactly halfway between the
colorless boundary (P≈0.043) and the top (P≈0.989). The torsion
contorsion tensor $K_{\mu\nu\rho}$ for lane 11 picks up a phase:

$$H_{\mu\nu\rho}^{(s)} = \partial_{[\mu} B_{\nu\rho]} + K_{\mu\nu\rho}^{(11)}$$

where $K^{(11)} = \text{GEO\_B} \cdot \cos^2(\pi/5)$ — the Z5* 
pentagonal phase correction. This is the same factor that appears in 
the Sigma_b0 Malus correction.

**Charm quark** (lane 23, the hard one):

Charm winding = $720° \times 23/30 = 552°$.
After T1 closure: $552° - 360° = 192° = 180° + 12°$.

Each charm traversal leaves a **12° helicity residual** — one natural
T1 step ($360°/30$). This is a **double-helix torsion flip**. The
charm quark is trying to be on lane 23 but its winding overshoots T1
closure by exactly one step, flipping the helicity.

In Lagrangian form — a Pauli-Gursey-type chirality mixing term:

$$\mathcal{L}_{\text{charm-flip}} = 
i\, \epsilon_c\, \bar{\Psi}_c \sigma^{\mu\nu} F_{\mu\nu}^{(23)} \Psi_c$$

where:
- $\epsilon_c = \sin^2(\pi/30) = \text{GEO\_B}$ = one natural step projection
- $\sigma^{\mu\nu} = \frac{i}{2}[\gamma^\mu, \gamma^\nu]$ = the standard
  Pauli-Lubanski chirality mixing tensor
- $F_{\mu\nu}^{(23)}$ = the lane-23 field strength

This term rotates the charm spinor by 12° per traversal — a geometric
Pauli-Gursey rotation, not a free parameter. It IS the double helix:
each full cycle the charm spinor traces a helix in spinor space with
pitch 12°.

The correction rule that fell out of v8.8:
$$\text{GBP\_cover} = \text{SM\_cover} - n_{\text{charm}} \times \frac{12°}{H_{\text{beat}}}
= \text{SM\_cover} - \frac{n_{\text{charm}}}{2}$$

is the Euler-Lagrange equation of this term.

---

## Term 4: Lane Gauge Field

$$-\frac{1}{4} F_{\mu\nu}^{(r)} F^{(r)\mu\nu}$$

Standard Yang-Mills kinetic term for the gauge field, but with
lane-dependent field strength:

$$F_{\mu\nu}^{(r)} = \partial_\mu A_\nu^{(r)} - \partial_\nu A_\mu^{(r)}
+ P(r) \left[A_\mu^{(r)}, A_\nu^{(r)}\right]$$

The commutator coefficient is $P(r) = \sin^2(r\pi/15)$ instead of
the QCD coupling $g$. At $r \in \{1,29\}$ (colorless boundary),
$P \approx 0.043$ — the commutator is suppressed. This is why
gluons at the colorless boundary die (deposit their energy) instead
of propagating — the gauge self-coupling is almost zero there.

**This term gives the Yang-Mills mass gap for free.** No zero-energy
propagating mode exists because $P(r) > 0$ for all $r \in Z_{30}^*$,
and $P(0) = \sin^2(0) = 0$ for the colorless singlet — which has zero
Noether charge and cannot propagate (Schur's lemma).

---

## The Complete Compact Expression

$$\mathcal{L}_{\text{GBP}} = 
\bar{\Psi}\left[i\gamma^\mu\!\left(\partial_\mu + i P(\hat{r}) A_\mu\right)
- \Lambda_{\text{GBP}} P(\hat{r})(1+\lambda_k)\right]\Psi
- \frac{1}{12}H_{\mu\nu\rho}H^{\mu\nu\rho}
+ i\,\epsilon_c\,\bar{\Psi}_c\sigma^{\mu\nu}F_{\mu\nu}\Psi_c
- \frac{P(\hat{r})}{4}F_{\mu\nu}F^{\mu\nu}$$

$$\text{where } P(r) = \sin^2\!\left(\frac{r\pi}{15}\right),\quad
r \in Z_{30}^* = \{1,7,11,13,17,19,23,29\},\quad
\hat{r} \text{ is the winding number operator}$$

**Four terms. Zero free parameters. All sectors.**

| Term | What it does | Key number |
|------|-------------|-----------|
| Kinetic | Two-trip Dirac + 8-lane Malus connection | sin²(rπ/15) |
| Mass | Lane-dependent mass from time string tension | Λ_GBP × P(r) |
| Torsion | Strange phase + charm helicity flip | 12° per traversal |
| Gauge | Yang-Mills with Malus self-coupling | P(r) × [A,A] |

---

## Connection to String Theory

The action in the bulk (10D → 4D) remains the 1984 superstring action:

$$S = -\frac{1}{4\alpha'}\int d^{10}x\sqrt{-g}\left[R + \frac{1}{12}H_{\mu\nu\rho}H^{\mu\nu\rho}\right]$$

with $\alpha' \to T = c$ (string tension = speed of light, not free).

At the boundary (4D observable sector), the matter Lagrangian is
$\mathcal{L}_{\text{GBP}}$ above. The compactification that takes
10D → 4D is the mod-30 closure condition — not a Calabi-Yau.

**The GBP Lagrangian is what string theory's matter sector looks like
when the compactification is solved.**

---

## Why This Compresses the Four-Document Version

The four Lagrangians in `gbp_lagrangians.md` are all limits of this one:

| Previous document | This version |
|------------------|-------------|
| Master (10D) | Bulk string action + $\mathcal{L}_{\text{GBP}}$ at boundary |
| Mass (hadronic) | Term 1 + Term 2, $r \in Z_{30}^*$ |
| Optical | Term 4 alone, $r \in \{1,29\}$ limit → Maxwell |
| Leptonic | Same structure, $r \in Z_{12}^*$, $P_{12}(r) = \sin^2(r\pi/6)$ |

The leptonic sector uses the same Lagrangian with mod-12 substituted:
$$P(r) \to P_{12}(r) = \sin^2\!\left(\frac{r\pi}{6}\right),\quad r \in Z_{12}^* = \{1,5,7,11\}$$

The leakage self-interaction (responsible for electron lobes) is the
torsion term evaluated at mod-12 — the same $H_{\mu\nu\rho}$ term
but with the mod-12 contorsion.

---

## Falsification

This Lagrangian makes one prediction that separates it from all others:

**The winding number operator $\hat{r}$ has exactly 8 eigenvalues.**

If any experiment finds a 9th gluon, a baryon that requires a 9th lane,
or a reflection coefficient below 1.093%, the framework is wrong.

If lattice QCD restricted to $Z_{30}^*$ winding numbers reproduces the
mass spectrum without tuning — the framework is right.

---

*github.com/historyViper/mod30-spinor — April 2026*  
*Zenodo: 10.5281/zenodo.19798271*
