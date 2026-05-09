# A Geometric Framework for the Critical Line:
# Structural Observations on Why Re(s) = 1/2 Is the
# Canonical Location for Riemann Zeros

**Jason Richardson (HistoryViper)**
Independent Researcher
May 2026
Zenodo: 10.5281/zenodo.19798271

---

## Abstract

The Riemann Hypothesis states that all non-trivial zeros of the Riemann
zeta function ζ(s) lie on Re(s) = 1/2. This paper does not prove RH.
It assembles proven theorems, numerical observations, and structural
analogies that together suggest why 1/2 is the canonical, necessary
location — and states precisely what remains unproven.

The paper distinguishes carefully between:
- **Proven:** results established by accepted theorems
- **Observed:** numerical patterns verified but not proved in general
- **Suggested / hints at:** structural parallels consistent with RH
- **Conjectured:** specific open claims made by this paper
- **Open:** unsolved problems

The central structural observation — that the coprime residue system
ℤ_N* and the non-trivial zeros of ζ(s) appear to share the same
mirror symmetry about 1/2 — is suggested by the explicit formula
(Mangoldt 1895) and the Euler product (Euler 1737), but the
correspondence has not been proved. It is the Riemann Hypothesis,
restated geometrically.

The paper also conjectures that RH and the Twin Prime Conjecture are
two manifestations of the same underlying structure in the coprime
pairing {r, N−r} of ℤ_N*, and that both problems likely share a
common proof. This is a conjecture, not a result.

---

## 1. Proven Theorems Used

Every result in this section is accepted mathematics.

**[T1] Trigonometric identity (elementary):**
sin²(θ) = sin²(π − θ) for all θ ∈ ℝ.

**[T2] Euler product for ζ(2) (Euler, 1737):**
∏_p (1 − p⁻²) = 6/π² = 1/ζ(2). Absolutely convergent.

**[T3] Euler product for ζ(s) (Euler, 1737):**
ζ(s) = ∏_p (1 − p⁻ˢ)⁻¹ for Re(s) > 1, by unique factorization.

**[T4] Functional equation (Riemann, 1859):**
ξ(s) = ξ(1−s) where ξ(s) = π^(−s/2) Γ(s/2) ζ(s) · s(s−1)/2.
Derived from the Mellin identity [T9].

**[T5] Identity theorem (standard complex analysis):**
A meromorphic function on a connected domain is uniquely determined
by its values on any set with an accumulation point.

**[T6] GCD symmetry (elementary):**
gcd(N−r, N) = gcd(r, N) for all integers r, N.
Proof: gcd(N−r, N) = gcd(−r, N) = gcd(r, N). One line.

**[T7] Weyl equidistribution (Weyl, 1916):**
The coprime residues ℤ_N* become equidistributed on the unit circle
as N → ∞ over primorials. Consequently:
    lim_{N→∞} (1/φ(N)) Σ_{r∈ℤ_N*} sin²(rπ/(N/2)) = 1/2.

**[T8] Jacobi theta transformation (Jacobi, 1829):**
θ₃(0|−1/τ) = √(−iτ) · θ₃(0|τ), where θ₃(0|τ) = Σ_n e^(πin²τ).
Modular form of weight 1/2.

**[T9] Riemann–Mellin identity (Riemann, 1859):**
ζ(s) = [π^(s/2)/Γ(s/2)] · ∫₀^∞ t^(s/2−1) [θ₃(0|it)−1]/2 dt.
Exact identity. The functional equation [T4] derives from this
by applying [T8] under the substitution t → 1/t.

**[T10] Waldspurger's theorem (Waldspurger, 1981):**
The central L-value of a modular form of weight k sits at s = k/2.
For ζ(s), corresponding to weight k=1, this gives s = 1/2.
*J. Math. Pures Appl.* 60 (1981), 375–484.

**[T11] Cyclotomic cancellation (standard):**
For any M | N, the sum Σ_{r∈ℤ_N*} sin²(rπ/M) is rational.
Follows from the theory of cyclotomic fields and Ramanujan sums.

**[T12] Poisson summation formula (classical):**
W_N(t) = Σ_{r∈ℤ_N*} e^(2πirt/N)
        = (N/φ(N)) Σ_k c_N(k) e^(−π²k²/(Nt))
