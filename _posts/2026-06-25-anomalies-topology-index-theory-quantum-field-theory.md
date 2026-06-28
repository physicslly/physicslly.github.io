---
title: "Anomalies, Topology, and Index Theory in Quantum Field Theory"
date: 2026-06-25 00:01:00 +0800
categories: [Physics, Theory]
tags: [physics, theoretical-physics, quantum-field-theory, anomalies, topology, index-theory, mathematical-physics]
description: "A rigorous treatment of chiral anomalies and the Atiyah-Singer index theorem, with emphasis on anomaly cancellation conditions, topological invariants, and the structural constraints these impose on consistent quantum field theories."
math: true
---

## Abstract

An anomaly is the failure of a classical symmetry to survive quantization. That sentence is compact, but it hides several distinct mechanisms: a regulator can fail to preserve a current, a fermion determinant can acquire a nontrivial phase, or a global obstruction can prevent the path integral from being defined consistently. This article asks when a classical symmetry fails to survive quantization. I focus on chiral fermions coupled to background gauge fields, derive the axial anomaly with Fujikawa's method, connect the local anomaly to characteristic classes and the Atiyah-Singer index theorem, and separate perturbative anomalies from global anomalies and topological terms. The useful lesson is not that symmetries sometimes break; it is that quantum consistency can be a topological constraint on the allowed matter content [1], [2].

**Keywords:** anomalies, chiral fermions, Fujikawa method, index theorem, topology, gauge consistency

## 1. Introduction

Classical symmetries are promises made before the path integral is regulated. Quantum theory asks whether those promises can be kept after one defines the measure, the determinant, and the ultraviolet limit. Sometimes the answer is no. That failure is an anomaly.

The central question is this: when does a classical symmetry fail to survive quantization? For a global symmetry, the failure can be a physical effect. The axial anomaly explains why the classical axial current of massless QED is not conserved. For a gauge symmetry, the same kind of failure is usually fatal, because gauge symmetry is not an optional physical symmetry; it is the redundancy that removes unphysical states.

This discussion sits between [gauge symmetry](/posts/gauge-symmetry-structure-fundamental-interactions/) and [BRST symmetry](/posts/brst-symmetry-gauge-theories/). The topological side connects naturally to [Topology, Geometry, and the Search for Deeper Physical Laws](/posts/topology-geometry-deeper-physical-laws/), while the path-integral language is the one used throughout [Quantum Field Theory as a Framework for Particles and Fields](/posts/quantum-field-theory-framework-particles-fields/).

## 2. Assumptions and Scope

Work in Euclidean signature on a compact spin manifold $M$ of even dimension $d=2n$. The fermions are massless unless stated otherwise, and the gauge field $A_\mu$ is treated as a background connection. This is enough to see the anomaly without first solving gauge-field dynamics.

Let the covariant Dirac operator be

$$
D_A
=
i\gamma^\mu(\nabla_\mu + A_\mu).
$$

The gamma matrices obey

$$
\{\gamma^\mu,\gamma^\nu\}
=
2g^{\mu\nu}.
$$

The chirality operator in even dimension is denoted $\Gamma_{\mathrm{ch}}$ and satisfies

$$
\Gamma_{\mathrm{ch}}^2=1,
\qquad
\{\Gamma_{\mathrm{ch}},D_A\}=0
$$

for a massless Dirac operator. The chiral projectors are

$$
P_\pm
=
\frac{1}{2}(1\pm \Gamma_{\mathrm{ch}}).
$$

The index of the chiral Dirac operator is

$$
\operatorname{Ind}(D_A)
=
\dim \ker D_A^+
-
\dim \ker D_A^- .
$$

Term by term, the first dimension counts zero modes of positive chirality, the second counts zero modes of negative chirality, and the difference is stable under smooth deformations of the background. That stability is why topology enters.

## 3. Fujikawa Derivation of the Axial Anomaly

Consider a massless Dirac fermion in four dimensions:

$$
S
=
\int d^4x\,
\bar\psi\, i\gamma^\mu(\partial_\mu + A_\mu)\psi .
$$

The classical action is invariant under the local axial rotation

$$
\psi
\mapsto
e^{i\alpha(x)\gamma_5}\psi,
\qquad
\bar\psi
\mapsto
\bar\psi e^{i\alpha(x)\gamma_5}.
$$

The subtlety is the measure. Expand the fermion in eigenfunctions of the Dirac operator,

$$
\psi(x)
=
\sum_n a_n \phi_n(x),
\qquad
\bar\psi(x)
=
\sum_n \bar b_n \phi_n^\dagger(x).
$$

The formal measure is

$$
\mathcal{D}\psi\,\mathcal{D}\bar\psi
=
\prod_n da_n\,d\bar b_n .
$$

Under the axial rotation this measure acquires a Jacobian. Formally it contains the divergent trace

$$
\operatorname{Tr}\bigl(\alpha\gamma_5\bigr).
$$

Fujikawa's point was to regulate the trace in a gauge-covariant way [3]:

$$
\operatorname{Tr}\bigl(\alpha\gamma_5\bigr)
\mapsto
\lim_{M\to\infty}
\operatorname{Tr}
\bigl[
\alpha(x)\gamma_5
\exp\bigl(
-\frac{D_A^2}{M^2}
\bigr)
\bigr].
$$

The heat-kernel expansion gives

