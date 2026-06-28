---
title: "Reflection Positivity and the Osterwalder–Schrader Axioms: Reconstructing Unitary QFT from Euclidean Correlators"
date: 2026-06-28 00:01:00 +0800
categories: [Physics, Theory]
tags: [physics, theoretical-physics, quantum-field-theory, euclidean-field-theory, reflection-positivity, osterwalder-schrader, axiomatic-qft]
description: "How reflection positivity encodes unitarity in Euclidean quantum field theory, and why the Osterwalder–Schrader reconstruction is the rigorous bridge between Euclidean correlators and a Wightman QFT."
math: true
---

## Abstract

Euclidean quantum field theory is often introduced as a computational trick: rotate to imaginary time, compute correlators by path integral, then analytically continue back. The trick works far better than a trick has any right to, and the reason is structural. The Osterwalder–Schrader axioms identify a single condition, reflection positivity, that is both necessary and sufficient for a set of Euclidean correlators to reconstruct a unitary, Lorentz-invariant Wightman quantum field theory. This article examines why reflection positivity is the Euclidean shadow of unitarity, how it enters the reconstruction theorem, and where the argument becomes formal in interacting four-dimensional theories.

**Keywords:** reflection positivity, Osterwalder–Schrader axioms, Euclidean quantum field theory, Wightman reconstruction, unitarity, analytic continuation

## 1. Introduction and Central Question

Much of modern quantum field theory is done in Euclidean signature. Critical exponents, lattice simulations, and the conformal bootstrap all live on Euclidean space, yet the physical predictions we want — scattering amplitudes, spectral densities, unitary time evolution — live in Lorentzian signature. The central question is precise:

> Under what exact conditions does a Euclidean path-integral measure define a physically admissible Lorentzian quantum field theory with a positive-definite Hilbert space and unitary time evolution?

The answer, formulated by Osterwalder and Schrader in the 1970s, is that a Euclidean theory must satisfy a short list of axioms, and the decisive one among them is reflection positivity. Without it, the Euclidean correlators may be perfectly well-defined as analytic functions but they do not correspond to any quantum theory with a self-adjoint Hamiltonian. With it, one can reconstruct the Hilbert space, the Hamiltonian, and the local fields rigorously.

This is not merely a mathematical nicety. Reflection positivity is the reason lattice gauge theory can claim to compute physical spectra, and it is the structural reason the conformal bootstrap's Euclidean crossing equations have anything to do with unitary conformal field theories. The subtlety is not the Wick rotation itself, but the positivity condition that survives it.

## 2. Assumptions and Notation

We work in $d$-dimensional Euclidean space. The distinguished Euclidean "time" direction is the $d$-th coordinate; reflections are taken across the hyperplane $x^d = 0$.

For two points $x$ and $y$, the Euclidean inner product is

$$
x \cdot y
=
\sum_{\mu=1}^d x^\mu y^\mu.
$$

Assumptions and scope:

- We consider scalar fields first; the extension to fermions and gauge fields requires care with spinor reflections and is noted where relevant.
- The Euclidean correlators are assumed to be tempered distributions, satisfying Euclidean covariance, symmetry, and cluster decomposition — the other Osterwalder–Schrader axioms.
- We assume the theory is defined by a (possibly formal) Euclidean path-integral measure on the space of field configurations.
- The reconstruction is rigorous for free and super-renormalizable theories; for interacting four-dimensional theories it is expected but not yet proven in full generality.

Let $\Theta$ denote the reflection operator. It acts on coordinates by leaving the first $d-1$ components unchanged and flipping the sign of the $d$-th component. For a smeared functional of the field, the reflected functional is obtained by composing with the reflected field; the precise formula is given in the definition below.

## 3. Definitions and Setup

Let $\mathcal{S}(\mathbb{R}^d)$ be the Schwartz space of test functions and let $\mathcal{S}'(\mathbb{R}^d)$ be the space of tempered distributions. A Euclidean quantum field theory assigns to each test function $f$ a smeared field $\phi(f)$, and the basic objects are the Schwinger functions (Euclidean correlators)