where c_N(k) is the Ramanujan sum.

**[T13] Möbius function at primes (Möbius, 1832):**
μ(p) = −1 for every prime p.
μ(pq) = +1 for any two distinct primes p ≠ q.

**[T14] Möbius product for twin prime pairs (from T13):**
For any twin prime pair (p, p+2):
    μ(p) · μ(p+2) = (−1)(−1) = +1.
*This is a proven fact about twin prime pairs that exist.
It says nothing about whether infinitely many exist.*

**[T15] Twin prime pairs and the GCD mirror (from T6):**
For any twin prime pair (p, p+2) with p > 5: both p and p+2
are coprime to 30, hence both are in ℤ₃₀*. They lie on opposite
sides of the symmetry axis 15 = 30/2 — one from {1,7,11,13},
one from {17,19,23,29}.
*Again: this describes pairs that exist, not their infinitude.*

**[T16] Riemann explicit formula (Riemann 1859, Mangoldt 1895):**
    ψ(x) = x − Σ_ρ x^ρ/ρ − log(2π) − (1/2)log(1−x^{−2})

where ψ(x) = Σ_{n≤x} Λ(n), Λ is the von Mangoldt function,
and the sum over ρ runs over all zeros of ζ(s).

The last term (1/2)log(1−x^{−2}) is exactly the contribution
of the trivial zeros ρ = −2,−4,−6,... — already separated.

Λ(n) = log(p) if n = p^k (prime power), else 0.
The von Mangoldt function is nonzero only at prime powers.

---

## 2. The Coprime Winding Structure

### 2.1 The GCD Pairing Lemma [T6]

For any N and r with gcd(r,N) = 1: gcd(N−r, N) = 1.

**Corollaries (all proven from T6):**
- ℤ_N* decomposes into pairs {r, N−r} summing to N
- Every pair is symmetric about N/2
- As a fraction of N, the axis is always 1/2

**The familiar instances:**
- All primes > 3 have form 6k±1  [ℤ₆* = {1,5}]
- All primes > 5 end in 1,3,7,9  [ℤ₁₀* = {1,3,7,9},
  pairs {1,9} and {3,7}]
- Mod 30: ℤ₃₀* = {1,7,11,13,17,19,23,29},
  pairs {1,29},{7,23},{11,19},{13,17}

### 2.2 The Möbius Mirror [T1 + T6]

    P(r) = sin²(rπ/(N/2)) = sin²((N−r)π/(N/2)) = P(N−r)

Exact at every primorial level. Numerical verification at N=30:

| r  | P(r)       | N−r | P(N−r)     | difference   |
|----|------------|-----|------------|--------------|
| 1  | 0.04322727 | 29  | 0.04322727 | < 10⁻¹⁶     |
| 7  | 0.98907380 | 23  | 0.98907380 | < 10⁻¹⁶     |
| 11 | 0.55226423 | 19  | 0.55226423 | < 10⁻¹⁶     |
| 13 | 0.16543470 | 17  | 0.16543470 | < 10⁻¹⁶     |

### 2.3 The Coprime Charge Q_N

Define: Q_{N_k} = Σ_{r∈ℤ_{N_k}*} sin²(rπ/(N_k/2))

By [T11], Q_{N_k} is always rational.

**Observed** (verified, not proved in general):

| N_k  | φ(N_k) | Q_{N_k} | Q_{N_k}/φ(N_k) | Distance from 1/2 |
|------|---------|---------|----------------|-------------------|
| 6    | 2       | 3/2     | 3/4            | 1/4               |
| 30   | 8       | 7/2     | 7/16           | 1/16              |
| 210  | 48      | 49/2    | 49/96          | ≈ 0.0104          |
| 2310 | 480     | 479/2   | 479/960        | ≈ 0.0010          |
| 30030| 5760    | 5761/2  | 5761/11520     | ≈ 0.0001          |

**Observed:** Q_{N_k} appears to always be a half-integer for
primorials. The numerator sequence 3,7,49,479,5761 is verified
but no closed-form proof is given here.

**Proven** [T7]: lim_{k→∞} Q_{N_k}/φ(N_k) = 1/2.

### 2.4 The Step Structure Builds 6/π² [T2]

