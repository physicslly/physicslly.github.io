---
title: "Entanglement Entropy in Quantum Field Theory: From the Area Law to Holography"
date: 2026-06-24 08:00:00 +0700
categories: [Physics, Quantum Field Theory]
tags: [physics, theoretical-physics, quantum-field-theory, entanglement, holography, entropy, ads-cft]
description: "A rigorous treatment of entanglement entropy in quantum field theory: reduced density matrices, replica trick, area law, entanglement entropy in conformal field theory, the Ryu-Takayanagi formula, and the role of entanglement in quantum gravity."
math: true
---

## Abstract

Entanglement entropy measures the quantum correlations between a spatial region and its complement in a quantum field theory. Unlike thermal entropy, it receives contributions from ultraviolet modes near the entangling surface, leading to a characteristic area-law scaling. This article provides a rigorous treatment of entanglement entropy in QFT: its definition in terms of reduced density matrices, the replica trick for computation, the area law for gapped systems and its logarithmic violation in conformal field theories, and the Calabrese-Cardy formula for the entanglement entropy of an interval in a 1+1 CFT. The Ryu-Takayanagi formula is introduced as a holographic dual of entanglement entropy in AdS/CFT, and its generalizations — holographic entanglement entropy for subregions, the entanglement wedge, and quantum extremal surfaces — are discussed. The connections between entanglement, spacetime geometry, and the emergence of bulk spacetime from boundary entanglement are explored, along with applications to black hole physics and the information paradox.

**Keywords:** entanglement entropy, quantum field theory, replica trick, Ryu-Takayanagi, holography, area law

## 1. Introduction

Entanglement is one of the most distinctive features of quantum mechanics. In quantum field theory, the vacuum state of a relativistic system exhibits intricate entanglement between spatially separated regions. The entanglement entropy of a region A measures how much information about the state of A is hidden in its correlations with the complement B.

Interest in entanglement entropy has grown dramatically with the recognition that it plays a central role in several fundamental problems:
- **Black hole thermodynamics**: The Bekenstein-Hawking entropy $S_{\mathrm{BH}} = A/(4G\hbar)$ suggests that spacetime degrees of freedom are encoded on holographic screens, with entanglement entropy providing a microscopic interpretation [1].
- **Holography**: The Ryu-Takayanagi formula relates entanglement entropy in the boundary CFT to the area of minimal surfaces in the bulk AdS spacetime, providing a deep link between quantum information and quantum gravity [2].
- **Quantum gravity**: The area law for entanglement entropy suggests that spacetime itself may emerge from the entanglement structure of more fundamental degrees of freedom [3].

This article develops the formalism and key results of entanglement entropy in QFT, from the replica trick and area law to the holographic principle and the Ryu-Takayanagi formula.

## 2. Preliminaries and Notation

Consider a quantum system with Hilbert space $\mathcal{H} = \mathcal{H}_A \otimes \mathcal{H}_B$. For a pure state $\lvert\psi\rangle \in \mathcal{H}$, the **reduced density matrix** for subsystem A is

$$
\rho_A = \operatorname{Tr}_B |\psi\rangle\langle \psi|.
$$

The **von Neumann entanglement entropy** of A is

$$
S_A = -\operatorname{Tr}(\rho_A \ln \rho_A).
$$

For a mixed state $\rho_{AB}$, the **mutual information** measures total correlations:

$$
I(A:B) = S_A + S_B - S_{AB}.
$$

In quantum field theory, we consider a spatial region A on a Cauchy surface $\Sigma$. The Hilbert space factorizes as

$$
\mathcal{H} = \mathcal{H}_{A} \otimes \mathcal{H}_{\bar A}
$$

only after introducing an ultraviolet regulator, since degrees of freedom arbitrarily close to the entangling surface $\partial A$ are infinitely entangled across the boundary [4].

A **entangling surface** $\partial A$ is the boundary between A and its complement. For a d-dimensional QFT, the entanglement entropy diverges in the continuum limit due to short-distance correlations across $\partial A$.

Throughout this article, we work in Euclidean signature for the replica trick, and use natural units $\hbar = c = 1$. For CFT calculations, the metric is $ds^2 = d\tau^2 + d\mathbf{x}^2$ for flat space.

