---
title: "Conformal Field Theory and the Bootstrap Program"
date: 2026-06-23 22:00:00 +0700
categories: [Physics, Quantum Field Theory]
tags: [physics, theoretical-physics, conformal-field-theory, quantum-field-theory, bootstrap, critical-phenomena, ads-cft]
description: "A rigorous treatment of conformal field theory: the conformal group, primary operators, operator product expansion, radial quantization, conformal bootstrap, minimal models, and the space of conformal theories."
math: true
---

## Abstract

Conformal field theory studies quantum field theories with no intrinsic length scale. At a conformal fixed point, local operator data replace Lagrangian parameters as the natural description. This article asks how far consistency alone can determine a quantum field theory. I define primary operators, scaling dimensions, OPE coefficients, and crossing symmetry, then explain how the conformal bootstrap turns unitarity and associativity into quantitative constraints. The method is powerful because it does not require a weakly coupled Lagrangian, but it is not magic: numerical truncation, non-unitary theories, high-dimensional complexity, and the relation to microscopic dynamics remain serious limitations [1], [2].

**Keywords:** conformal field theory, bootstrap, primary operators, OPE, crossing symmetry, operator data

## 1. Introduction

The central question is this: how far can consistency alone determine a quantum field theory? CFT gives this question a sharp form because scale invariance and special conformal symmetry strongly constrain correlation functions.

CFTs are fixed points of [Renormalization Group Flow](/posts/renormalization-group-flow-meaning-scale/) inside the broader framework of [Quantum Field Theory](/posts/quantum-field-theory-framework-particles-fields/). Holography uses CFT as a non-gravitational definition of bulk physics in [AdS/CFT](/posts/adscft-holographic-duality-and-quantum-gravity/). Entanglement properties of CFTs are central in [Entanglement Entropy in QFT and Holography](/posts/entanglement-entropy-qft-holography/).

## 2. Operator Data

Primary operators $\mathcal{O}_i$ are operators that transform covariantly under the full conformal group. Each has a scaling dimension $\Delta_i$ and spin. Descendants are obtained by derivatives.

The two-point function of scalar primaries is fixed:

$$
\langle
\mathcal{O}_i(x)
\mathcal{O}_j(0)
\rangle
=
\frac{\delta_{ij}}{|x|^{2\Delta_i}}.
$$

The Kronecker delta expresses orthogonality after normalization. The denominator is fixed by scaling. The exponent is twice the operator dimension.

## 3. Operator Product Expansion

The OPE states that nearby operators can be expanded in local operators:

$$
\mathcal{O}_i(x)\mathcal{O}_j(0)
=
\sum_k
C_{ijk}
|x|^{\Delta_k-\Delta_i-\Delta_j}
\mathcal{O}_k(0)
+
\cdots .
$$

The coefficients $C_{ijk}$ are OPE coefficients. The dimensions and OPE coefficients are the CFT data. If they are known consistently, the theory's local correlation functions are determined.

## 4. Crossing Symmetry

For a four-point function of identical scalar operators, the OPE can be applied in different channels. Consistency requires the same answer:

$$
\sum_{\mathcal{O}}
C_{\phi\phi\mathcal{O}}^2
G_{\Delta,\ell}(u,v)
=
\bigl(
\frac{u}{v}
\bigr)^{\Delta_\phi}
\sum_{\mathcal{O}}
C_{\phi\phi\mathcal{O}}^2
G_{\Delta,\ell}(v,u).
$$

Term by term: the sum runs over exchanged primary operators; the coefficients are squared OPE coefficients; $G_{\Delta,\ell}$ are conformal blocks; $u$ and $v$ are cross-ratios. Crossing says that operator associativity is compatible with conformal symmetry.

This single equation, combined with positivity in unitary theories, is the engine of the numerical bootstrap.

## 5. Bootstrap Logic

The bootstrap does not begin with a Lagrangian. It assumes a spectrum, unitarity, crossing, and symmetry, then asks which operator data can exist. In practice one searches for functionals that rule out inconsistent spectra.

The result is often a rigorous exclusion plot. In favorable cases, such as the three-dimensional Ising CFT, islands of allowed data are small enough to determine critical exponents with high precision [3].

## 6. Consistency Checks

**Generalized free field.** A theory with factorized correlators satisfies crossing but lacks the full dynamics of an interacting local CFT. It is a useful baseline.

**Two-dimensional minimal models.** In two dimensions, the Virasoro algebra can make the bootstrap analytically solvable.

**Unitarity bounds.** Operator dimensions must obey lower bounds in unitary CFTs. Violating them signals negative-norm states.

## 7. Limitations and Open Problems

Numerical bootstrap results depend on truncation choices and computational resources, though bounds can be rigorous within a setup. Non-unitary theories require different positivity assumptions. Higher-dimensional theories with spin, global symmetry, supersymmetry, or defects can be much more complex. Finally, bootstrap consistency does not always explain which microscopic theory flows to a given CFT.

## 8. Conclusion

CFT replaces couplings with operator data. The bootstrap asks whether that data can satisfy symmetry, unitarity, and crossing. This is a striking inversion of the usual Lagrangian method: instead of computing consistency from dynamics, it constrains dynamics from consistency. Its power is real, and so are its boundaries.

## References

[1] P. Di Francesco, P. Mathieu, and D. Senechal, _Conformal Field Theory_, Springer, 1997.

[2] S. Rychkov, _EPFL Lectures on Conformal Field Theory in D >= 3 Dimensions_, Springer, 2017.

[3] S. Rychkov, "Conformal bootstrap in three dimensions?" arXiv:1111.2115.

[4] D. Simmons-Duffin, "The conformal bootstrap," arXiv:1602.07982.
