---
title: "Quantum Gravity: The Clash Between General Relativity and Quantum Theory"
date: 2026-06-23 11:10:00 +0700
categories: [Physics, Quantum Gravity]
tags: [physics, theoretical-physics, quantum-gravity, general-relativity, string-theory, holography, unification]
description: "A rigorous analysis of the fundamental obstacles to quantizing gravity: perturbative non-renormalizability, background independence, the problem of time, black hole thermodynamics, and the conceptual foundations of candidate approaches."
math: true
---

## Abstract

Quantum gravity is the search for a consistent framework that unifies general relativity (GR) with quantum mechanics. The difficulty is not merely technical but conceptual: GR describes spacetime as a dynamical continuum whose geometry responds to stress-energy, while quantum field theory (QFT) treats spacetime as a fixed background arena. Perturbative quantization of the Einstein–Hilbert action yields a non-renormalizable expansion requiring infinitely many independent couplings. The Hamiltonian constraint of canonical quantum gravity eliminates external time, leading to the Wheeler–DeWitt equation and the problem of interpreting dynamical evolution. Black hole thermodynamics reveals that the entropy of a black hole scales with its area, not its volume — the holographic principle — suggesting a fundamental reorganization of the degrees of freedom. This article provides a rigorous analysis of these obstructions through power-counting arguments, the Wheeler–DeWitt equation, and black hole thermodynamics. It surveys the main candidate frameworks — string theory, loop quantum gravity, asymptotic safety, causal set theory — and identifies the open problems that any complete quantum gravity theory must resolve.

**Keywords:** quantum gravity, non-renormalizability, Wheeler–DeWitt equation, black hole thermodynamics, holographic principle, string theory, loop quantum gravity

## 1. Introduction

The incompatibility between general relativity and quantum mechanics is the deepest open problem in fundamental physics. Each framework is extraordinarily successful in its domain: GR has been confirmed by solar-system tests, gravitational-wave observations, and black hole imaging [1,2]; QFT has been validated to parts-per-billion precision in the Standard Model [3]. Yet they rest on incompatible assumptions about the nature of spacetime.

GR treats the metric $g_{\mu\nu}$ as a dynamical field governed by the Einstein equations, making spacetime itself a participant in physical processes. QFT, by contrast, requires a fixed, nondynamical background spacetime on which quantum fields propagate. A Theory of Everything must resolve this conflict [4].

This article analyzes the conceptual and technical obstructions to quantizing gravity, examines the low-energy EFT of gravity, and surveys the major candidate approaches. It does not claim that any approach is confirmed; all remain open research programs.

## 2. Preliminaries and Notation

The reduced Planck mass is $M_P = 1/\sqrt{8\pi G} \approx 2.4 \times 10^{18}\ \mathrm{GeV}$, the Planck length $\ell_P = 1/M_P \approx 1.6 \times 10^{-35}\ \mathrm{m}$. Natural units $\hbar = c = 1$ are used. Metric signature is (+,-,-,-). The Einstein–Hilbert action is

$$
S_{\mathrm{EH}} = \frac{1}{16\pi G} \int d^4x\, \sqrt{-g}\, R.
$$

The ADM decomposition of the metric is

$$
ds^2 = -N^2 dt^2 + h_{ij}(dx^i + N^i dt)(dx^j + N^j dt),
$$

with lapse $N$, shift $N^i$, and spatial metric $h_{ij}$.

## 3. Theoretical Framework

### 3.1 Perturbative Quantum Gravity

Expanding $g_{\mu\nu} = \eta_{\mu\nu} + \kappa h_{\mu\nu}$ with $\kappa = \sqrt{32\pi G}$ gives the graviton propagator

$$
\langle h_{\mu\nu}(p) h_{\rho\sigma}(-p) \rangle \propto \frac{i(\eta_{\mu\rho}\eta_{\nu\sigma} + \eta_{\mu\sigma}\eta_{\nu\rho} - \eta_{\mu\nu}\eta_{\rho\sigma})}{p^2 + i\epsilon}.
$$

Interactions are $\kappa\, h\, \partial h\, \partial h + \kappa^2 h^2 \partial h\, \partial h + \cdots$.

