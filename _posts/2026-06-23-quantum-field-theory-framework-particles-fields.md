---
title: "Quantum Field Theory as a Framework for Particles and Fields"
date: 2026-06-23 10:20:00 +0700
categories: [Physics, Quantum Field Theory]
tags: [physics, theoretical-physics, quantum-field-theory, path-integral, unification]
description: "A rigorous treatment of quantum field theory: canonical and path integral quantization, correlation functions, perturbative and non-perturbative methods, renormalization, and the limits of the framework."
math: true
---

## Abstract

Quantum field theory is the framework in which locality, quantum mechanics, and special relativity can coexist. Its basic objects are fields, but fields are not ordinary functions; they are operator-valued distributions whose correlation functions define physical content. This article asks in what precise sense particles are secondary to fields in relativistic quantum theory. I distinguish fields, operators, observables, and asymptotic particle states, interpret the scalar action and two-point function, and explain why renormalization is part of the definition rather than an afterthought. The limitations are equally important: confinement, curved spacetime, non-perturbative existence, and Haag's theorem all warn against reading the particle picture too literally [1], [2].

**Keywords:** quantum field theory, fields, particles, locality, correlation functions, renormalization

## 1. Introduction

The central question is this: in what precise sense are particles secondary to fields in relativistic quantum theory? A particle is usually what a detector records, but QFT is built from local fields and their correlation functions. Particles appear as special excitations, often only in asymptotic regions where interactions switch off enough to define scattering states.

Gauge interactions are developed in [Gauge Symmetry and the Structure of Fundamental Interactions](/posts/gauge-symmetry-structure-fundamental-interactions/). The scale dependence of QFT belongs to [Renormalization Group Flow and the Meaning of Scale](/posts/renormalization-group-flow-meaning-scale/). Exact functional identities appear in [Schwinger-Dyson Equations](/posts/schwinger-dyson-equations-structure-quantum-effective-action/), while the on-shell particle limit is treated in [Scattering Amplitudes and the S-Matrix Program](/posts/scattering-amplitudes-s-matrix-on-shell-methods/).

## 2. Assumptions and Basic Objects

Assume Minkowski spacetime, a Hilbert space with positive norm, locality, and a stable vacuum. A scalar field $\phi(x)$ is an operator-valued distribution. Products at the same point are singular and require renormalization.

A basic scalar action is

$$
S[\phi]
=
\int d^4x
\bigl[
\frac{1}{2}\partial_\mu\phi\partial^\mu\phi
-
\frac{1}{2}m^2\phi^2
-
\frac{\lambda}{4!}\phi^4
\bigr].
$$

The kinetic term controls propagation. The mass term sets the pole location in the free propagator. The interaction term defines local scattering and loop corrections. The action is not itself an observable; it is a compact generator of dynamics.

## 3. Correlation Functions

The two-point function is

$$
G(x-y)
=
\langle 0 \vert \phi(x)\phi(y) \vert 0 \rangle .
$$

It measures the amplitude for a field excitation inserted at $y$ to be detected by a field insertion at $x$. In momentum space, a free scalar has

$$
G(p)
=
\frac{i}{p^2-m^2+i\epsilon}.
$$

The pole at $p^2=m^2$ is what becomes a particle interpretation. In an interacting theory, stable one-particle states appear as isolated poles of exact two-point functions. If there is no isolated pole, the particle interpretation is not available.

## 4. Fields, Operators, and Observables

Fields are often gauge dependent or representation dependent. Observables must be compatible with the physical constraints of the theory. In gauge theory, a bare charged field may not be gauge invariant; in QCD, quark and gluon fields do not create asymptotic particles.

This is where the formal language becomes dangerous if taken too literally. A field in the Lagrangian is not automatically a particle in the detector. The particle concept is an infrared and asymptotic concept.

## 5. Renormalization

Loop corrections produce divergences because fields are distributions and local products are singular. Renormalization introduces a scale $\mu$ and defines finite parameters at that scale. For a coupling $g$,

$$
\mu\frac{dg}{d\mu}
=
\beta(g).
$$

The left side changes the coupling with resolution. The beta function encodes quantum fluctuations. Physical predictions are independent of arbitrary renormalization conventions when all terms are treated consistently.

## 6. Consistency Checks

**Free limit.** Setting $\lambda=0$ gives a Gaussian theory with exactly computable correlation functions and a clean one-particle pole.

**LSZ limit.** Scattering amplitudes are extracted from residues of time-ordered correlators at particle poles. This verifies that particles are derived, not fundamental inputs.

**Locality.** Spacelike separated observables commute or anticommute, preserving relativistic causality.

## 7. Limitations and Open Problems

Confinement blocks a naive particle interpretation for colored fields. Curved spacetime can lack a preferred vacuum and hence a preferred particle notion. Haag's theorem warns that the interaction picture is mathematically subtle. Non-perturbative construction of interacting QFTs in four dimensions remains difficult.

Quantum gravity adds the deepest stress: QFT assumes a background causal structure, while gravity makes that structure dynamical.

## 8. Conclusion

QFT is not a theory of little particles first and fields second. It is a theory of local operator algebras, correlation functions, and renormalized dynamics. Particles appear when the theory has stable asymptotic states. That distinction is not philosophical bookkeeping; it is essential in confinement, curved spacetime, and any attempt to merge QFT with gravity.

## References

[1] S. Weinberg, _The Quantum Theory of Fields, Volume I_, Cambridge University Press, 1995.

[2] R. Haag, _Local Quantum Physics_, Springer, 1996.

[3] M. E. Peskin and D. V. Schroeder, _An Introduction to Quantum Field Theory_, Westview Press, 1995.

[4] R. F. Streater and A. S. Wightman, _PCT, Spin and Statistics, and All That_, Princeton University Press, 2000.

[5] M. Srednicki, _Quantum Field Theory_, Cambridge University Press, 2007.