## 3. Theoretical Framework

### 3.1 The Replica Trick

The entanglement entropy $S_A$ of a spatial region A in a QFT is notoriously difficult to compute directly because the reduced density matrix $\rho_A$ is a complicated object in the continuum. The replica trick circumvents this by expressing $S_A$ in terms of partition functions on replicated geometries, which are computable using standard QFT methods.

The **Rényi entropies** are defined for integer $n \ge 2$ as

$$
S_A^{(n)} = \frac{1}{1-n} \ln \operatorname{Tr} \rho_A^n.
$$

The von Neumann entanglement entropy is recovered by analytic continuation:

$$
S_A = \lim_{n \to 1} S_A^{(n)}.
$$

In the Euclidean path integral formulation, the trace $\operatorname{Tr}\rho_A^{n}$ is computed on an n-sheeted covering space $\mathcal{M}_n$: we take n copies of the original Euclidean spacetime, cut each along region A, and glue them cyclically. This creates a conical singularity at the entangling surface $\partial A$ with deficit angle $2\pi(1-n)$.

The partition function on the replicated manifold is

$$
Z_n = \int_{\mathcal{M}_n} \mathcal{D}\phi \, e^{-S[\phi]},
$$

and the **Rényi entropy** follows from

$$
S_A^{(n)} = \frac{1}{1-n} \ln \frac{Z_n}{Z_1^n}.
$$

For a QFT that can be described by a path integral on a curved manifold with conical singularities, powerful techniques from conformal field theory and holography can be applied to evaluate $Z_n$ explicitly.

### 3.2 UV Divergences and the Area Law

The entanglement entropy in a d-dimensional QFT diverges in the continuum limit due to the infinite entanglement of ultraviolet modes across the entangling surface. For a region A with entangling surface $\partial A$, the leading divergence is proportional to the area:

$$
S_A = c_{d-2} \frac{\operatorname{Area}(\partial A)}{\epsilon^{d-2}} + c_{d-4} \frac{1}{\epsilon^{d-4}} + \cdots,
$$

with subleading power-law divergences for $d > 2$. Here $\epsilon$ is a short-distance cutoff (e.g., lattice spacing) and the coefficients $c_k$ depend on the field content.

This area law was first recognized by Srednicki (1993) for free scalar fields and subsequently proven to be a universal property of gapped systems: their ground-state entanglement entropy scales with the boundary area of the region, not its volume [4]. This is fundamentally different from thermal entropy, which is extensive.

In even spacetime dimensions, there is also a logarithmic term that is universal and scheme-independent:

$$
S_A = \cdots + (-1)^{d/2-1} \, \frac{4a}{180} \ln(\epsilon) + \cdots,
$$

where $a$ is the Euler anomaly coefficient for a CFT in $d$ dimensions.

### 3.3 Mutual Information and Other Measures

The mutual information $I(A:B) = S_A + S_B - S_{AB}$ is often a more convenient quantity than entanglement entropy because it is UV-finite and regulator-independent. It measures the total correlations between A and B, both classical and quantum.

Other measures of bipartite entanglement include:
- **Entanglement negativity**: $\mathcal{E} = \ln \|\rho^{T_A}\|_1$, where $T_A$ denotes partial transpose on $A$. This is a computable entanglement measure for mixed states.
- **Relative entropy**: $S(\rho\|\sigma) = \operatorname{Tr}(\rho \ln\rho) - \operatorname{Tr}(\rho \ln\sigma)$, measuring distinguishability of two states.
- **Quantum null energy condition**: A bound relating the von Neumann entropy of a region to the energy flux through its entangling surface, derived from the quantum focusing conjecture.

## 4. Main Derivation: Entanglement Entropy in 1+1 Dimensional CFT

### 4.1 The Calabrese-Cardy Formula

The replica trick for a 1+1 dimensional CFT is particularly tractable because the n-sheeted Riemann surface $\mathcal{M}_n$ can be mapped to the complex plane by a uniformizing transformation. For a CFT on the infinite line in its ground state, the entanglement entropy of a single interval of length $\ell$ is given by the Calabrese-Cardy formula [5,6]:

$$
S(\ell) = \frac{c}{3} \ln \frac{\ell}{\epsilon} + c_1,
$$