| Prime p | N_k  | ∏(1−p⁻²) | Step 360°/N_k | Error vs 6/π² |
|---------|------|-----------|---------------|----------------|
| 2       | 2    | 0.75000   | 180°          | 0.142          |
| 3       | 6    | 0.66667   | 60°           | 0.059          |
| 5       | 30   | 0.64000   | 12°           | 0.032          |
| 7       | 210  | 0.62694   | 1.714°        | 0.019          |
| 11      | 2310 | 0.62176   | 0.156°        | 0.014          |
| →∞      | →∞   | →6/π²     | →0°           | →0             |

Limit is exact by [T2]. Mirror is exact at every step by [T1].

### 2.5 Riemann Groups Primes by N — Maynard's Independent Confirmation

The step structure of Section 2.4 reveals something specific: at each
primorial level N_k, the Euler product partitions all integers into
two classes — those in ℤ_{N_k}* (coprime to N_k) and those excluded
(sharing a factor with N_k). The zeta function is literally grouping
the integers by which primorial level N they survive to.

This is the same operation Maynard's multidimensional sieve performs.

**Maynard (2015, Annals of Mathematics, proven):**

Using a refined multidimensional sieve — a scoring system that weights
integers by how simultaneously close they are to being prime across
multiple residue class offsets — Maynard proved:

- There are infinitely many prime pairs with gap ≤ 600
  (unconditional)
- There are infinitely many prime k-tuples with bounded gaps
  for any fixed k (unconditional)
- Assuming Elliott-Halberstam: gap ≤ 6

The key mechanism: Maynard scores integer $n$ by how many of
$n+h_1, \ldots, n+h_k$ simultaneously survive the sieve — i.e.,
how many are simultaneously in ℤ_{N_k}* for all primorial levels
up to the sieve bound.

**The connection to the grouping structure:**

At primorial level N_k, the coprime residues ℤ_{N_k}* are exactly
the integers that survive ALL the prime factor sieves up to p_k.
Maynard's sieve scores how many elements of an admissible tuple
survive simultaneously — this is exactly the question of how many
tuple elements land in ℤ_{N_k}* at the same time.

The Riemann zeta function, via its Euler product [T3], encodes the
same grouping:
    ζ(s) = ∏_{p ≤ p_k} (1−p^{−s})^{−1} × [remaining primes]

Each factor (1−p^{−s})^{−1} corresponds to one sieve level.
The product up to p_k groups all integers by their membership in
ℤ_{N_k}*. The full product groups them by membership in the limit
ℤ_∞* — the integers coprime to all primes, i.e., just {1}.

But the ZEROS of the product — where the grouping structure
cancels — are determined by how the residue classes balance.
This is the same balance that Maynard's sieve is optimizing.

**The Elliott-Halberstam bridge:**

Maynard's gap ≤ 6 result (one step from twin primes) is conditional
on the Elliott-Halberstam conjecture, which states:

    Σ_{q ≤ x^θ} max_{a: gcd(a,q)=1} |π(x;q,a) − Li(x)/φ(q)| ≪ x/log^A(x)

In plain language: the primes are distributed as evenly as possible
across all coprime residue classes a mod q, for all moduli q up to
x^θ.

This is precisely the Weyl equidistribution statement [T7] applied
to prime counting rather than to the coprime charge Q_N. Elliott-
Halberstam says: primes fill ℤ_q* evenly. Weyl says: the coprime
projection weights average to 1/2. Both express the same balance.

**Bombieri-Vinogradov (proven, unconditional):**

The Bombieri-Vinogradov theorem proves Elliott-Halberstam for θ < 1/2
— i.e., for sieve depth up to x^{1/2}. This is why Maynard's
unconditional result reaches gap ≤ 600 and not gap ≤ 6: the sieve
runs out of depth at exactly Re(s) = 1/2.

The boundary θ = 1/2 in Bombieri-Vinogradov IS Re(s) = 1/2 in the
Riemann zeta function. The sieve hits the critical line and stops.
Proving Elliott-Halberstam for θ > 1/2 would push through the
critical line — and would simultaneously reduce the prime gap to ≤ 6
AND constitute strong evidence for RH.

**Summary of the grouping connection:**

