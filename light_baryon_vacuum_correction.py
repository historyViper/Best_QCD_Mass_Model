#!/usr/bin/env python3
"""
light_baryon_vacuum_correction.py
---------------------------------
Applies the Malus vacuum beat correction to the light baryon octet.
The correction is:
    delta = C * sin²(π/30) * Λ_QCD * (1 - k * n_strange)
where C is a fitted coefficient (nominally 1.0) and k is strangeness suppression.
We fit C to minimize MAPE, with k=0.5 as a physically motivated starting point.
"""

import math

# Constants
LAMBDA_QCD = 217.0               # MeV
SIN2_6 = math.sin(math.pi/30)**2  # 0.010926
VACUUM_BEAT_ENERGY = SIN2_6 * LAMBDA_QCD   # 2.37 MeV

# Light baryon octet data from your output (name, n_strange, current_pred, obs, current_err_pct)
# We extract pred and obs from the numbers you gave.
# Based on your J=1/2 table:
baryons = [
    ("proton",   0, 934.4, 938.272, -0.410),
    ("neutron",  0, 937.1, 939.565, -0.266),
    ("Lambda0",  1, 1121.3, 1115.683, +0.504),
    ("Sigma+",   1, 1182.5, 1189.370, -0.580),
    ("Sigma0",   1, 1187.2, 1192.642, -0.453),
    ("Sigma-",   1, 1192.2, 1197.449, -0.440),
    ("Xi0",      2, 1313.8, 1314.860, -0.083),
    ("Xi-",      2, 1320.8, 1321.710, -0.066),
]

def current_mape():
    """Compute MAPE from current errors (absolute percent)."""
    total = sum(abs(err) for _,_,_,_,err in baryons)
    return total / len(baryons)

def apply_correction(C, k=0.5):
    """
    Apply delta = C * VACUUM_BEAT_ENERGY * (1 - k * n_strange)
    to the current prediction, then recompute errors and MAPE.
    """
    new_errors = []
    for name, ns, pred, obs, _ in baryons:
        delta = C * VACUUM_BEAT_ENERGY * (1 - k * ns)
        new_pred = pred + delta
        err_pct = (new_pred - obs)/obs * 100
        new_errors.append(abs(err_pct))
    return sum(new_errors)/len(new_errors)

# Current MAPE
mape0 = current_mape()
print(f"Current MAPE (light octet): {mape0:.4f}%")

# Try to find optimal coefficient C (k=0.5)
best_C = 1.0
best_mape = mape0
for C in [c/100 for c in range(-100, 201, 5)]:  # -1.0 to 2.0 step 0.05
    m = apply_correction(C, k=0.5)
    if m < best_mape:
        best_mape = m
        best_C = C

print(f"Optimal C with k=0.5: {best_C:.2f}  ->  MAPE = {best_mape:.4f}%")

# Try k=0 (no strangeness suppression) and k=1 (full strangeness kill)
print("\nExploring different strangeness suppression factors:")
for k in [0.0, 0.5, 1.0]:
    best_Ck = 1.0
    best_mk = mape0
    for C in [c/100 for c in range(-100, 201, 5)]:
        m = apply_correction(C, k=k)
        if m < best_mk:
            best_mk = m
            best_Ck = C
    print(f"  k={k:.1f}:  best C={best_Ck:.2f}  ->  MAPE = {best_mk:.4f}%")

# For reference, the predicted delta for a nucleon with C=1.0, k=0.5:
delta_nuc = 1.0 * VACUUM_BEAT_ENERGY * (1 - 0.5*0)
print(f"\nVacuum beat energy scale: {VACUUM_BEAT_ENERGY:.2f} MeV")
print(f"With C=1.0, k=0.5, proton/neutron shift = {delta_nuc:.2f} MeV")