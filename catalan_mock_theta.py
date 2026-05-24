import math
from fractions import Fraction

# ============================================================
# Catalan's Constant as a Mock Theta Euler Product
# G = (15/16) x PROD_{p in Theta_30} p^2 / (p^2 - chi_{-4}(p))
#
# Theta_30 = primes coprime to 30 = {7, 11, 13, 17, 19, 23, 29, 31, ...}
# chi_{-4}(p) = +1 if p ≡ 1 mod 4  (C1 lane)
#             = -1 if p ≡ 3 mod 4  (C2 lane)
#
# Boundary terms (p=3, p=5 outside Theta_30 core):
#   p=3: 9/10   (C2 lane)
#   p=5: 25/24  (C1 lane)
#   combined: 9/10 * 25/24 = 15/16
# ============================================================

def sieve(limit):
    is_prime = [True]*(limit+1)
    is_prime[0]=is_prime[1]=False
    for i in range(2, int(limit**0.5)+1):
        if is_prime[i]:
            for j in range(i*i, limit+1, i):
                is_prime[j]=False
    return [i for i in range(2,limit+1) if is_prime[i]]

def chi(p):
    return 1 if p % 4 == 1 else -1

def is_coprime_to_30(n):
    return math.gcd(n, 30) == 1

G_true = 0.915965594177219

primes = sieve(100000)
theta30_primes = [p for p in primes if is_coprime_to_30(p)]

# Boundary term
boundary = Fraction(15, 16)

# Build mock theta Euler product
product = Fraction(1)
print(f"G (true) = {G_true}")
print()
print(f"{'N primes':>10} | {'G approx':>18} | {'error':>12} | {'last fraction'}")
print("-"*65)

for i, p in enumerate(theta30_primes):
    c = chi(p)
    product *= Fraction(p**2, p**2 - c)
    G_approx = float(boundary * product)
    error = abs(G_approx - G_true)
    if (i+1) in [1,2,5,10,20,50,100,200,500,1000,2000]:
        frac = Fraction(p**2, p**2 - c)
        print(f"{i+1:>10} | {G_approx:>18.12f} | {error:>12.2e} | {frac}")

print()
print("Final formula (exact):")
print("G = (15/16) x PROD_{p in Theta_30} p^2 / (p^2 - chi_{-4}(p))")
print()
print("Where Theta_30 = mock theta normalization = primes coprime to 30")
print("chi_{-4} = C1/C2 chirality lane assignment from GBP vortex theorem")