### 3.2 The Effective Field Theory of Gravity

At $E \ll M_P$, quantum gravity is described by an EFT:

$$
S = \int d^4x\, \sqrt{-g} \left[ \frac{M_P^2}{2} R + c_1(\mu) R^2 + c_2(\mu) R_{\mu\nu}^2 + \cdots \right] + S_{\mathrm{matter}}.
$$

Higher-curvature terms are suppressed by $(E/M_P)^2$ [5].

### 3.3 Canonical Quantum Gravity

In the ADM formalism, the Hamiltonian constraint $\mathcal{H} = 0$ encodes diffeomorphism invariance. Upon quantization, the wavefunctional $\Psi[h_{ij}]$ satisfies the Wheeler–DeWitt equation

$$
\left[ -G_{ijkl} \frac{\delta^2}{\delta h_{ij} \delta h_{kl}} + \sqrt{h} \left( -R^{(3)} + 2\Lambda + 16\pi G\, \hat{\rho}_{\mathrm{matter}} \right) \right] \Psi[h_{ij}] = 0,
$$

where $G_{ijkl} = \frac{1}{2\sqrt{h}} (h_{ik}h_{jl} + h_{il}h_{jk} - h_{ij}h_{kl})$ is the DeWitt supermetric [6,7].

## 4. Main Derivation: Power Counting for Quantum Gravity

Consider a diagram with $L$ loops, $E$ external graviton lines, $I$ internal lines, and $V$ vertices. The superficial degree of divergence in $d = 4$ is

$$
D = 4L - 2I + \sum_v \delta_v.
$$

Using $L = I - V + 1$ and $2I + E = \sum_v n_v$, and noting that each Einstein–Hilbert vertex has $\delta_v = 0$ (exactly two derivatives), one obtains

$$
D = 2 - \frac{E}{2}.
$$

Results:
- $E = 2$: $D = 1$ — linear divergence.
- $E = 4$: $D = 0$ — logarithmic divergence requiring $R^2$, $R_{\mu\nu}^2$ counterterms.
- Higher $E$: superficially convergent, but higher loops produce divergences with more derivatives.

At each loop order, new independent curvature invariants appear. At $L = 1$: $R^2$ and $R_{\mu\nu}^2$; at $L = 2$: $R^3$ and $R\Box R$; and so on. Each requires an independent coupling. Perturbative quantum gravity thus loses all predictive power at the Planck scale because an infinite number of measurements would be needed [5,8].

## 5. Interpretation of the Main Equations

**The Wheeler–DeWitt equation.** The DeWitt supermetric $G_{ijkl}$ defines a metric on superspace (the space of all 3-metrics). The first term is a kinetic term for the spatial metric; the second term is a potential involving the three-curvature and the cosmological constant. The equation contains **no explicit time derivative** — a direct consequence of the Hamiltonian constraint $\mathcal{H} = 0$ following from diffeomorphism invariance. This absence of external time is the problem of time: "evolution" must be extracted relationally from the geometry itself.

**Black hole thermodynamics.** Hawking's calculation yields a thermal spectrum with temperature

$$
T_H = \frac{1}{8\pi G M},
$$

and entropy

$$
S_{\mathrm{BH}} = \frac{A}{4G},
$$

where $A$ is the horizon area. The entropy scales as $A$ rather than volume — a qualitative departure from local QFT. This area law is the origin of the holographic principle: the number of degrees of freedom inside a region is bounded by its surface area in Planck units.

## 6. Consistency Checks and Limiting Cases

**Classical limit.** Any candidate theory must reproduce GR in the limit $\hbar \to 0$ (or $\ell_P/L \to 0$). In string theory, the massless spin-2 closed-string excitation reproduces the graviton. In loop quantum gravity, the classical limit yields the Regge action of discrete gravity.

**Low-energy EFT.** The leading quantum correction to Newton's potential is a genuine prediction [5]:

$$
V(r) = -\frac{Gm_1 m_2}{r} \left[ 1 + \frac{41}{10\pi} \frac{G\hbar}{r^2 c^3} + \mathcal{O}\left(\frac{G^2}{r^4}\right) \right].
$$

