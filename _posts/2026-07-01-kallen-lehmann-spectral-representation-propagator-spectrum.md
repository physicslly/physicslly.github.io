---
title: "The Källén–Lehmann Spectral Representation: How the Full Propagator Encodes the Physical Spectrum"
date: 2026-07-01 00:01:00 +0800
categories: [Physics, Theory]
tags: [physics, theoretical-physics, quantum-field-theory, spectral-representation, unitarity, two-point-function]
description: "A derivation of the Källén–Lehmann spectral representation for the exact two-point function, its interpretation in terms of the physical particle spectrum, and the constraints unitarity and causality impose on the spectral density."
math: true
---

## Abstract

The exact two-point function of a quantum field carries more structure than its free-field counterpart. The Källén–Lehmann spectral representation expresses the full time-ordered propagator as a weighted integral of free propagators, with a spectral density that directly encodes the physical particle content of the theory—stable single-particle poles, multiparticle continua, and bound states. This article derives the representation from Poincaré invariance, locality, and spectral positivity, then interprets each of its features: the pole mass, the wavefunction renormalization constant, the multiparticle threshold, and the resulting sum rules. Several limiting cases and consistency checks are worked out, and the limitations of the representation for gauge theories and theories without a mass gap are discussed.

**Keywords:** Källén–Lehmann spectral representation, two-point function, propagator, unitarity, spectral density, analyticity

## 1. Introduction and Central Question

The free propagator of a scalar field is a simple object. Its pole at $p^2 = m_0^2$ identifies the particle mass, and the residue is fixed by the canonical commutation relations. In an interacting theory, neither statement survives unchanged: the mass receives quantum corrections from self-energy insertions, the residue is renormalized by field-strength dressing, and the analytic structure develops multiparticle branch cuts above threshold.

The central question is the following. How does the full two-point function of an interacting quantum field encode the complete physical particle spectrum, and what structural constraints do unitarity and causality impose on the exact propagator?

The answer is the Källén–Lehmann spectral representation [1, 2], an exact integral representation for the time-ordered two-point function that is valid for any local, Poincaré-invariant quantum field theory satisfying the Wightman axioms. It shows that the full propagator is completely determined by a single non-negative spectral density and that the contribution of any stable single-particle state appears as an isolated pole whose residue is bounded between zero and one. The representation also provides a clean route to the optical theorem at the level of two-point functions and gives direct insight into the nature of wavefunction renormalization.

This article derives the representation for a real scalar field, works out its physical interpretation in detail, and examines several limiting cases and limitations.

## 2. Assumptions and Notation

The derivation relies on the following standard assumptions.

1. **Poincaré invariance.** There exists a unitary representation $U(a,\Lambda)$ of the Poincaré group acting on the Hilbert space, and the field transforms as

$$
U(a,\Lambda)\phi(x)U(a,\Lambda)^{-1} = \phi(\Lambda x + a).
$$

2. **Spectral condition.** The energy-momentum operator $P^\mu$ has spectrum contained in the closed forward light cone, so $p^0 \ge 0$ and $p^2 \ge 0$. There is a unique vacuum state $\lvert 0 \rangle$ with

$$
P^\mu \lvert 0 \rangle = 0.
$$

3. **Locality.** For spacelike separations, $[\phi(x), \phi(y)] = 0$.

4. **Asymptotic completeness.** In states that describe scattering experiments, the fields interpolate between the vacuum and the physical multi-particle states of the theory.

The metric signature is $(+,-,-,-)$. The field $\phi(x)$ is a real scalar field in a theory with a mass gap, so the lightest particle has a positive mass $m_h$. The momentum-space conventions follow [3]: the Fourier transform of a function $f(x)$ is

$$
\tilde{f}(p) = \int d^4x\, e^{ip\cdot x}\, f(x),
$$

and the inverse transform includes a factor $1/(2\pi)^4$.

## 3. Definitions of the Central Objects

Define the Wightman two-point function

$$
W(x-y) = \langle 0 \lvert \phi(x)\phi(y) \rvert 0 \rangle,
$$

which by translation invariance depends only on the difference $x-y$. The time-ordered (Feynman) propagator is

$$
\Delta_F(x-y) = \langle 0 \lvert T\phi(x)\phi(y) \rvert 0 \rangle
= \theta(x^0-y^0)\, W(x-y) + \theta(y^0-x^0)\, W(y-x),
$$

where $\theta$ is the Heaviside step function.

Insert a complete set of asymptotic momentum eigenstates into the Wightman function:

$$
W(x-y) = \sum_n \langle 0 \lvert \phi(x) \rvert n \rangle \langle n \lvert \phi(y) \rvert 0 \rangle.
$$