where $c$ is the central charge of the CFT, $\epsilon$ is a UV cutoff, and $c_1$ is a non-universal constant.

For a CFT on a circle of circumference L, the result is

$$
S(\ell) = \frac{c}{3} \ln \left( \frac{L}{\pi\epsilon} \sin \frac{\pi\ell}{L} \right) + c_1,
$$

reducing to the infinite-line result for $\ell \ll L$.

### 4.2 Derivation via Twist Fields

The key insight is that $\operatorname{Tr}\rho_A^{n}$ on the n-sheeted covering space is equivalent to a correlation function of twist fields in the replicated CFT. The twist fields $\mathcal{T}_n(z)$ and $\tilde{\mathcal{T}}_n(\bar{z})$ are primary operators inserted at the endpoints of the interval, implementing the cyclic permutation among sheets.

The conformal weight of the twist fields is determined by the stress-energy tensor on the replicated manifold. The uniformizing map $z \to w = (z/\ell)^{1/n}$ maps the n-sheeted plane to a single-sheeted plane. Under this map, the stress tensor transforms anomalously due to the Schwarzian derivative, giving

$$
\Delta_n = \bar\Delta_n = \frac{c}{24} \left( n - \frac{1}{n} \right).
$$

The two-point function of twist fields on the complex plane is fixed by conformal invariance:

$$
\langle \mathcal{T}_n(0) \tilde{\mathcal{T}}_n(\ell) \rangle = \frac{c_n}{|\ell|^{2\Delta_n}}.
$$

The **Rényi entropy** follows from

$$
\operatorname{Tr} \rho_A^n = \langle \mathcal{T}_n(0) \tilde{\mathcal{T}}_n(\ell) \rangle_{\text{CFT}^{\otimes n}}
= c_n \left( \frac{\ell}{\epsilon} \right)^{-(c/6)(n-1/n)},
$$

where the cutoff $\epsilon$ regularizes the twist-field self-contractions. Taking $n \to 1$ yields the logarithmic result.

### 4.3 Finite Temperature and Finite Size

At finite temperature $\beta^{-1}$, the CFT lives on a cylinder of circumference $\beta$. The twist-field correlation function on the cylinder is obtained from the plane by the exponential map $w = e^{2\pi z/\beta}$, giving

$$
\operatorname{Tr} \rho_A^n = c_n \left( \frac{\beta}{\pi\epsilon} \sinh \frac{\pi\ell}{\beta} \right)^{-(c/6)(n-1/n)}.
$$

The entanglement entropy follows as

$$
S(\ell) = \frac{c}{3} \ln \left( \frac{\beta}{\pi\epsilon} \sinh \frac{\pi\ell}{\beta} \right) + c_1.
$$

For $\ell \gg \beta$, this gives $S \sim (c/3)(\pi\ell/\beta) = (2\pi c/3) \ell T$ — a volume law arising from thermal mixing. This transition from area-law to volume-law scaling is a generic feature of entanglement entropy at finite temperature.

### 4.4 Disjoint Intervals and Higher Genus

For two disjoint intervals $[x_1, x_2]$ and $[x_3, x_4]$ on the line, the **Rényi entropy** involves the four-point function of twist fields:

$$
\operatorname{Tr} \rho_A^n = \langle \mathcal{T}_n(x_1) \tilde{\mathcal{T}}_n(x_2) \mathcal{T}_n(x_3) \tilde{\mathcal{T}}_n(x_4) \rangle.
$$

This four-point function depends on the full operator content of the CFT through the conformal block expansion, and in general is not universal. The result can be expressed as

$$
S_A^{(n)} = \frac{1}{1-n} \ln \left[ c_n^2 \left( \frac{|x_{12}||x_{34}|}{|x_{13}||x_{24}||x_{14}||x_{23}|} \right)^{(c/6)(n-1/n)} \mathcal{F}_n(x) \right],
$$

where $x = (x_{12}x_{34})/(x_{13}x_{24})$ is the conformal cross-ratio and $\mathcal{F}_n(x)$ encodes the nontrivial dynamics.

## 5. Interpretation of the Main Equations

