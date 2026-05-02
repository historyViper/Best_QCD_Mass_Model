#!/usr/bin/env python3
"""
gbp_riemann_sweep_500.py
========================
Checks the first 500 Riemann zeta zeros against the geometric ceiling n×(9π/2)

AUTHORS: HistoryViper (Jason Richardson) & Claude Sonnet 4.6
"""

import mpmath
import math
import statistics

mpmath.mp.dps = 35

PI  = mpmath.pi
NINE_PI_2 = 9 * PI / 2

GEO_B      = mpmath.sin(PI/15)**2
PHI30      = 8
OMEGA_0    = 2*PI / PHI30

print("=" * 70)
print("GBP RIEMANN SWEEP — 500 ZEROS")
print("Verifying: γ_n < n×(9π/2) always")
print("=" * 70)
print(f"\n9π/2       = {float(NINE_PI_2):.10f}")
print(f"GEO_B      = {float(GEO_B):.10f}")
print(f"ω₀ = π/4   = {float(OMEGA_0):.10f}")
print()

# ── PART 1: 500-zero signed gap sweep ─────────────────────────────────────
print("-" * 70)
print("PART 1: Signed gap  γ_n - n×(9π/2)  for n = 1..500")
print("-" * 70)
print(f"{'n':>5}  {'γ_n':>20}  {'n×9π/2':>20}  {'gap':>16}  {'gap/9π/2n':>12}  sign")
print("-" * 90)

gaps       = []
ratios     = []
all_negative = True

for n in range(1, 501):
    g         = mpmath.zetazero(n).imag
    ceiling   = n * NINE_PI_2
    gap       = float(g - ceiling)
    ratio     = float(g / ceiling)
    gaps.append(gap)
    ratios.append(ratio)

    if gap >= 0:
        all_negative = False

    sign = "-" if gap < 0 else "+"

    # Print first 20, then every 50th
    if n <= 20 or n % 50 == 0:
        print(f"{n:>5}  {float(g):>20.10f}  {float(ceiling):>20.10f}  "
              f"{gap:>16.10f}  {ratio:>12.8f}  {sign}")

print()
print(f"All 500 gaps negative (γ_n < n×9π/2): {all_negative}")

neg_count = sum(1 for g in gaps if g < 0)
pos_count = sum(1 for g in gaps if g >= 0)
print(f"Negative: {neg_count}/500,  Non-negative: {pos_count}/500")

# Find any positive gaps (violations)
violations = [(i+1, gaps[i]) for i in range(len(gaps)) if gaps[i] >= 0]
if violations:
    print(f"\n*** VIOLATIONS FOUND: {len(violations)} ***")
    for n, gap in violations:
        print(f"  n={n}: gap = {gap:.10f}")
else:
    print(f"\n*** NO VIOLATIONS - All 500 zeros below ceiling ***")

# ── PART 2: Statistics by blocks ────────────────────────────────────────
print()
print("-" * 70)
print("PART 2: Block statistics (50 zeros per block)")
print("-" * 70)

print(f"\n{'Block':>12}  {'mean ratio':>14}  {'std dev':>12}")
print("-" * 44)
for block_start in range(0, 500, 50):
    block = ratios[block_start:block_start+50]
    mean_r = statistics.mean(block)
    std_r  = statistics.stdev(block)
    print(f"  n={block_start+1:>3}–{block_start+50:<3}   {mean_r:>14.8f}  {std_r:>12.8f}")

print()
print(f"Overall mean ratio γ_n/(n×9π/2) = {statistics.mean(ratios):.8f}")
print(f"Overall std dev                  = {statistics.stdev(ratios):.8f}")
print()

# ── SUMMARY ─────────────────────────────────────────────────────────────
print("=" * 70)
print("SUMMARY")
print("=" * 70)
print(f"""
CLAIM 1 — γ_n < n×(9π/2) always:
  Negative gaps: {neg_count}/500
  Non-negative:  {pos_count}/500
  → {"CONFIRMED - All zeros below ceiling!" if neg_count == 500 else "FAILED - Violations found!"}
""")