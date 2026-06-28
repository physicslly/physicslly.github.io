---
title: "Scattering Amplitudes and the S-Matrix Program: From the Optical Theorem to Modern On-Shell Methods"
date: 2026-06-26 00:01:00 +0800
categories: [Physics, Quantum Field Theory]
tags: [physics, theoretical-physics, quantum-field-theory, scattering-amplitudes, s-matrix, on-shell-methods, unitarity, lsz]
description: "A rigorous treatment of the S-matrix program: LSZ reduction, the optical theorem and Cutkosky rules, dispersion relations, and modern on-shell methods including BCFW recursion and color-kinematics duality."
math: true
---

## Abstract

Scattering amplitudes are the part of quantum field theory closest to experiment: they describe transitions between asymptotic particle states. The modern on-shell program asks how much of QFT can be reconstructed from on-shell data alone. This article develops that question from LSZ reduction, unitarity, and the optical theorem to factorization, cuts, BCFW recursion, and the double-copy relation between gauge theory and gravity. The emphasis is not on calculational shortcuts. It is on the structural constraints imposed by locality, analyticity, and probability conservation, and on the places where those constraints are insufficient without extra assumptions [1], [2].

**Keywords:** scattering amplitudes, S-matrix, LSZ reduction, optical theorem, unitarity cuts, BCFW recursion, double copy

## 1. Introduction

Fields are not measured directly in a detector. What is measured is the probability for one set of asymptotic states to become another. The S-matrix packages those transition amplitudes. That fact gives the on-shell program its sharp question: how much of quantum field theory can be reconstructed from on-shell data?

The old S-matrix program tried to build physics from unitarity, analyticity, crossing, and symmetry without committing to a Lagrangian. The modern amplitudes program is more modest and more successful. It uses Lagrangians when useful, but treats them as one representation of deeper on-shell structures. Poles know about particles. Residues know about lower-point amplitudes. Branch cuts know about multiparticle thresholds. Soft limits know about symmetry.

This viewpoint is close to the general framework of [quantum field theory](/posts/quantum-field-theory-framework-particles-fields/), but it reorganizes the data. Gauge redundancy, discussed in [Gauge Symmetry and the Structure of Fundamental Interactions](/posts/gauge-symmetry-structure-fundamental-interactions/), disappears from final amplitudes. Connections to gravity and holography meet naturally with [AdS/CFT](/posts/adscft-holographic-duality-and-quantum-gravity/), although flat-space scattering is not the same object as boundary CFT data.

## 2. Assumptions and Notation

Work in four-dimensional Minkowski spacetime with metric signature $(+,-,-,-)$. The basic assumptions are asymptotic particle states, unitarity of the S-matrix, analyticity in complexified kinematic variables away from physical singularities, and locality as reflected in factorization on physical poles.

These assumptions are strong. They fail or become subtle in confining theories, theories without a mass gap, gauge theories with infrared divergences, and curved spacetimes where global in/out particle states may not exist.

For a $2\to 2$ process, define the Mandelstam invariants

$$
s = (p_1+p_2)^2,
\qquad
t = (p_1-p_3)^2,
\qquad
u = (p_1-p_4)^2 .
$$

They obey

$$
s+t+u = \sum_i m_i^2 .
$$

The S-matrix is written

$$
S = \mathbb{1} + iT .
$$

The identity term represents no scattering. The operator $T$ contains the interacting transition amplitudes. After removing the momentum-conserving delta function and normalization factors, the remaining invariant amplitude is denoted $\mathcal{M}$.

## 3. LSZ: From Correlators to Amplitudes

The LSZ reduction formula explains why an amplitude is an on-shell residue of a correlation function [1]. For a scalar field with one-particle overlap

$$
\langle 0 \lvert \phi(0) \rvert p \rangle
=
\sqrt{Z_\phi},
$$

an $n$-point connected amplitude is obtained schematically as

$$
\mathcal{M}_n
=
\bigl[
\prod_{i=1}^n
\lim_{p_i^2\to m_i^2}
\frac{p_i^2-m_i^2}{\sqrt{Z_i}}
\bigr]
G_n(p_1,\ldots,p_n) .
$$

Here $G_n$ is the Fourier-transformed time-ordered connected correlator. The factor $p_i^2-m_i^2$ amputates the external propagator. The limit $p_i^2\to m_i^2$ projects onto the physical mass shell. The residue factor $Z_i$ corrects the normalization of the interpolating field.

