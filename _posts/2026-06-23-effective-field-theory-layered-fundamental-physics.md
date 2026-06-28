---
title: "Effective Field Theory and Why Fundamental Physics Is Layered"
date: 2026-06-23 11:00:00 +0700
categories: [Physics, Quantum Field Theory]
tags: [physics, theoretical-physics, effective-field-theory, quantum-field-theory, renormalization, unification]
description: "A rigorous treatment of effective field theory: Wilsonian decoupling, operator expansions, power counting, matching, symmetry constraints, naturalness, and the layered structure of physical law."
math: true
---

## Abstract

Effective field theory is the reason a theory can be useful without being final. If there is scale separation, low-energy observables can be organized using local operators constrained by symmetry, with unknown short-distance physics absorbed into Wilson coefficients. This article asks how a theory can be predictive while explicitly not being fundamental. I explain cutoff dependence, decoupling, power counting, matching, and relevant versus irrelevant operators, then interpret an effective action expansion term by term. EFT is not free of problems: naturalness, strong coupling, gravity, and unknown UV completions all test its assumptions [1], [2].

**Keywords:** effective field theory, cutoff, Wilson coefficients, power counting, matching, naturalness

## 1. Introduction

The central question is this: how can a theory be predictive while explicitly not being fundamental? EFT answers by separating what low-energy experiments can see from what they cannot. Heavy physics does not disappear; it becomes encoded in suppressed local operators.

The scale logic is developed in [Renormalization Group Flow and the Meaning of Scale](/posts/renormalization-group-flow-meaning-scale/). The QFT foundation is reviewed in [Quantum Field Theory as a Framework for Particles and Fields](/posts/quantum-field-theory-framework-particles-fields/). Gravity as an EFT connects to [Quantum Gravity](/posts/quantum-gravity-clash-general-relativity-quantum-theory/), while inflation is a major cosmological use case in [Cosmology, Inflation, and the Early Universe](/posts/cosmology-inflation-early-universe/).

## 2. Assumptions

Assume locality, unitarity, symmetries, and a separation between the energy of interest $E$ and a heavy scale $\Lambda$:

$$
E\ll\Lambda.
$$

The EFT action has the form

$$
S_{\mathrm{EFT}}
=
\int d^4x
\bigl[
\mathcal{L}_{\mathrm{ren}}
+
\sum_i
\frac{c_i}{\Lambda^{\Delta_i-4}}
\mathcal{O}_i
\bigr].
$$

The first term contains relevant and marginal operators. The sum contains higher-dimension operators. The coefficients $c_i$ are Wilson coefficients. The powers of $\Lambda$ enforce dimensional analysis.

## 3. Power Counting

If an operator has dimension $\Delta_i$, its contribution at energy $E$ scales as

$$
\bigl(
\frac{E}{\Lambda}
\bigr)^{\Delta_i-4}.
$$

For $\Delta_i>4$, the operator is irrelevant at low energy. This does not mean unimportant in principle; it means systematically suppressed. Predictivity comes from truncating the expansion at a chosen accuracy.

A useful way to see the point is that EFT gives an error estimate. If all operators through order $1/\Lambda^2$ are included, missing terms begin at the next power.

## 4. Matching and Decoupling

Matching determines Wilson coefficients by requiring the UV theory and EFT to give the same low-energy amplitudes. Schematically,

$$
\mathcal{A}_{\mathrm{UV}}(E)
=
\mathcal{A}_{\mathrm{EFT}}(E)
+
O(E/\Lambda)^n.
$$

The left side knows about heavy fields. The right side uses only light fields and local operators. Equality fixes the coefficients $c_i$ order by order.

Decoupling is the statement that heavy particles affect low-energy physics through renormalized parameters and suppressed operators, provided no symmetry or infrared effect prevents it [3].

## 5. Consistency Checks

**Fermi theory.** At energies much below the $W$ mass, weak interactions are described by a four-fermion operator with coefficient proportional to $1/M_W^2$.

**Chiral perturbation theory.** Low-energy pions are organized by derivatives and quark masses, not by quark and gluon fields directly.

**Gravity.** General relativity is an EFT at low energies, with higher-curvature corrections suppressed by the cutoff.

## 6. Limitations and Open Problems

Naturalness is the hardest conceptual pressure point. Relevant operators such as scalar masses can be sensitive to heavy scales, and EFT by itself does not explain why the Higgs mass is small compared with much higher UV scales.

Strongly coupled EFTs may lack a simple perturbative expansion. Gravity has no known ordinary Wilsonian UV completion in four-dimensional perturbation theory. Unknown UV physics can also impose nontrivial positivity, causality, or anomaly constraints on Wilson coefficients.

## 7. Conclusion

EFT is predictive because it is honest about scale. It does not claim to be final; it claims to be complete to a specified accuracy at a specified energy. Symmetry fixes the operator basis, power counting ranks corrections, and matching connects low-energy coefficients to high-energy physics. That is why layered descriptions are not a weakness of modern physics. They are how precision becomes possible.

## References

[1] K. G. Wilson and J. Kogut, "The renormalization group and the epsilon expansion," _Physics Reports_ 12, 75-199 (1974).

[2] H. Georgi, "Effective field theory," _Annual Review of Nuclear and Particle Science_ 43, 209-252 (1993).

[3] T. Appelquist and J. Carazzone, "Infrared singularities and massive fields," _Physical Review D_ 11, 2856-2861 (1975).

[4] C. P. Burgess, "Introduction to effective field theory," _Annual Review of Nuclear and Particle Science_ 57, 329-362 (2007).
