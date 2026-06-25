---
title: "String Theory and the Worldsheet: Conformal Gauge and the Graviton"
date: 2026-06-24 10:00:00 +0700
categories: [Physics, String Theory]
tags: [physics, theoretical-physics, string-theory, quantum-gravity, conformal-field-theory, unification]
description: "A rigorous treatment of the worldsheet formulation of string theory."
math: true
---


## Abstract

String theory replaces point-like particles with one-dimensional extended objects. Their dynamics is governed by a two-dimensional conformal field theory on the worldsheet. The closed-string spectrum contains a massless spin-2 state that reproduces general relativity at low energies, while open strings yield Yang-Mills gauge bosons. This article develops the worldsheet formulation: the Nambu-Goto and Polyakov actions, symmetries, gauge fixing, canonical quantization, the Virasoro algebra, the no-ghost theorem, the critical dimension D = 26, and the massless spectrum including the graviton.

**Keywords:** string theory, worldsheet, Polyakov action, Virasoro algebra, BRST quantization, critical dimension, graviton

## 1. Introduction

The central obstacle to quantizing general relativity is the perturbative non-renormalizability of the Einstein-Hilbert action in four dimensions. Power-counting arguments show that the superficial degree of divergence of Feynman diagrams in perturbative quantum gravity grows with the loop order, requiring an infinite number of independent counterterms — one for each curvature-squared, curvature-cubed, and higher-derivative invariant [1]. String theory resolves this pathology by replacing point-like elementary particles with one-dimensional extended objects whose finite spatial extent acts as a natural ultraviolet regulator. All string amplitudes are finite at each order of perturbation theory, and the infinite tower of massive states conspires to cancel ultraviolet divergences in a manner impossible in point-particle field theory.

The historical origin of string theory lies in the dual resonance model of the strong interaction. The Veneziano amplitude for four-tachyon scattering,

$$
A(s,t) = \frac{\Gamma(-\alpha(s)) \Gamma(-\alpha(t))}{\Gamma(-\alpha(s)-\alpha(t))},
$$

with linear Regge trajectories $\alpha(s) = \alpha(0) + \alpha' s$, exhibited the property of crossing symmetry and Regge behavior long before a dynamical explanation was available [2]. This amplitude was later shown to follow from a relativistic string model. The critical discovery that the closed-string spectrum necessarily contains a massless spin-2 particle — identified with the graviton through the equivalence principle — transformed string theory from a model of hadrons into a candidate quantum theory of gravity [3].

This article develops the worldsheet formulation of the bosonic string as a pedagogical foundation. All essential features — the Virasoro algebra, the critical dimension, the emergence of massless states, and modular invariance — are already present in this simplest case. The supersymmetric extension (superstring theory) is discussed at the conceptual level, but a full treatment of the Neveu-Schwarz-Ramond or Green-Schwarz formalisms lies beyond the scope of this article [4,5].

## 2. Preliminaries and Notation

The fundamental object in string theory is the embedding of a one-dimensional extended object, the string, into a D-dimensional target spacetime. As the string propagates, it sweeps out a two-dimensional Lorentzian surface called the worldsheet, parametrized by coordinates $(\tau, \sigma)$, where $\tau \in \mathbb{R}$ plays the role of evolution time and $\sigma \in [0,\pi]$ parametrizes the spatial extent of an open string. For a closed string, $\sigma \in [0,2\pi)$ with periodic identification.

The embedding functions $X^{\mu}(\tau, \sigma)$ for $\mu = 0,1,\ldots,D-1$ map the worldsheet into a D-dimensional Minkowski target space with metric $\eta_{\mu\nu} = \mathrm{diag}(-1,+1,\ldots,+1)$. The dynamics of the string is governed by the area swept out by the worldsheet, analogous to the action for a relativistic point particle but extended to one dimension.

The induced metric on the worldsheet is the pullback of the target-space metric:

$$
h_{ab} = \partial_a X^{\mu} \partial_b X_{\mu} = \eta_{\mu\nu} \partial_a X^{\mu} \partial_b X^{\nu},
$$

