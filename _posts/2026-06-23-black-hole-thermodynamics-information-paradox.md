---
title: "Black Hole Thermodynamics and the Information Paradox"
date: 2026-06-23 21:00:00 +0700
categories: [Physics, Quantum Gravity]
tags: [physics, theoretical-physics, general-relativity, quantum-gravity, black-holes, information-paradox, thermodynamics]
description: "A rigorous treatment of black hole thermodynamics: the four laws, Hawking radiation via Bogoliubov transformation, Bekenstein-Hawking entropy, the information paradox, Page curve, replica wormholes, and implications for a theory of quantum gravity."
math: true
---

## Abstract

Black holes, once regarded as purely classical objects, are fundamentally thermodynamic systems governed by definite laws analogous to those of ordinary thermodynamics. Hawking's discovery that black holes radiate thermally — $T_H = \hbar/8\pi GM$ — forces a synthesis of general relativity, quantum theory, and statistical mechanics. This article provides a rigorous treatment of black hole thermodynamics from first principles: the four laws derived from classical general relativity, Hawking's calculation of particle creation via Bogoliubov transformation, the Bekenstein–Hawking entropy formula $S_{\mathrm{BH}} = A/4G\hbar$, the information paradox and its resolution through the Page curve and replica wormholes, and the deep implications for a theory of quantum gravity. The holographic principle, the AdS/CFT correspondence, and recent progress on the island formula are discussed as essential developments toward resolving the paradox.

**Keywords:** black hole thermodynamics, Hawking radiation, Bekenstein–Hawking entropy, information paradox, Page curve, replica wormholes, holography

## 1. Introduction

The discovery that black holes have thermodynamic properties is among the most profound results in theoretical physics. It emerged from a series of thought experiments and calculations spanning the 1970s, beginning with Bekenstein's observation that the area of a black hole horizon behaves like an entropy [1], and culminating in Hawking's demonstration that black holes emit thermal radiation [2]. These results forced the recognition that black holes are not the final-state sinks they were thought to be, but rather thermodynamic objects with a temperature, an entropy, and a finite lifetime.

The black hole information paradox — the apparent loss of information when a black hole evaporates — has been the central conceptual problem in quantum gravity for nearly five decades. It pits the unitarity of quantum mechanics against the semiclassical reasoning that led to Hawking radiation. Recent developments involving replica wormholes and the island formula have provided strong evidence that information is not lost, but these results rely on the AdS/CFT correspondence and raise new questions about the nature of spacetime geometry [3,4].

This article develops the formalism of black hole thermodynamics from the classical laws through Hawking radiation, the paradox, and its proposed resolution. The focus is on conceptual clarity, mathematical rigor, and the implications for a complete theory of quantum gravity.

## 2. Preliminaries and Notation

We work in units $G = \hbar = c = 1$ unless otherwise noted. The metric signature is $(+,-,-,-)$. The Schwarzschild metric for a black hole of mass $M$ is

$$
ds^2 = -\left(1 - \frac{2M}{r}\right) dt^2 + \left(1 - \frac{2M}{r}\right)^{-1} dr^2 + r^2 d\Omega^2.
$$

The event horizon is at the Schwarzschild radius $r_s = 2M$. Surface gravity $\kappa$ is defined by

$$
\kappa^2 = -\frac12 (\nabla_\mu \xi_\nu)(\nabla^\mu \xi^\nu),
$$

evaluated at the horizon, where $\xi = \partial_t$ is the time-translation Killing vector. For Schwarzschild, $\kappa = 1/4M = 1/2r_s$.

The null coordinates that penetrate the horizon are Eddington–Finkelstein coordinates: the tortoise coordinate $r^* = r + 2M \ln\lvert (r/2M) - 1\rvert$, and advanced/retarded null coordinates $v = t + r^*$, $u = t - r^*$. Kruskal–Szekeres coordinates $(U,V)$ extend the manifold maximally:

$$
U = -e^{-u/4M}, \quad V = e^{v/4M},
$$

so that the metric becomes

$$
ds^2 = -\frac{32M^3}{r} e^{-r/2M}\, dU\, dV + r^2 d\Omega^2.
$$

The Penrose diagram of the maximally extended Schwarzschild solution reveals the causal structure: regions I (exterior), II (black hole interior), III (parallel exterior), and IV (white hole).

