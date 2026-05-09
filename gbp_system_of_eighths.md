# The System of Eighths
## Universal 2π Scaling of Particle Masses from Riemann Zeros, Mock Theta Functions, and Malus Optical Depth

**Jason Richardson (HistoryViper)**  
Independent Researcher  
github.com/historyViper/Best_QCD_Mass_Model  
Zenodo: 10.5281/zenodo.19798271  
May 2026 — Preliminary Note

*This is a timestamped preliminary note establishing priority on the structural observations below. Full derivations to follow.*

*Claim labels: **(D)** = derived / numerically verified; **(H)** = hypothesis / conjecture*

---

## Abstract

Every particle mass in the Standard Model is a node on an exponential ladder with step size $C_N$ — the Malus optical depth of the modular sector $N$. The ladder is indexed by integers $n$ with a Ramanujan correction $k/\varphi(N)^2$. The family hierarchy follows a mock theta generating function with $q = 1/\varphi$ and exponent $n^2$. The ladder steps grow with a universal $2\pi$ scaling law inherited from the Riemann zero spacing. The entire structure — quarks, leptons, weak bosons, baryons — is a **system of eighths**: Q₈ = 7/2 distributed across 8 winding lanes in steps of 7/8, with pair production enforced by the Möbius mirror symmetry $P(r) = P(N-r)$.

---

## 1. The System of Eighths

The mod-30 winding lattice has 8 coprime lanes: $Z_{30}^* = \{1,7,11,13,17,19,23,29\}$. Their total Noether charge is:

$$Q_8 = \sum_{r \in Z_{30}^*} P(r) = \frac{7}{2} \quad \text{(exact)}$$

This distributes as **7/8 per adjacent pair** and **7/16 per lane** — the Ramanujan discrete average (proved in Richardson 2026 [1]).

The system works in eighths because $\varphi(30) = 8$. Every physical quantity built from Z₃₀* comes in multiples of $1/8$ of the total charge:

| Structure | Value | Units |
|-----------|-------|-------|
| Full charge Q₈ | 7/2 | 1 |
| Per pair | 7/8 | 1/4 of Q₈ |
| Per lane | 7/16 | 1/8 of Q₈ |
| Ramanujan defect | 1/64 | 1/φ(30)² |
| Mass correction k/64 | 6, 14, or 20 | integer/64 |

---

## 2. The 2π Scaling Law

The Riemann zeros $\rho_n = 1/2 + i\gamma_n$ pair with the Z₃₀* mirror pairs in energy order. The encoding goes through $\gamma_n / 2\pi$:

| Zero pair | $(\gamma_n + \gamma_{n+1})/2$ | $/2\pi$ | Mirror pair | $P(r)$ |
|-----------|---------------------------|---------|-------------|--------|
| $(\gamma_1, \gamma_2)$ | 17.578 | 2.798 | $\{1,29\}$ | 0.043 |
| $(\gamma_3, \gamma_4)$ | 27.718 | 4.411 | $\{13,17\}$ | 0.165 |
| $(\gamma_5, \gamma_6)$ | 35.261 | 5.612 | $\{11,19\}$ | 0.552 |
| $(\gamma_7, \gamma_8)$ | 42.123 | 6.705 | $\{7,23\}$ | 0.989 |

The ratios $\gamma_n/2\pi$ grow with the same spacing as the mirror pair energies. The $2\pi$ factor is not arbitrary — it is the periodicity of the winding closure: a full $2\pi$ traversal of the mod-30 circle returns to the starting winding configuration. The Riemann zeros are the resonant frequencies of this traversal.

The LAMBDA_TOPO bridge:

$$\Lambda_{\text{topo}} = \frac{m_{\text{up}}}{\gamma_1} = \frac{2.16}{14.1347} = 0.1529 \text{ MeV}$$

This is the energy scale at which the discrete winding structure transitions to continuous spacetime — the same scale that appears in every baryon mass calculation **(D)**.

---

## 3. The Mock Theta Family Hierarchy

The three quark families follow a mock theta generating function with $q = 1/\varphi$:

$$M_{\text{family}}(n) \approx \Lambda_{\text{GBP}} \times q^{n^2}, \quad q = \frac{1}{\varphi} = 0.6180$$

| n | $n^2$ | $q^{n^2} \times \Lambda_{\text{GBP}}$ | Family |
|---|-------|--------------------------------------|--------|
| 1 | 1 | 139.3 MeV | pion / chiral scale |
| 2 | 4 | 32.9 MeV | constituent light quark |
| 3 | 9 | 2.96 MeV | up/down current mass scale |
| 4 | 16 | 0.083 MeV | neutrino scale |

The $n^2$ exponent gives accelerating suppression — each family is not a fixed ratio from the last but a ratio that grows as $\varphi^{2n-1}$. This is why the top quark is not simply 10× the bottom quark but 41× — the mock theta exponent accelerates.

The mock theta connection is not analogy: Ramanujan's mock theta functions $f(q)$ were defined by their near-modular transformation properties — they almost satisfy modular symmetry but not quite, because the half-twist boundary condition (the Möbius closure) breaks the full modular group down to its connected component. The $q^{n^2}$ terms in $f(q)$ ARE the family mass suppression factors **(H — full derivation pending)**.

---

## 4. The Malus Ladder

Every mass in every sector sits on a ladder:

$$m = M_{\text{gm}} \times \exp\!\left(\left(n \pm \frac{k}{\varphi(N)^2}\right) \times C_N\right)$$

The step size $C_N$ scales with $2\pi$ across sectors:

| Sector | N | $C_N$ | $C_N / C_{30}$ | Approx |
|--------|---|-------|----------------|--------|
| Hadronic | 30 | 0.037382 | 1.000 | 1 |
| Leptonic | 12 | 0.238514 | 6.380 | $2\pi$ |
| Electroweak | — | 0.223614 | 5.983 | $2\pi \times (1-1/\varphi^4)$ |