Using the translation property

$$
\phi(x) = e^{iP\cdot x}\phi(0)e^{-iP\cdot x}
$$

gives

$$
W(x-y) = \sum_n \lvert \langle 0 \lvert \phi(0) \rvert n \rangle \rvert^2 e^{-i p_n \cdot (x-y)}.
$$

The spectral density

$$
\rho(p) = (2\pi)^3 \sum_n \lvert \langle 0 \lvert \phi(0) \rvert n \rangle \rvert^2 \delta^{(4)}(p - p_n)
$$

collects the contribution of all states. Because the theory is Poincaré invariant, $\rho(p)$ depends only on $p^2$ and the sign of $p^0$. The spectral condition restricts $p^0 > 0$ for all non-vacuum states, so we write

$$
\rho(p) = \theta(p^0)\, \tilde{\rho}(p^2), \qquad \tilde{\rho}(s) \ge 0.
$$

Here $\tilde{\rho}(s)$ is supported on $s \ge 0$, and for theories with a mass gap it vanishes for $0 \le s < m_h^2$ except possibly at the single-particle mass shell.

## 4. Derivation of the Spectral Representation

The Wightman function becomes

$$
W(x-y) = \int \frac{d^4p}{(2\pi)^3}\; \theta(p^0)\, \tilde{\rho}(p^2)\, e^{-ip\cdot(x-y)}.
$$

This is the Fourier representation of $W$ in terms of the spectral density.

To obtain the time-ordered propagator, express the step function through its spectral representation:

$$
\theta(x^0) = -\frac{1}{2\pi i} \int_{-\infty}^\infty \frac{d\omega}{\omega + i\epsilon}\, e^{-i\omega x^0}.
$$

Combining this with the representation of $W$ and its counterpart $W(y-x)$, one finds

$$
\Delta_F(p) = \int \frac{d^4x}{(2\pi)^4}\, e^{ip\cdot(x-y)}\, \Delta_F(x-y)
= i \int_0^\infty dm^2\, \frac{\tilde{\rho}(m^2)}{p^2 - m^2 + i\epsilon}.
$$

The key step is that the integral over $p^0$ in the Fourier transform of the $\theta$-function factorizes from the spectral integral, producing a single pole denominator. The $i\epsilon$ prescription for the time-ordered product emerges automatically from the Fourier representation of the step function.

Writing $\rho(m^2)$ for brevity, the Källén–Lehmann representation in its standard form is

$$
\Delta_F(p^2) = i \int_0^\infty dm^2\, \frac{\rho(m^2)}{p^2 - m^2 + i\epsilon}.
\tag{1}
$$

For a free scalar field of mass $m_0$, the spectral density is a single delta function, $\rho(m^2) = \delta(m^2 - m_0^2)$, and (1) reduces to the free Feynman propagator. In an interacting theory the spectral density contains a discrete part from stable single-particle states and a continuous part from multiparticle states.

## 5. Interpretation of the Spectral Density

The power of the representation (1) is that every feature of the full propagator maps directly onto a physical property of the theory.

**Single-particle pole.** A stable one-particle state of mass $m_h$ contributes a discrete term

$$
\rho(m^2) = Z\, \delta(m^2 - m_h^2) + \rho_c(m^2),
$$

where

$$
Z = \lvert \langle 0 \lvert \phi(0) \rvert p,\lambda \rangle \rvert^2
$$

is the wavefunction renormalization constant. The full propagator near the pole behaves as

$$
\Delta_F(p^2) \;=\; \frac{i Z}{p^2 - m_h^2 + i\epsilon} + \text{regular},
$$

so $m_h$ is the physical (pole) mass and $Z$ is the residue.

**Multiparticle continuum.** The continuum part $\rho_c(m^2)$ is supported on $m^2 \ge M_{\mathrm{th}}^2$, where $M_{\mathrm{th}}$ is the lightest multiparticle threshold. The continuum begins at the branch cut of the self-energy function $\Pi(p^2)$.

**Sum rule.** The canonical equal-time commutation relation

$$
[\phi(0,\mathbf{x}), \partial^0 \phi(0,\mathbf{y})] = i\delta^{(3)}(\mathbf{x} - \mathbf{y})
$$

implies a sum rule for the spectral density. Differentiating the commutator spectral representation and evaluating at equal times gives

$$
\int_0^\infty dm^2\, \rho(m^2) = 1.
\tag{2}
$$

Writing the one-particle contribution separately yields

$$
Z + \int_{M_{\mathrm{th}}^2}^\infty dm^2\, \rho_c(m^2) = 1.
$$