The area law for entanglement entropy $S_A \propto \operatorname{Area}(\partial A)/\epsilon^{d-2}$ reveals a fundamental difference between entanglement entropy and thermal entropy. Thermal entropy is extensive (proportional to volume) because it measures classical uncertainty about the microstate. Entanglement entropy measures quantum correlations between A and its complement, which are strongest across the boundary separating them.

The logarithmic violation in CFTs ($\gamma \neq 0$) is a signature of long-range correlations. The coefficient of the logarithmic term is proportional to the central charge $c$, which counts the degrees of freedom. This connection is formalized by the c-theorem in 2D: the central charge decreases along RG flows, and entanglement entropy provides a way to define a c-function [7].

The Calabrese-Cardy formula $S = (c/3)\ln(\ell/\epsilon)$ shows that entanglement entropy grows logarithmically with interval length in 1+1 CFTs, reflecting the power-law decay of correlations. In higher dimensions, the leading area-law divergence dominates, but universal logarithmic terms appear for even-dimensional CFTs and depend on the geometry of the entangling surface.

## 6. Consistency Checks and Limiting Cases

### 6.1 Free Boson in 2D

For a free compactified boson with central charge c = 1, the entanglement entropy of an interval of length $\ell$ on an infinite line is

$$
S(\ell) = \frac{1}{3} \ln \frac{\ell}{\epsilon} + c_1,
$$

matching the Calabrese-Cardy formula with c = 1. This can be verified by explicit computation of the two-point function of twist fields.

### 6.2 Ground State of a Gapped System

For a gapped system with correlation length $\xi$, the entanglement entropy of a region of size R $\gg$ $\xi$ saturates to

$$
S_A = \alpha \frac{\operatorname{Area}(\partial A)}{\epsilon^{d-2}} - \gamma + \mathcal{O}(e^{-R/\xi}),
$$

where $\gamma$ is the topological entanglement entropy for topologically ordered phases. For the toric code, $\gamma = \ln 2$, reflecting the quantum dimension of anyons [8].

### 6.3 Single Interval in Free Fermion Theory

For a free fermion on a lattice, the entanglement entropy of an interval of length L in the ground state is

$$
S(L) = \frac{1}{3} \ln L + c_1,
$$

exactly matching the CFT result with c = 1 for a massless Dirac fermion. Numerical lattice calculations confirm this scaling with high precision.

## 7. Discussion

### 7.1 The Ryu-Takayanagi Formula

One of the most striking developments in holography is the Ryu-Takayanagi (RT) formula, which relates entanglement entropy in the boundary CFT to the area of minimal surfaces in the bulk AdS spacetime [2]:

$$
S_A = \frac{\operatorname{Area}(\gamma_A)}{4G},
$$

where $\gamma_A$ is the minimal-area codimension-2 surface in the bulk that is homologous to the boundary region A. This is the holographic dual of entanglement entropy.

For a strip of width $\ell$ in a d-dimensional CFT dual to Ad$S_{d+1}$, the RT formula gives

$$
S_A = \frac{1}{2G} \left[ \frac{R^{d-1}}{2(d-2)} \left( \frac{1}{\epsilon^{d-2}} - \frac{c_0}{\ell^{d-2}} \right) \right],
$$

reproducing the area law plus a universal term. The RT formula satisfies all known properties of entanglement entropy: strong subadditivity, monogamy, and the Araki-Lieb inequality.

### 7.2 Quantum Extremal Surfaces and the Island Formula

The RT formula has been generalized to include bulk quantum effects. The **quantum extremal surface** prescription [9] states

$$
S_A = \min_{\chi} \ext \left[ \frac{\operatorname{Area}(\chi)}{4G} + S_{\rm{bulk}}(\Sigma_\chi) \right],
$$

where $\chi$ is a codimension-2 surface homologous to A, and $S_{\rm{bulk}}$ is the entanglement entropy of bulk quantum fields in the region bounded by $\chi$ and A. This formula has been crucial in deriving the Page curve for evaporating black holes, resolving the information paradox [10].

### 7.3 Entanglement Wedge Reconstruction

The **entanglement wedge** is the bulk region dual to a boundary subregion A: the domain of dependence of any spacelike surface bounded by A and $\gamma_A$. The entanglement wedge reconstruction conjecture states that all bulk operators in the entanglement wedge can be reconstructed from boundary operators in A. This provides a concrete realization of the holographic principle and the emergence of bulk spacetime from boundary entanglement [3].

