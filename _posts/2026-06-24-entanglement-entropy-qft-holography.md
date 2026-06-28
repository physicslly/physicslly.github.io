---
title: "Entanglement Entropy in Quantum Field Theory: From the Area Law to Holography"
date: 2026-06-24 08:00:00 +0700
categories: [Physics, Quantum Field Theory]
tags: [physics, theoretical-physics, quantum-field-theory, entanglement, holography, entropy, ads-cft]
description: "A rigorous treatment of entanglement entropy in quantum field theory: reduced density matrices, replica trick, area law, entanglement entropy in conformal field theory, the Ryu-Takayanagi formula, and the role of entanglement in quantum gravity."
math: true
---

## Abstract

Entanglement entropy measures how a quantum state fails to factorize across a spatial division. In continuum quantum field theory this is both powerful and subtle: the answer is ultraviolet divergent, depends on the regulator, and is dominated by short-distance correlations near the entangling surface. This article asks what entanglement entropy measures in a continuum QFT and why it knows about geometry. I define reduced density matrices with a regulator, derive the replica formula, explain the area law and the universal logarithm in two-dimensional conformal field theory, and then interpret the Ryu-Takayanagi formula as a geometric encoding of boundary entanglement. The main point is not that entropy equals area in every context, but that locality makes entanglement sharply sensitive to boundaries [1], [2].

**Keywords:** entanglement entropy, reduced density matrix, area law, replica trick, holography, Ryu-Takayanagi formula

## 1. Introduction

The vacuum of a quantum field theory is not empty in the tensor-product sense. If space is divided into a region $A$ and its complement, the vacuum usually does not factor into a state of $A$ times a state of the complement. Entanglement entropy quantifies that failure.

The central question is this: what does entanglement entropy measure in a continuum quantum field theory, and why does it know about geometry? The answer starts with local correlations across the entangling surface. Modes separated by arbitrarily short distances contribute, so a UV cutoff is not a technical nuisance; it is part of the definition.

This topic sits naturally beside [Quantum Field Theory as a Framework for Particles and Fields](/posts/quantum-field-theory-framework-particles-fields/). Its holographic side connects to [AdS/CFT](/posts/adscft-holographic-duality-and-quantum-gravity/) and to [quantum gravity](/posts/quantum-gravity-clash-general-relativity-quantum-theory/). The causal role of entangling surfaces also touches the geometry discussed in [causal structure](/posts/causal-structure-singularity-theorems/).

## 2. Assumptions and Definitions

Start with a regulated quantum system whose Hilbert space factorizes:

$$
\mathcal{H}
=
\mathcal{H}_A\otimes\mathcal{H}_{\bar A}.
$$

For a pure state, the reduced density matrix of region $A$ is

$$
\rho_A
=
\operatorname{Tr}_{\bar A}
\lvert\psi\rangle\langle\psi\rvert .
$$

The von Neumann entanglement entropy is

$$
S_A
=
-\operatorname{Tr}
\rho_A\log\rho_A .
$$

In continuum QFT, this factorization is subtle. A lattice regulator makes it concrete by assigning degrees of freedom to sites or links. Gauge theories are even more delicate because Gauss-law constraints prevent a naive tensor factorization across a spatial cut.

The entangling surface $\partial A$ is the boundary of the region. The cutoff is denoted $\epsilon$. All continuum statements below should be read as statements about the limit $\epsilon\to 0$ after a regulator has been specified.

## 3. Replica Trick

The Renyi entropies are

$$
S_A^{(n)}
=
\frac{1}{1-n}
\log\operatorname{Tr}\rho_A^n .
$$

The von Neumann entropy is recovered by analytic continuation:

$$
S_A
=
\lim_{n\to 1}
S_A^{(n)}.
$$

In a Euclidean path integral, $\operatorname{Tr}\rho_A^n$ is computed by gluing $n$ copies of the spacetime cyclically along the cut defining region $A$. If $Z_n$ is the partition function on the replicated geometry, then

$$
S_A^{(n)}
=
\frac{1}{1-n}
\log
\frac{Z_n}{Z_1^n}.
$$

Term by term: the replicated partition function contains the geometry with a branch structure around the entangling surface. The denominator removes the disconnected normalization. The prefactor converts the replicated trace into an entropy. The hard step is analytic continuation from integer $n$ to real $n$ near one.

## 4. UV Divergence and the Area Law

In $d$ spacetime dimensions, locality gives the leading divergence

$$
S_A
=
c_{d-2}
\frac{\operatorname{Area}(\partial A)}{\epsilon^{d-2}}
+
c_{d-4}
\frac{1}{\epsilon^{d-4}}
+
\cdots .
$$

The first term is proportional to the area of the entangling surface. The cutoff power counts the number of short-distance modes straddling the boundary. The coefficients $c_i$ depend on the regulator and field content. Subleading terms may contain universal data, especially logarithmic terms in conformal field theories.