Because $\rho_c(m^2) \ge 0$, the sum rule implies $0 \le Z \le 1$. The wavefunction renormalization constant is strictly less than one in any nontrivial interacting theory, a direct consequence of the fact that the field creates not only single-particle states but also multi-particle excitations. The deviation $1 - Z$ measures the weight of the multiparticle admixture in the field.

**Spectral positivity.** The spectral density is non-negative by construction because it is a sum of squares of matrix elements. This positivity, together with the representation (1), implies that the full propagator satisfies a dispersion relation: for spacelike momenta $p^2 < 0$, the denominator never vanishes and the representation converges.

## 6. Consistency Checks and Limiting Cases

The representation (1) passes several consistency checks.

**Free-field limit.** When interactions are turned off, the only intermediate state is the single-particle state, so $\rho(m^2) = \delta(m^2 - m_0^2)$ and $Z = 1$. The sum rule (2) is saturated by the discrete term. The propagator reduces to the familiar form.

**Conformal limit.** In a conformal field theory there is no mass gap and no discrete particle pole. The spectral density for a primary scalar field of scaling dimension $\Delta$ takes the power-law form

$$
\rho(m^2) \propto (m^2)^{\Delta - 2},
$$

which follows from scale invariance. The representation (1) then reproduces the standard conformal two-point function after Fourier transformation. The sum rule (2) is not directly applicable in this case because the theory lacks a particle interpretation at short distances.

**Perturbation theory.** In $\phi^4$ theory at one loop, the self-energy $\Pi(p^2)$ develops an imaginary part above the two-particle threshold $p^2 = 4m^2$. The spectral density derived from $\Pi(p^2)$ via the optical theorem

$$
\rho_c(m^2) = \frac{1}{\pi}\, \frac{\mathrm{Im}\,\Pi(m^2)}{|m^2 - m_0^2 - \Pi(m^2)|^2}
$$

is indeed positive and reproduces the perturbative cut structure. This is a direct verification that the spectral representation is consistent with unitarity: the positivity of the spectral integral guarantees a non-negative imaginary part for the self-energy.

**Bound states.** If the theory supports a two-particle bound state of mass $m_B < 2m$, the spectral density acquires an additional discrete term $Z_B \delta(m^2 - m_B^2)$ below the continuum threshold. The bound-state pole appears in the propagator on the same footing as the elementary particle pole, reflecting the fact that the interpolating field $\phi$ couples to any state with the same quantum numbers, whether elementary or composite.

## 7. Relation to Existing Frameworks

The Källén–Lehmann representation is not an isolated result. It is the zero-multiplicity special case of the general dispersion relations that the S-matrix satisfies as a consequence of causality and unitarity. The spectral density $\rho(m^2)$ is directly related to the discontinuity of the propagator across its branch cut:

$$
\mathrm{Disc}\,\Delta_F(p^2) = \Delta_F(p^2 + i\epsilon) - \Delta_F(p^2 - i\epsilon) = 2\pi i\, \rho(p^2).
$$

This is the tree-level expression of the optical theorem for the two-point function, and it connects directly to the [S-matrix program and dispersion relations](/posts/scattering-amplitudes-s-matrix-on-shell-methods/).

The representation also connects naturally to the broader reconstruction program of axiomatic quantum field theory. The Euclidean Schwinger functions obtained by analytic continuation of the Wightman functions satisfy the Källén–Lehmann representation in Euclidean momentum space, and the [reflection-positivity condition](/posts/osterwalder-schrader-reflection-positivity-euclidean-qft/) [4] guarantees the spectral positivity $\rho(m^2) \ge 0$ that is essential for unitarity.

In the language of effective field theory, the spectral representation constrains the matching of Wilson coefficients: any ultraviolet completion whose two-point function satisfies the Källén–Lehmann representation yields a spectral density that automatically respects unitarity bounds and analyticity, ensuring that the low-energy effective theory can be consistently UV-completed.

Full propagators that satisfy the Källén–Lehmann representation also necessarily satisfy the [Schwinger–Dyson equations](/posts/schwinger-dyson-equations-structure-quantum-effective-action/) for the two-point function, where the self-energy $\Pi(p^2)$ is defined by

$$
\Delta_F^{-1}(p^2) = p^2 - m_0^2 - \Pi(p^2),
$$

and the spectral representation provides the explicit solution

$$
\Pi(p^2) = \int dm^2\,
\frac{\rho(m^2)(p^2 - m_0^2)}{p^2 - m^2 + i\epsilon}.
$$

## 8. Limitations and Open Problems

