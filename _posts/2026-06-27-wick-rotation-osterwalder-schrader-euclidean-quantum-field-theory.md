---
title: "Wick Rotation and the Osterwalder-Schrader Axioms: Rigorous Foundations of the Euclidean Path Integral"
date: 2026-06-27 00:01:00 +0800
categories: [Physics, Quantum Field Theory]
tags: [physics, theoretical-physics, quantum-field-theory, wick-rotation, euclidean-field-theory, osterwalder-schrader, path-integral, axiomatic-field-theory]
description: "A rigorous treatment of Wick rotation and the Osterwalder-Schrader reconstruction theorem: from Minkowski path integrals to Euclidean quantum field theory, with emphasis on the analytic continuation of correlation functions, regularity axioms, and the role of Euclidean methods in non-perturbative physics."
math: true
---

## Abstract

**Keywords:** Wick rotation, Euclidean quantum field theory, Osterwalder-Schrader axioms, path integral, analytic continuation, reconstruction theorem

The Euclidean path integral is the central computational tool in modern quantum field theory, yet its mathematical status is more subtle than its Minkowski counterpart. In this article, we develop the rigorous foundations of Euclidean quantum field theory. We begin with the formal manipulation of the time coordinate that relates the two signatures, then give a precise statement of the Osterwalder-Schrader axioms that a Euclidean correlation function must satisfy in order to reconstruct a physical, unitary Minkowski theory. We examine the regularity, Euclidean covariance, reflection positivity, and symmetry conditions in detail, and we discuss the role of Euclidean methods in lattice gauge theory, instanton physics, and the search for a non-perturbative definition of quantum gravity.

## 1. Introduction

The Feynman path integral is one of the most powerful conceptual and computational tools in quantum physics. In its Minkowski form, it expresses transition amplitudes as sums over histories weighted by the complex phase $\exp(iS/\hbar)$, where $S$ is the classical action. Direct evaluation of such an integral is difficult because the integrand oscillates rapidly.

A standard formal maneuver, the Wick rotation, replaces the time coordinate $t$ by imaginary time $\tau = it$. This converts the oscillatory weight into a real, positive-definite Boltzmann-like factor $e^{-S_{\mathrm{E}}/\hbar}$, where $S_{\mathrm{E}}$ denotes the Euclidean action.

On a formal level, this rotation is familiar to every graduate student. On a rigorous level, it raises deep questions. Under what conditions does a Euclidean correlation function correspond to a physically acceptable Minkowski quantum field theory? What axioms must the Euclidean correlators satisfy so that the reconstructed theory obeys unitarity, locality, and the spectral condition? The answer is provided by the Osterwalder-Schrader reconstruction theorem, which gives a precise dictionary between Euclidean and Minkowski descriptions.

This article develops the theory of Wick rotation and the Osterwalder-Schrader axioms at a level suitable for a reader with graduate training in quantum field theory and functional analysis.

## 2. The Minkowski Path Integral: Formal Setup

Consider a single scalar field $\phi$ in $d$-dimensional Minkowski spacetime with classical action

$$
S[\phi]
=
\int d^{d}x\,
\Bigl(
\frac{1}{2}\partial_{\mu}\phi\,\partial^{\mu}\phi
-
\frac{1}{2}m^{2}\phi^{2}
-
V(\phi)
\Bigr),
$$

where $V(\phi)$ is a local potential and the metric signature is $(+,-,\dots,-)$. The formal path integral expression for the vacuum-to-vacuum transition amplitude in the presence of a source $J(x)$ is

$$
Z[J]
=
\int \mathcal{D}\phi\,
\exp\!\Bigl(
\frac{i}{\hbar}\bigl(S[\phi] + \int d^{d}x\,J(x)\phi(x)\bigr)
\Bigr).
$$

Correlation functions are obtained by functional differentiation:

$$
\langle 0\lvert T\{\phi(x_{1})\cdots\phi(x_{n})\}\rvert 0\rangle
=
\frac{1}{Z[0]}
\left.\frac{\delta^{n}Z[J]}{\delta J(x_{1})\cdots\delta J(x_{n})}\right|_{J=0}.
$$

The difficulty with the Minkowski path integral is that the integrand is a pure phase. The measure $\mathcal{D}\phi$ is not a well-defined Lebesgue-type measure on an infinite-dimensional space, and the oscillatory integral does not converge absolutely. The Wick rotation is the standard way to give the integral a better chance of being well defined.

## 3. Wick Rotation: Formal Manipulation

The Wick rotation consists of the substitution

$$
t = -i\tau,
\qquad
\tau \in \mathbb{R},
$$