This formula is a useful discipline. Off-shell Green's functions depend on field choices and gauge choices. On-shell amplitudes do not. In a confining theory, elementary colored fields do not create asymptotic states, so LSZ cannot be applied to them as if they were particles.

## 4. Unitarity and the Optical Theorem

Unitarity is probability conservation:

$$
S^\dagger S = \mathbb{1}.
$$

Using $S=\mathbb{1}+iT$ gives

$$
-i(T-T^\dagger)
=
T^\dagger T .
$$

Insert an initial state $\lvert i \rangle$ and final state $\lvert f \rangle$:

$$
-i
\bigl[
\langle f \lvert T \rvert i \rangle
-
\langle f \lvert T^\dagger \rvert i \rangle
\bigr]
=
\sum_X
\langle f \lvert T^\dagger \rvert X \rangle
\langle X \lvert T \rvert i \rangle .
$$

The sum runs over a complete set of on-shell intermediate states. For forward scattering, $f=i$, this becomes

$$
2\,\mathrm{Im}\,\mathcal{M}(i\to i)
=
\sum_X
\int d\Pi_X\,
|\mathcal{M}(i\to X)|^2 .
$$

The left side is the absorptive part of the forward elastic amplitude. The right side is a sum over total transition probabilities into all allowed final states. This is the optical theorem. Its force is practical: if a calculation gives a negative total rate or misses an allowed cut, it is wrong.

## 5. Poles, Residues, Cuts, and Factorization

The analytic structure of an amplitude has a physical dictionary. A simple pole at

$$
P^2 \to m^2
$$

means that an intermediate particle can go on shell. Locality requires the residue to factorize:

$$
\mathcal{A}_n
\longrightarrow
\sum_h
\mathcal{A}_L(\ldots,P^h)
\frac{i}{P^2-m^2+i\epsilon}
\mathcal{A}_R(-P^{-h},\ldots).
$$

The denominator is the propagating on-shell channel. The sum over $h$ runs over physical intermediate polarizations or helicities. The left and right amplitudes are lower-point on-shell data. This is the central recursive idea behind much of modern amplitudes.

Branch cuts appear when multiparticle states can go on shell. Cutkosky's rule replaces cut propagators by on-shell delta functions [2]:

$$
\frac{i}{p^2-m^2+i\epsilon}
\longrightarrow
2\pi\,\delta^{(+)}(p^2-m^2).
$$

The discontinuity across a cut is therefore

$$
\mathrm{Disc}\,\mathcal{A}
=
\sum_{\mathrm{states}}
\int d\Pi\,
\mathcal{A}_L
\mathcal{A}_R .
$$

Term by term: the discontinuity measures the jump across a branch cut; the phase-space integral puts internal particles on shell; the state sum includes all allowed internal species and helicities; the product of lower amplitudes expresses unitarity in factorized form.

## 6. BCFW Recursion

At tree level in many massless theories, amplitudes are rational functions of spinor-helicity variables. BCFW recursion deforms two external momenta into complex momenta while preserving momentum conservation and on-shellness [3]:

$$
\lambda_i
\mapsto
\lambda_i + z\lambda_j,
\qquad
\tilde{\lambda}_j
\mapsto
\tilde{\lambda}_j - z\tilde{\lambda}_i .
$$

The deformed amplitude $A_n(z)$ is meromorphic in $z$. If

$$
A_n(z) \to 0
\qquad
\text{as}
\qquad
z\to\infty,
$$

Cauchy's theorem reconstructs the physical amplitude:

$$
A_n(0)
=
\sum_P\sum_h
A_L(z_P,h)
\frac{i}{P^2}
A_R(z_P,-h).
$$

The partitions $P$ are the factorization channels separating the shifted legs. The value $z_P$ is fixed by putting the internal momentum on shell. The helicity sum supplies the physical intermediate states.

The boundary condition at infinity is not a footnote. If it fails, the recursion misses a boundary term. A useful way to see the point is the following: factorization determines residues at finite poles, but it does not determine polynomial contact terms unless the large-$z$ behavior is controlled.

## 7. Color-Kinematics and Double Copy

Gauge-theory tree amplitudes can be arranged as

$$
\mathcal{A}_n^{\mathrm{tree}}
=
g^{n-2}
\sum_i
\frac{c_i n_i}{D_i},
$$