$$
S_n(x_1, \dots, x_n)
=
\langle \phi(x_1) \cdots \phi(x_n) \rangle_{\mathrm{Euc}},
$$

defined as moments of the formal measure.

**Definition 1 (Schwinger functions).** The $n$-point Schwinger functions are the tempered distributions obtained from the Euclidean measure by

$$
S_n(f_1 \otimes \cdots \otimes f_n)
=
\int \phi(f_1) \cdots \phi(f_n)\, \mathrm{d}\mu(\phi).
$$

These are symmetric in their arguments and, for a covariant theory, invariant under the Euclidean group $O(d)$.

The key structure is a reflection of test functions across the $x^d = 0$ hyperplane. For a test function $f$ supported in the half-space $x^d > 0$, define the reflected test function by

$$
(f_\theta)(x^1, \dots, x^{d-1}, x^d)
=
f(x^1, \dots, x^{d-1}, -x^d).
$$

**Definition 2 (Reflection positivity).** A set of Schwinger functions satisfies reflection positivity if, for every finite collection of test functions $f_1, \dots, f_n$ supported in the half-space $x^d > 0$,

$$
\sum_{m,n} S_{m+n}\bigl(f_{\theta}^{(1)} \otimes \cdots \otimes f_{\theta}^{(m)} \otimes f^{(m+1)} \otimes \cdots \otimes f^{(m+n)}\bigr)
\geq 0.
$$

In words: the matrix of Schwinger functions with arguments reflected on one side and unreflected on the other must be positive semi-definite. This is the Euclidean counterpart of the statement that the inner product on a Hilbert space is positive.

## 4. Main Derivation: From Reflection Positivity to a Hilbert Space

The payoff is that reflection positivity alone lets us build the physical Hilbert space. The construction follows a clear chain: positivity → inner product → completion → Hamiltonian → fields.

**Step 1: A pre-Hilbert space of observables.** Let $\mathcal{A}_+$ be the space of smeared field functionals built from test functions supported in $x^d > 0$. For $F, G \in \mathcal{A}_+$, define a sesquilinear form

$$
\langle F, G \rangle
:=
\int \overline{F[\phi]}\, (G[\Theta \cdot \phi])\, \mathrm{d}\mu(\phi).
$$

Reflection positivity is exactly the statement that this sesquilinear form is non-negative. This form may be degenerate; we quotient by the null space of zero-norm functionals.

**Step 2: Completion.** Let $\mathcal{H}$ be the Hilbert space completion of $\mathcal{A}_+ / \mathcal{N}$ with respect to this inner product. This is the physical Hilbert space of the reconstructed theory.

**Step 3: The Hamiltonian.** Euclidean time translation in the $x^d$ direction, restricted to the algebra of observables, defines a symmetric operator. Reflection positivity guarantees that this operator is bounded below and admits a self-adjoint continuation, the Hamiltonian $H \geq 0$.

The Euclidean two-point function then has a spectral representation: there exists a spectral measure such that $S_2(x, y)$ is the Laplace transform of a positive spectral density in the time separation. The vacuum $\Omega$ is identified as the constant functional in the physical Hilbert space, and the positivity of $H$ is the Euclidean shadow of Lorentzian unitarity.

**Step 4: Analytic continuation of correlators.** The Schwinger functions, initially defined for Euclidean points, are boundary values of functions analytic in a "cut" Lorentzian domain. The Wightman functions are obtained as

$$
W_n(x_1, \dots, x_n)
=
\lim_{\varepsilon \to 0^+}
S_n\bigl(x_1; i t_1 + \varepsilon, \dots; x_n; i t_n + (n-1)\varepsilon\bigr),
$$

and reflection positivity guarantees that these limits exist as tempered distributions and satisfy the Wightman axioms, including positivity of the Lorentzian inner product.