or equivalently $x^{0} = -i x^{d}$, so that the Minkowski metric becomes the Euclidean metric. Under this change, the derivative transforms as

$$
\partial_{0}
=
\frac{\partial}{\partial t}
=
i\frac{\partial}{\partial \tau}
=
i\partial_{\tau},
$$

and the Minkowski kinetic term becomes the Euclidean kinetic term:

$$
\frac{1}{2}\partial_{\mu}\phi\,\partial^{\mu}\phi
\;\longrightarrow\;
\frac{1}{2}\Bigl(
(\partial_{\tau}\phi)^{2}
+
\nabla\phi\cdot\nabla\phi
\Bigr).
$$

The Euclidean action $S_{\mathrm{E}}[\phi]$ is defined by the relation

$$
iS[\phi]
=
-S_{\mathrm{E}}[\phi],
$$

so that for the scalar theory above,

$$
S_{\mathrm{E}}[\phi]
=
\int d^{d}x_{\mathrm{E}}\,
\Bigl(
\frac{1}{2}(\partial_{\tau}\phi)^{2}
+
\frac{1}{2}\nabla\phi\cdot\nabla\phi
+
\frac{1}{2}m^{2}\phi^{2}
+
V(\phi)
\Bigr),
$$

where $d^{d}x_{\mathrm{E}} = d\tau\,d^{d-1}x$ is the Euclidean volume element. The Euclidean generating functional is

$$
Z_{\mathrm{E}}[J]
=
\int \mathcal{D}\phi\,
\exp\!\Bigl(
-\frac{1}{\hbar}\bigl(
S_{\mathrm{E}}[\phi]
+
\int d^{d}x_{\mathrm{E}}\,J(x)\phi(x)
\bigr)
\Bigr).
$$

The crucial difference is the sign: the Euclidean integrand is a real, positive-definite weight when the Euclidean action is non-negative. This makes the Euclidean path integral amenable to probabilistic interpretation and rigorous measure-theoretic analysis.

## 4. Analytic Continuation of Correlation Functions

The formal manipulation above is only a heuristic. The rigorous content is captured by the analytic continuation of correlation functions. One begins with the Wightman functions, which are the vacuum expectation values of field operators in the Minkowski theory:

$$
W_{n}(x_{1},\dots,x_{n})
=
\langle 0\lvert \phi(x_{1})\cdots\phi(x_{n})\rvert 0\rangle.
$$

These are boundary values of functions analytic in a complex domain called the tube. The key insight of Osterwalder and Schrader is that the Wightman functions, when restricted to spacelike-separated points, coincide with the expectation values of a Euclidean field theory. More precisely, there exists a family of Euclidean correlation functions

$$
S_{n}(x_{1}^{\mathrm{E}},\dots,x_{n}^{\mathrm{E}})
=
\int \mathcal{D}\phi\,
\phi(x_{1}^{\mathrm{E}})\cdots\phi(x_{n}^{\mathrm{E}})
\,e^{-S_{\mathrm{E}}[\phi]/\hbar},
$$

that are the analytic continuations of the Wightman functions to imaginary times. The reconstruction theorem states that, given a set of Euclidean correlators satisfying certain axioms, one can reconstruct a unique, unitary Minkowski quantum field theory whose Wightman functions are the analytic continuations.

## 5. The Osterwalder-Schrader Axioms

We now state the axioms that a set of Euclidean correlation functions $S_{n}$ must satisfy. Let $\mathcal{S}(\mathbb{R}^{d})$ denote the Schwartz space of rapidly decreasing test functions on $\mathbb{R}^{d}$, and let $\mathcal{S}'(\mathbb{R}^{d})$ be the space of tempered distributions.

**Axiom 1 (Regularity).** The Euclidean correlators $S_{n}$ are tempered distributions on $\mathbb{R}^{nd}$:

$$
S_{n} \in \mathcal{S}'(\mathbb{R}^{nd}),
$$

and they are symmetric under permutations of their arguments.

**Axiom 2 (Euclidean covariance).** For any Euclidean isometry $(R,a) \in \mathrm{ISO}(d)$, the correlation functions transform as

$$
S_{n}(Rx_{1}+a,\dots,Rx_{n}+a)
=
S_{n}(x_{1},\dots,x_{n}).
$$

This axiom encodes the invariance of the Euclidean theory under rotations and translations.

**Axiom 3 (Reflection positivity).** This is the central axiom. Let $\theta$ denote the reflection of the Euclidean time coordinate, so that $\theta$ reverses the sign of the time coordinate. For any finite linear combination

