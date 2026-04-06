#!/usr/bin/env python3
"""
Check error consistency by OCTET vs DECUPLET
============================================
Octet (spin-1/2): Λ, Σ, Ξ, Σ, Ξ, Ω
Decuplet (spin-3/2): Δ, Σ*, Ξ*, Ω*

These are the two lightest baryon multiplets in QCD!
"""

import math
from collections import defaultdict
import statistics

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

# ASSIGN PARTICLES TO OCTET OR DECUPLET
# Octet = spin-1/2, Decuplet = spin-3/2
# Distinguished by * in name (Σ*, Ξ*, Ω*) or specific states

PARTICLE_MULTIPLET = {
    # OCTET (spin-1/2)
    'Lambda': 'octet',
    'Sigma+': 'octet', 'Sigma0': 'octet', 'Sigma-': 'octet',
    'Xi0': 'octet', 'Xi-': 'octet',
    'Lambda_c+': 'octet',
    'Sigma_c++': 'octet', 'Sigma_c+': 'octet', 'Sigma_c0': 'octet',
    'Xi_c+': 'octet', 'Xi_c0': 'octet',
    'Lambda_b0': 'octet',
    'Sigma_b+': 'octet', 'Sigma_b0': 'octet',
    'Xi_b0': 'octet', 'Xi_b-': 'octet',
    
    # DECUPLET (spin-3/2)
    'Omega-': 'decuplet',
    'Xi_c*+': 'decuplet', 'Xi_c*0': 'decuplet',
    'Omega_c0': 'decuplet',
    'Sigma_c*++': 'decuplet', 'Sigma_c*+': 'decuplet', 'Sigma_c*0': 'decuplet',
    'Omega_c*0': 'decuplet',
    'Omega_b-': 'decuplet',
    
    # Doubly heavy (special - could be either or neither)
    'Xi_cc++': 'heavy', 'Xi_cc+': 'heavy', 'Omega_cc+': 'heavy',
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

E_ref = 2200

print("=" * 70)
print("OCTET vs DECUPLET ANALYSIS")
print("=" * 70)
print("\nOctet: spin-1/2 baryons (Λ, Σ, Ξ)")
print("Decuplet: spin-3/2 baryons (Δ, Σ*, Ξ*, Ω*)")

# Analyze by MULTIPLET
print("\n" + "=" * 70)
print("BY MULTIPLET (OCTET vs DECUPLET)")
print("=" * 70)

multiplet_errors = defaultdict(list)
for name in PARTICLE_MASSES:
    if name in PARTICLE_MULTIPLET:
        mult = PARTICLE_MULTIPLET[name]
        if mult in ['octet', 'decuplet']:
            gen = PARTICLE_FAMILIES[name]
            k = PARTICLE_TOPOLOGY[name]
            actual = PARTICLE_MASSES[name]
            pred = E_ref * S2(gen) * (1 + boundary_scale(k))
            error = (pred - actual) / actual * 100
            multiplet_errors[mult].append((name, k, actual, pred, error))

for mult in ['octet', 'decuplet']:
    errors = [e[4] for e in multiplet_errors[mult]]
    avg = statistics.mean(errors)
    stdev = statistics.stdev(errors) if len(errors) > 1 else 0
    spread = max(errors) - min(errors)
    
    print(f"\n{'='*50}")
    print(f"{mult.upper()}: {len(errors)} particles")
    print(f"{'='*50}")
    print(f"Errors: {[f'{e:+.1f}%' for e in sorted(errors)]}")
    print(f"Average: {avg:+.1f}%")
    print(f"Std Dev: {stdev:.1f}%")
    print(f"Spread: {spread:.1f}%")
    
    if stdev < 5:
        print(f"  ★★★ PERFECT - mass scaling is EXACTLY right for this multiplet!")
    elif stdev < 10:
        print(f"  ✓ VERY CONSISTENT - mass scaling works perfectly")
    elif stdev < 20:
        print(f"  ✓ CONSISTENT - mass scaling works")
    elif stdev < 30:
        print(f"  △ REASONABLE - some variation")
    else:
        print(f"  ✗ INCONSISTENT - mass scaling broken")

# Show details
print("\n" + "=" * 70)
print("DETAILED BREAKDOWN")
print("=" * 70)

for mult in ['octet', 'decuplet']:
    print(f"\n{mult.upper()}:")
    print(f"{'Particle':<12} {'k':<3} {'Actual':<10} {'Pred':<10} {'Error%'}")
    print("-" * 50)
    for name, k, actual, pred, error in sorted(multiplet_errors[mult], key=lambda x: x[2]):
        print(f"{name:<12} {k:<3} {actual:<10.1f} {pred:<10.1f} {error:+.1f}%")

# Analyze by (multiplet, topology)
print("\n" + "=" * 70)
print("BY (MULTIPLET, TOPOLOGY)")
print("=" * 70)

mult_k_errors = defaultdict(list)
for name in PARTICLE_MASSES:
    if name in PARTICLE_MULTIPLET:
        mult = PARTICLE_MULTIPLET[name]
        if mult in ['octet', 'decuplet']:
            gen = PARTICLE_FAMILIES[name]
            k = PARTICLE_TOPOLOGY[name]
            actual = PARTICLE_MASSES[name]
            pred = E_ref * S2(gen) * (1 + boundary_scale(k))
            error = (pred - actual) / actual * 100
            mult_k_errors[(mult, k)].append((name, error))

for (mult, k) in sorted(mult_k_errors.keys()):
    errors = [e[1] for e in mult_k_errors[(mult, k)]]
    if len(errors) > 1:
        avg = statistics.mean(errors)
        stdev = statistics.stdev(errors)
        spread = max(errors) - min(errors)
        
        status = "★★★" if stdev < 5 else "✓" if stdev < 15 else "△" if stdev < 25 else "✗"
        
        print(f"\n{mult}, k={k}: {len(errors)} particles {status}")
        print(f"  Errors: {[f'{e:+.1f}%' for e in sorted(errors)]}")
        print(f"  Avg: {avg:+.1f}%, StdDev: {stdev:.1f}%")

print("\n" + "=" * 70)
print("CONCLUSION")
print("=" * 70)

# Check which multiplet works better
octet_stdev = statistics.stdev([e[4] for e in multiplet_errors['octet']])
decuplet_stdev = statistics.stdev([e[4] for e in multiplet_errors['decuplet']])

if octet_stdev < decuplet_stdev:
    print(f"Octet works better! (stddev {octet_stdev:.1f}% vs {decuplet_stdev:.1f}%)")
else:
    print(f"Decuplet works better! (stddev {decuplet_stdev:.1f}% vs {octet_stdev:.1f}%)")

print("\nIf one multiplet is consistent and other isn't:")
print("- The consistent one has correct mass scaling")
print("- The inconsistent one needs different formula or more terms")