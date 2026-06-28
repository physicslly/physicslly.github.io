---
title: "Spontaneous Symmetry Breaking, the Higgs Mechanism, and Goldstone's Theorem"
date: 2026-06-26 00:01:00 +0800
categories: [Physics, Theory]
tags: [physics, theoretical-physics, quantum-field-theory, spontaneous-symmetry-breaking, higgs-mechanism, goldstone-theorem, standard-model]
description: "A rigorous treatment of spontaneous symmetry breaking in quantum field theory: Goldstone's theorem, the Higgs mechanism, the Englert-Brout-Higgs-Guralnik-Hagen-Kibble mechanism, and the structure of the Standard Model scalar sector."
math: true
---

## Abstract

Spontaneous symmetry breaking is the statement that a symmetric set of equations can have an asymmetric vacuum. In relativistic quantum field theory, that statement has two sharply different outcomes. For a broken continuous global symmetry, Goldstone's theorem produces physical massless modes. For a gauge symmetry, the would-be Goldstone modes are gauge-dependent variables that become the longitudinal polarizations of massive vector bosons. This article asks when symmetry breaking produces physical massless particles and when those modes are absorbed by gauge fields. I develop the order parameter, vacuum manifold, Goldstone theorem, Abelian Higgs model, and Standard Model scalar sector with attention to assumptions, degree-of-freedom counting, and the limits of the usual perturbative picture [1], [2].

**Keywords:** spontaneous symmetry breaking, Goldstone theorem, Higgs mechanism, vacuum manifold, order parameter, gauge symmetry

## 1. Introduction

The phrase "broken symmetry" is useful, but it is also a trap. The Lagrangian can remain exactly symmetric while the vacuum fails to be invariant. In a global theory that failure produces new physical particles. In a gauge theory it does not, because gauge redundancy is not a physical symmetry acting on distinct states.

The central question is therefore not whether a symmetry is broken. The better question is this: when does symmetry breaking produce physical massless modes, and when are those modes absorbed by gauge fields? The answer depends on the distinction between global symmetries, which act on the physical Hilbert space, and gauge redundancies, which describe the same physical state in many coordinate systems.

This distinction connects directly to [gauge symmetry](/posts/gauge-symmetry-structure-fundamental-interactions/) and to the BRST treatment of redundant variables in [BRST symmetry](/posts/brst-symmetry-gauge-theories/). The current-algebra side is close to [Noether currents and Ward identities](/posts/noether-currents-ward-identities-qft/). The Higgs sector is not an isolated trick; it is one controlled example of how symmetry, locality, and the spectrum constrain a quantum field theory.

## 2. Assumptions and Basic Definitions

Assume a local relativistic quantum field theory with a stable Poincare-invariant vacuum, a positive-norm physical Hilbert space after gauge fixing, and a conserved current for each continuous global symmetry. Goldstone's theorem also assumes that the charge associated with the current acts nontrivially on the vacuum. These assumptions fail or require modification in finite volume, in gauge theories before projection onto physical states, and in systems with long-range constraints.

An order parameter is a quantity whose vacuum expectation value distinguishes phases. For a scalar field $\phi_i$ transforming under a group $G$,

$$
\phi_i
\mapsto
\bigl[
\exp(i\alpha^a T^a)
\bigr]_{ij}\phi_j,
$$

a vacuum value

$$
\langle 0 \lvert \phi_i \rvert 0 \rangle
=
v_i
$$

breaks $G$ to the subgroup $H$ that leaves $v_i$ invariant. The vacuum manifold is the orbit

$$
\mathcal{M}_{\mathrm{vac}}
=
G/H .
$$

The tangent directions along this manifold are flat directions of the potential. In a global theory they are the Goldstone modes. In a gauge theory they are directions along a redundancy, not automatically particles.

## 3. Global Symmetry Breaking and Goldstone's Theorem

Let $J_\mu^a$ be the conserved Noether current of a continuous global symmetry,

$$
\partial^\mu J_\mu^a = 0,
$$

and define the charge

$$
Q^a
=
\int d^3x\,J_0^a(t,\mathbf{x}).
$$

Spontaneous breaking means there exists an operator $\mathcal{O}$ such that

$$
\langle 0 \lvert [Q^a,\mathcal{O}(0)] \rvert 0 \rangle
\neq
0.
$$

Writing the commutator in terms of the current gives

$$
\int d^3x\,
\langle 0 \lvert [J_0^a(t,\mathbf{x}),\mathcal{O}(0)] \rvert 0 \rangle
\neq
0.
$$