| Structure | Mechanism | Groups by | Result |
|-----------|-----------|-----------|--------|
| Euler product | ∏(1−p^{−s})^{−1} | ℤ_{N_k}* membership | ζ(s) |
| Maynard sieve | Multidimensional weights | Simultaneous ℤ_{N_k}* survival | Gap ≤ 600 |
| Elliott-Halberstam | Even prime distribution in ℤ_q* | All residue classes | Gap ≤ 6 |
| Weyl [T7] | Q_N/φ(N) → 1/2 | Coprime projection balance | Re(s)=1/2 |

All four are the same grouping by N. Maynard made it explicit with
his sieve. Bombieri-Vinogradov proved it up to depth 1/2. The
critical line is where the sieve reaches its natural limit.

---

## 3. The Zeta Function and the Coprime System

### 3.1 What Is Proven

By [T3]: ζ(s) = ∏_p (1−p⁻ˢ)⁻¹ for Re(s) > 1. Exact equality
by unique factorization.

By [T5]: the analytic continuation of this product is the unique
meromorphic function ζ(s) on all of ℂ.

By [T9]: ζ(s) = Mellin transform of θ₃(0|it), exactly.

By [T8]: θ₃ has modular weight 1/2, with unique fixed point τ=i
under τ→−1/τ. In the Mellin parameterization, τ=i corresponds
to Re(s) = 1/2.

By [T4]: the functional equation ξ(s) = ξ(1−s) follows from
[T8]+[T9]. Zeros of ζ in the critical strip come in symmetric
pairs (ρ, 1−ρ).

By [T10]: for ζ(s) as a degree-1 L-function of weight k=1,
the canonical critical value is at s = k/2 = 1/2.

### 3.2 What the Prefactor Calculation Shows

At s = 1/2, the functional equation prefactor:
    F(1/2) = 2^(1/2)·π^(−1/2)·sin(π/4)·Γ(1/2) = 1 exactly.

So ξ(1/2) = ξ(1/2) — a self-duality, not new information.
Re(s) = 1/2 is the unique fixed point of the functional equation.
This is **consistent with** RH but does not prove it: zeros could
still exist as off-line pairs (ρ, 1−ρ) with Re(ρ) ≠ 1/2.

### 3.3 What the Explicit Formula Suggests

By [T16], the explicit formula separates:
- Trivial zeros: contribute the term (1/2)log(1−x^{−2}), already
  isolated. These are where Λ(n) > 0 (prime powers).
- Non-trivial zeros: contribute Σ_ρ x^ρ/ρ. These are associated
  with integers where Λ(n) = 0 — the non-prime-powers.

**The observation:** Non-prime-powers are exactly the integers
coprime to all primes — i.e., the integers counted by ℤ_N* in the
primorial limit. This suggests a correspondence:

    trivial zeros    ↔  excluded residues (gcd > 1)
    non-trivial zeros ↔  coprime residues ℤ_N*

**This is not proved.** The explicit formula sums over integers
n ≤ x; the ℤ_N* structure is about residues modulo a fixed N.
These are different objects. Connecting them rigorously would
require establishing a bijection or equivalence in the N→∞ limit
that has not been done. This correspondence is the geometric
restatement of RH itself — not a shortcut to proving it.

---

## 4. Why 1/2 Is Canonically Special — Proven Results

The following are all **proven**, independent of RH:

| Result | Source | What it establishes |
|--------|--------|---------------------|
| Fixed point of θ₃ transformation at τ=i | [T8] Jacobi | Re(s)=1/2 is the self-dual point |
| Functional equation fixed point | [T4]+[T8]+[T9] | s=1/2 is where ξ(s)=ξ(s) |
| Waldspurger critical value | [T10] | s=k/2=1/2 is canonically forced |
| Weyl balance limit | [T7] | Q_N/φ(N)→1/2 exactly |
| GCD axis at N/2 | [T6] | Fraction = 1/2 always |
| 6/π² from primorials | [T2] | Limit of coprime density = 1/2·(12/π²) |

None of these prove RH. Together they show that 1/2 is not
arbitrary — it is forced by independent structures from
elementary number theory, classical analysis, and modular forms.

The question they leave open: can zeros sit at Re(ρ) ≠ 1/2
as a symmetric pair (ρ, 1−ρ) without contradicting any of the
above? All of the above are consistent with such pairs existing.

