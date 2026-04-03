## GBP v5 Updates — April 2026

### geo_factor is now derived, not fitted

Every baryon geo_factor is computed by `derive_geo_factor()` from:

```
S2[gen] = sin²(GEN_N[g] · π/15)

S2[1] = sin²(48°) = 0.552264   gen1: up/down
S2[2] = sin²(84°) = 0.989074   gen2: strange/charm
S2[3] = sin²(24°) = 0.165435   gen3: bottom/top
GEO_B = sin²(12°) = 0.043227   boundary quantum
```

MAPE ALL = 0.5% — V5 final

### Physical mechanism: Malus's Law

The geo_factor is the **Malus transmission coefficient** for spinor 
toroid boundary projection. The toroid phase rotates; the 3D observable 
boundary is a fixed polarizing filter. When phases align → maximum 
transmission. Misalignment builds tension (rubber band stretch) that 
releases at the Y-junction vertices.

sin²(θ/2) is the projection of toroid arm sweep angle θ onto the 
boundary — identical mathematics to Malus's Law in optics.

### Toroid cover system

| Cover | Mod  | Steps | Step° | Physical structure              |
|-------|------|-------|-------|---------------------------------|
| T1    | 30   | 30    | 24°   | Single parallelogram + Möbius   |
| T2    | 36   | 20    | 20°   | Two toroids, figure-8, HE21     |
| T3    | 18   | 18    | 40°   | Three toroids 120°, Y-junction  |

### Results

| Group  | MAPE    | RMSE    |
|--------|---------|---------|
| clean  | 0.8500% | 22.4 MeV |
| wide   | 0.3568% | 13.2 MeV |
| degen  | 0.2268% | 9.7 MeV  |
| J=1/2  | 0.6425% | —        |
| J=3/2  | 0.3086% | —        |
| ALL 44 | 0.4907% | 18.2 MeV |

(with Sigma+/0/- triangular toroid correction sin²(30°)=0.25)
