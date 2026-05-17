# TFFT v3 — Chapter 03: Chirality, Helicity, and the TX/TY/TZ Structure

---

## 2. Chirality and the Three Spatial Dimensions

### 2.1 Helicity Flip vs. Chirality Crossing

These are distinct topological operations with different physical costs:

**Helicity flip** — the particle re-enters its own chirality Hilbert space with
orientation inverted. Cost: zero mass, zero entanglement. The winding stays within
one chirality Hilbert space throughout. Example: photon (2×T0, same chirality,
helicity flip at inversion point — gives spin-1, zero mass, χ̂=0 by theorem).
Gluon figure-8 crossings also preserve chirality via helicity flip.

**Chirality crossing** — the particle crosses to the opposite chirality space via
an Einstein-Rosen bridge. Cost: mass, color-anticolor pairing, entanglement.
Example: W/Z boson (T4 ER bridge). Gluons are NOT T4 — they are the interior
Hamiltonian paths of T1/T2/T3 windings, the same object as the quark viewed
from inside the Y-junction.

This distinction is the origin of the massless/massive split — not the Higgs
mechanism per se, but the topological cost of crossing the chirality boundary
versus staying within it.

| Operation | Chirality space | Mass cost | Example |
|-----------|----------------|-----------|---------|
| Helicity flip | Same — orientation inverted | Zero | Photon, gluon figure-8 |
| Chirality crossing | Opposite — ER bridge | Yes | W/Z, mass generation |

---

### 2.2 TX, TY, TZ — Why Three Spatial Dimensions and Why Only One Persists **(H)**

The time string deflection produces chirality parabolas. There are two chirality
directions — left (G=+1) and right (G=−1). Each opens its own local spatial
dimension. The three observable spatial dimensions arise from this structure:

- **TX** — left-chirality parabola. Opens locally around each particle for one
  winding cycle and closes behind it. Belongs entirely to the left-chirality
  Hilbert space (G=+1). Cannot persist globally.

- **TY** — right-chirality parabola. Same: opens and closes within the
  right-chirality Hilbert space (G=−1), cycle by cycle.

- **TZ** — the dimension that both TX and TY project their spacetime curvature
  into, **continuously**, throughout every winding cycle.

The projection into TZ is not a one-time event at closure. TX and TY load TZ
with curvature at every moment during the winding:

```
TX curvature projected into TZ  →  Electric field E
TY curvature projected into TZ  →  Magnetic field B
```

The electromagnetic field is not merely a consequence of the winding geometry —
it is the active mechanism by which TX and TY continuously hold TZ open. Every
particle everywhere, at every moment, is projecting its fields into TZ.

**Why TZ never closes:**

TX and TY each belong to one chirality Hilbert space and cannot sustain themselves
globally. They open and close so fast they appear as internal degrees of freedom
(spin, chirality, polarization) from the outside. But TZ receives continuous
curvature input from *both* chirality channels simultaneously. The dual input
keeps it open. No other spatial dimension has this property.

This is why all observable physics happens in TZ. The three quarks in a baryon,
the three arms of the T3 Y-junction, the three spatial dimensions of everyday
experience — all are the geometry of TZ projected outward from the winding cycles.

**The absolute vacuum would close TZ:**

TZ stays open because TX and TY are continuously projecting fields into it.
In a true absolute vacuum — zero particles, zero winding, no fields — TZ
would receive zero curvature input and close. All three spatial dimensions
would collapse to T0: the time string alone.

This cannot happen. The same P(0) = 0 floor that prevents any winding from
fully unwinding (ZPE) also ensures TX and TY field projections into TZ never
reach zero. The three spatial dimensions and zero-point energy are the same
topological fact at different scales — both follow from P(0) = 0 being
unreachable.

```
P(0) = sin²(0) = 0  →  unreachable floor
→  ZPE (individual winding never fully unwinds)
→  TZ never closes (field projection never reaches zero)
→  Three spatial dimensions are topologically stable
```

*Full treatment including the parabola geometry, the 10D structure, and the
dimensions-as-object-properties derivation: tensor_time v7 §3.2.*

---

### 2.3 The Two Chirality Hilbert Spaces

The two chirality spaces are not arbitrary — they are forced by the topology
of the time string deflection:

```
G = +1  (push left)   →  TX opens  →  left-chirality Hilbert space
G = −1  (push right)  →  TY opens  →  right-chirality Hilbert space
```

In free propagation, G=+1 and G=−1 states do not interact. Two photon beams
crossing in vacuum do not scatter — they inhabit separate chirality spaces and
pass through each other.

The only location where both spaces share a common projection is the **84° seam
angle** on the mod-30 spinor circle (cos²(π/30) = 0.989074). At this boundary,
G=+1 and G=−1 states can exchange energy. This is the geometric origin of
the interaction vertex — absorption, emission, scattering all happen at the seam.

---

### 2.4 Consequences for the Mass Spectrum

The helicity flip / chirality crossing distinction propagates through the entire
mass spectrum:

**Massless particles** — stay within one chirality space throughout. Their winding
never pays the ER bridge cost. Photon: 2×T0, same chirality, helicity flip.
Gluons: T3 interior Hamiltonian paths, chirality preserved along the Y-junction.

**Massive fermions** — T1 Möbius winding. The 720° closure requires the winding
to cross between sheets. The boundary crossing cost IS the mass — Malus projection
P(r) accumulated at each colorless boundary traversal.

**Massive bosons (W/Z)** — T4 ER bridge, chirality crossing. The bridge cost is
the full chirality-crossing energy. Higgs is a T2 resonance at the T3 threshold;
its chirality structure is consistent with crossing but not yet formally derived
**(H — see tfft_v3_05_mass.md §5.4)**.

**Why the Higgs appears and disappears:** The Higgs resonance involves a figure-8
configuration at T2. The instability and finite lifetime are consistent with
chirality crossing at the figure-8 midpoint — opposing chiralities cannot
permanently constructively interfere. Whether the two lobes are opposing-chirality
(chirality crossing) or same-chirality with helicity flip is not yet determined
from first principles **(H)**.

---