A quantum scalar field $\phi$ on this background satisfies the Klein–Gordon equation $\Box \phi = 0$. Positive-frequency modes are defined with respect to Killing time $t$. The central object in Hawking's calculation is the Bogoliubov transformation relating mode expansions in the distant past and far future.


## 3. Theoretical Framework

### 3.1 The Four Laws of Black Hole Mechanics

Bardeen, Carter, and Hawking [5] established four laws of black hole mechanics that parallel ordinary thermodynamics. Consider a stationary black hole with mass $M$, angular momentum $J$, charge $Q$, surface gravity $\kappa$, angular velocity $\Omega$, and electric potential $\Phi$.

**Zeroth law.** The surface gravity $\kappa$ is constant over the event horizon of a stationary black hole. This parallels the constancy of temperature in thermal equilibrium.

**First law.** For a stationary black hole perturbed by infalling matter,

$$
\delta M = \frac{\kappa}{8\pi} \delta A + \Omega \, \delta J + \Phi \, \delta Q.
$$

Comparing with the thermodynamic first law $dU = T\,dS + \text{work terms}$ suggests the identifications

$$
T_{\mathrm{BH}} = \frac{\kappa}{2\pi}, \qquad S_{\mathrm{BH}} = \frac{A}{4}.
$$

Restoring units: $T_H = \hbar\kappa/2\pi$ and $S_{\mathrm{BH}} = A/4G\hbar$.