The Källén–Lehmann representation as derived above has several important limitations.

**Gauge theories.** For gauge fields such as the photon or gluon, the derivation fails because the assumption of positivity of the metric on the Hilbert space is incompatible with the indefinite metric required for covariant gauge fixing. The spectral density for a gauge field is not positive-definite, and the simple pole structure is replaced by more complicated singularities. The physical degrees of freedom must be extracted from the gauge-invariant correlators, which often require a separate analysis using the BRST formalism.

**Massless particles.** When the theory contains massless particles, the infrared structure of the propagator changes qualitatively. The spectral density for a massless scalar field diverges at $m^2 = 0$, and the representation (1) requires an infrared regulator. In QED, the electron propagator develops an infrared branch cut rather than an isolated pole, a phenomenon known as the infrared catastrophe that is resolved by inclusive cross-section measurements.

**Unstable particles.** The representation (1) only distinguishes stable single-particle states from the continuum. An unstable resonance appears not as a pole on the real axis but as a complex pole on the second Riemann sheet, which the Källén–Lehmann representation does not directly exhibit. The resonance manifests itself indirectly as a peak in the spectral density $\rho_c(m^2)$, but the width must be extracted by analytic continuation across the cut.

**Non-perturbative access.** Although the representation is exact, computing the spectral density $\rho(m^2)$ from first principles in a strongly interacting theory is difficult. Lattice QCD provides numerical access to spectral functions via the maximum entropy method or Bayesian reconstruction of Euclidean correlators, but the inverse problem is ill-conditioned. Progress on this front remains an active research area.

## 9. Relation to the Theory of Everything

A unified theory that consistently describes all interactions must respect the fundamental principles—unitarity, causality, and locality—from which the Källén–Lehmann representation follows. Any candidate theory of quantum gravity, whether based on strings, loops, or discrete structures, must produce a well-defined two-point function for its fundamental degrees of freedom that satisfies a spectral representation of this form, or a suitable generalization.

In this sense the spectral representation is not a feature of any particular model but a consequence of the framework: it serves as a consistency condition that any local, unitary quantum field theory must satisfy. A non-perturbative formulation of quantum gravity that ultimately reduces to an effective quantum field theory at low energies must reproduce the analytic structure of the spectral representation for its propagating degrees of freedom, or provide a convincing explanation for why the assumptions of the derivation break down.

## 10. Common Pitfalls

Several misunderstandings about the spectral representation recur in the literature and in classroom discussions.

- **The sum rule does not imply $Z = 1$ in a free theory only.** The sum rule (2) always holds in a canonically normalized theory; the difference is that in an interacting theory the weight is distributed between the discrete pole and the continuum, so $Z < 1$.

- **The spectral density is not the imaginary part of the self-energy.** It is related to the imaginary part of the *full propagator*.

- **The representation is not limited to scalar fields.** Identical derivations hold for fermions and for conserved currents (where the transverse structure modifies the tensor decomposition).

- **The pole mass $m_h$ is not the bare mass $m_0$.** The bare mass is the parameter in the Lagrangian; the pole mass is the physical mass read off from the propagator pole. The difference is encoded in the self-energy: $m_h^2 = m_0^2 + \Pi(m_h^2)$.

## 11. Conclusion

The Källén–Lehmann spectral representation is a rigorous and physically transparent encoding of the exact two-point function in relativistic quantum field theory. It expresses the full propagator as a weighted integral of free propagators, with a spectral density that is non-negative by unitarity and integrates to one by the canonical commutation relations. The representation cleanly separates the contribution of stable particles from the multiparticle continuum and provides a direct link between the analytic structure of the propagator and the physical spectrum of the theory.

The constraints it imposes—spectral positivity, the bound $0 \le Z \le 1$, the threshold behaviour of the continuum—are consequences of the fundamental principles of quantum field theory and serve as non-perturbative checks on any approximation scheme. While the representation has limitations for gauge theories, massless particles, and unstable resonances, it remains one of the most general and useful exact results in quantum field theory [3, 5].

## References

[1] G. Källén, *Quantenelektrodynamik*, Handbuch der Physik V/1, Springer, 1958.

[2] H. Lehmann, *Über Eigenschaften von Ausbreitungsfunktionen und Renormierungskonstanten quantisierter Felder*, Nuovo Cimento 11, 342 (1954).

[3] M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory*, Westview Press, 1995.

[4] K. Osterwalder and R. Schrader, *Axioms for Euclidean Green's Functions*, Comm. Math. Phys. 31, 83 (1973).

[5] C. Itzykson and J.-B. Zuber, *Quantum Field Theory*, Dover, 2005.