This explains why entanglement entropy is not a conventional thermodynamic entropy. Thermal entropy scales with volume because it counts uncertainty throughout a region. Vacuum entanglement in a local QFT is dominated by correlations across the boundary.

For a single interval of length $\ell$ in a two-dimensional CFT,

$$
S(\ell)
=
\frac{c}{3}
\log\frac{\ell}{\epsilon}
+
c_1 .
$$

Here $c$ is the central charge and $c_1$ is non-universal. The logarithm is universal; it reflects scale invariance and the absence of a finite correlation length [3].

## 5. Twist-Field Derivation in Two Dimensions

For a 2D CFT, the replicated theory contains twist fields at the endpoints of the interval. Their conformal dimensions are

$$
\Delta_n
=
\bar\Delta_n
=
\frac{c}{24}
\bigl(
n-\frac{1}{n}
\bigr).
$$

The two-point function has the conformal form

$$
\langle
\mathcal{T}_n(0)
\tilde{\mathcal{T}}_n(\ell)
\rangle
=
\frac{C_n}{\ell^{2\Delta_n+2\bar\Delta_n}} .
$$

Restoring the cutoff gives

$$
\operatorname{Tr}\rho_A^n
=
C_n
\bigl(
\frac{\ell}{\epsilon}
\bigr)^{
-(c/6)(n-1/n)
}.
$$

Taking the derivative at $n=1$ yields the Calabrese-Cardy formula. The central charge appears because the stress tensor transforms anomalously under the map from the replicated surface to the plane.

## 6. Holographic Entanglement Entropy

In holographic CFTs, the Ryu-Takayanagi formula states [2]

$$
S_A
=
\frac{\operatorname{Area}(\gamma_A)}{4G_N}.
$$

The surface $\gamma_A$ is a bulk codimension-two minimal surface anchored on $\partial A$ and homologous to $A$. The numerator is the bulk geometric area. The denominator is Newton's constant. The formula says that a boundary entropy is computed by an extremal geometric object in one higher dimension.

For time-dependent states the minimal surface is replaced by the Hubeny-Rangamani-Takayanagi extremal surface. With quantum corrections, the generalized entropy is

$$
S_{\mathrm{gen}}
=
\frac{\operatorname{Area}(\gamma)}{4G_N}
+
S_{\mathrm{bulk}}.
$$

The first term is classical geometry. The second is bulk entanglement across the surface. Extremizing this generalized entropy gives quantum extremal surfaces, which are central in modern discussions of black hole evaporation.

## 7. Consistency Checks

**Pure states.** If the total state is pure, then

$$
S_A=S_{\bar A}.
$$

This is a basic check on any calculation.

**Mutual information.** The combination

$$
I(A:B)
=
S_A+S_B-S_{A\cup B}
$$

is finite for separated regions in a continuum QFT. Divergences cancel because they are local to entangling surfaces.

**Gapped systems.** In a gapped phase with correlation length $\xi$, regions much larger than $\xi$ obey an area law up to exponentially small corrections and possible topological constants.

## 8. Limitations and Open Problems

Entanglement entropy is regulator dependent. The leading area term cannot be compared across regulators without specifying a scheme. Gauge theories add factorization subtleties because physical states obey constraints across the boundary; one must choose an algebraic or extended-Hilbert-space prescription.

Time dependence is harder than static entanglement. In holography, extremal surfaces can change phase, and quantum corrections require bulk entropy. In ordinary QFT, analytic continuation in the replica trick can be difficult or ambiguous. The relation between entanglement, spacetime emergence, and quantum error correction is powerful, but it is not a complete non-perturbative definition of quantum gravity.

## 9. Conclusion

Entanglement entropy in QFT measures correlations across a spatial division, but in the continuum it is inseparable from the UV regulator and the geometry of the entangling surface. The area law follows from locality. The replica trick turns the entropy into a partition function on a branched geometry. Holography turns that branched-geometry problem into an area problem in the bulk. The shared theme is that entanglement is not only a property of states; in quantum field theory it is also a probe of geometry.

## References

[1] M. Srednicki, "Entropy and area," _Physical Review Letters_ 71, 666-669 (1993).

[2] S. Ryu and T. Takayanagi, "Holographic derivation of entanglement entropy from AdS/CFT," _Physical Review Letters_ 96, 181602 (2006).

[3] P. Calabrese and J. Cardy, "Entanglement entropy and quantum field theory," _Journal of Statistical Mechanics_ 2004, P06002 (2004).

[4] H. Casini and M. Huerta, "Entanglement entropy in free quantum field theory," _Journal of Physics A_ 42, 504007 (2009).

[5] T. Faulkner, A. Lewkowycz, and J. Maldacena, "Quantum corrections to holographic entanglement entropy," _Journal of High Energy Physics_ 2013, 74 (2013).

[6] A. C. Wall, "Maximin surfaces, and the strong subadditivity of the covariant holographic entanglement entropy," _Classical and Quantum Gravity_ 31, 225007 (2014).
