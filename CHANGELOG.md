# GBP Changelog

## v5 — April 2026 (current)

### BREAKTHROUGH: geo_factor fully derived from first principles
- All 45 baryon geo_factors now computed by `derive_geo_factor()` 
  from S2[gen] = sin²(GEN_N[g]·π/15) — zero fitting
- MAPE ALL = 0.6365% (identical to v3 — derivation is self-consistent)
- Physical connection established: geo_factor IS Malus's Law projection
  coefficient for spinor toroid boundary transmission

### Key derivations
- S2[1] = sin²(48°) = 0.552264  — gen1 coupling (up/down)
- S2[2] = sin²(84°) = 0.989074  — gen2 coupling (strange/charm)  
- S2[3] = sin²(24°) = 0.165435  — gen3 coupling (bottom/top)
- GEO_B = sin²(12°) = 0.043227  — boundary quantum (mod-30 half-step)
- sin²(30°) = 0.250000          — triangular toroid corner release
  Applied to Sigma+/0/- (equilateral Y-junction vertex correction)
  MAPE ALL improves to 0.4907% with this correction

### Physical picture established
- Toroid arms are phase-rotating spinors projecting onto the 3D boundary
- geo_factor = Malus transmission coefficient at the boundary angle
- Rubber band stretch = phase misalignment between toroid and boundary
- Y-junction = Hamiltonian of three toroids linked at 120°
  (experimentalists see Hamiltonian, not toroids)
- Omega- symmetric tension: all three arms identical → coherent release
  → explains doubled gc term in omega rule

### Cover system physical derivation (hypothesis)
- T1 = mod-30: single parallelogram toroid, Möbius twist, 24° steps
- T2 = mod-36: two toroids, figure-8 linking at 4 points, HE21 shape,
  20° steps (hypothesis — needs scan confirmation)
- T3 = mod-18: three toroids at 120°, triangular toroid, 40° steps,
  Y-junction Hamiltonian

### Winding numbers
- 6 quark winding fractions as free parameters (no lane derivation needed):
  up=19/30, down=11/30, strange=7/30, charm=23/30, bottom=13/30, top=17/30
- 21/24 prime numerators (3 prime-square exceptions: proton 7²/30,
  Xi_c+ 7²/30, Omega_b 3³/30)

### Known systematics (documented, not patched)
- Xi0/Xi- ~-4%: triangle wave extreme phase mismatch at isoceles
  vertex (two strange quarks at same residue 7)
- Omega_c* +1.67%: ssc J=3/2 omega sector
- Sigma_c+ +1.44%: geometric lambda with charm

### BARYON_CLASS changes
- Now stores (sheet, geo_sign, chirality, cover, T, rule)
- geo_factor column removed — computed by derive_geo_factor()
- 8 chirality label corrections vs naive name-matching
- 4 heavy-dominated overrides: Sigma_b+/-, Sigma_c++/0

---

## v3 — February 2026

### Empirical classification
- BARYON_CLASS lookup table with fitted geo_factors
- MAPE ALL = 0.6365%  |  free params: 2 (kappa_0, lam_s1)
- Fibonacci lambda ladder: LU × phi^n per cover depth

---

## v2 — January 2026

### Mod-30 residue arithmetic
- Sheet/geo classification from residue products
- Known issue: closed-loop Hamiltonian washes out arm contributions

---

## v1 — December 2025

### Initial framework
- Basic spinor geometry + constituent mass model
- Winding sum prime filter theorem (21/24 prime numerators)