where a, b = 0, 1 denote worldsheet indices. The simplest classical action for the string is the Nambu-Goto action, proportional to the invariant area of the worldsheet:

$$
S_{\mathrm{NG}} = -T \int d\tau\, d\sigma\, \sqrt{-\det h_{ab}}.
$$

The string tension $T = 1/(2\pi\alpha')$ has dimensions of $[\mathrm{mass}]^2$; the Regge slope parameter $\alpha'$ has dimensions of $[\mathrm{length}]^2$ and defines the fundamental string length scale $l_s = \sqrt{2\alpha'}$. The string mass scale is $M_s = 1/l_s$, typically taken near the Planck scale. In this article, we set $\alpha' = 1/2$, giving $T = 1/\pi$ and $l_s = 1$, unless otherwise stated.

The square root in the Nambu-Goto action makes quantization cumbersome. An equivalent action with polynomial field content is the Polyakov action, which introduces an auxiliary worldsheet metric $g_{ab}(\tau, \sigma)$ independent of the embedding functions:

$$
S_P = -\frac{T}{2} \int d^2\sigma\, \sqrt{-g}\, g^{ab} \partial_a X^{\mu} \partial_b X_{\mu}.
$$

Classically, $S_P$ and $S_{\mathrm{NG}}$ are equivalent: the equation of motion obtained by varying $S_P$ with respect to $g^{ab}$ yields the constraint that the two-dimensional stress-energy tensor vanishes:

$$
T_{ab} \equiv -\frac{2}{T} \frac{1}{\sqrt{-g}} \frac{\delta S_P}{\delta g^{ab}} = 0,
$$

which forces $g_{ab}$ to be equal to the induced metric $h_{ab}$ up to a Weyl rescaling, thereby recovering $S_{\mathrm{NG}}$ [6].

The Polyakov action possesses three fundamental local symmetries that are essential for its consistency:

1. **D-dimensional Poincaré invariance** of the target spacetime: $X^{\mu} \to \Lambda^{\mu}_{\ \nu} X^{\nu} + a^{\mu}$.
2. **Two-dimensional diffeomorphism invariance**: the worldsheet coordinates can be freely reparametrized: $(\tau, \sigma) \to (\tilde\tau(\tau,\sigma), \tilde\sigma(\tau,\sigma))$.
3. **Weyl invariance**: the auxiliary metric can be rescaled by an arbitrary positive function: $g_{ab} \to e^{\omega(\tau,\sigma)} g_{ab}$.

The Weyl symmetry is the key to the solvability of string theory. It allows fixing the auxiliary metric to the flat Minkowski metric in conformal gauge:

$$
g_{ab} = \eta_{ab} = \begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix}.
$$

Even after this gauge fixing, a residual symmetry remains: conformal transformations that preserve the metric up to a Weyl factor. These are the two-dimensional conformal transformations, which are generated by holomorphic and antiholomorphic reparametrizations.

Throughout this article, natural units $\hbar = c = 1$ are used. The spacetime metric signature is mostly-plus: $(-,+,+,\ldots,+)$. The target-space dimension $D$ is left as a free parameter that will be fixed by consistency conditions.

## 3. Theoretical Framework

### 3.1 Equations of Motion and Boundary Conditions

In conformal gauge, the Polyakov action reduces to a free-field theory in two dimensions:

$$
S_P = -\frac{T}{2} \int d^2\sigma\, \eta^{ab} \partial_a X^{\mu} \partial_b X_{\mu}.
$$

The equations of motion are the two-dimensional wave equations

$$
\partial_a \partial^a X^{\mu} = (\partial_\tau^2 - \partial_\sigma^2) X^{\mu} = 0.
$$

The general solution is a superposition of left-moving and right-moving waves. In light-cone coordinates $\sigma^{\pm} = \tau \pm \sigma$, the wave equation becomes $\partial_+\partial_- X^{\mu} = 0$, with general solution

$$
X^{\mu}(\tau, \sigma) = X^{\mu}_L(\sigma^+) + X^{\mu}_R(\sigma^-).
$$

The boundary conditions depend on the topology of the worldsheet:
- **Closed strings**: Periodicity in $\sigma$: $X^{\mu}(\tau, \sigma+2\pi) = X^{\mu}(\tau, \sigma)$. Both left-moving and right-moving sectors are independent.
- **Open strings**: The boundary terms from the variation of the action must vanish at $\sigma = 0,\pi$. Two possibilities exist:
  - **Neumann** (free endpoint): $\partial_\sigma X^{\mu} = 0$ at the boundary.
  - **Dirichlet** (fixed endpoint): $\delta X^{\mu} = 0$ at the boundary.

Modern understanding identifies Dirichlet boundary conditions with D-branes — dynamical objects on which open strings end. The Neumann case corresponds to free endpoints moving in spacetime.

### 3.2 Mode Expansions

For closed strings with periodic boundary conditions, the mode expansion is

$$
X^{\mu}(\tau, \sigma) = x^{\mu} + 2\alpha' p^{\mu} \tau
+ i\sqrt{2\alpha'} \sum_{n\neq 0} \frac{1}{n}
\left( \alpha_n^{\mu} e^{-in(\tau-\sigma)} + \tilde\alpha_n^{\mu} e^{-in(\tau+\sigma)} \right),
$$

where $x^{\mu}$ and $p^{\mu}$ are the center-of-mass position and momentum of the string, and $\alpha_n^{\mu}$, $\tilde\alpha_n^{\mu}$ are Fourier modes. Reality of $X^{\mu}$ implies $\alpha_{-n}^{\mu} = (\alpha_n^{\mu})^\dagger$.

Canonical quantization imposes the commutation relations

$$
[x^{\mu}, p^{\nu}] = i \eta^{\mu\nu},
$$

$$
[\alpha_m^{\mu}, \alpha_n^{\nu}] = m \eta^{\mu\nu} \delta_{m+n,0},
$$

$$
[\tilde\alpha_m^{\mu}, \tilde\alpha_n^{\nu}] = m \eta^{\mu\nu} \delta_{m+n,0}.
$$

The oscillators satisfy $\alpha_{-n}^{\mu} = \alpha_n^{\mu\dagger}$ for $n > 0$, and the ground state $\lvert 0; p\rangle$ is annihilated by all $\alpha_n^{\mu}$ for $n > 0$ and is an eigenstate of $p^{\mu}$.

### 3.3 The Virasoro Constraints

The vanishing of the stress-energy tensor provides the physical state conditions. In conformal gauge, the components of the stress tensor are

$$
T_{++} = \partial_+ X^{\mu} \partial_+ X_{\mu} = 0, \qquad
T_{--} = \partial_- X^{\mu} \partial_- X_{\mu} = 0.
$$

These are the Virasoro constraints. In terms of the oscillator modes, the Fourier components of T_{++} and T_{--} are the Virasoro generators:

$$
L_m = \frac{T}{2} \int_0^{2\pi} d\sigma\, e^{im\sigma^-} T_{--} = \frac{1}{2} \sum_{n\in\mathbb{Z}} : \alpha_{m-n} \cdot \alpha_n :,
$$

$$
\tilde L_m = \frac{T}{2} \int_0^{2\pi} d\sigma\, e^{-im\sigma^+} T_{++} = \frac{1}{2} \sum_{n\in\mathbb{Z}} : \tilde\alpha_{m-n} \cdot \tilde\alpha_n :.
$$

The colons denote normal ordering, which is necessary because the oscillator modes do not commute. The normal-ordering prescription is unambiguous except for $L_0$, where an additive constant must be included.

### 3.4 The Virasoro Algebra

The commutators of the Virasoro generators define the Virasoro algebra:

$$
[L_m, L_n] = (m-n) L_{m+n} + \frac{c}{12} (m^3 - m) \delta_{m+n,0},
$$

where $c$ is the central charge. For a single free scalar field in two dimensions, $c = 1$. Since we have $D$ such fields ($X^{\mu}$ for $\mu = 0,\ldots,D-1$), the total central charge from the matter sector is $c = D$.

The $\tilde L_m$ satisfy an identical algebra with the same central charge. The zero-mode generators have special significance: $L_0$ generates $\sigma^+$ translations (worldsheet energy), and $(L_0 - \tilde L_0)$ generates $\sigma^-$ translations, which must annihilate physical states for closed strings — this is the level-matching condition.

The quantum Virasoro constraints on physical states are

$$
(L_0 - a) |\psi\rangle = 0, \qquad L_m |\psi\rangle = 0 \quad (m > 0),
$$

and similarly for $\tilde L_m$. The constant $a$ arises from the normal-ordering ambiguity in $L_0$. For the bosonic string, $a = 1$, as determined by consistency with the no-ghost theorem [4].

## 4. Main Derivation: The Critical Dimension

### 4.1 The Conformal Anomaly

The Polyakov action is classically Weyl-invariant: the metric can be rescaled by an arbitrary positive function without affecting the dynamics. In the quantum theory, however, the path integral over metrics can break this symmetry through the conformal anomaly. The anomaly arises because the measure for the metric integration is not Weyl-invariant, and the ghost fields introduced to fix diffeomorphism invariance contribute their own central charge.

After gauge-fixing the diffeomorphism and Weyl symmetries using the Faddeev-Popov procedure, one obtains a system consisting of $D$ free scalar fields (the $X^{\mu}$) and a ghost-antighost system $(b,c)$ with conformal weights $(2,-1)$. The ghost system contributes central charge $c_{\mathrm{gh}} = -26$ [1,6].

The total central charge of the combined matter-plus-ghost system is

$$
c_{\mathrm{tot}} = c_{\mathrm{matter}} + c_{\mathrm{gh}} = D - 26.
$$

For the quantum theory to be consistent, the Weyl anomaly must vanish, since the alternative would introduce an unwanted dependence on the conformal factor of the metric. This requires

$$
c_{\mathrm{tot}} = 0 \quad \Longrightarrow \quad D = 26.
$$

The critical dimension $D = 26$ is thus a consistency condition, not a choice. In $D < 26$, the anomaly can be absorbed into a dynamical conformal factor (the Liouville mode), but the resulting theory is non-critical and the conformal mode becomes a dynamical degree of freedom.

### 4.2 The Physical Spectrum and the No-Ghost Theorem

The physical state conditions can be solved level by level. Writing the Virasoro generators in terms of oscillators, the $L_0$ condition gives the mass-shell equation:

$$
M^2 = -p^{\mu} p_{\mu} = \frac{2}{\alpha'} (N + \tilde N - 2),
$$

where the number operators are

$$
N = \sum_{n=1}^\infty \alpha_{-n} \cdot \alpha_n, \qquad
\tilde N = \sum_{n=1}^\infty \tilde\alpha_{-n} \cdot \tilde\alpha_n,
$$

and the $-2$ comes from the normal-ordering constant $a = 1$ (for both left and right sectors). Level matching $N = \tilde N$ is required by the $L_0 - \tilde L_0 = 0$ condition.

The spectrum organizes by mass level:

- **Level 0** ($N = \tilde N = 0$): The ground state $\lvert 0; p\rangle$ with $M^2 = -4/\alpha' < 0$. This is the **tachyon**, indicating instability of the bosonic string vacuum.

- **Level 1** ($N = \tilde N = 1$): Massless states. The general state is

$$
|\zeta\rangle = \zeta_{\mu\nu} \alpha_{-1}^{\mu} \tilde\alpha_{-1}^{\nu} |0; p\rangle.
$$

The physical state conditions

$$
L_1\lvert\zeta\rangle
=
\tilde L_1\lvert\zeta\rangle
=
0
$$

impose transversality:

$$
p^{\mu}\zeta_{\mu\nu}
=
p^{\nu}\zeta_{\mu\nu}
=
0.
$$

The residual gauge symmetry

$$
\zeta_{\mu\nu}
\sim
\zeta_{\mu\nu}
+
p_{\mu}\xi_{\nu}
+
\xi_{\mu}p_{\nu}
$$

eliminates the longitudinal components. The remaining physical polarizations decompose into irreducible representations of the little group $SO(D-2)$:

- **Graviton**: symmetric traceless part, $\zeta_{(\mu\nu)} - \frac{1}{D-2}\eta_{\mu\nu}\zeta^{\rho}_{\rho}$, with $(D-2)(D-1)/2 - 1$ states.
- **Dilaton**: trace part, $\eta^{\mu\nu}\zeta_{\mu\nu}$, one scalar state.
- **Kalb-Ramond field**: antisymmetric part, $\zeta_{[\mu\nu]}$, with $(D-2)(D-3)/2$ states.

The graviton is the key discovery: string theory necessarily contains a massless spin-2 particle, which can be identified with the mediator of gravity [3].

The no-ghost theorem guarantees that for D = 26 and a = 1, all physical states have positive norm after factoring out null states (states orthogonal to all physical states including themselves). This theorem ensures unitarity of the quantum theory [4].

### 4.3 BRST Quantization

An alternative to the Gupta-Bleuler-like Virasoro constraints is BRST quantization. The BRST operator is

$$
Q_{\mathrm{B}} = \sum_{n\in\mathbb{Z}} \left( L_n c_{-n} + \frac{1}{2} (m-n) : c_{-m} c_{-n} b_{m+n} : \right) - a c_0,
$$

where $b_n,c_n$ are ghost modes with anticommutation relations $\{c_m,b_n\} = \delta_{m+n,0}$. Physical states satisfy $Q_{\mathrm{B}}\lvert\psi\rangle = 0$ modulo $Q_{\mathrm{B}}$-exact states. BRST cohomology at ghost number 1 reproduces the physical spectrum. The nilpotence condition $Q_{\mathrm{B}}^{2} = 0$ requires $a = 1$ and $D = 26$, confirming the earlier result.

## 5. Interpretation of the Main Equations

The Virasoro algebra with central charge c = D captures the quantum breaking of Weyl invariance. The condition D = 26 is not a choice but a consistency requirement: in any other dimension, the Weyl anomaly makes the theory inconsistent at the quantum level. This is the first example of string theory making a definite prediction about the spacetime dimension.

The graviton emerges naturally from the closed-string spectrum. Unlike in quantum field theory, where spin-2 particles must be introduced by hand, string theory forces their existence through the structure of the worldsheet oscillator algebra. The graviton state $h_{\mu\nu}$ is symmetric and traceless: $\eta^{\mu\nu}h_{\mu\nu} = 0$.

The tachyon at M^2 < 0 indicates that the bosonic string vacuum is unstable. This is not fatal in the full theory: the GSO projection in superstring theory removes the tachyon, yielding a stable ground state [5].

## 6. Consistency Checks and Limiting Cases

### 6.1 Low-Energy Effective Action

String scattering amplitudes at low energies ($E \ll M_s$) reproduce the Einstein-Hilbert action. The S-matrix for graviton-graviton scattering at tree level gives

$$
\Gamma = \int d^{26} x \sqrt{-g} e^{-2\Phi}
\left( R + 4(\nabla\Phi)^2 - \frac{1}{12} H_{\mu\nu\rho} H^{\mu\nu\rho} \right),
$$

where $\Phi$ is the dilaton and $H_{\mu\nu\rho} = \partial_{[\mu}B_{\nu\rho]}$ is the Kalb-Ramond field strength. This is the low-energy effective action of the bosonic string [3].

### 6.2 One-Loop Vacuum Amplitude

Modular invariance at one loop requires the integration over the fundamental domain of the torus modulus:

$$
Z = \int_{\mathcal{F}} \frac{d^2\tau}{\tau_2^2} (4\pi^2 \tau_2)^{-12} |\eta(i\tau)|^{-48}.
$$

The integration converges due to the restriction to the fundamental domain, confirming UV finiteness.

### 6.3 T-Duality

For a compactified dimension $X^{25} \sim X^{25} + 2\pi R$, the spectrum is invariant under $R \to \alpha'/R$ accompanied by the exchange of winding and momentum modes. This T-duality is a uniquely stringy phenomenon with no field theory analog.

## 7. Discussion

String theory achieves UV finiteness through the extended nature of the string, which softens interactions at high energies. The worldsheet CFT organizes the infinite number of particle states into a single coherent structure. The critical dimension D = 26 and the central charge cancellation are consequences of quantum consistency, not assumptions.

The bosonic string presented here is a toy model. The full theory requires:
- **Worldsheet supersymmetry** (NSR formalism) to remove the tachyon and achieve D = 10 [5].
- **GSO projection** for spacetime fermions.
- **D-branes** as endpoints for open strings, realizing gauge theories.
- **Compactification** on Calabi-Yau manifolds to connect to four-dimensional physics.

## 8. Relation to the Theory of Everything

String theory is the most developed framework for unification. The graviton emerges from the closed-string spectrum, Yang-Mills gauge bosons from open strings ending on D-branes, and chiral fermions from specific compactification geometries. The requirement of supersymmetry for consistency and the existence of an enormous landscape of vacua are both strengths (predictivity) and challenges (uniqueness).

Any ToE must reproduce the low-energy effective action of GR, the gauge group and matter content of the Standard Model, and explain the parameters of the universe. String theory addresses the first two requirements through its worldsheet structure but faces the vacuum selection problem: which Calabi-Yau compactification describes our universe?

## 9. Common Pitfalls

1. **Strings are not just tiny oscillating strings.** String theory is a framework for computing scattering amplitudes that happen to be organized by worldsheet CFTs. The interpretation in terms of moving strings is heuristic.

2. **D = 26 does not conflict with observation.** The bosonic string is a pedagogical toy model; the superstring lives in D = 10, and compactification hides six dimensions at sub-Planckian scales.

3. **String theory is not the only approach.** Loop quantum gravity, asymptotic safety, and causal set theory are independent research programs.

4. **The tachyon is not the end of the story.** The superstring GSO projection removes it, and the open-string tachyon signals D-brane decay, not instability of the vacuum.

5. **Perturbative finiteness does not imply non-perturbative completeness.** String theory is defined perturbatively; non-perturbative definitions (M-theory, AdS/CFT) are still under development.

## 10. Conclusion

The worldsheet formulation of string theory replaces point particles with one-dimensional extended objects whose dynamics is a conformal field theory. Quantization of the Polyakov action leads to the Virasoro algebra, whose central extension forces the critical dimension D = 26. The closed-string spectrum contains a massless spin-2 state — the graviton — proving that string theory naturally incorporates gravity. The bosonic string is unstable due to the tachyon, motivating the supersymmetric extension. String theory remains the most promising, though not unique, framework for a Theory of Everything.

## References

[1] J. Polchinski, *String Theory*, Vol. I: An Introduction to the Bosonic String, Cambridge University Press, 1998.

[2] G. Veneziano, "Construction of a Crossing-Symmetric, Regge-Behaved Amplitude for Linearly Rising Trajectories," *Nuovo Cimento A* 57, 190 (1968).

[3] T. Yoneya, "Connection of Dual Models to Electrodynamics and Gravidynamics," *Prog. Theor. Phys.* 51, 1907 (1974).

[4] M. B. Green, J. H. Schwarz, and E. Witten, *Superstring Theory*, Vol. I, Cambridge University Press, 1987.

[5] D. J. Gross, J. A. Harvey, E. Martinec, and R. Rohm, "Heterotic String Theory (I). The Free Heterotic String," *Nucl. Phys. B* 256, 253 (1985).

[6] A. M. Polyakov, "Quantum Geometry of Bosonic Strings," *Phys. Lett. B* 103, 207 (1981).