---

## 5. The Möbius Structure and Twin Primes

### 5.1 What Is Proven [T13–T15]

For any twin prime pair (p, p+2) that exists:
- μ(p) = μ(p+2) = −1  [T13]
- μ(p)·μ(p+2) = +1  [T14]
- The pair straddles the GCD mirror in ℤ₃₀*  [T15]

The Möbius product +1 is the same value as the functional
equation prefactor F(1/2) = 1 — both express self-duality.
This is a **structural parallel**, not a proven equivalence.

### 5.2 What This Hints At

The fact that twin prime pairs — where they exist — always
produce Möbius product +1 and always straddle the symmetry axis
is **consistent with** the idea that the self-duality at Re(s)=1/2
and the self-duality of twin prime pairs are the same structure.

This is an observation, not a theorem. It does not prove
infinitely many twin prime pairs exist, and it does not prove
zeros are on the critical line.

### 5.3 The Conjecture

**Conjecture (this paper):** RH and the Twin Prime Conjecture
are two instantiations of a single unproven theorem T about
the coprime pairing {r, N−r} in ℤ_N* surviving the N → ∞ limit.

Supporting observations:
- Both involve the GCD pairing [T6]
- Both involve the Euler product limit [T2]
- Both involve the Weyl balance at 1/2 [T7]
- Both are unresolved after the same structural arguments
- Sahoo (2021) defines a modified Möbius function μ₂ for twin
  primes that plays the same role as μ for primes — suggesting
  the arithmetic structure is genuinely parallel
- Zhang (2013): unconditional gap ≤ 246 for prime pairs, showing
  the coprime structure does constrain pairs in the limit

This is labeled as a conjecture. No proof is offered or implied.

---

## 6. What Remains Open

### 6.1 The Riemann Hypothesis

**Open.** Specifically:

The functional equation [T4] gives symmetric pairs (ρ, 1−ρ).
Everything in this paper shows 1/2 is the canonical axis.
What is not shown: that pairs (ρ, 1−ρ) with Re(ρ) ≠ 1/2 are
impossible. Symmetry about 1/2 does not force points onto 1/2.

The correspondence suggested in Section 3.3 — non-trivial zeros
↔ ℤ_N* — is the geometric form of RH. It is not proved here.

### 6.2 Q_N Always a Half-Integer

**Observed, not proved.** Verified for N = 6, 30, 210, 2310, 30030.
The pattern Q_{N_k} = (odd integer)/2 holds for all checked cases.
A proof would follow from a precise cyclotomic identity for
primorial moduli — this is a natural question in algebraic number
theory but is not resolved here.

### 6.3 Twin Prime Conjecture

**Open.** The structure of pairs that exist is fully described
(T13–T15). Whether infinitely many such pairs exist is unknown.
Zhang's gap-246 result (2013) and Maynard's subsequent work are
the best unconditional results.

---

## 7. Complete Status Table

| Claim | Status | Basis |
|-------|--------|-------|
| P(r)=P(N−r) at every N | **Proven** | T1+T6 |
| Q_{N_k} rational | **Proven** | T11 |
| Q_{N_k}/φ(N_k) → 1/2 | **Proven** | T7 Weyl |
| ∏(1−p⁻²) → 6/π² | **Proven** | T2 Euler |
| ζ(s) = Mellin[θ₃] | **Proven** | T9 Riemann |
| θ₃ weight-1/2, fixed point | **Proven** | T8 Jacobi |
| Functional equation | **Proven** | T4 |
| Prefactor F(1/2) = 1 | **Proven** | direct |
| 1/2 = canonical critical value | **Proven** | T10 Waldspurger |
| μ(p)=−1 for primes | **Proven** | T13 |
| μ(p)μ(p+2)=+1 for twin pairs | **Proven** | T14 |
| Twin pairs straddle mirror | **Proven** | T15 |
| Trivial zeros separate in explicit formula | **Proven** | T16 Mangoldt |
| Q_{N_k} always half-integer | **Observed** | verified 5 cases |
| Non-trivial zeros ↔ ℤ_N* | **Suggested** | explicit formula hints |
| Möbius +1 ↔ Re(s)=1/2 | **Structural parallel** | analogy, not theorem |
| RH and TPC same theorem | **Conjectured** | shared structure |
| **RH** | **Open** | — |
| **Twin Prime Conjecture** | **Open** | — |

