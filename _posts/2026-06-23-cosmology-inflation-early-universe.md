---
title: "Cosmology, Inflation, and the Early Universe"
date: 2026-06-23 11:20:00 +0700
categories: [Physics, Cosmology]
tags: [physics, theoretical-physics, cosmology, general-relativity, inflation, cmb, perturbation-theory]
description: "A rigorous treatment of modern cosmology: FRW geometry, Friedmann equations, inflation as an effective theory, cosmological perturbation theory, the cosmic microwave background, and the connections between early-universe physics and fundamental theory."
math: true
---

## Abstract

Modern cosmology describes the universe as an expanding spacetime whose evolution is governed by general relativity and whose initial conditions may originate in quantum fluctuations during an early phase of accelerated expansion — inflation. This article provides a rigorous treatment: the Friedmann–Robertson–Walker (FRW) metric and its justification by symmetry, the Friedmann equations and their derivation from Einstein's equations, the horizon and flatness problems that motivate inflation, the slow-roll approximation and the Mukhanov–Sasaki equation for cosmological perturbations, the connection to cosmic microwave background (CMB) observables, and the open questions about the initial singularity, the nature of dark energy, and the UV completion of inflation. The article concludes with the implications of cosmology for a Theory of Everything: any complete theory must resolve the initial singularity, explain the dark sector, and account for the spectrum of primordial fluctuations.

**Keywords:** cosmology, inflation, FRW metric, Friedmann equations, cosmic microwave background, cosmological perturbation theory, dark energy

## 1. Introduction

Modern cosmology addresses the origin, evolution, and large-scale structure of the universe as a whole. The standard cosmological model, Lambda-CDM, is a six-parameter description that fits thousands of data points from the cosmic microwave background (CMB), large-scale structure surveys, and supernova distance measurements [1,2]. Despite this empirical success, the model rests on foundations that point to deeper physics: the nature of dark matter, the origin of dark energy, the mechanism that generated the primordial density perturbations, and the resolution of the initial singularity.

The early universe is the only laboratory for physics at energy scales far beyond the reach of terrestrial accelerators. Inflation — a period of accelerated expansion in the very early universe — provides a causal mechanism for the generation of primordial perturbations from quantum vacuum fluctuations [3,4]. This article develops the mathematical framework of modern cosmology from the FRW geometry through the theory of inflationary perturbations to the observables imprinted on the CMB.

## 2. Preliminaries and Notation

Metric signature is $(+,-,-,-)$. Natural units $\hbar = c = 1$ are used. The reduced Planck mass is $M_P = 1/\sqrt{8\pi G} \approx 2.4 \times 10^{18}\ \mathrm{GeV}$.

The universe is described by the Friedmann–Robertson–Walker (FRW) metric, which follows from the cosmological principle (homogeneity and isotropy on large scales):

$$
ds^2 = -dt^2 + a(t)^2 \left[ \frac{dr^2}{1 - k r^2} + r^2 d\Omega^2 \right],
$$

where $a(t)$ is the scale factor, $k \in \{-1, 0, +1\}$ is the spatial curvature parameter, and $d\Omega^2 = d\theta^2 + \sin^2\theta\, d\phi^2$.

The Hubble parameter is $H(t) = \dot a / a$. Comoving coordinates $x^i$ are related to physical distances by $d_{\mathrm{phys}} = a(t) \Delta x$.

## 3. Theoretical Framework

### 3.1 The Friedmann Equations

Assume the universe is filled with a perfect fluid with stress-energy tensor

$$
T_{\mu\nu} = (\rho + p) u_\mu u_\nu + p g_{\mu\nu},
$$

where $\rho$ is the energy density and $p$ is the pressure. Inserting the FRW metric into the Einstein equations $G_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi G T_{\mu\nu}$ yields the Friedmann equations [1,2]:

$$
H^2 = \frac{8\pi G}{3} \rho - \frac{k}{a^2} + \frac{\Lambda}{3},
\qquad
\frac{\ddot a}{a} = -\frac{4\pi G}{3} (\rho + 3p) + \frac{\Lambda}{3}.
$$

Energy-momentum conservation $\nabla^\mu T_{\mu\nu} = 0$ gives the continuity equation

$$
\dot\rho + 3H(\rho + p) = 0.
$$

For a component with equation of state $w = p/\rho$, this integrates to $\rho \propto a^{-3(1+w)}$.

### 3.2 Inflation as an Effective Theory

Inflation is a period of accelerated expansion ($\ddot a > 0$). From the acceleration equation, this requires $\rho + 3p < 0$. A scalar field $\phi$ (the inflaton) with potential $V(\phi)$ satisfies this:

$$
\rho_\phi = \frac12 \dot\phi^2 + V(\phi), \qquad
p_\phi = \frac12 \dot\phi^2 - V(\phi).
$$

The homogeneous inflaton field obeys the Klein–Gordon equation in an expanding universe:

$$
\ddot\phi + 3H \dot\phi + V'(\phi) = 0.
$$

The slow-roll parameters are defined as [3,4]

