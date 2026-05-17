## 7. Corrected: QCD Running Coupling **(D)**

### 7.1 What v2 Got Right

TFFT v2 fit α_s(Q) = A·exp(s·n/π) with s ≈ 1/π, achieving 7.5% better RMSE than
SM 2-loop (RMSE 0.0248 vs 0.0268). The slope s ≈ 1/π was not fitted — it emerged
from the geometry. This was a correct approximation but not the full derivation.

### 7.2 v3's Derivation from Fourier Averaging **(D)**

The discrete projection weights have an exact Fourier decomposition:

```
sin²(rπ/15) = 1/2 − (1/2)cos(2rπ/15)
```

- **DC component: 1/2** — identical for all lanes, independent of r
- **AC component:** oscillates with r, averages to zero over large volumes

By the Riemann-Lebesgue lemma:

```
⟨cos(2rπ/15)⟩_V = O(a/L)   →   0   as L/a → ∞
```

Therefore in the continuum limit:

```
⟨P(r)⟩_continuum = 1/2   (exact)
```

The continuum QCD action emerges from:

```
S_cont = ∫ d⁴x (1/4) F_{μν}^a F^{aμν}
```

with the 1/2 factor absorbed into coupling renormalization (standard Wilson
lattice gauge theory procedure). This is how Maxwell's equations and Yang-Mills
emerge as the continuum limit of the mod-30 winding geometry.

The s ≈ 1/π of v2 now appears in the beta function sum rule:

```
Q₈ = 7/2 = b₀(n_f=6)/2   →   7 = b₀ = 11 − 2×6/3
```

The 7/2 is the geometric origin of the 1/π approximation. It is not 1/π exactly
— it is 7/2. The v2 approximation was within ~10% of the correct geometric origin.

---

## 8. Natural UV Cutoff **(D)**

The time string cannot curve arbitrarily fast. The gradient constraint applies
in all four spacetime directions:

```
|∂_μχ| ≤ π   for all μ
```

The **fundamental quantum step** is the beat angle:

```
Δχ_min = π/30   (6° = one beat step)
```

The full winding budget π = 30 × (π/30) — saturation corresponds to traversing
all 30 winding steps, reaching the colorless boundary {1,29} where P(1) = GEO_B =
sin²(π/15) ≈ 0.043 is the minimum non-zero projection.

**Physical interpretation:** QFT divergences signal approach to the geometric
saturation limit of time string tension. The UV cutoff is not a mathematical
regulator inserted by hand — it is the physical limit at which the time string
reaches maximum curvature. Renormalization in standard QFT is, in this picture,
**curvature normalization**: subtracting the background tension to measure
deviations from the vacuum configuration.

---