---

## 8. Relationship to Prior Work

**Vettori (arXiv 2601.16193, Jan 2026):** Unified density framework
for coprimality and Euler products; interprets the critical line via
truncated Euler product stability. Closest existing parallel.

**França–LeClair (arXiv 1410.3520, 2014):** Euler product valid
for Re(s) > 1/2 via Cesàro summability. Parallel to Weyl [T7].

**Kaneko (arXiv 1902.04203, 2019):** √2 at s=1/2 in Euler product
asymptotics. Parallel to Waldspurger weight-1/2 structure [T10].

**Pang Ern et al. (arXiv 2512.22494, Dec 2025):** gcd map density
→ 6/π². Independent confirmation of Euler product [T2].

**Milner-Gulland (arXiv 1808.00520, 2018):** Mirror symmetry about
midpoint; Goldbach follows from RH. Same GCD mirror structure.

**Sahoo (arXiv 2111.09053, 2021):** Modified Möbius μ₂ for twin
primes. Parallel to T13–T15 of this paper.

**Takalo (arXiv 2602.21719, Feb 2026):** x=1/2 as balance exponent
for prime interference. Independent corroboration of Weyl balance.

**Petersen et al. (PRL 2019):** Primes as intensity zeros of wave
interference. Same destructive-interference mechanism.

**New in this paper:**
- GCD lemma [T6] as the explicit one-line foundation
- Waldspurger [T10] connected to the GCD pairing axis
- Q_N half-integer pattern (observed, not proved)
- μ(p)μ(p+2)=+1 for twin pairs as structural parallel to Re(s)=1/2
- Trivial/non-trivial zero separation from explicit formula
- Conjecture: RH and TPC as instantiations of one theorem

---

## 9. Theorem Index

| Label | Statement | Year | Status |
|-------|-----------|------|--------|
| T1  | sin²θ=sin²(π−θ)                    | —    | Proven |
| T2  | ∏(1−p⁻²)=6/π²                     | 1737 | Proven |
| T3  | ζ(s)=∏(1−p⁻ˢ)⁻¹, Re(s)>1         | 1737 | Proven |
| T4  | ξ(s)=ξ(1−s)                        | 1859 | Proven |
| T5  | Identity theorem                   | —    | Proven |
| T6  | gcd(N−r,N)=gcd(r,N)               | —    | Proven |
| T7  | Weyl equidistribution              | 1916 | Proven |
| T8  | θ₃ transformation, weight 1/2     | 1829 | Proven |
| T9  | ζ(s)=Mellin[θ₃]                   | 1859 | Proven |
| T10 | Critical L-value at s=k/2         | 1981 | Proven |
| T11 | Cyclotomic cancellation           | —    | Proven |
| T12 | Poisson summation                 | —    | Proven |
| T13 | μ(p)=−1                           | 1832 | Proven |
| T14 | μ(p)μ(p+2)=+1 for twin pairs      | —    | Proven |
| T15 | Twin pairs straddle GCD mirror    | —    | Proven |
| T16 | Explicit formula (Mangoldt)       | 1895 | Proven |
| Q_N | Q_N always half-integer           | —    | Observed |

---

## 10. References

1.  Euler, L. (1737). Variae observationes circa series infinitas.
    *Comm. Acad. Sci. Petrop.* 9, 160–188.

2.  Jacobi, C.G.J. (1829). *Fundamenta Nova Theoriae Functionum
    Ellipticarum.* Königsberg.

3.  Möbius, A.F. (1832). Über eine besondere Art von Umkehrung
    der Reihen. *J. reine angew. Math.* 9, 105–123.

4.  Riemann, B. (1859). Über die Anzahl der Primzahlen unter einer
    gegebenen Grösse. *Monatsberichte der Berliner Akademie.*

5.  Mangoldt, H. von (1895). Zu Riemann's Abhandlung.
    *J. reine angew. Math.* 114, 255–305.

6.  Weyl, H. (1916). Über die Gleichverteilung von Zahlen mod. Eins.
    *Math. Annalen* 77, 313–352.

