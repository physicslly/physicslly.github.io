---
title: "String Theory and the Worldsheet: Conformal Gauge and the Graviton"
date: 2026-06-24 10:00:00 +0700
categories: [Physics, String Theory]
tags: [physics, theoretical-physics, string-theory, quantum-gravity, conformal-field-theory, unification]
description: "A rigorous treatment of the worldsheet formulation of string theory."
math: true
---

## Abstract

The worldsheet formulation of string theory replaces a particle trajectory by a two-dimensional quantum field theory. The Polyakov action has worldsheet diffeomorphism and Weyl redundancy, and quantization is consistent only when that redundancy survives gauge fixing and regularization. This article asks how worldsheet gauge redundancy constrains the consistency of string quantization. I derive the stress-tensor constraints from the Polyakov action, explain conformal gauge, interpret the Virasoro constraints, and show why the bosonic critical dimension is not an arbitrary preference but a cancellation of the Weyl anomaly. The result is a useful miniature of string theory: gravity appears in the closed-string spectrum, but only after a highly constrained worldsheet quantum theory is made consistent [1], [2].

**Keywords:** string theory, Polyakov action, conformal gauge, Virasoro constraints, critical dimension, graviton

## 1. Introduction

String theory begins with a strange economy. Instead of quantizing spacetime geometry directly, it asks for a consistent two-dimensional theory of maps from a worldsheet into target spacetime. The target-space consequences are large: a closed string contains a massless spin-2 state, and its low-energy interactions reproduce general relativity.

The central technical question is this: how does worldsheet gauge redundancy constrain the consistency of string quantization? The answer runs through conformal gauge, the vanishing of the worldsheet stress tensor, the Virasoro algebra, and the cancellation of the Weyl anomaly.

The connection to [quantum gravity](/posts/quantum-gravity-clash-general-relativity-quantum-theory/) is direct but should not be overstated at the first step. The worldsheet is a two-dimensional conformal field theory, so [conformal field theory](/posts/conformal-field-theory-bootstrap-program/) is part of the basic grammar. In holographic settings the same string logic meets [AdS/CFT](/posts/adscft-holographic-duality-and-quantum-gravity/), but the present article stays with the perturbative Polyakov formulation.

## 2. Assumptions and Definitions

Consider a worldsheet $\Sigma$ with local coordinates denoted by $\sigma^a$ and intrinsic metric $g_{ab}$. The embedding fields

$$
X^\mu(\tau,\sigma)
$$

map the worldsheet into a $D$-dimensional target spacetime with metric $G_{\mu\nu}(X)$. For most of the derivation take flat target space,

$$
G_{\mu\nu}=\eta_{\mu\nu}.
$$

The Polyakov action is

