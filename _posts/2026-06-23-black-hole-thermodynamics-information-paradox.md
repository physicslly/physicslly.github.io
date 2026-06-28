---
title: "Black Hole Thermodynamics and the Information Paradox"
date: 2026-06-23 21:00:00 +0700
categories: [Physics, Quantum Gravity]
tags: [physics, theoretical-physics, general-relativity, quantum-gravity, black-holes, information-paradox, thermodynamics]
description: "A rigorous treatment of black hole thermodynamics: the four laws, Hawking radiation via Bogoliubov transformation, Bekenstein-Hawking entropy, the information paradox, Page curve, replica wormholes, and implications for a theory of quantum gravity."
math: true
---

## Abstract

Black holes behave like thermodynamic systems because horizons hide information and quantum fields respond to curved causal structure. The classical laws of black hole mechanics become physical thermodynamics only after Hawking radiation assigns a temperature to the horizon. This article asks why a classical horizon behaves like a thermodynamic system. I review surface gravity, temperature, entropy, the first law, evaporation, and the information paradox, then identify the assumptions behind semiclassical gravity. The unresolved parts are not small: trans-Planckian sensitivity, backreaction, Page curves, firewalls, and non-perturbative quantum gravity remain central [1], [2].

**Keywords:** black holes, Hawking radiation, entropy, surface gravity, information paradox, Page curve

## 1. Introduction

The central question is this: why does a classical horizon behave like a thermodynamic system? Classically, a black hole absorbs but does not emit. Quantum fields on a black hole background change that conclusion: the horizon has a temperature.

The geometric background is [General Relativity](/posts/general-relativity-geometry-spacetime/), especially causal horizons from [Causal Structure and Singularity Theorems](/posts/causal-structure-singularity-theorems/). The deeper issue belongs to [Quantum Gravity](/posts/quantum-gravity-clash-general-relativity-quantum-theory/). Entanglement gives a complementary language in [Entanglement Entropy in QFT and Holography](/posts/entanglement-entropy-qft-holography/).

## 2. Surface Gravity and Temperature

For a Schwarzschild black hole,

$$
ds^2
=
-\left(1-\frac{2GM}{r}\right)dt^2
+
\frac{dr^2}{1-2GM/r}
+
r^2d\Omega^2.
$$

The horizon is at

$$
r_s=2GM.
$$

The surface gravity is

$$
\kappa
=
\frac{1}{4GM}.
$$

Hawking's result is

$$
T_H
=
\frac{\kappa}{2\pi}
=
\frac{1}{8\pi GM}.
$$

The first equality is general for stationary horizons. The second is the Schwarzschild value. The inverse dependence on $M$ means smaller black holes are hotter.

## 3. First Law and Entropy

The first law of black hole mechanics is

$$
dM
=
\frac{\kappa}{8\pi G}dA
+
\Omega dJ
+
\Phi dQ.
$$

Term by term: $dM$ is the change in mass; the area term is the horizon contribution; $\Omega dJ$ is rotational work; $\Phi dQ$ is electromagnetic work. Comparing with thermodynamics,

$$
dE=TdS+\text{work},
$$

and using $T=\kappa/2\pi$, one obtains

$$
S_{\mathrm{BH}}
=
\frac{A}{4G}.
$$

The entropy scales with area, not volume. That is the first strong hint that quantum gravity does not count degrees of freedom like ordinary local QFT.

## 4. Evaporation and the Paradox

Hawking radiation causes mass loss. A black hole formed from a pure state appears to evaporate into nearly thermal radiation. If evaporation is complete and the radiation is exactly thermal, pure states evolve into mixed states, violating unitary quantum mechanics [3].

The Page curve is the expected entropy curve for unitary evaporation: radiation entropy rises at first, then falls after the Page time. Semiclassical Hawking calculation gives only the rising part unless new correlations or gravitational saddles are included.

## 5. Consistency Checks

**Classical limit.** As $G$ is fixed and $M$ becomes large, $T_H$ becomes small. Large black holes are cold, matching semiclassical intuition.

**Area theorem.** Classically, under suitable energy conditions, horizon area does not decrease. This parallels the second law before quantum evaporation is included.

**Thermal spectrum.** Near-horizon redshift gives a universal thermal factor independent of details of the collapsing matter.

## 6. Limitations and Open Problems

The Hawking derivation uses modes that, traced backward, can become trans-Planckian. Backreaction is difficult beyond approximations. The Page curve suggests unitary evaporation, but the microscopic mechanism depends on the quantum gravity framework. Firewall arguments show that unitarity, smooth horizons, and ordinary effective field theory cannot all be naively maintained. Replica wormholes and islands represent major progress, but a complete real-time microscopic account remains difficult.

## 7. Conclusion

Black hole thermodynamics is not an analogy that survived by luck. Surface gravity becomes temperature, horizon area becomes entropy, and evaporation forces the information problem. The paradox is valuable because it is precise: it tells us exactly where semiclassical gravity and ordinary quantum reasoning strain each other.

## References

[1] J. D. Bekenstein, "Black holes and entropy," _Physical Review D_ 7, 2333-2346 (1973).

[2] S. W. Hawking, "Particle creation by black holes," _Communications in Mathematical Physics_ 43, 199-220 (1975).

[3] S. W. Hawking, "Breakdown of predictability in gravitational collapse," _Physical Review D_ 14, 2460-2473 (1976).

[4] D. N. Page, "Information in black hole radiation," _Physical Review Letters_ 71, 3743-3746 (1993).

[5] A. Almheiri, N. Engelhardt, D. Marolf, and H. Maxfield, "The entropy of bulk quantum fields and the entanglement wedge of an evaporating black hole," _Journal of High Energy Physics_ 2019, 63 (2019).