## 8. Relation to the Theory of Everything

Entanglement entropy provides a bridge between quantum information and quantum gravity. Several deep connections are relevant to a ToE:

1. **Spacetime from entanglement**: The Einstein equations can be derived from the first law of entanglement entropy for small perturbations of the vacuum in AdS/CFT. This suggests that spacetime geometry is emergent from the entanglement structure of the boundary theory [3].

2. **Holographic principle**: The area law for entanglement entropy mirrors the Bekenstein-Hawking entropy formula. Both suggest that the degrees of freedom in a region of space are encoded on its boundary at the Planck scale.

3. **UV/IR connection**: Entanglement entropy reveals a deep connection between ultraviolet (short-distance) and infrared (large-distance) physics. The area law shows that UV modes at the entangling surface contribute to IR observable quantities.

4. **Quantum gravity as error correction**: The entanglement wedge reconstruction implies that the AdS/CFT correspondence is a quantum error-correcting code, protecting bulk information from boundary erasures.

## 9. Common Pitfalls

1. **Entanglement entropy is not thermal entropy.** Entanglement entropy measures quantum correlations and vanishes for product states. Thermal entropy measures classical uncertainty and is always positive for mixed states.

2. **The area law is not the same as the holographic principle.** The area law for entanglement entropy is a UV effect in QFT, while the holographic principle bounds the total number of degrees of freedom in quantum gravity.

3. **The replica trick requires analytic continuation.** The analytic continuation n $\to$ 1 is not unique in general and requires careful treatment in non-CFT theories.

4. **The RT formula applies only to static holographic duals.** Time-dependent backgrounds require the HRT (Hubeny-Rangamani-Takayanagi) covariant prescription.

5. **Entanglement entropy in gauge theories is subtle.** The factorization of the Hilbert space is not straightforward due to Gauss's law constraints; the entropy depends on how edge modes are treated.

## 10. Conclusion

Entanglement entropy in quantum field theory is a rich subject that connects quantum information, critical phenomena, and quantum gravity. The area law and its logarithmic violations in CFTs are universal features that characterize the entanglement structure of the vacuum. The replica trick provides a computational framework, while the Ryu-Takayanagi formula gives a geometric dual in holographic theories. The deep connection between entanglement and spacetime geometry — most dramatically realized in the derivation of the Einstein equations from entanglement — suggests that entanglement entropy may be a fundamental concept in a Theory of Everything.

## References

[1] S. Ryu and T. Takayanagi, "Holographic Derivation of Entanglement Entropy from AdS/CFT," *Phys. Rev. Lett.* 96, 181602 (2006).

[2] S. Ryu and T. Takayanagi, "Aspects of Holographic Entanglement Entropy," *JHEP* 08, 045 (2006).

[3] T. Faulkner, M. Guica, T. Hartman, R. C. Myers, and M. Van Raamsdonk, "Gravitation from Entanglement in Holographic CFTs," *JHEP* 03, 051 (2014).

[4] J. Eisert, M. Cramer, and M. B. Plenio, "Colloquium: Area Laws for the Entanglement Entropy," *Rev. Mod. Phys.* 82, 277 (2010).

[5] P. Calabrese and J. Cardy, "Entanglement Entropy and Quantum Field Theory," *J. Stat. Mech.* P06002 (2004).

[6] P. Calabrese and J. Cardy, "Entanglement Entropy and Conformal Field Theory," *J. Phys. A* 42, 504005 (2009).

[7] H. Casini and M. Huerta, "Entanglement Entropy in Free Quantum Field Theory," *J. Phys. A* 42, 504007 (2009).

[8] A. Kitaev and J. Preskill, "Topological Entanglement Entropy," *Phys. Rev. Lett.* 96, 110404 (2006).

[9] N. Engelhardt and A. C. Wall, "Quantum Extremal Surfaces: Holographic Entanglement Entropy beyond the Classical Regime," *JHEP* 01, 073 (2015).

[10] A. Almheiri, T. Hartman, J. Maldacena, E. Shaghoulian, and A. Tajdini, "The Entropy of Hawking Radiation," *Rev. Mod. Phys.* 93, 035002 (2021).