$$
S_P
=
-\frac{1}{4\pi\alpha'}
\int_\Sigma d^2\sigma\,
\sqrt{-g}\,
g^{ab}
\partial_a X^\mu
\partial_b X_\mu .
$$

Term by term: $\alpha'$ sets the string length scale; $\sqrt{-g}\,d^2\sigma$ is the invariant worldsheet area element; $g^{ab}$ contracts worldsheet derivatives; the target metric contracts spacetime indices. The auxiliary metric $g_{ab}$ is not the physical spacetime metric.

The action has three relevant symmetries: target-space Poincare symmetry in flat space, worldsheet diffeomorphism invariance, and Weyl invariance

$$
g_{ab}
\mapsto
e^{2\omega(\sigma)}g_{ab}.
$$

The last two are redundancies. They remove unphysical components of $g_{ab}$ and make conformal gauge possible.

## 3. From Polyakov Action to Stress-Tensor Constraints

Varying the action with respect to $X^\mu$ gives

$$
\frac{1}{\sqrt{-g}}
\partial_a
\bigl(
\sqrt{-g}\,g^{ab}\partial_b X^\mu
\bigr)
=
0 .
$$

This is the wave equation on the worldsheet. Varying instead with respect to $g^{ab}$ defines the worldsheet stress tensor:

$$
T_{ab}
=
-\frac{4\pi}{\sqrt{-g}}
\frac{\delta S_P}{\delta g^{ab}} .
$$

For the Polyakov action,

$$
T_{ab}
=
\frac{1}{\alpha'}
\bigl[
\partial_a X^\mu\partial_b X_\mu
-
\frac{1}{2}g_{ab}g^{cd}
\partial_c X^\mu\partial_d X_\mu
\bigr].
$$

The equation of motion for the auxiliary metric is

$$
T_{ab}=0.
$$

This is the key constraint. The first term measures local stretching of the embedding in the $a$ and $b$ directions. The second subtracts the trace part. The equation says that the physical worldsheet embedding must carry no independent stress tensor after gauge redundancy is imposed.

## 4. Conformal Gauge and Virasoro Constraints

Using diffeomorphism and Weyl symmetry, one may locally set

$$
g_{ab}
=
\eta_{ab}.
$$

This is conformal gauge. The action becomes a free two-dimensional field theory,

$$
S_P
=
-\frac{1}{4\pi\alpha'}
\int d^2\sigma\,
\eta^{ab}\partial_a X^\mu\partial_b X_\mu .
$$

In light-cone coordinates

$$
\sigma^\pm
=
\tau\pm\sigma,
$$

the equations of motion are

$$
\partial_+\partial_-X^\mu=0.
$$

The stress-tensor constraints become

$$
T_{++}
=
\frac{1}{\alpha'}
\partial_+X^\mu\partial_+X_\mu
=
0,
\qquad
T_{--}
=
\frac{1}{\alpha'}
\partial_-X^\mu\partial_-X_\mu
=
0.
$$

The first constraint removes unphysical right-moving excitations. The second does the same for left-moving excitations. Together they are the classical Virasoro constraints.

For a closed string the mode expansion is

$$
X^\mu(\tau,\sigma)
=
x^\mu
+
2\alpha' p^\mu\tau
+
i\sqrt{\frac{\alpha'}{2}}
\sum_{n\neq 0}
\frac{1}{n}
\bigl(
\alpha_n^\mu e^{-in(\tau-\sigma)}
+
\tilde\alpha_n^\mu e^{-in(\tau+\sigma)}
\bigr).
$$

The Fourier modes of the stress tensor define Virasoro generators,

$$
L_m
=
\frac{1}{2}
\sum_{n\in\mathbb{Z}}
:\alpha_{m-n}\cdot\alpha_n: .
$$

The colons denote normal ordering. This is not cosmetic. Normal ordering produces the central term in the quantum algebra.

## 5. Quantum Consistency and the Critical Dimension

The Virasoro generators obey

$$
[L_m,L_n]
=
(m-n)L_{m+n}
+
\frac{c}{12}(m^3-m)\delta_{m+n,0}.
$$

For $D$ free embedding fields $X^\mu$, the matter central charge is

$$
c_{\mathrm{matter}}=D.
$$

Gauge fixing diffeomorphisms introduces the $bc$ ghost system with

$$
c_{\mathrm{ghost}}=-26.
$$

Thus

$$
c_{\mathrm{tot}}
=
c_{\mathrm{matter}}+c_{\mathrm{ghost}}
=
D-26.
$$

The Weyl anomaly vanishes only if

$$
c_{\mathrm{tot}}=0,
\qquad
D=26.
$$

Term by term, $D$ counts target-space embedding scalars; $-26$ is the ghost contribution required by gauge fixing; the sum measures the quantum failure of Weyl invariance. In the bosonic string, $D=26$ is therefore a consistency condition. Superstrings change the matter and ghost systems and lead to the critical dimension $D=10$.

## 6. Spectrum and the Graviton

The physical state conditions are

$$
(L_0-a)\lvert\psi\rangle=0,
\qquad
L_m\lvert\psi\rangle=0
\quad
m>0,
$$

with identical conditions in the right-moving sector. For the closed bosonic string,

$$
M^2
=
\frac{4}{\alpha'}
(N+\tilde N-2)
$$

with level matching

$$
N=\tilde N.
$$

At level $N=\tilde N=1$ the state

$$
\zeta_{\mu\nu}
\alpha_{-1}^\mu
\tilde\alpha_{-1}^\nu
\lvert 0;p\rangle
$$

is massless. The polarization decomposes into a symmetric traceless tensor, an antisymmetric tensor, and a scalar. The symmetric traceless part is identified as the graviton. The point is not merely that a spin-2 particle appears; its gauge redundancy and low-energy interactions match the structure expected from general relativity [3].

## 7. Consistency Checks

**Point-particle limit.** At energies much lower than the string scale, massive string modes decouple and the massless sector dominates. This recovers an effective field theory containing gravity and gauge fields.

**Residual conformal symmetry.** Even after conformal gauge, conformal transformations remain. The Virasoro constraints are precisely the generators of this residual redundancy. Physical states must be invariant under it.

**Noncritical dimension.** If $D\neq 26$ in the bosonic theory, the conformal factor becomes dynamical through Liouville theory. That is a different theory, not a harmless gauge choice.

## 8. Limitations and Open Problems

The Polyakov formulation is perturbative in the worldsheet topology expansion. Each genus contributes a term in the string coupling expansion, and a complete non-perturbative definition is not supplied by the genus series alone. Background dependence is another limitation: the worldsheet CFT is usually defined after choosing a target-space background.

Moduli integration is also essential. Fixing conformal gauge does not remove the finite-dimensional moduli of higher-genus worldsheets, and amplitudes require integration over that moduli space. Divergences can arise from degenerations of Riemann surfaces, infrared physics, or unstable backgrounds. The formal language becomes dangerous if one reads perturbative finiteness as a full non-perturbative definition of quantum gravity.

## 9. Conclusion

The worldsheet theory is a constrained two-dimensional quantum field theory. The Polyakov action makes the gauge redundancies visible. Conformal gauge makes the dynamics solvable. The Virasoro constraints identify physical states. The central-charge cancellation fixes the critical dimension. From that constrained system, the graviton emerges as a massless closed-string excitation. The route to spacetime gravity therefore runs through the consistency of a two-dimensional gauge-fixed quantum theory.

## References

[1] J. Polchinski, _String Theory, Volume 1: An Introduction to the Bosonic String_, Cambridge University Press, 1998.

[2] M. B. Green, J. H. Schwarz, and E. Witten, _Superstring Theory, Volume 1_, Cambridge University Press, 1987.

[3] T. Yoneya, "Connection of dual models to electrodynamics and gravidynamics," _Progress of Theoretical Physics_ 51, 1907-1920 (1974).

[4] P. Goddard, J. Goldstone, C. Rebbi, and C. B. Thorn, "Quantum dynamics of a massless relativistic string," _Nuclear Physics B_ 56, 109-135 (1973).

[5] P. Di Francesco, P. Mathieu, and D. Senechal, _Conformal Field Theory_, Springer, 1997.