**Generalized second law.** The sum $S_{\mathrm{BH}} + S_{\mathrm{outside}}$ never decreases — a consistency condition any quantum gravity framework must respect.

## 7. Discussion

**String theory.** Strings are one-dimensional extended objects whose closed-string spectrum includes a massless spin-2 state — the graviton. String theory is UV-finite at each order of perturbation theory and naturally includes gauge interactions and chiral fermions through compactification. The landscape of consistent compactifications is enormous, and supersymmetry is required for consistency [9].

**Loop quantum gravity.** Canonical quantization using Ashtekar variables ($SU(2)$ connection and densitized triad) yields discrete area and volume spectra:

$$
\hat{A}_{\Sigma} |\text{spin net}\rangle = 8\pi \ell_P^2 \gamma \sum_{p\in\Sigma\cap\Gamma} \sqrt{j_p(j_p+1)} \, |\text{spin net}\rangle,
$$

where $\gamma$ is the Immirzi parameter. The dynamics encoded in the Hamiltonian constraint remains an active problem [10].

**Asymptotic safety.** The hypothesis that GR has a non-Gaussian UV fixed point of the RG. Evidence from the functional RG suggests a fixed point at $g_* \equiv G_* k^2 \sim 1$ in the Einstein–Hilbert truncation.

**The information paradox.** If black holes evaporate thermally, information appears lost, violating unitarity. AdS/CFT resolves this in anti-de Sitter space, but the mechanism for information retrieval in realistic settings remains debated.

## 8. Relation to the Theory of Everything

Quantum gravity is the core of the ToE problem. Each major approach naturally incorporates (or attempts to incorporate) the Standard Model: through compactification (string theory), representation theory (LQG with matter), or emergence from discrete structures (causal sets). No approach yet provides a complete, testable unification, but the cross-constraints among them are narrowing the space of possibilities.

## 9. Common Pitfalls

1. **"Gravitons are the quanta of gravity."** Gravitons describe weak perturbations around a fixed background. At the Planck scale, the true degrees of freedom may not resemble gravitons.

2. **"Quantum gravity is only about small distances."** Quantum gravity also affects horizon-scale physics (black hole information) and cosmology (inflationary perturbations, the big bang).

3. **"Non-renormalizability means GR cannot be quantized."** GR as an EFT is predictive at $E \ll M_P$. Non-renormalizability means perturbation theory fails, not that quantization is impossible.

4. **"String theory is the only candidate."** Several frameworks exist (LQG, causal sets, asymptotic safety, CDT).

## 10. Conclusion

Quantum gravity is the deepest open problem in fundamental physics. Perturbative non-renormalizability, the problem of time, and the information paradox each expose a different aspect of the incompatibility between GR and QFT. Candidate approaches offer different resolutions, but none has achieved the status of a complete, experimentally tested theory.

## References

[1] C. W. Misner, K. S. Thorne, and J. A. Wheeler, *Gravitation*, W. H. Freeman, 1973.

[2] R. M. Wald, *General Relativity*, University of Chicago Press, 1984.

[3] M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory*, Westview Press, 1995.

[4] S. Weinberg, "Ultraviolet Divergences in Quantum Theories of Gravitation," in *General Relativity: An Einstein Centenary Survey*, Cambridge University Press, 1979.

[5] J. F. Donoghue, "General Relativity as an Effective Field Theory: The Leading Quantum Corrections," *Phys. Rev. D* 50, 3874 (1994).

[6] B. S. DeWitt, "Quantum Theory of Gravity. I. The Canonical Theory," *Phys. Rev.* 160, 1113 (1967).

[7] C. Rovelli, *Quantum Gravity*, Cambridge University Press, 2004.

[8] M. H. Goroff and A. Sagnotti, "The Ultraviolet Behavior of Einstein Gravity," *Nucl. Phys. B* 266, 709 (1986).

[9] J. Polchinski, *String Theory*, Vol. I and II, Cambridge University Press, 1998.

[10] T. Thiemann, *Modern Canonical Quantum General Relativity*, Cambridge University Press, 2007.
