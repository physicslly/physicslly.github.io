---
title: "Causal Structure, Penrose Diagrams, and the Singularity Theorems of Hawking and Penrose"
date: 2026-06-24 12:00:00 +0700
categories: [Physics, General Relativity]
tags: [physics, theoretical-physics, general-relativity, causality, black-holes, cosmology, singularity-theorems]
description: "A rigorous geometric treatment of causal structure in general relativity: conformal compactification, Penrose diagrams, global hyperbolicity, the Raychaudhuri equation, the focusing theorem, and the Penrose-Hawking singularity theorems."
math: true
---

## Abstract

The singularity theorems do not say that curvature must literally become infinite. They prove a sharper and more geometric statement: under specific causal and energy assumptions, spacetime cannot be geodesically complete. This article asks what assumptions force spacetime to become geodesically incomplete. I define causal futures, Cauchy surfaces, trapped surfaces, conjugate points, and geodesic incompleteness, then derive the focusing result from the Raychaudhuri equation. The Penrose theorem is presented as the cleanest example: a trapped surface plus null energy and global assumptions force incomplete null geodesics. The limitations are equally important, because quantum fields, inflation, cosmic censorship, and semiclassical gravity all stress the classical hypotheses [1], [2].

**Keywords:** causal structure, geodesic incompleteness, Raychaudhuri equation, trapped surfaces, singularity theorems, energy conditions

## 1. Introduction

General relativity predicts situations in which its own classical description becomes incomplete. The modern content of that statement is not merely that some symmetric solutions have curvature blowups. The Hawking-Penrose theorems show that incompleteness follows from causal structure, focusing, and energy conditions.

The central question is this: what assumptions force spacetime to become geodesically incomplete? Answering it requires care. A singularity in the theorem is not a point in spacetime. It is a failure of timelike or null geodesics to extend to arbitrary affine parameter.

The background geometry belongs to [general relativity](/posts/general-relativity-geometry-spacetime/). The failure of classical spacetime points toward [quantum gravity](/posts/quantum-gravity-clash-general-relativity-quantum-theory/). Cosmological applications connect to [inflation and the early universe](/posts/cosmology-inflation-early-universe/), while horizon entropy and quantum corrections connect naturally to [entanglement entropy](/posts/entanglement-entropy-qft-holography/).

## 2. Assumptions and Definitions

Let $(M,g_{\mu\nu})$ be a time-oriented Lorentzian manifold with signature $(-,+,+,+)$. A tangent vector $v^\mu$ is timelike, null, or spacelike according as

$$
g_{\mu\nu}v^\mu v^\nu
<0,
\qquad
=0,
\qquad
>0 .
$$

The chronological future of $p$ is

$$
I^+(p)
=
\{q\in M:\text{there is a future-directed timelike curve from }p\text{ to }q\}.
$$

The causal future $J^+(p)$ is defined the same way but allows null curves. A Cauchy surface is a hypersurface intersected exactly once by every inextendible causal curve. A spacetime is globally hyperbolic if it admits such a surface.

A null geodesic with tangent $k^\mu$ is affinely parametrized if

$$
k^\nu\nabla_\nu k^\mu=0.
$$

It is complete if its affine parameter can be extended to all real values. Geodesic incompleteness means this extension fails.

A conjugate point along a geodesic is a point where neighboring geodesics in a congruence focus. In the singularity theorems, conjugate points are the geometric mechanism that prevents certain null generators from remaining on causal boundaries.

## 3. Energy Conditions and Trapped Surfaces

The null energy condition is

$$
T_{\mu\nu}k^\mu k^\nu\ge 0
$$

for every null vector $k^\mu$. Using Einstein's equation, this implies

$$
R_{\mu\nu}k^\mu k^\nu\ge 0
$$

when the cosmological constant term drops out by null contraction.

A closed trapped surface is a compact spacelike two-surface for which both future-directed null normal congruences have negative expansion:

$$
\theta_{(\ell)}<0,
\qquad
\theta_{(n)}<0.
$$

The interpretation is severe. Even the outgoing light rays are converging. In a Schwarzschild black hole, round spheres inside the event horizon are trapped.

## 4. Raychaudhuri Equation

For a null geodesic congruence with tangent $k^\mu$, decompose the transverse derivative into expansion, shear, and twist. The Raychaudhuri equation is

$$
\frac{d\theta}{d\lambda}
=
-\frac{1}{2}\theta^2
-
\sigma_{\mu\nu}\sigma^{\mu\nu}
+
\omega_{\mu\nu}\omega^{\mu\nu}
-
R_{\mu\nu}k^\mu k^\nu .
$$

Term by term: $\theta$ measures the fractional rate of change of the cross-sectional area of the congruence; the shear term distorts the bundle and is nonnegative before the minus sign; the twist term measures rotation and can oppose focusing; the Ricci term couples matter to convergence through Einstein's equation.