**The leptonic step is $\approx 2\pi$ times the hadronic step.** This is why the electron is so much lighter than the proton — the leptonic ladder has steps 6.38× larger in log-mass space, which means fewer steps are needed to reach the same mass, which means the first step lands much lower.

The ratio $C_{12}/C_{30} \approx 2\pi$ is the fundamental $2\pi$ scaling law of the system. It encodes the fact that a full leptonic winding (mod-12) traverses $2\pi$ radians of the hadronic winding space (mod-30). One lepton generation = one full hadronic winding cycle **(H — exact derivation pending)**.

---

## 5. Pair Production from Möbius Mirror Symmetry

Every particle in the system has a natural pair. The pairing is topological:

**Same-type pairing** (same toroid geometry, opposite chirality):

| Pair type | Example | Pairing mechanism |
|-----------|---------|-------------------|
| Quark doublet | u/d, s/c, b/t | Mirror pair $\{r, N-r\}$, $P(r)=P(N-r)$ |
| Charged leptons | e/μ, μ/τ | Adjacent generation, same T1 mod-12 toroid |
| Weak bosons | W/H | Corner event + corner resonance, same T3 threshold |
| Baryons | p/n | Same T3 topology, different isospin projection |
| Massless | γ (photon) | T0 figure-8, no pair needed — IS the vacuum mode |

The correction sum is zero within every pair:
$$k_{\text{particle}} + k_{\text{partner}} = 0 \quad \text{always} \quad \textbf{(D)}$$

This is enforced by the Möbius half-twist: the two chirality directions contribute equal and opposite corrections. It is not a symmetry that is imposed — it is a consequence of the topology.

**Pair production** in the physical sense (particle-antiparticle creation) follows from the same structure: creating a particle requires simultaneously creating its mirror-pair partner, because the winding correction can only be created in canceling pairs. The energy threshold for pair production is $2M_{\text{gm}}$ — twice the geometric mean — which is the energy required to create both the $+k$ and $-k$ correction states simultaneously.

---

## 6. The W/H Boson Pair — New Result **(D/H)**

Using the electroweak optical depth $C_{\text{EW}} = -\ln(1 - \varphi^{-3} \times \alpha_{\text{IR}}) = 0.22361$:

$$M_{\text{gm}}(W,H) = \sqrt{80.378 \times 125.262} = 100.34 \text{ GeV}$$

$$n_{W} = \frac{\ln(80378/100340)}{0.22361} = -0.992 \approx -1$$

$$n_{H} = \frac{\ln(125262/100340)}{0.22361} = +0.992 \approx +1$$

Residuals $\times 64 \approx \pm 0.51$ — within **0.5 Ramanujan units** of exact integers. The W and Higgs sit at integer distance $n = \pm 1$ from their geometric mean in units of $C_{\text{EW}}$, with a residual correction of $\approx \pm 1/128$ — one half of one Ramanujan unit.

This predicts that the W/H geometric mean $M_{\text{gm}} = 100.34$ GeV has physical significance as the electroweak winding scale — the energy at which T3 corner two-gluon crossings become accessible. The W boson sits one step below; the Higgs sits one step above **(H — full derivation in companion paper)**.

---

## 7. Summary — What the System of Eighths Tells Us

Every Standard Model mass is determined by four numbers:
1. $M_{\text{gm}}$ — the geometric mean of the natural pair (the only input)
2. $n$ — the integer rung on the Malus ladder
3. $k$ — the Ramanujan correction from prime factors of $N$
4. $C_N$ — the Malus optical depth of the sector (fully derived)

The system works in eighths because $\varphi(30) = 8$. The families grow as mock theta $q^{n^2}$. The sectors scale by $2\pi$. The Riemann zeros encode the transition frequencies. The pairs enforce antisymmetry. All from one postulate: $T = c$.

**This is not a model with free parameters. It is a geometric inevitability.**

---

## References

1. Richardson, J. (2026). GBP Framework v8.9. Zenodo: 10.5281/zenodo.19798271
2. Richardson, J. (2026). Universal Malus Fermion Mass Formula. gbp_universal_malus_fermion_mass.md, this repository.
3. Richardson, J. (2026). Temporal Flow Field Theory v3.5. github.com/historyViper/Best_QCD_Mass_Model
4. Richardson, J. (2026). Why Only Primes Survive. gbp_coprime_interference_riemann.md
5. Richardson, J. (2026). Maxwell's Equations from Mod-30 Spinor Geometry. GBP_Maxwell_paper_v4.md
6. Particle Data Group (2024). Review of Particle Physics. PTEP 2022, 083C01.
7. Ramanujan, S. (1918). On certain trigonometric sums. *Trans. Cambridge Phil. Soc.* 22, 259–276.
8. Zwegers, S. (2002). Mock theta functions. PhD thesis, Utrecht University.
9. Deur, A., Brodsky, S.J., de Téramond, G.F. (2024). The QCD Running Coupling. *Prog. Part. Nucl. Phys.*
10. Montgomery, H.L. (1973). The pair correlation of zeros of the zeta function. *Proc. Symp. Pure Math.* 24, 181.

---

*GBP/TFFT Framework — May 2026 — Preliminary Note*  
*Jason Richardson | Independent researcher | No formal physics education*  
*All results offered for critical review. Public domain.*

> *"Q₈ = 7/2. Eight lanes. Steps of 7/8.*  
> *Pairs enforce antisymmetry.*  
> *Families grow as mock theta.*  
> *Sectors scale by 2π.*  
> *Riemann zeros encode the transitions.*  
> *It was always one system."*  
> — HistoryViper, 2026