$$
\epsilon \equiv -\frac{\dot H}{H^2} = \frac{M_P^2}{2} \left( \frac{V'}{V} \right)^2,
\qquad
\eta \equiv M_P^2 \frac{V''}{V}.
$$

Inflation occurs when $\epsilon < 1$ and $\lvert\eta\rvert < 1$. The number of e-folds is

$$
\begin{aligned}
N = \ln\frac{a_{\mathrm{end}}}{a_{\mathrm{start}}} &= \int_{t_{\mathrm{start}}}^{t_{\mathrm{end}}} H\, dt \\
&\approx \frac{1}{M_P^2} \int_{\phi_{\mathrm{end}}}^{\phi_{\mathrm{start}}} \frac{V}{V'}\, d\phi.
\end{aligned}
$$

## 4. Main Derivation: Cosmological Perturbations

The generation of primordial perturbations from quantum fluctuations during inflation is the central success of the inflationary paradigm. Perturbations of the inflaton field couple to metric perturbations. The gauge-invariant Mukhanov variable $v$ satisfies [4,5]

$$
v''_k + \left( c_s^2 k^2 - \frac{z''}{z} \right) v_k = 0,
$$

where primes denote derivatives with respect to conformal time $\tau = \int dt/a(t)$, $z = a\dot\phi/H$, and $c_s$ is the speed of sound (unity for single-field slow-roll). Deep inside the horizon ($k \gg aH$), the solution is the Bunch–Davies vacuum:

$$
v_k \to \frac{1}{\sqrt{2k}} e^{-ik\tau} \quad (k\tau \to -\infty).
$$

On super-horizon scales ($k \ll aH$), the curvature perturbation $\mathcal{R}_k = v_k/z$ becomes constant:

$$
|\mathcal{R}_k|^2 \to \frac{H^2}{2k^3\dot\phi^2} = \frac{H^4}{2k^3 M_P^2 \epsilon}.
$$

### 4.1 Primordial Power Spectra

The dimensionless power spectrum of scalar (curvature) perturbations is

$$
\begin{aligned}
\Delta_s^2(k) &\equiv \frac{k^3}{2\pi^2} \langle |\mathcal{R}_k|^2 \rangle = \left( \frac{H^2}{2\pi\dot\phi} \right)^2 \\
&\approx \frac{1}{8\pi^2 M_P^2} \frac{V}{M_P^4} \frac{1}{\epsilon}.
\end{aligned}
$$

The scalar spectral index is

$$
n_s - 1 = \frac{d\ln\Delta_s^2}{d\ln k} = -6\epsilon + 2\eta.
$$

Planck 2018 measurements give $n_s = 0.9649 \pm 0.0042$, consistent with slow-roll predictions [6]. Tensor perturbations (primordial gravitational waves) have power spectrum

$$
\Delta_t^2(k) = \frac{2}{\pi^2} \frac{H^2}{M_P^2},
$$

with tensor-to-scalar ratio $r = \Delta_t^2/\Delta_s^2 = 16\epsilon$. Current bounds $r \lesssim 0.036$ constrain the energy scale of inflation.

## 5. Interpretation of the Main Equations

**The Mukhanov–Sasaki equation.** The term $z''/z$ in the Mukhanov–Sasaki equation acts as an effective mass. During slow-roll inflation, $z''/z \approx 2/\tau^2$, giving the general solution

$$
v_k(\tau) = \frac{\sqrt{-\pi\tau}}{2} e^{i\pi(2\nu+1)/4} H_\nu^{(1)}(-k\tau),
$$

where $\nu = 3/2 + 2\epsilon - \eta$ for slow-roll. The power spectrum amplitude at horizon crossing ($k = aH$) is proportional to $H^2/\epsilon$ — larger Hubble scale and flatter potential produce larger fluctuations.

**The spectral index $n_s$.** A scale-invariant spectrum would have $n_s = 1$. The measured red tilt ($n_s < 1$) indicates $\epsilon \sim 0.01$, consistent with a slowly rolling inflaton. The deviation from scale invariance is a direct probe of the inflaton potential.

**The Friedmann equation in density parameters.** Dividing by $H^2$ gives

$$
1 = \Omega_m(a) + \Omega_r(a) + \Omega_k(a) + \Omega_\Lambda(a),
$$

where $\Omega_i = 8\pi G\rho_i/(3H^2)$. Current values: $\Omega_m \approx 0.31$, $\Omega_r \approx 9 \times 10^{-5}$, $\Omega_\Lambda \approx 0.69$, $\lvert\Omega_k\rvert < 0.01$ [6].

## 6. Consistency Checks and Limiting Cases

**Matter-dominated universe.** For $k = 0$, $\Lambda = 0$, and $w = 0$, the Friedmann equation gives $a(t) \propto t^{2/3}$, $\rho \propto a^{-3}$.

**Radiation-dominated universe.** For $w = 1/3$, $a(t) \propto t^{1/2}$, $\rho \propto a^{-4}$. The early universe before matter-radiation equality is radiation-dominated.

**de Sitter limit.** For $\Lambda > 0$ with no other matter, $a(t) \propto e^{Ht}$ with constant $H = \sqrt{\Lambda/3}$. de Sitter space has a cosmological horizon at $r_H = 1/H$, analogous to a black hole horizon.

**Newtonian limit.** On sub-horizon scales, perturbations evolve according to

$$
\ddot\delta_m + 2H\dot\delta_m - 4\pi G\rho_m \delta_m = 0,
$$

which reproduces the Jeans instability in an expanding background. The growing mode $\delta_m \propto a$ during matter domination.

## 7. Discussion

**Reheating.** Inflation ends when $\epsilon \sim 1$. The inflaton oscillates around the minimum of its potential, decaying into Standard Model particles. The reheating temperature is $T_{\mathrm{reh}} \sim \sqrt{M_P \Gamma_\phi}$, where $\Gamma_\phi$ is the inflaton decay width.

**Primordial non-Gaussianity.** Single-field slow-roll models predict nearly Gaussian fluctuations. Non-Gaussianity is parameterized by the bispectrum amplitude $f_{\mathrm{NL}}$. Current bounds ($f_{\mathrm{NL}} = -0.9 \pm 5.1$) are consistent with zero [6]. Detection would rule out all single-field models.

**The trans-Planckian problem.** CMB modes had physical wavelengths shorter than $\ell_P$ early in inflation. Trans-Planckian physics could imprint oscillatory features on the CMB — model-dependent but potentially observable [7].

**Dark energy.** The observed value $\rho_\Lambda \sim (10^{-3}\ \mathrm{eV})^4$ is $10^{120}$ times smaller than the Planck-scale QFT expectation. This is the cosmological constant problem, arguably the deepest fine-tuning in physics [8].

## 8. Relation to the Theory of Everything

Cosmology intersects with unification at several points:

- **Inflation requires a UV completion.** The inflaton potential is sensitive to Planck-scale physics. A ToE should predict the inflaton couplings, mass, and potential shape.
- **The baryon asymmetry** requires CP violation beyond the Standard Model (baryogenesis or leptogenesis) [9].
- **Dark matter** constitutes 27% of the universe but is absent from the Standard Model. A ToE must provide a dark matter candidate.
- **The initial singularity** of classical GR is resolved in quantum cosmology. The wavefunction of the universe (Hartle–Hawking, Vilenkin, or other proposals) depends on the underlying quantum gravity framework [10].
- **The cosmological constant** is both a low-energy puzzle and a quantum gravity puzzle.

## 9. Common Pitfalls

1. **"The universe is expanding into something."** Expansion means $a(t)$ increases. There is no "outside" or "edge" — the FRW metric describes a self-contained spacetime.

2. **"Inflation explains everything."** Inflation solves the horizon and flatness problems and generates perturbations, but does not explain the initial singularity, the inflaton identity, or the exit mechanism without additional assumptions.

3. **"CMB data prove inflation."** Inflation is consistent with CMB data but not uniquely proven. Alternatives (bouncing cosmologies, string gas cosmology) also produce nearly scale-invariant spectra.

4. **"Dark energy is a new force."** Dark energy is best interpreted as a component of $T_{\mu\nu}$ with $w \approx -1$, possibly a cosmological constant, dynamical field, or IR modification of gravity.

## 10. Conclusion

Modern cosmology combines general relativity, quantum field theory, and precision observations into a coherent picture of cosmic evolution. The FRW model describes expansion; inflation provides a mechanism for generating primordial perturbations; and the CMB encodes the resulting structure with extraordinary precision. The Lambda-CDM model is remarkably successful, yet it leaves deep questions unanswered — the nature of dark matter, dark energy, the inflaton, and the initial singularity. These are precisely the questions that point toward a more fundamental theory.

## References

[1] S. Weinberg, *Gravitation and Cosmology: Principles and Applications of the General Theory of Relativity*, Wiley, 1972.

[2] P. J. E. Peebles, *Principles of Physical Cosmology*, Princeton University Press, 1993.

[3] A. H. Guth, "Inflationary Universe: A Possible Solution to the Horizon and Flatness Problems," *Phys. Rev. D* 23, 347 (1981).

[4] V. F. Mukhanov, H. A. Feldman, and R. H. Brandenberger, "Theory of Cosmological Perturbations," *Phys. Rep.* 215, 203 (1992).

[5] S. Dodelson, *Modern Cosmology*, Academic Press, 2003.

[6] N. Aghanim et al. (Planck Collaboration), "Planck 2018 Results. VI. Cosmological Parameters," *Astron. Astrophys.* 641, A6 (2020).

[7] J. Martin and R. H. Brandenberger, "The Trans-Planckian Problem of Inflationary Cosmology," *Phys. Rev. D* 63, 123501 (2001).

[8] S. Weinberg, "The Cosmological Constant Problem," *Rev. Mod. Phys.* 61, 1 (1989).

[9] M. Fukugita and T. Yanagida, "Baryogenesis Without Grand Unification," *Phys. Lett. B* 174, 45 (1986).

[10] J. B. Hartle and S. W. Hawking, "Wave Function of the Universe," *Phys. Rev. D* 28, 2960 (1983).