$$
f
=
\sum_{m,n} c_{m,n}
\int d^{d}x_{1}^{\mathrm{E}}\cdots d^{d}x_{m}^{\mathrm{E}}\,
f_{m,n}(x_{1}^{\mathrm{E}},\dots,x_{m}^{\mathrm{E}})
\,
\phi(x_{1}^{\mathrm{E}})\cdots\phi(x_{m}^{\mathrm{E}}),
$$

where the test functions $f_{m,n}$ have support in the region of positive Euclidean time, one requires

$$
\langle \theta f,\, f\rangle
\geq
0,
$$

where $\langle f,g\rangle$ denotes the Euclidean expectation value. Reflection positivity is the Euclidean counterpart of the positivity of the Hilbert space inner product in the Minkowski theory. It guarantees that the reconstructed theory has a positive-definite Hilbert space and a Hamiltonian bounded below.

**Axiom 4 (Symmetry).** If the classical action is invariant under a group of internal symmetries, the Euclidean correlators are required to be invariant as well. For a $\mathbb{Z}_{2}$-symmetric scalar theory with $V(\phi) = V(-\phi)$, one requires

$$
S_{n}(x_{1},\dots,x_{n})
=
(-1)^{n}\,S_{n}(x_{1},\dots,x_{n}),
$$

which forces all odd-point functions to vanish.

These four axioms are sufficient for the reconstruction theorem. For fermionic fields, additional axioms encode the spin-statistics relation and the correct grading of the Hilbert space.

## 6. The Reconstruction Theorem

Given a set of Euclidean correlators $\{S_{n}\}$ satisfying the axioms above, the reconstruction theorem guarantees a unique Minkowski quantum field theory whose Wightman functions are the analytic continuations of $\{S_{n}\}$ to real times.

Reflection positivity guarantees a positive-definite inner product on the space of smeared field operators; completion yields a Hilbert space $\mathcal{H}$. Euclidean time translation defines a contraction semigroup on $\mathcal{H}$, which by the Hille-Yosida theorem generates a positive self-adjoint Hamiltonian $H$. Euclidean covariance guarantees that the full Poincaré group acts on $\mathcal{H}$ after analytic continuation. Locality of the Minkowski theory follows from the symmetry of the Euclidean correlators under permutations of spacelike-separated points.

## 7. Applications to Scalar Field Theory

Consider the Euclidean $\phi^{4}$ theory in four dimensions, with Euclidean action

$$
S_{\mathrm{E}}[\phi]
=
\int d^{4}x_{\mathrm{E}}\,
\Bigl(
\frac{1}{2}(\partial_{\mu}\phi)^{2}
+
\frac{1}{2}m^{2}\phi^{2}
+
\frac{\lambda}{4!}\phi^{4}
\Bigr),
$$

where $\lambda > 0$ for stability. The Euclidean correlators are defined by the formal measure

$$
d\mu(\phi)
=
\frac{1}{Z_{\mathrm{E}}[0]}\,e^{-S_{\mathrm{E}}[\phi]/\hbar}\,\mathcal{D}\phi.
$$

For $d=2$ and $d=3$, the measure can be constructed rigorously as a probability measure on $\mathcal{S}'(\mathbb{R}^{d})$ using the methods of constructive quantum field theory. The Osterwalder-Schrader axioms have been verified in these dimensions. For $d=4$, the theory is super-renormalizable only at the level of perturbation theory; a non-perturbative construction remains an open problem, closely related to the problem of triviality.

The two-point function in the free theory is the Green's function of the Euclidean Klein-Gordon operator:

$$
S_{2}(x^{\mathrm{E}})
=
\int \frac{d^{d}p}{(2\pi)^{d}}\,
\frac{e^{ip\cdot x^{\mathrm{E}}}}{p^{2} + m^{2}}.
$$

This is a positive-definite function, and its Fourier transform is supported on the mass shell $p^{2} = -m^{2}$ in Minkowski space, consistent with the spectral condition.

## 8. Euclidean Methods in Non-Perturbative Physics

The Euclidean formulation is not merely a formal trick; it is the natural setting for several non-perturbative phenomena.

**Lattice gauge theory.** The Wilson formulation of lattice gauge theory is defined in Euclidean spacetime. The lattice path integral is a finite-dimensional integral that satisfies reflection positivity by construction, and the continuum limit is taken while preserving the Osterwalder-Schrader axioms. This is the primary tool for the non-perturbative study of quantum chromodynamics.

**Instantons and tunneling.** In non-Abelian gauge theories, the Euclidean action admits finite-action solutions, instantons, that describe quantum tunneling between topologically distinct vacua. The instanton contribution is weighted by $e^{-S_{\mathrm{inst}}/\hbar}$, where $S_{\mathrm{inst}}$ is the Euclidean action of the instanton solution. These effects are invisible in perturbation theory.