where $c_i$ are color factors, $n_i$ are kinematic numerators, and $D_i$ are products of propagator denominators. Color factors obey Jacobi identities such as

$$
c_i+c_j+c_k=0 .
$$

Color-kinematics duality asserts that the numerators can often be chosen so that

$$
n_i+n_j+n_k=0
$$

whenever the corresponding color identity holds [4]. Replacing color with a second copy of kinematics gives a gravity amplitude:

$$
\mathcal{M}_n^{\mathrm{tree}}
=
\bigl(
\frac{\kappa}{2}
\bigr)^{n-2}
\sum_i
\frac{n_i\tilde{n}_i}{D_i}.
$$

This should not be read as a proof of unification. It is a structural analogy with enormous computational power. At tree level the double copy is well established; at loop level it is highly constrained and widely checked, but the most general foundations remain an active research problem [5].

## 8. Consistency Checks and Limiting Cases

**Forward limit.** Setting $f=i$ in the unitarity relation must reproduce a positive total cross section. This is the fastest check on signs and normalization in the optical theorem.

**Factorization limit.** As $P^2\to m^2$, the residue of the pole must equal a product of lower-point amplitudes. Failure here is not a minor algebra error; it violates locality or the assumed particle spectrum.

**Soft and collinear limits.** Gauge-theory amplitudes have universal behavior when a gauge boson becomes soft or two massless particles become collinear. A BCFW result that fails these limits is missing a channel, a helicity contribution, or a boundary term.

**Low-energy EFT limit.** If a heavy particle of mass $M$ is integrated out, the full amplitude must expand in powers of $E/M$ and match the operators of the effective theory. This is the on-shell version of the logic in [effective field theory](/posts/effective-field-theory-layered-fundamental-physics/).

## 9. Limitations and Open Problems

The S-matrix is not always the right object. Confinement prevents colored quarks and gluons from appearing as asymptotic states. Massless gauge theories have infrared divergences, so inclusive observables or dressed states are needed. Curved spacetime may not have a global notion of in and out particles. Cosmology is especially resistant to a flat-space S-matrix interpretation.

There are also theoretical limits inside the on-shell program itself. Analyticity assumptions require control over high-energy behavior. Dispersion relations may need subtractions. Recursion relations need valid large-complex-momentum behavior. Non-perturbative definitions of the S-matrix remain hard in strongly coupled four-dimensional theories. The on-shell program is powerful because it uses less unphysical structure, but it does not eliminate the need for dynamical input.

## 10. Conclusion

Scattering amplitudes expose the part of quantum field theory that survives contact with asymptotic measurement. LSZ identifies amplitudes as on-shell residues. Unitarity gives the optical theorem and cutting rules. Locality gives factorization on poles. Analyticity lets those data constrain, and sometimes reconstruct, the full answer. The modern on-shell program works because these principles are stronger than they first appear, but also because its assumptions are explicit enough to fail cleanly in theories where ordinary scattering is not available.

## References

[1] H. Lehmann, K. Symanzik, and W. Zimmermann, "On the formulation of quantized field theories," _Nuovo Cimento_ 1, 205-225 (1955).

[2] R. E. Cutkosky, "Singularities and discontinuities of Feynman amplitudes," _Journal of Mathematical Physics_ 1, 429-433 (1960).

[3] R. Britto, F. Cachazo, B. Feng, and E. Witten, "Direct proof of tree-level recursion relation in Yang-Mills theory," _Physical Review Letters_ 94, 181602 (2005).

[4] Z. Bern, J. J. M. Carrasco, and H. Johansson, "New relations for gauge-theory amplitudes," _Physical Review D_ 78, 085011 (2008).

[5] Z. Bern, J. J. M. Carrasco, and H. Johansson, "Perturbative quantum gravity as a double copy of gauge theory," _Physical Review Letters_ 105, 061602 (2010).

[6] R. J. Eden, P. V. Landshoff, D. I. Olive, and J. C. Polkinghorne, _The Analytic S-Matrix_, Cambridge University Press, 1966.

[7] S. Weinberg, _The Quantum Theory of Fields, Volume I: Foundations_, Cambridge University Press, 1995.

[8] H. Elvang and Y.-t. Huang, _Scattering Amplitudes in Gauge Theory and Gravity_, Cambridge University Press, 2015.
