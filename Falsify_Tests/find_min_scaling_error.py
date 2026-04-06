#!/usr/bin/env python3
"""
Find minimum error with just the mass scaling law
E = E_ref × S2[gen] × (1 + LU × φ^k)
"""

import math
from collections import defaultdict

# Constants
GEN_N = {'gen1': 4, 'gen2': 7, 'gen3': 2}
PHI = (1 + math.sqrt(5)) / 2
GEO_B = math.sin(math.pi / 15) ** 2
ALPHA_IR = 0.848809
LU = GEO_B / ALPHA_IR

PARTICLE_MASSES = {
    'Xi_cc++': 3621.4, 'Xi_cc+': 3518.94, 'Omega_cc+': 2695.2,
    'Lambda_c+': 2286.46, 'Xi_c+': 2467.71, 'Xi_c0': 2470.44,
    'Sigma_c++': 2453.97, 'Sigma_c+': 2452.65, 'Sigma_c0': 2453.75,
    'Omega_c0': 2674.4, 'Xi_c*+': 2645.53, 'Xi_c*0': 2646.33,
    'Sigma_c*++': 2520.2, 'Sigma_c*+': 2518.8, 'Sigma_c*0': 2517.5, 'Omega_c*0': 2765.9,
    'Lambda': 1115.683, 'Sigma+': 1189.37, 'Sigma0': 1192.642, 'Sigma-': 1197.449,
    'Xi0': 1314.86, 'Xi-': 1321.71, 'Omega-': 1672.45,
    'Lambda_b0': 5620.6, 'Xi_b-': 5797.0, 'Xi_b0': 5768.4,
    'Sigma_b+': 5811.0, 'Sigma_b0': 5813.4, 'Omega_b-': 6046.0,
}

PARTICLE_FAMILIES = {
    'Lambda_c+': 'gen1', 'Sigma_c++': 'gen1', 'Sigma_c+': 'gen1', 'Sigma_c0': 'gen1',
    'Sigma_c*++': 'gen1', 'Sigma_c*+': 'gen1', 'Sigma_c*0': 'gen1',
    'Xi_c+': 'gen2', 'Xi_c0': 'gen2', 'Xi_c*+': 'gen2', 'Xi_c*0': 'gen2',
    'Omega_c0': 'gen2', 'Omega_c*0': 'gen2',
    'Xi_cc++': 'gen3', 'Xi_cc+': 'gen3', 'Omega_cc+': 'gen3',
    'Lambda': 'gen1', 'Sigma+': 'gen1', 'Sigma0': 'gen1', 'Sigma-': 'gen1',
    'Xi0': 'gen2', 'Xi-': 'gen2', 'Omega-': 'gen2',
    'Lambda_b0': 'gen1', 'Sigma_b+': 'gen1', 'Sigma_b0': 'gen1',
    'Xi_b-': 'gen2', 'Xi_b0': 'gen2', 'Omega_b-': 'gen2',
}

PARTICLE_TOPOLOGY = {
    'Lambda_c+': 1, 'Sigma_c++': 1, 'Sigma_c+': 1, 'Sigma_c0': 1,
    'Xi_c+': 2, 'Xi_c0': 2, 'Omega_c0': 3,
    'Xi_c*+': 2, 'Xi_c*0': 2, 'Omega_c*0': 3,
    'Sigma_c*++': 1, 'Sigma_c*+': 1, 'Sigma_c*0': 1,
    'Xi_cc++': 2, 'Xi_cc+': 2, 'Omega_cc+': 3,
    'Lambda': 1, 'Sigma+': 1, 'Sigma0': 1, 'Sigma-': 1,
    'Xi0': 2, 'Xi-': 2, 'Omega-': 3,
    'Lambda_b0': 1, 'Sigma_b+': 1, 'Sigma_b0': 1,
    'Xi_b-': 2, 'Xi_b0': 2, 'Omega_b-': 3,
}

def S2(gen):
    return math.sin(GEN_N[gen] * math.pi / 15) ** 2

def boundary_scale(k):
    return LU * (PHI ** k)

# Find best E_ref that minimizes overall MAPE
best_E_ref = None
best_mape = float('inf')

for E_ref in range(500, 4000, 10):
    total_error = 0
    for name in PARTICLE_MASSES:
        gen = PARTICLE_FAMILIES[name]
        k = PARTICLE_TOPOLOGY[name]
        actual = PARTICLE_MASSES[name]
        pred = E_ref * S2(gen) * (1 + boundary_scale(k))
        total_error += abs(pred - actual) / actual * 100
    
    mape = total_error / len(PARTICLE_MASSES)
    if mape < best_mape:
        best_mape = mape
        best_E_ref = E_ref

print(f"Best E_ref: {best_E_ref}")
print(f"Best MAPE: {best_mape:.2f}%")
print()

# Now show individual errors with best E_ref
print("=" * 70)
print("INDIVIDUAL ERRORS WITH OPTIMIZED E_ref")
print("=" * 70)

errors = []
for name in PARTICLE_MASSES:
    gen = PARTICLE_FAMILIES[name]
    k = PARTICLE_TOPOLOGY[name]
    actual = PARTICLE_MASSES[name]
    pred = best_E_ref * S2(gen) * (1 + boundary_scale(k))
    error = (pred - actual) / actual * 100
    errors.append((name, k, gen, actual, pred, error))

# Sort by absolute error
errors.sort(key=lambda x: abs(x[5]))

print("\nAll particles sorted by |error|:")
print(f"{'Particle':<12} {'k':<2} {'gen':<6} {'Actual':<10} {'Pred':<10} {'Error%':<10}")
print("-" * 60)
for name, k, gen, actual, pred, error in errors:
    print(f"{name:<12} {k:<2} {gen:<6} {actual:<10.1f} {pred:<10.1f} {error:+.2f}%")

# Find smallest absolute errors
print("\n" + "=" * 70)
print("TOP 10 SMALLEST ABSOLUTE ERRORS")
print("=" * 70)
for i, (name, k, gen, actual, pred, error) in enumerate(errors[:10]):
    print(f"{i+1}. {name}: {error:+.2f}%")

print("\n" + "=" * 70)
print("WORST 10 ERRORS")
print("=" * 70)
for i, (name, k, gen, actual, pred, error) in enumerate(errors[-10:]):
    print(f"{i+1}. {name}: {error:+.2f}%")