$$
\partial_\mu J_5^\mu
=
\frac{1}{16\pi^2}
\operatorname{tr}
F_{\mu\nu}\tilde F^{\mu\nu}.
$$

Here $J_5^\mu$ is the axial current. The dual field strength is

$$
\tilde F^{\mu\nu}
=
\frac{1}{2}\epsilon^{\mu\nu\rho\sigma}F_{\rho\sigma}.
$$

The interpretation is precise. The left side is the divergence of a current that was conserved classically. The right side is the topological density of the background gauge field. The trace runs over gauge indices. The coefficient is fixed by the ultraviolet regulator, but once the regulator preserves gauge covariance the final anomaly is not adjustable by ordinary renormalization.

## 4. Index Theory and Topological Charge

The same density appears in the index theorem. In four dimensions the gauge part of the index is

$$
\operatorname{Ind}(D_A)
=
\frac{1}{8\pi^2}
\int_M
\operatorname{tr}(F\wedge F)
$$

up to representation-dependent normalization. The two sides look different. The left side is analytic: it counts zero modes of a differential operator. The right side is topological: it is a characteristic number of the gauge bundle.

This is the payoff. The anomaly is local, but its integrated form knows about global topology. For instanton number $k$,

$$
\frac{1}{8\pi^2}
\int_M
\operatorname{tr}(F\wedge F)
=
k .
$$

The axial charge violation is therefore tied to the difference between left- and right-handed zero modes. This is why anomaly equations are more rigid than ordinary loop corrections.

## 5. Perturbative, Global, and Topological Anomalies

Perturbative anomalies are visible in local current divergences and in triangle diagrams. In a chiral gauge theory, the dangerous cubic gauge anomaly has the schematic form

$$
\mathcal{A}^{abc}
\propto
\operatorname{tr}_R
\bigl(
T^a\{T^b,T^c\}
\bigr).
$$

The generators $T^a$ act in the fermion representation $R$. If this symmetric trace does not cancel after summing over all chiral fermions, the gauge theory is inconsistent.

Global anomalies are different. They are not detected by an infinitesimal gauge variation. Witten's $SU(2)$ anomaly is the canonical example: a theory with an odd number of left-handed fermion doublets has a sign ambiguity under a large gauge transformation [4]. No local triangle diagram announces the problem.

Topological terms are different again. A theta term,

$$
S_\theta
=
\frac{\theta}{8\pi^2}
\int_M
\operatorname{tr}(F\wedge F),
$$

is gauge-invariant modulo global periodicity and changes the quantum theory without being an anomaly by itself. The distinction matters: not every topological density is an obstruction, and not every obstruction is local.

## 6. Consistency Checks

**Vectorlike theories.** A Dirac fermion with left and right components in conjugate representations has canceling gauge anomalies. This is why QED is consistent even though it has an axial anomaly: the vector gauge current remains conserved.

**Standard Model cancellation.** One generation of Standard Model fermions cancels all gauge anomalies when hypercharges are assigned correctly. This is not aesthetic bookkeeping. Without the cancellation, the electroweak gauge theory would fail at the quantum level.

**Mass terms.** Adding a fermion mass explicitly breaks axial symmetry. Then the divergence contains both the classical mass term and the anomaly:

$$
\partial_\mu J_5^\mu
=
2im\bar\psi\gamma_5\psi
+
\frac{1}{16\pi^2}
\operatorname{tr}
F_{\mu\nu}\tilde F^{\mu\nu}.
$$

The first term is explicit breaking. The second is quantum-mechanical and remains in the massless limit.

## 7. Limitations and Open Problems

Intermediate anomaly calculations are regulator dependent. Pauli-Villars, dimensional regularization, heat kernels, and lattice regulators distribute the breaking differently among currents. The physical question is not whether a particular current definition can be shifted by a counterterm, but whether all required gauge symmetries can be preserved simultaneously.

Global anomalies are subtler because they require control over the full determinant line bundle, not just local current algebra. Non-perturbative definitions are also delicate for chiral gauge theories. The lattice gives a clean regulator for vectorlike theories, but chiral gauge theories require additional structure, such as overlap or domain-wall fermions, to represent chirality and topology correctly.

## 8. Conclusion

Anomalies are obstructions to quantizing symmetries, and the strongest obstructions are topological. Fujikawa's method shows how the path-integral measure fails. The index theorem explains why the answer is stable. Perturbative anomaly cancellation protects gauge consistency, while global anomalies test the topology of the full gauge group. A useful rule is simple: a global anomaly can be a signal; a gauge anomaly is a consistency failure.

## References

[1] S. L. Adler, "Axial-vector vertex in spinor electrodynamics," _Physical Review_ 177, 2426-2438 (1969).

[2] J. S. Bell and R. Jackiw, "A PCAC puzzle: pi0 to gamma gamma in the sigma model," _Nuovo Cimento A_ 60, 47-61 (1969).

[3] K. Fujikawa, "Path-integral measure for gauge-invariant fermion theories," _Physical Review Letters_ 42, 1195-1198 (1979).

[4] E. Witten, "An SU(2) anomaly," _Physics Letters B_ 117, 324-328 (1982).

[5] M. F. Atiyah and I. M. Singer, "The index of elliptic operators: I," _Annals of Mathematics_ 87, 484-530 (1968).

[6] L. Alvarez-Gaume and E. Witten, "Gravitational anomalies," _Nuclear Physics B_ 234, 269-330 (1984).
