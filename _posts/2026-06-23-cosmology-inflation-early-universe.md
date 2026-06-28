---
title: "Cosmology, Inflation, and the Early Universe"
date: 2026-06-23 11:20:00 +0700
categories: [Physics, Cosmology]
tags: [physics, theoretical-physics, cosmology, general-relativity, inflation, cmb, perturbation-theory]
description: "A rigorous treatment of modern cosmology: FRW geometry, Friedmann equations, inflation as an effective theory, cosmological perturbation theory, the cosmic microwave background, and the connections between early-universe physics and fundamental theory."
math: true
---

## Abstract

Inflation is a dynamical proposal about the very early universe: a period of accelerated expansion can make a large, nearly flat, causally coherent region while turning quantum fluctuations into primordial density perturbations. This article asks what inflation explains dynamically and what it leaves unresolved. I review FLRW geometry, Friedmann dynamics, scalar-field inflation, slow-roll conditions, and the origin of scalar perturbations. The useful conclusion is balanced: inflation explains the horizon and flatness problems and predicts a nearly scale-invariant spectrum, but it leaves questions about initial conditions, reheating, measures, trans-Planckian sensitivity, and quantum gravity [1], [2].

**Keywords:** cosmology, inflation, Friedmann equations, slow roll, primordial perturbations, early universe

## 1. Introduction

The central question is this: what does inflation explain dynamically, and what does it leave unresolved? It explains why a universe that looks causally puzzling in a decelerating big-bang model can arise from a small accelerated patch. It does not by itself explain why the patch began inflating.

The spacetime background is general relativity, reviewed in [General Relativity and the Geometry of Spacetime](/posts/general-relativity-geometry-spacetime/). Quantum fluctuations use the language of [Quantum Field Theory](/posts/quantum-field-theory-framework-particles-fields/). Inflation is often treated as an [effective field theory](/posts/effective-field-theory-layered-fundamental-physics/), and its earliest regime may be sensitive to [quantum gravity](/posts/quantum-gravity-clash-general-relativity-quantum-theory/).

## 2. FLRW Assumptions

Homogeneity and isotropy lead to the FLRW metric

$$
ds^2
=
-dt^2
+
a(t)^2
\bigl[
\frac{dr^2}{1-kr^2}
+
r^2d\Omega^2
\bigr].
$$

The scale factor $a(t)$ measures expansion. The parameter $k$ encodes spatial curvature. Matter is approximated as a perfect fluid with density $\rho$ and pressure $p$.

The Friedmann equation is

$$
H^2
=
\frac{8\pi G}{3}\rho
-
\frac{k}{a^2}.
$$

The Hubble parameter $H=\dot a/a$ measures fractional expansion rate. The first term is matter-energy. The second is spatial curvature. Inflation suppresses the curvature term by rapidly increasing $a$.

## 3. Scalar-Field Inflation

A simple inflationary model uses a scalar field $\phi$ with action

$$
S
=
\int d^4x\,\sqrt{-g}
\bigl[
-\frac{1}{2}g^{\mu\nu}\partial_\mu\phi\partial_\nu\phi
-
V(\phi)
\bigr].
$$

The kinetic term measures field motion in spacetime. The potential stores vacuum-like energy. For a homogeneous field,

$$
\rho
=
\frac{1}{2}\dot\phi^2+V(\phi),
\qquad
p
=
\frac{1}{2}\dot\phi^2-V(\phi).
$$

Accelerated expansion requires approximately

$$
p\simeq -\rho,
$$

which holds when potential energy dominates kinetic energy.

## 4. Slow-Roll Conditions

Define

$$
\epsilon
=
\frac{M_{\mathrm{Pl}}^2}{2}
\bigl(
\frac{V'}{V}
\bigr)^2,
\qquad
\eta
=
M_{\mathrm{Pl}}^2
\frac{V''}{V}.
$$

Slow roll requires

$$
\epsilon\ll 1,
\qquad
|\eta|\ll 1.
$$

The first condition says the potential is not too steep. The second says the curvature of the potential is small enough that acceleration persists. The number of e-folds is

$$
N
=
\int H\,dt.
$$

Solving the horizon and flatness problems typically requires roughly 50 to 60 e-folds, depending on reheating.

## 5. Perturbations

Quantum fluctuations of the inflaton and metric become classical curvature perturbations. The scalar power spectrum is commonly written

$$
\mathcal{P}_{\mathcal{R}}(k)
=
A_s
\bigl(
\frac{k}{k_\ast}
\bigr)^{n_s-1}.
$$

The amplitude $A_s$ sets the fluctuation size. The tilt $n_s-1$ measures deviation from scale invariance. Slow-roll inflation predicts a nearly scale-invariant spectrum, consistent with observed CMB data.

## 6. Consistency Checks

**de Sitter limit.** If $V$ is constant and $\dot\phi=0$, then $H$ is constant and expansion is exponential.

**End of inflation.** Inflation ends when $\epsilon$ becomes order one. Without an exit, the model is not cosmology.

**Curvature dilution.** Since the curvature term scales as $a^{-2}$, accelerated expansion rapidly makes it negligible.

## 7. Limitations and Open Problems

Inflation does not fully solve its own initial-condition problem. The measure problem makes probabilities in eternal inflation difficult to define. The trans-Planckian issue asks whether currently observed modes began with wavelengths below the regime of controlled EFT. Reheating is model-dependent. Finally, embedding inflation in quantum gravity can constrain field ranges, potentials, and initial states.

## 8. Conclusion

Inflation is powerful because it turns accelerated expansion into predictions for geometry and perturbations. It explains flatness, horizon-scale correlations, and a nearly scale-invariant spectrum. It also leaves serious questions about initial conditions, UV sensitivity, and reheating. The right attitude is neither dismissal nor overstatement: inflation is the best-developed early-universe mechanism, but not a completed theory of the beginning.

## References

[1] A. H. Guth, "Inflationary universe: A possible solution to the horizon and flatness problems," _Physical Review D_ 23, 347-356 (1981).

[2] A. D. Linde, "A new inflationary universe scenario," _Physics Letters B_ 108, 389-393 (1982).

[3] V. Mukhanov, _Physical Foundations of Cosmology_, Cambridge University Press, 2005.

[4] D. Baumann, "TASI lectures on inflation," arXiv:0907.5424.