For hypersurface-orthogonal null congruences, the twist vanishes:

$$
\omega_{\mu\nu}=0.
$$

If the null energy condition holds, then

$$
\frac{d\theta}{d\lambda}
\le
-\frac{1}{2}\theta^2.
$$

Integrating this inequality gives

$$
\theta(\lambda)
\le
\frac{\theta_0}{1+\theta_0\lambda/2}
$$

for initial expansion $\theta_0<0$. Thus $\theta$ diverges to negative infinity within affine parameter

$$
\lambda
\le
\frac{2}{|\theta_0|}.
$$

This is the focusing theorem. It is the engine inside the singularity theorems.

## 5. Penrose Singularity Theorem

A standard form of Penrose's theorem is the following [1]. Let $(M,g)$ be globally hyperbolic with a noncompact Cauchy surface. Suppose the null energy condition holds and there exists a closed trapped surface. Then the spacetime is null geodesically incomplete.

The proof has a clean structure. The trapped surface makes both future null expansions negative. Raychaudhuri focusing then forces conjugate points along the null geodesics orthogonal to the surface within finite affine parameter. But the boundary of the future of a compact trapped surface is generated by null geodesics without conjugate points. If the spacetime were null complete, the causal boundary would have the wrong compactness properties relative to the noncompact Cauchy surface. The contradiction forces incomplete null geodesics.

The important point is what the theorem does not say. It does not identify a point called "the singularity." It proves that the manifold description cannot be extended along at least one null geodesic while preserving the assumptions.

## 6. Hawking Cosmological Theorem

Hawking's cosmological theorem uses timelike congruences and the strong energy condition. In an expanding universe, run the timelike geodesics backward. If gravity is attractive in the required sense, the congruence focuses in finite proper time, producing past timelike geodesic incompleteness [2].

For a flat FRW metric,

$$
ds^2
=
-dt^2+a(t)^2d\mathbf{x}^2,
$$

the expansion is

$$
\theta
=
3\frac{\dot a}{a}
=
3H.
$$

For ordinary matter satisfying the strong energy condition, the backward evolution focuses. Inflation evades the simple conclusion by violating the strong energy condition; it does not automatically remove every past-incompleteness issue.

## 7. Consistency Checks

**Minkowski spacetime.** It is geodesically complete and has no trapped surfaces. The theorem does not apply, as it should not.

**Schwarzschild interior.** Spheres with $r<2GM$ are trapped. The Penrose theorem predicts null incompleteness, consistent with the $r=0$ singularity of the maximally extended solution.

**de Sitter spacetime.** Classical de Sitter violates the strong energy condition. This explains why Hawking's cosmological theorem cannot be applied in its simplest form.

**Plane waves.** Certain plane-wave spacetimes evade generic focusing assumptions. They are useful reminders that the hypotheses are not decorative.

## 8. Limitations and Open Problems

Energy conditions are classical. Quantum fields can violate pointwise energy conditions, although quantum energy inequalities restrict the duration and magnitude of violations. Semiclassical gravity replaces the classical stress tensor by an expectation value, and the singularity theorems require reformulation.

Cosmic censorship remains open. The theorems imply incompleteness under assumptions; they do not prove that singularities are hidden behind horizons. They also do not classify the singularity as curvature blowup, Cauchy-horizon pathology, or something else.

Quantum gravity is expected to change the conclusion near Planckian curvature. The open problem is not whether classical GR is incomplete; the theorems already tell us that. The problem is what replaces the incomplete classical spacetime.

## 9. Conclusion

Causal structure gives singularity theorems their force. Raychaudhuri's equation converts energy conditions into focusing. Trapped surfaces supply negative expansion. Global assumptions turn focusing into a contradiction with geodesic completeness. The result is not a detailed model of a singular region, but a rigorous diagnosis: under the stated assumptions, classical spacetime cannot be extended indefinitely along all causal geodesics.

## References

[1] R. Penrose, "Gravitational collapse and space-time singularities," _Physical Review Letters_ 14, 57-59 (1965).

[2] S. W. Hawking and R. Penrose, "The singularities of gravitational collapse and cosmology," _Proceedings of the Royal Society A_ 314, 529-548 (1970).

[3] S. W. Hawking and G. F. R. Ellis, _The Large Scale Structure of Space-Time_, Cambridge University Press, 1973.

[4] R. M. Wald, _General Relativity_, University of Chicago Press, 1984.

[5] E. Poisson, _A Relativist's Toolkit_, Cambridge University Press, 2004.

[6] E. Witten, "Light rays, singularities, and all that," _Reviews of Modern Physics_ 92, 045004 (2020).