**Thermal field theory.** The Euclidean path integral on a manifold with compact Euclidean time describes a quantum system at temperature $T = 1/\beta$. The thermal partition function is

$$
Z(\beta)
=
\mathrm{Tr}\,e^{-\beta H}
=
\int_{\mathrm{periodic}} \mathcal{D}\phi\,
e^{-S_{\mathrm{E}}[\phi]/\hbar},
$$

where the path integral is taken over fields periodic in Euclidean time with period $\beta = 1/T$. This connection between Euclidean geometry and thermodynamics is one of the deepest insights of quantum field theory.

## 9. Relation to the Theory of Everything

The Euclidean path integral plays a central role in several approaches to a Theory of Everything. In quantum gravity, the Hartle-Hawking proposal for the wave function of the universe is expressed as a path integral over compact four-geometries:

$$
\Psi[h_{ij}]
=
\int \mathcal{D}g\,
e^{-S_{\mathrm{E}}[g]/\hbar},
$$

where $h_{ij}$ is the induced metric on a spatial hypersurface and the integral is over compact Euclidean four-manifolds that bound $h_{ij}$. This proposal replaces the initial singularity of the Big Bang with a smooth, finite Euclidean geometry.

In string theory, the worldsheet formulation is naturally Euclidean, and the Osterwalder-Schrader axioms apply to the worldsheet conformal field theory. The consistency of the string perturbation theory depends on the reflection positivity of the worldsheet theory.

A complete Theory of Everything would require a non-perturbative definition of the path integral for quantum gravity, including a resolution of the conformal factor problem and the unboundedness of the Euclidean Einstein action. These remain open problems at the frontier of quantum gravity research.

## 10. Common Pitfalls

Several confusions arise in the study of Wick rotation and Euclidean field theory.

**Pitfall 1: Treating the Wick rotation as a theorem.** The Wick rotation is a formal manipulation. The rigorous content is the Osterwalder-Schrader reconstruction theorem, which gives precise conditions under which the rotation is justified.

**Pitfall 2: Ignoring reflection positivity.** Reflection positivity is the Euclidean counterpart of unitarity. A Euclidean theory that violates reflection positivity does not correspond to a physical quantum theory. In gauge theories, the Faddeev-Popov procedure must preserve reflection positivity.

**Pitfall 3: Confusing Euclidean and Minkowski correlators.** The Euclidean correlators are not simply the Minkowski correlators evaluated at imaginary time. They are boundary values of analytic functions, and the analytic continuation must respect the $i\epsilon$ prescription.

**Pitfall 4: Assuming the Euclidean path integral is always well defined.** The Euclidean path integral is better behaved than the Minkowski one, but it is not automatically rigorous. The measure $\mathcal{D}\phi$ is still a formal object.

## 11. Conclusion

The Osterwalder-Schrader reconstruction theorem provides the rigorous foundation for the Euclidean path integral. The theorem guarantees that a Euclidean correlation function satisfying the axioms of regularity, Euclidean covariance, reflection positivity, and symmetry corresponds to a unique, unitary Minkowski quantum field theory. This result justifies the use of Euclidean methods in perturbative and non-perturbative quantum field theory, from lattice gauge theory to instanton physics to thermal field theory. The Euclidean formulation also plays a central role in candidate Theories of Everything, including quantum gravity and string theory, where the path integral over Euclidean geometries offers a promising approach to the non-perturbative definition of these theories.

## References

[1] K. Osterwalder and R. Schrader, _Axioms for Euclidean Green's Functions I & II_, Communications in Mathematical Physics 31 (1973) 83–112 and 42 (1975) 281–305.

[2] J. Glimm and A. Jaffe, _Quantum Physics: A Functional Integral Point of View_, Springer, 2nd edition, 1987.

[3] R. F. Streater and A. S. Wightman, _PCT, Spin and Statistics, and All That_, Princeton University Press, revised edition, 2000.

[4] G. Parisi, _Statistical Field Theory_, Addison-Wesley, 1988.

[5] M. E. Peskin and D. V. Schroeder, _An Introduction to Quantum Field Theory_, Westview Press, 1995.

[6] K. Wilson and J. Kogut, _The Renormalization Group and the ε Expansion_, Physics Reports 12 (1974) 75–199.

[7] J. B. Hartle and S. W. Hawking, _Wave Function of the Universe_, Physical Review D 28 (1983) 2960–2975.

[8] J. Polchinski, _String Theory_, Cambridge University Press, 1998.