**Second law.** The area theorem (Hawking's area theorem) states that the horizon area $A$ is non-decreasing:

$$
\delta A \geq 0,
$$

provided cosmic censorship holds and the null energy condition is satisfied. The analog in thermodynamics is the entropy increase law $\Delta S \geq 0$.

**Third law.** No physical process can reduce the surface gravity to zero (i.e., extremal black holes with $\kappa = 0$ are unattainable in finite time). This parallels the unattainability of absolute zero.

These formal analogies are exact, not coincidental. Hawking's calculation made them physical by providing the numerical factor linking $\kappa$ and $T_H$.

### 3.2 Quantum Field Theory in Curved Spacetime

Hawking's derivation of black hole radiation uses QFT on a fixed Schwarzschild background, treating the gravitational field classically while quantizing matter fields. Consider a massless scalar field $\phi$ satisfying $\Box \phi = 0$.

In the distant past (past null infinity $\mathcal{I}^-$), the field can be expanded in a complete set of positive-frequency modes $f_{\omega\ell m}$ with respect to Killing time $t$:

$$
\phi = \sum_{\ell m} \int_0^\infty d\omega\, \left( a_{\omega\ell m} f_{\omega\ell m} + a^\dagger_{\omega\ell m} f^*_{\omega\ell m} \right),
$$

where $a_{\omega\ell m}$ annihilate the `in` vacuum: $a\lvert 0_{\mathrm{in}}\rangle = 0$.

The modes $f_{\omega\ell m}$ are incoming from $\mathcal{I}^-$, partly scattering off the black hole and partly falling through the horizon. In the far future (future null infinity $\mathcal{I}^+$), the outgoing field is expanded in modes $p_{\omega\ell m}$:

$$
\phi = \sum_{\ell m} \int_0^\infty d\omega\, \left( b_{\omega\ell m} p_{\omega\ell m} + b^\dagger_{\omega\ell m} p^*_{\omega\ell m} + \text{horizon modes} \right).
$$

The `in` and `out` creation/annihilation operators are related by a Bogoliubov transformation. The key subtlety is that the past and future mode decompositions are inequivalent: a mode that appears purely positive-frequency to a distant observer in the far future has a mixed-frequency decomposition in the past, because the mode undergoes gravitational redshift near the horizon.

### 3.3 Hawking's Calculation

Hawking considered the collapse of a spherical star forming a Schwarzschild black hole. He showed that an outgoing mode at late times $p_\omega$ originates from an ingoing mode of extremely high frequency near the horizon. The relationship between the `in` and `out` mode functions involves exponentials of the surface gravity [2].

The Bogoliubov coefficients relating $b_\omega$ to $a_\omega$ and $a^\dagger_\omega$ are

$$
\beta_{\omega\omega'} = -i e^{\pi\omega/2\kappa} \alpha_{\omega\omega'}.
$$

The number of particles detected at $\mathcal{I}^+$ in mode $p_\omega$ by an observer initially in the `in` vacuum is

$$
\langle 0_{\mathrm{in}} | b^\dagger_\omega b_{\omega'} |0_{\mathrm{in}}\rangle = \frac{1}{e^{2\pi\omega/\kappa} - 1} \delta(\omega - \omega').
$$

This is a Planck spectrum with temperature

$$
T_H = \frac{\kappa}{2\pi} = \frac{1}{8\pi M}.
$$

Restoring units: $T_H = \hbar c^3 / 8\pi G M k_B$, giving a temperature of approximately $6 \times 10^{-8}\,\mathrm{K}\,(M_\odot/M)$.



### 3.4 Bekenstein–Hawking Entropy and the Generalized Second Law

The identification $S_{\mathrm{BH}} = A/4$ suggests that the total entropy of the universe includes a gravitational contribution from black hole horizons. Bekenstein [1] proposed the generalized second law (GSL):

$$
\delta\left( S_{\mathrm{matter}} + \frac{A}{4} \right) \geq 0,
$$

where $S_{\mathrm{matter}}$ is the entropy of matter outside the black hole. The GSL has been verified in numerous thought experiments involving lowering matter into black holes, and it suggests that black hole entropy is not a mere analogy but a genuine statistical entropy counting microstates.

The entropy scaling $S \propto A$ rather than $S \propto V$ is the origin of the holographic principle [6,7]: the maximum entropy in a region of space scales with its boundary area, not its volume. This revolutionary insight suggests that the degrees of freedom in quantum gravity are fundamentally lower-dimensional.

## 4. Main Derivation: Hawking Radiation via Bogoliubov Transformation

We now present a streamlined version of Hawking's calculation [2]. Consider a massless scalar field $\phi$ in a Schwarzschild background formed by gravitational collapse. The collapse geometry is asymptotically flat in the past and future, but they are not isometric due to the presence of the horizon.

### 4.1 Mode Functions

Past null infinity $\mathcal{I}^-$ is characterized by advanced null coordinate $v$. Incoming modes that are purely positive-frequency with respect to $v$ are

$$
f_\omega \sim \frac{1}{\sqrt{4\pi\omega}} \frac{e^{-i\omega v}}{r},
$$

normalized by $(f_\omega, f_{\omega'}) = \delta(\omega - \omega')$ in the Klein–Gordon inner product.

A fraction of each incoming wave enters the collapsing star and emerges on $\mathcal{I}^+$. Near the horizon, the geometric optics approximation (eikonal approximation) applies: the phase $\theta$ of the wave satisfies $\nabla^\mu \theta \nabla_\mu \theta = 0$. For an outgoing ray at late times, the ray is traced backward in time and experiences a large gravitational redshift near the horizon.

### 4.2 Relation Between Past and Future Modes

For an outgoing mode $p_\omega$ on $\mathcal{I}^+$ with retarded time $u$, the backward-traced ray passes near the horizon, where $v$ and $u$ are related by

$$
v(v_0) \approx v_0 - 4M \ln\left( \frac{u_0 - u}{4M} \right),
$$

for late-time outgoing rays (large $u$). Here $v_0$ is the critical advanced time of the last ray to escape before collapse completes.

The outgoing mode $p_\omega \propto e^{-i\omega u}$ therefore appears on $\mathcal{I}^-$ as

$$
p_\omega \propto \begin{cases}
e^{-i\omega u(v)}, & v < v_0 \\
0, & v > v_0,
\end{cases}
$$

where $u(v) = v - 2r^*(v)$ and the logarithmic relation above holds near the horizon. This function has support on $\mathcal{I}^-$ but is not purely positive-frequency; its Fourier decomposition contains negative-frequency components.

### 4.3 Bogoliubov Coefficients and Thermal Spectrum

The Bogoliubov coefficient $\beta_{\omega\omega'}$ encoding the negative-frequency content is

$$
\beta_{\omega\omega'} = -\frac{i}{2\pi} \sqrt{\frac{\omega}{\omega'}} \int_{-\infty}^{v_0} dv\, e^{-i\omega' v} e^{i\omega u(v)}.
$$

Using the relation $u \approx v - 4M \ln((v_0 - v)/4M)$ and extending the integral to $+\infty$ with a suitable analytic continuation, one finds

$$
\beta_{\omega\omega'} = -\frac{1}{2\pi} \sqrt{\frac{\omega}{\omega'}} e^{\pi\omega/2\kappa} \times (\text{gamma function factors}) \times \delta(\omega - \omega').
$$

The crucial result is the ratio

$$
|\beta_{\omega\omega'}|^2 = e^{-2\pi\omega/\kappa} |\alpha_{\omega\omega'}|^2.
$$

The `out` number operator expectation value in the `in` vacuum is

$$
\langle b^\dagger_\omega b_{\omega'} \rangle = \int d\omega''\, \beta_{\omega\omega''} \beta^*_{\omega'\omega''}
= \frac{1}{e^{2\pi\omega/\kappa} - 1} \delta(\omega - \omega').
$$

This is a Planck blackbody spectrum at temperature $T_H = \kappa/2\pi$. For Schwarzschild, $T_H = 1/8\pi M$.

### 4.4 Black Hole Evaporation

From $T_H \sim 1/M$, the black hole radiates energy with luminosity

$$
L = -\frac{dM}{dt} = \frac{\hbar}{15360\pi G^2 M^2},
$$

obtained by integrating the Stefan–Boltzmann law over the Hawking spectrum for a massless scalar field. The evaporation time is

$$
\tau_{\mathrm{evap}} \sim \frac{5120\pi G^2 M^3}{\hbar} \sim 10^{67} \left(\frac{M}{M_\odot}\right)^3 \mathrm{years}.
$$

As the black hole loses mass, its temperature increases, leading to runaway evaporation in the final moments. The endpoint of evaporation — a Planck-scale remnant or complete disappearance — is unknown and depends on the correct quantum gravity theory.



## 5. Interpretation of the Main Equations

### 5.1 The Thermal Spectrum and Its Meaning

The Planck spectrum derived above implies that a distant observer sees the black hole as a perfect blackbody at temperature $T_H$. This is remarkable: a classical object that absorbs everything emits thermal radiation. The origin of this radiation is the gravitational redshift suffered by modes near the horizon — a kinematical effect of the curved spacetime, not a dynamical process at the horizon itself.

Importantly, the Hawking derivation is semiclassical: the matter field is quantized on a fixed classical background, but the gravitational field (the metric) is not quantized. This approximation breaks down when the black hole mass approaches the Planck mass $M_P$, where back-reaction and quantum gravity effects become dominant.

### 5.2 Entropy and Holography

The Bekenstein–Hawking entropy $S_{\mathrm{BH}} = A/4$ is the simplest known instance of holographic behavior. For a Schwarzschild black hole, the entropy is

$$
S_{\mathrm{BH}} = 4\pi M^2 = \frac{A}{4}.
$$

Microscopic derivations using string theory [8] count D-brane bound state degeneracies whose logarithm reproduces this area scaling. For extremal and near-extremal black holes in string theory, the agreement is exact:

$$
S_{\mathrm{micro}} = \ln\Omega = \frac{A}{4} + \mathcal{O}(\text{corrections}).
$$

This is one of the strongest pieces of evidence for string theory as a quantum gravity framework.

### 5.3 The Information Paradox

Hawking's 1976 argument [3] concludes that the final state of black hole evaporation is mixed (thermal) even though the initial state that formed the black hole was pure. This violates unitarity: the $S$-matrix relating asymptotic `in` and `out` states is not unitary.

The paradox can be quantified by the Page curve [9]. Consider a black hole formed from a pure state, evaporating into radiation. Let $R$ denote the emitted radiation and $B$ the remaining black hole. The fine-grained (von Neumann) entropy of the radiation is

$$
S(R) = -\mathrm{Tr}(\rho_R \ln \rho_R).
$$

If the total evolution is unitary, $S(R)$ must start at 0 (no radiation), rise as radiation is emitted, and eventually return to 0 when the black hole has fully evaporated, since the final state is pure. Hawking's semiclassical calculation gives $S(R)$ increasing monotonically without returning to zero — the information is lost.

The Page time $t_{\mathrm{Page}}$ is the time when $S(R)$ reaches its maximum (half the Bekenstein–Hawking entropy of the initial black hole). Before $t_{\mathrm{Page}}$, the radiation entropy rises; after $t_{\mathrm{Page}}$, it must decrease to preserve unitarity. This decreasing behavior is the hallmark of information recovery.



## 6. Consistency Checks and Limiting Cases

**Large black hole limit.** For $M \gg M_P$, the Hawking temperature is negligible ($T_H \ll M_P$), and the evaporation time vastly exceeds the age of the universe. Classical general relativity is an excellent approximation, consistent with observations.

**Charged and rotating black holes.** The first law generalizes:

$$
\delta M = T_H \delta S + \Omega_H \delta J + \Phi_H \delta Q.
$$

For Kerr–Newman black holes, the horizon area is [1,5]

$$
A = 4\pi\left( 2M^2 - Q^2 + 2M\sqrt{M^2 - Q^2 - a^2} \right),
$$

where $a = J/M$. The extremal limit $M^2 = a^2 + Q^2$ gives $\kappa = 0$ and $T_H = 0$, consistent with the third law.

**The Unruh effect as a consistency check.** An accelerating observer in flat spacetime sees a thermal bath at temperature $T_{\mathrm{Unruh}} = a/2\pi$, where $a$ is the proper acceleration. Hawking radiation can be understood as the Unruh effect experienced by an observer just outside the horizon, who must accelerate to remain stationary and therefore sees a thermal bath. The equivalence principle guarantees the consistency of this picture.

**AdS/CFT and unitarity.** In asymptotically AdS spacetimes, the AdS/CFT correspondence provides a unitary dual description of black hole formation and evaporation. The boundary CFT is manifestly unitary, implying that bulk gravitational evolution must also be unitary. This is our strongest argument that information is not lost, and it motivates the developments below.

## 7. Discussion

### 7.1 The Firewall Paradox

Almheiri, Marolf, Polchinski, and Sully (AMPS) [10] argued that the Page curve implies a violation of the equivalence principle. For an old black hole (after $t_{\mathrm{Page}}$), the radiation $R$ and the black hole interior $B$ are entangled. For the total state to be pure, the late-time radiation $R$ must be entangled with the early radiation $R_B$. But Page's argument shows that $R$ and $R_B$ are also entangled. Quantum mechanics forbids a system being maximally entangled with two systems simultaneously — this is the "monogamy of entanglement" [10].

If near-horizon modes are entangled with early radiation rather than with interior modes, the horizon becomes a "firewall" — a region of high energy density that destroys infalling observers. This directly contradicts the equivalence principle.

### 7.2 Replica Wormholes and the Island Formula

A resolution emerged from the gravitational path integral [4,11]. The fine-grained entropy of Hawking radiation can be computed using the QES (quantum extremal surface) prescription:

$$
S(R) = \min_X \left\{ \frac{\mathrm{Area}(X)}{4} + S_{\mathrm{QFT}}(R \cup I_X) \right\},
$$

where $X$ is a quantum extremal surface and $I_X$ is the "island" — a region behind the horizon whose quantum state purifies the radiation. At early times, the minimal surface has zero area, giving Hawking's monotonically increasing result. After the Page time, the minimal surface lies just behind the horizon, and its area contribution causes $S(R)$ to decrease, reproducing the Page curve.

The island formula was derived from replica wormholes — saddle points of the gravitational path integral that connect different replicas of the geometry. These wormhole saddles contribute to the replica trick calculation of $\mathrm{Tr}\rho_R^n$ and are essential for unitarity. The formula shows that the information is encoded in the radiation via entanglement with the island, resolving the paradox modulo the precise nature of the replica wormhole contributions [12].

### 7.3 The Holographic Principle

The black hole entropy result motivated the holographic principle [6,7]: a theory of quantum gravity in a $d$-dimensional volume should be describable by a $d-1$-dimensional theory on its boundary. The AdS/CFT correspondence is the best-understood realization: type IIB string theory in $AdS_5 \times S^5$ is equivalent to $\mathcal{N} = 4$ super-Yang–Mills theory on the four-dimensional boundary. In this duality, black hole formation and evaporation are unitary from the boundary perspective.



## 8. Relation to the Theory of Everything

Black hole thermodynamics is not a peripheral consequence of quantum gravity — it is arguably its most concrete prediction and most stringent test. Any candidate ToE must:

- **Reproduce the Bekenstein–Hawking entropy** via a microstate count. String theory achieves this for extremal and near-extremal black holes [8]. Loop quantum gravity reproduces the area scaling with a numerical coefficient that depends on the Barbero–Immirzi parameter. Asymptotic safety and other approaches must match this universal result.

- **Resolve the information paradox unitarily.** The Page curve and island formula suggest that gravity has a built-in mechanism for information conservation, but a full description requires understanding the endpoint of evaporation.

- **Explain the holographic nature of spacetime.** The area scaling of entropy is not accidental — it reflects the holographic degrees of freedom of quantum gravity. A complete theory should derive this from first principles.

- **Reconcile the semiclassical approximation with unitarity.** The replica wormhole calculation shows that non-perturbative effects in the gravitational path integral restore unitarity, but the calculation relies on Euclidean saddle points whose physical interpretation remains debated.

## 9. Common Pitfalls

1. **"Hawking radiation originates from particle-antiparticle pair creation at the horizon."** This popular picture is misleading. The correct derivation involves Bogoliubov transformation of mode functions: the vacuum state near the horizon appears as a thermal state to an observer at infinity. The pair-creation analogy oversimplifies the gravitational redshift mechanism.

2. **"The information paradox is solved by AdS/CFT."** AdS/CFT demonstrates that unitarity holds in asymptotically AdS spacetimes, but this does not automatically resolve the paradox for asymptotically flat or cosmological spacetimes. The island formula provides a bulk mechanism, but its generalization beyond AdS remains incomplete.

3. **"Firewalls are inevitable."** The AMPS argument assumes that the black hole interior and exterior are independent systems. The island formula suggests that the interior is encoded in the radiation, relaxing the assumption that leads to the firewall.

4. **"Black hole evaporation leaves a remnant."** Small stable remnants are a logical possibility but face challenges: they must be produced in infinite varieties (to conserve information) and must not overproduce via virtual processes, which would violate effective field theory.

5. **"The Page curve only applies to AdS."** The Page curve is a general consequence of unitarity and is expected in any consistent quantum gravity theory. The island formula has been extended to asymptotically flat spacetimes and de Sitter space.

## 10. Conclusion

Black hole thermodynamics is the most concrete link between general relativity, quantum theory, and statistical mechanics. The four laws of black hole mechanics provide an exact thermodynamic analogy; Hawking's derivation made this analogy physical by demonstrating that black holes radiate at a definite temperature. The Bekenstein–Hawking entropy $S = A/4$ implies that the fundamental degrees of freedom of quantum gravity scale with area, not volume — the holographic principle.

The information paradox has driven theoretical physics for nearly 50 years. Recent progress using the island formula and replica wormholes has provided a gravitational mechanism that restores unitarity, reproducing the Page curve and suggesting that information is not lost. These developments rely on the gravitational path integral and the AdS/CFT correspondence, and they point toward a deeper understanding of spacetime geometry in quantum gravity.

Black hole thermodynamics remains an active frontier. The resolution of the information paradox, the microscopic underpinning of horizon entropy for generic black holes, and the role of non-perturbative gravitational effects are central to the search for a Theory of Everything.

## References

[1] J. D. Bekenstein, "Black Holes and Entropy," *Phys. Rev. D* 7, 2333 (1973).

[2] S. W. Hawking, "Particle Creation by Black Holes," *Commun. Math. Phys.* 43, 199 (1975).

[3] S. W. Hawking, "Breakdown of Predictability in Gravitational Collapse," *Phys. Rev. D* 14, 2460 (1976).

[4] A. Almheiri, T. Hartman, J. Maldacena, E. Shaghoulian, and A. Tajdini, "The Entropy of Hawking Radiation," *Rev. Mod. Phys.* 93, 035002 (2021).

[5] J. M. Bardeen, B. Carter, and S. W. Hawking, "The Four Laws of Black Hole Mechanics," *Commun. Math. Phys.* 31, 161 (1973).

[6] G. 't Hooft, "Dimensional Reduction in Quantum Gravity," *Conf. Proc. C* 930308, 284 (1993).

[7] L. Susskind, "The World as a Hologram," *J. Math. Phys.* 36, 6377 (1995).

[8] A. Strominger and C. Vafa, "Microscopic Origin of the Bekenstein–Hawking Entropy," *Phys. Lett. B* 379, 99 (1996).

[9] D. N. Page, "Information in Black Hole Radiation," *Phys. Rev. Lett.* 71, 3743 (1993).

[10] A. Almheiri, D. Marolf, J. Polchinski, and J. Sully, "Black Holes: Complementarity or Firewalls?" *JHEP* 02, 062 (2013).

[11] G. Penington, S. H. Shenker, D. Stanford, and Z. Yang, "Replica Wormholes and the Black Hole Interior," arXiv:1911.11977.

[12] A. Almheiri, T. Hartman, J. Maldacena, E. Shaghoulian, and A. Tajdini, "Replica Wormholes and the Entropy of Hawking Radiation," *JHEP* 05, 013 (2020).