Insert a complete set of energy-momentum eigenstates. Lorentz invariance and current conservation force a spectral contribution that can survive at zero momentum only if there are states with arbitrarily small invariant mass. In a relativistic theory with the standard assumptions, that contribution is a massless scalar pole [3], [4].

The common counting statement is

$$
N_{\mathrm{GB}}
=
\dim G - \dim H .
$$

Term by term: $\dim G$ counts all continuous generators of the original global symmetry; $\dim H$ counts those that annihilate the chosen vacuum; the difference counts broken directions along the vacuum manifold. In Lorentz-invariant theories, each broken generator gives one Nambu-Goldstone boson. Nonrelativistic systems require a more refined counting because commutators of broken charges can themselves acquire expectation values.

## 4. Scalar Potential and Vacuum Manifold

The simplest useful model is a complex scalar with a $U(1)$ symmetry:

$$
V(\phi)
=
\mu^2|\phi|^2
+
\lambda|\phi|^4,
\qquad
\lambda>0 .
$$

The first term sets whether the origin is stable. The second term stabilizes the potential at large field. If $\mu^2>0$, the minimum is at $\phi=0$ and the symmetry is unbroken. If $\mu^2<0$, the minima satisfy

$$
|\phi|^2
=
\frac{-\mu^2}{2\lambda}
\equiv
\frac{v^2}{2}.
$$

The vacuum manifold is a circle. Choose one representative and write

$$
\phi(x)
=
\frac{1}{\sqrt{2}}
\bigl[
v+h(x)+i\pi(x)
\bigr].
$$

Expanding the potential around the chosen vacuum gives a massive radial mode $h$ and a massless angular mode $\pi$. The massless mode is not an accident of a low-order expansion. It is protected by the fact that moving along the vacuum manifold costs no potential energy.

A useful sanity check is explicit breaking. Add

$$
\Delta V
=
-\epsilon(\phi+\phi^\ast).
$$

The circle of minima is tilted. The angular mode now acquires a small mass. The Goldstone boson has become a pseudo-Goldstone boson, as happens for pions when quark masses explicitly break chiral symmetry.

## 5. Abelian Higgs Mechanism

Now gauge the same $U(1)$ symmetry:

$$
\mathcal{L}
=
-\frac{1}{4}F_{\mu\nu}F^{\mu\nu}
+
(D_\mu\phi)^\ast(D^\mu\phi)
-
V(\phi),
$$

with

$$
D_\mu
=
\partial_\mu - i e A_\mu .
$$

Use the polar parameterization

$$
\phi(x)
=
\frac{1}{\sqrt{2}}
\bigl[
v+h(x)
\bigr]
\exp\bigl(
\frac{i\theta(x)}{v}
\bigr).
$$

The covariant kinetic term contains

$$
(D_\mu\phi)^\ast(D^\mu\phi)
\supset
\frac{1}{2}e^2 v^2 A_\mu A^\mu
+
e^2 v h A_\mu A^\mu
+
\frac{1}{2}e^2 h^2 A_\mu A^\mu .
$$

The first term is the vector-boson mass term, with

$$
m_A = e v .
$$

The second term is a three-point interaction between one Higgs excitation and two gauge bosons. The third term is the corresponding four-point interaction. These terms all come from the same gauge-invariant kinetic term, not from inserting a Proca mass by hand.

The degree-of-freedom count is the cleanest interpretation. Before symmetry breaking, the theory has a massless vector with two polarizations and a complex scalar with two real components. After symmetry breaking, it has a massive vector with three polarizations and one real scalar $h$. The field $\theta$ has not vanished as a mathematical variable; it has become the longitudinal polarization of the massive vector after gauge fixing [5].

## 6. Standard Model Scalar Sector

The Standard Model uses a complex $SU(2)_L$ doublet with hypercharge $Y=1/2$:

$$
V(\Phi)
=
\mu^2 \Phi^\dagger\Phi
+
\lambda(\Phi^\dagger\Phi)^2 .
$$

For $\lambda>0$ and $\mu^2<0$,

$$
\langle \Phi \rangle
=
\frac{1}{\sqrt{2}}
\begin{pmatrix}
0 \\
v
\end{pmatrix},
\qquad
v
=
\sqrt{\frac{-\mu^2}{\lambda}} .
$$

The unbroken generator is

$$
Q = T^3 + Y,
$$

so

$$
SU(2)_L \times U(1)_Y
\longrightarrow
U(1)_{\mathrm{em}} .
$$

Three generators are broken. The three would-be Goldstone modes supply the longitudinal polarizations of $W^+$, $W^-$, and $Z$. The photon remains massless because the electromagnetic generator leaves the vacuum invariant.