This chain is the Osterwalder–Schrader reconstruction theorem: reflection positivity plus the other Euclidean axioms implies the existence of a unitary, Poincaré-covariant Wightman QFT.

## 5. Interpretation of the Main Equation

The reflection-positivity inequality deserves a term-by-term reading. The sum over $m$ and $n$ runs over all ways of splitting a collection of test functions into a reflected set and an unreflected set. The reflected test functions $f_\theta^{(i)}$ live, in the path integral, on the "other side" of the reflection hyperplane. The inequality says that the path integral computes a positive norm when we glue a configuration to its mirror image.

- The **reflected arguments** encode the adjoint operation in the Hilbert space: reflecting a test function corresponds to taking the Hermitian conjugate of the associated operator.
- The **unreflected arguments** are the "ket" side of the inner product.
- The **positivity** is the statement that the norm of the state created by the unreflected fields acting on the vacuum is non-negative.

A useful way to see the point is the following. In a Lorentzian theory, unitarity is the positivity of the inner product. After Wick rotation, the inner product becomes a Euclidean reflection, and unitarity becomes reflection positivity. The two statements are equivalent; neither is a stronger assumption than the other.

## 6. Consistency Checks and Limiting Cases

Several checks confirm that reflection positivity is the right condition.

**Free-field limit.** For a free scalar field of mass $m$, the Euclidean two-point function is the Green function

$$
S_2(x, y)
=
\int \frac{\mathrm{d}^d p}{(2\pi)^d}\,
\frac{e^{i p \cdot (x - y)}}{p^2 + m^2}.
$$

Reflection positivity follows from the positivity of the free spectral density, which is a non-negative delta peak at $\mu^2 = m^2$. The reconstructed Hamiltonian is the free Hamiltonian, whose spectrum is bounded below by $m$, and the vacuum is the Gaussian measure's zero mode.

**Lattice check.** On a lattice with spacing $a$ and a positive transfer matrix $T$, the Euclidean correlator factorizes as

$$
\langle \mathcal{O}_1 \mathcal{O}_2 \rangle
=
\langle \Omega \rvert\> \mathcal{O}_1\, T^n\, \mathcal{O}_2 \lvert \Omega \rangle.
$$

Reflection positivity is the statement that $T$ is a positive operator, which is automatic if the lattice Boltzmann weights are positive. This is the structural reason the lattice program works: a reflection-positive lattice theory defines a unitary continuum limit, if the limit exists.

**Failure mode: the wrong sign.** If the Euclidean measure assigns negative weight to some configurations — as happens with fermions before introducing the spinor reflection, or with certain sign problems — reflection positivity fails, and the reconstructed "Hamiltonian" is not bounded below. The Euclidean correlators may still be computable, but they do not correspond to a physical quantum theory.

## 7. Relation to Existing Frameworks

Reflection positivity sits at the intersection of several frameworks discussed in related posts. The [Schwinger-Dyson equations](/posts/schwinger-dyson-equations-structure-quantum-effective-action/) constrain the same Euclidean correlators, but they are differential identities; reflection positivity is an inequality, and inequalities are what guarantee a probabilistic interpretation. The [renormalization group flow](/posts/renormalization-group-flow-meaning-scale/) preserves reflection positivity along the flow, which is why a unitary UV fixed point flows to a unitary IR theory. In the [conformal bootstrap](/posts/conformal-field-theory-bootstrap-program/), reflection positivity is the hidden axiom that rules out formally crossing-symmetric but non-unitary solutions.

The comparison with canonical quantization is instructive. In the canonical approach, unitarity is imposed by hand: one chooses a positive-definite inner product on the physical Hilbert space, as in [BRST quantization](/posts/brst-symmetry-gauge-theories/) where the physical states are identified as the cohomology of $Q_{\mathrm{BRST}}$ and positivity is nontrivial. In the Euclidean approach, unitarity is not imposed but derived: reflection positivity of the measure does the work. The two are complementary, and the Euclidean formulation is often the sharper tool for non-perturbative questions.