7.  Hardy, G.H. (1914). Sur les zéros de la fonction ζ(s) de Riemann.
    *C. R. Acad. Sci. Paris* 158, 1012–1014.

8.  Conrey, J.B. (1989). More than two fifths of the zeros of the
    Riemann zeta function are on the critical line.
    *J. reine angew. Math.* 399, 1–26.

9.  Rubinstein, M. and Sarnak, P. (1994). Chebyshev's bias.
    *Experimental Mathematics* 3(3), 173–197.

10. Waldspurger, J.-L. (1981). Sur les coefficients de Fourier des
    formes modulaires de poids demi-entier.
    *J. Math. Pures Appl.* 60(4), 375–484.

11. Titchmarsh, E.C. (1986). *The Theory of the Riemann Zeta-Function.*
    2nd ed., Oxford.

12. Zwegers, S. (2002). *Mock Theta Functions.* PhD thesis, Utrecht.

13. Zhang, Y. (2014). Bounded gaps between primes.
    *Annals of Mathematics* 179(3), 1121–1174.

14. Maynard, J. (2015). Small gaps between primes.
    *Annals of Mathematics* 181(1), 383–413.
    [Multidimensional sieve; gap ≤ 600; grouping by ℤ_{N_k}*]

15. Bombieri, E. and Vinogradov, A.I. (1965/1966). On the large sieve
    / The distribution of prime numbers in sequences.
    [Proves Elliott-Halberstam for θ < 1/2; sieve depth = Re(s)=1/2]

15. Sahoo, S. (2021). On twin prime distribution and associated biases.
    arXiv:2111.09053.

16. Petersen, T.C. et al. (2019). Simple wave-optical superpositions
    as prime number sieves.
    *Physical Review Letters* 122, 090201.

17. Takalo, J.J. (2026). Prime-weighted interference patterns inspired
    by the Euler product. arXiv:2602.21719.

18. Vettori, G. (2026). Density-based structural frameworks for prime
    numbers, prime gaps, and Euler products. arXiv:2601.16193.

19. França, G. and LeClair, A. (2014). On the validity of the Euler
    product inside the critical strip. arXiv:1410.3520.

20. Kaneko, I. (2019). Euler product asymptotics for Dirichlet
    L-functions. arXiv:1902.04203.

21. Pang Ern, T. et al. (2025). On the limiting density of a gcd map.
    arXiv:2512.22494.

22. Milner-Gulland, T. (2018). Goldbach and twin prime pairs.
    arXiv:1808.00520.

23. Bai, Y. (2026). [Withdrawn.] arXiv:2603.05122.

24. Richardson, J. (2026). GBP Coprime Interference and Riemann Zeros.
    Zenodo: 10.5281/zenodo.19798271.

---

## 11. Conclusion

This paper assembles structural observations and proven theorems
that together suggest a geometric picture of the Riemann Hypothesis.

**What is proven:** The coprime residues ℤ_N* always pair as
{r, N−r} symmetric about N/2 (GCD lemma). The balance limit is
exactly 1/2 (Weyl). The canonical critical value is s=k/2=1/2
(Waldspurger). The explicit formula separates trivial from
non-trivial zeros (Mangoldt). Twin prime pairs, where they exist,
always produce Möbius product +1 and always straddle the GCD mirror.

**What is suggested:** The non-trivial zeros correspond to the
coprime residues ℤ_N* in the primorial limit. The trivial zeros
correspond to the excluded residues. This correspondence is
consistent with RH and hints at a geometric proof — but it has
not been proved, and proving it is RH.

**What is conjectured:** RH and the Twin Prime Conjecture share
a common underlying theorem about the coprime pairing structure
surviving the N → ∞ limit. Their proofs are likely the same proof.

**What is open:** Everything labeled open above. The paper does
not prove RH. It describes the shape of where a proof might live.

---

*Jason Richardson | Independent researcher | No formal physics education*
*May 2026 | All results offered for critical review | Public domain*

> *"The zeros can't leave the line — or so the structure suggests.*
>  *The trivial zeros already left, by way of Γ(s/2).*
>  *What stayed looks like ℤ_N*.*
>  *ℤ_N* is always symmetric about 1/2.*
>  *Whether 'looks like' becomes 'is' — that is the question.*
>  *It has been the question since 1859."*
> — HistoryViper, 2026