The gauge boson masses are

$$
m_W
=
\frac{gv}{2},
\qquad
m_Z
=
\frac{v}{2}\sqrt{g^2+g'^2}.
$$

Here $g$ and $g'$ are the $SU(2)_L$ and $U(1)_Y$ couplings. The massless orthogonal combination is the photon. The tree-level relation

$$
\rho
=
\frac{m_W^2}{m_Z^2\cos^2\theta_W}
=
1
$$

is a nontrivial consistency check tied to custodial symmetry in the scalar sector.

The physical Higgs mass is

$$
m_h^2
=
2\lambda v^2 .
$$

The Higgs mechanism explains how weak gauge boson and elementary fermion masses are compatible with gauge invariance. It does not explain the numerical pattern of Yukawa couplings, and it does not account for most of the mass of ordinary matter, which is dominated by QCD binding energy.

## 7. Gauge Versus Global Breaking

The sentence "a gauge symmetry is spontaneously broken" is conventional but imprecise. A gauge symmetry is a redundancy in description. What changes physically is the phase: the spectrum, the realization of constraints, and the behavior of gauge-invariant operators. Elitzur's theorem makes this sharp on the lattice: a local gauge-variant operator cannot acquire a gauge-invariant expectation value without gauge fixing.

Perturbation theory still works because one fixes a gauge and expands around a convenient representative of the vacuum. In $R_\xi$ gauges the would-be Goldstone fields remain in propagators with gauge-dependent masses. In unitary gauge they are absent, but the ultraviolet behavior is less transparent. BRST symmetry is the clean bookkeeping device that keeps the unphysical variables from entering physical observables.

This is where the formal language becomes dangerous if taken too literally. Global symmetry breaking creates degenerate physical vacua in the infinite-volume limit. Gauge "breaking" reorganizes redundant variables and produces massive vector particles while preserving the gauge-invariant content of the theory.

## 8. Limitations and Open Problems

The Higgs mechanism is internally consistent, but it leaves hard questions exposed. The hierarchy problem is the sensitivity of the Higgs mass parameter to ultraviolet physics. Vacuum stability is the question of whether the measured Higgs and top masses place the Standard Model vacuum in an absolutely stable or metastable region under renormalization-group evolution. The fermion mass hierarchy remains unexplained.

There are also non-perturbative subtleties. Gauge-fixed perturbation theory makes the Higgs phase look simple, but a fully gauge-invariant description must be phrased in terms of physical operators. In strongly coupled gauge-Higgs systems, the distinction between Higgs-like and confinement-like regimes can be more delicate than the elementary perturbative picture suggests [6].

## 9. Conclusion

Spontaneous symmetry breaking is not one mechanism with one consequence. In a global relativistic theory, broken continuous generators imply physical massless Goldstone bosons. In a gauge theory, the would-be Goldstone directions are absorbed into vector fields, producing massive gauge bosons without explicit gauge-symmetry violation. The difference is not semantic. It is the difference between a physical symmetry acting on states and a redundancy in the variables used to describe those states.

## References

[1] J. Goldstone, "Field Theories with Superconductor Solutions," _Nuovo Cimento_ 19, 154-164 (1961).

[2] J. Goldstone, A. Salam, and S. Weinberg, "Broken Symmetries," _Physical Review_ 127, 965-970 (1962).

[3] Y. Nambu, "Quasi-particles and gauge invariance in the theory of superconductivity," _Physical Review_ 117, 648-663 (1960).

[4] P. W. Anderson, "Plasmons, Gauge Invariance, and Mass," _Physical Review_ 130, 439-442 (1963).

[5] F. Englert and R. Brout, "Broken Symmetry and the Mass of Gauge Vector Mesons," _Physical Review Letters_ 13, 321-323 (1964).

[6] P. W. Higgs, "Broken Symmetries and the Masses of Gauge Bosons," _Physical Review Letters_ 13, 508-509 (1964).

[7] G. S. Guralnik, C. R. Hagen, and T. W. B. Kibble, "Global Conservation Laws and Massless Particles," _Physical Review Letters_ 13, 585-587 (1964).

[8] S. Coleman and E. Weinberg, "Radiative Corrections as the Origin of Spontaneous Symmetry Breaking," _Physical Review D_ 7, 1888-1910 (1973).

[9] S. Weinberg, _The Quantum Theory of Fields, Volume II: Modern Applications_, Cambridge University Press, 1996.

[10] M. E. Peskin and D. V. Schroeder, _An Introduction to Quantum Field Theory_, Westview Press, 1995.