## 8. Limitations and Open Problems

The reconstruction theorem is rigorous for free and super-renormalizable theories in two and three dimensions. For interacting four-dimensional gauge theories — quantum chromodynamics being the canonical example — the construction of a reflection-positive Euclidean measure remains an open problem, closely related to the [mass gap problem](/posts/quantum-gravity-clash-general-relativity-quantum-theory/) and the broader question of whether non-Abelian gauge theory exists as a mathematically well-defined quantum field theory.

Several technical limitations deserve mention:

- **Fermions and gauge fields.** The reflection must be combined with a spinor reflection and a gauge-fixing condition. Reflection positivity in the physical subspace is subtle and is one reason the BRST formulation is indispensable.
- **Non-compact target spaces.** For sigma models with non-compact targets, reflection positivity can fail at the non-perturbative level even when perturbation theory looks healthy.
- **Sign problems.** Systems with a complex action — finite-density QCD, real-time dynamics — violate reflection positivity in the naive formulation, and reconstructing a unitary theory requires reweighting or contour deformation, neither of which is fully understood non-perturbatively.

This is where the formal language becomes dangerous if taken literally. Reflection positivity is the right axiom, but proving it for the theories that matter most is an outstanding open problem.

## 9. Relation to the Theory of Everything

Reflection positivity is not a candidate for a Theory of Everything, but it is a consistency condition any such theory must satisfy. A putative unified theory must, in some limit, reduce to a unitary quantum field theory coupled to general relativity. If that limit is formulated in Euclidean signature — as in certain approaches to quantum gravity — then reflection positivity of the gravitational measure is a minimal requirement for unitarity. This should not be read as a proof that Euclidean quantum gravity is the right path; it is a structural constraint that any viable path must respect.

## 10. Common Pitfalls

A few recurring confusions are worth naming.

- **Confusing reflection positivity with Euclidean invariance.** Euclidean $O(d)$ symmetry is a separate axiom. A theory can be Euclidean-invariant but not reflection-positive, and then it does not define a unitary Lorentzian theory.
- **Assuming the Wick rotation is automatic.** The rotation from Euclidean to Lorentzian signature requires analyticity in the time variables, which is guaranteed by the axioms but must be checked case by case.
- **Ignoring the null space.** The pre-inner product is only positive semi-definite; forgetting to quotient by the null space leads to negative-norm states in the reconstructed theory.
- **Treating reflection positivity as a perturbative statement.** It is an inequality about the full measure. Perturbation theory can obscure its failure, especially in the presence of anomalies or sign problems.

## 11. Conclusion

Reflection positivity is the structural reason Euclidean quantum field theory is more than a computational convenience. It is the single axiom that encodes unitarity in Euclidean language, and the Osterwalder–Schrader reconstruction theorem shows that it is sufficient to build a physical Hilbert space, a positive Hamiltonian, and local fields whose correlators satisfy the Wightman axioms. The limitation is not conceptual but technical: proving reflection positivity for interacting four-dimensional gauge theories remains one of the central open problems in mathematical physics. Until that is settled, the Euclidean path integral is a powerful formal tool whose rigorous justification is partial at best.

## References

[1] K. Osterwalder and R. Schrader, *Axioms for Euclidean Green's Functions I & II*, Communications in Mathematical Physics 31 (1973) 83–112; 42 (1975) 281–305.

[2] J. Glimm and A. Jaffe, *Quantum Physics: A Functional Integral Point of View*, Springer, 2nd ed., 1987.

[3] V. Rivasseau, *From Perturbative to Constructive Renormalization*, Princeton University Press, 1991.

[4] M. Reed and B. Simon, *Methods of Modern Mathematical Physics II: Fourier Analysis, Self-Adjointness*, Academic Press, 1975.

[5] K. Osterwalder, *Supersymmetric quantum field theory*, in: *Constructive Quantum Field Theory*, Springer, 1988.
