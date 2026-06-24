---
title: "Conformal Field Theory and the Bootstrap Program"
date: 2026-06-23 22:00:00 +0700
categories: [Physics, Quantum Field Theory]
tags: [physics, theoretical-physics, conformal-field-theory, quantum-field-theory, bootstrap, critical-phenomena, ads-cft]
description: "A rigorous treatment of conformal field theory: the conformal group, primary operators, operator product expansion, radial quantization, conformal bootstrap, minimal models, and the space of conformal theories."
math: true
---

## Abstract

Conformal field theories (CFTs) describe the fixed points of the renormalization group — scale-invariant quantum theories that capture the universal behavior of critical systems and form the basis of the AdS/CFT correspondence. This article provides a rigorous treatment of CFT in general spacetime dimension $d \geq 2$, with special attention to $d = 2$ where the conformal symmetry algebra is infinite-dimensional. We develop the conformal group and its representations, primary and descendant operators, the operator product expansion (OPE), radial quantization, unitarity bounds, the conformal bootstrap equation, and the solution of minimal models in two dimensions. The relation to RG fixed points, critical exponents, and the modern conformal bootstrap program for $d > 2$ is discussed. The article concludes with the role of CFT in holography and the search for a quantum theory of gravity.

**Keywords:** conformal field theory, conformal bootstrap, operator product expansion, primary operators, minimal models, AdS/CFT

## 1. Introduction

Conformal invariance is the largest symmetry group of spacetime that preserves the causal structure. A quantum field theory at an RG fixed point is scale-invariant, and under mild assumptions (unitarity, Poincaré invariance), scale invariance implies full conformal invariance [1]. Conformal field theories therefore describe the critical points of statistical systems and the ultraviolet/infrared limits of quantum field theories.

The conformal bootstrap program, initiated by Ferrara, Grillo, and Gatto [2] and Polyakov [3], seeks to determine the space of conformal field theories from consistency conditions alone — crossing symmetry, unitarity, and the structure of the operator product expansion. This program has been remarkably successful: the critical exponents of the 3D Ising model have been computed to high precision, and rigorous bounds on operator dimensions constrain the space of viable CFTs [4,5].

In two dimensions, the conformal algebra is infinite-dimensional (the Virasoro algebra), enabling exact solvability. Minimal models — the simplest interacting CFTs — have been fully classified [6]. In higher dimensions, the bootstrap is a numerical and analytical program that continues to produce new results.

This article develops CFT systematically from the conformal group through the bootstrap equation, emphasizing conceptual structure and the connection to the search for a Theory of Everything.

## 2. Preliminaries and Notation

We work in $d$-dimensional Minkowski or Euclidean spacetime, with metric $\eta_{\mu\nu} = \mathrm{diag}(+1, -1, \dots, -1)$ in Lorentzian signature and $\delta_{\mu\nu}$ in Euclidean signature. Coordinates are $x^\mu$ with $\mu = 0, 1, \dots, d-1$.

The conformal group $\mathrm{SO}(d,2)$ (Lorentzian) or $\mathrm{SO}(d+1,1)$ (Euclidean) includes:

- Translations $P_\mu = -i\partial_\mu$
- Lorentz rotations $L_{\mu\nu} = i(x_\mu\partial_\nu - x_\nu\partial_\mu)$
- Dilatations $D = -i x^\mu\partial_\mu$
- Special conformal transformations $K_\mu = -i(2x_\mu x^\nu\partial_\nu - x^2\partial_\mu)$

The commutation relations define the conformal algebra:

$$
\begin{aligned}
[D, P_\mu] &= iP_\mu, \quad [D, K_\mu] = -iK_\mu, \quad [K_\mu, P_\nu] = 2i(\eta_{\mu\nu}D - L_{\mu\nu}), \\
[L_{\mu\nu}, P_\rho] &= i(\eta_{\nu\rho}P_\mu - \eta_{\mu\rho}P_\nu), \quad [L_{\mu\nu}, K_\rho] = i(\eta_{\nu\rho}K_\mu - \eta_{\mu\rho}K_\nu),
\end{aligned}
$$

with the usual Lorentz algebra $[L_{\mu\nu}, L_{\rho\sigma}]$ and all other commutators vanishing.

A local operator $\mathcal{O}(x)$ is called a **primary operator** of scaling dimension $\Delta$ and Lorentz spin $\ell$ if it transforms under conformal transformations $x \to x'$ as

$$
\mathcal{O}'(x') = \left| \frac{\partial x'}{\partial x} \right|^{-\Delta/d} \mathcal{O}(x),
$$

up to spin indices. More precisely, under a conformal transformation $x \to x'$, a spinless primary satisfies

$$
\mathcal{O}(x) \to \left| \frac{\partial x'}{\partial x} \right|^{\Delta/d} \mathcal{O}(x').
$$

Descendant operators are obtained by acting with derivatives $\partial_\mu$ on primaries; they form the conformal multiplet.

The two-point function of scalar primaries is fixed by symmetry:

$$
\langle \mathcal{O}_1(x_1) \mathcal{O}_2(x_2) \rangle = \frac{\delta_{\Delta_1\Delta_2}}{|x_{12}|^{2\Delta_1}},
$$

where $x_{12} = x_1 - x_2$ and $\lvert x_{12}\rvert^2 = \sum_\mu (x_{12}^\mu)^2$ in Euclidean signature. The three-point function is fixed up to a structure constant $f_{123}$:

$$
\langle \mathcal{O}_1(x_1) \mathcal{O}_2(x_2) \mathcal{O}_3(x_3) \rangle = \frac{f_{123}}{|x_{12}|^{\Delta_1+\Delta_2-\Delta_3} |x_{23}|^{\Delta_2+\Delta_3-\Delta_1} |x_{13}|^{\Delta_1+\Delta_3-\Delta_2}}.
$$


## 3. Theoretical Framework

### 3.1 The Operator Product Expansion

In any quantum field theory, the product of two local operators at nearby points can be expanded as a sum over local operators — the operator product expansion (OPE) [7]. In a CFT, the OPE converges:


$$
\mathcal{O}_i(x) \mathcal{O}_j(0) = \sum_k f_{ijk}\, |x|^{\Delta_k - \Delta_i - \Delta_j} \left( \mathcal{O}_k(0) + \text{descendants} \right),
$$

where the sum runs over all primary operators, and the structure constants $f_{ijk}$ are the same as those appearing in three-point functions. The descendant contributions are uniquely determined by conformal symmetry in terms of $f_{ijk}$ and the scaling dimensions.

The convergence of the OPE in CFT follows from state-operator correspondence: inserting an operator at $x$ is equivalent to creating a state on a sphere surrounding $x$. The OPE converges at finite separation because the sum over operators corresponds to a sum over energy eigenstates in radial quantization.

### 3.2 Radial Quantization and the State-Operator Correspondence

Map $\mathbb{R}^d$ to the cylinder $\mathbb{R} \times S^{d-1}$ via the conformal transformation

$$
x^\mu \to (\tau, n^a), \quad r = e^\tau, \quad n^a = \frac{x^a}{r},
$$

where $\tau$ is radial time on the cylinder. The dilatation operator $D$ becomes the Hamiltonian on the cylinder: $H_{\mathrm{cyl}} = D$.

In radial quantization, states are defined on spheres centered at the origin. Inserting an operator at the origin creates a state:

$$
|\mathcal{O}\rangle = \lim_{x \to 0} \mathcal{O}(x)|0\rangle.
$$

The scaling dimension $\Delta$ is the eigenvalue of $D$:

$$
D|\mathcal{O}\rangle = i\Delta |\mathcal{O}\rangle.
$$

Conversely, every state on $S^{d-1}$ corresponds to a local operator at the origin — this is the state-operator correspondence, a defining feature of CFT. The Hilbert space on the cylinder decomposes into representations of the conformal group:

$$
\mathcal{H} = \bigoplus_{\Delta,\ell} \mathcal{H}_{\Delta,\ell}.
$$

### 3.3 Unitarity Bounds

Unitarity imposes lower bounds on scaling dimensions. For a spin-$\ell$ primary in $d > 2$,

$$
\Delta \geq \begin{cases}
\frac{d-2}{2}, & \ell = 0 \text{ (scalar)} \\
d - 2 + \ell, & \ell \geq 1 \text{ (symmetric traceless)}.
\end{cases}
$$

Saturating these bounds gives free (generalized free) fields: the scalar bound $\Delta = (d-2)/2$ corresponds to a free scalar, and $\Delta = d-2+\ell$ corresponds to a conserved current. These bounds follow from requiring positivity of norms in the conformal multiplet.

### 3.4 Conformal Blocks and Crossing Symmetry

The four-point function of identical scalar primaries $\phi$ with dimension $\Delta_\phi$ can be written using the OPE in two inequivalent channels:

$$
\langle \phi(x_1) \phi(x_2) \phi(x_3) \phi(x_4) \rangle = \frac{1}{|x_{12}|^{2\Delta_\phi} |x_{34}|^{2\Delta_\phi}} \sum_{\mathcal{O}} f_{\phi\phi\mathcal{O}}^2\, g_{\Delta,\ell}(u,v),
$$

where $g_{\Delta,\ell}$ are conformal blocks — functions of the conformally invariant cross-ratios

$$
u = \frac{x_{12}^2 x_{34}^2}{x_{13}^2 x_{24}^2}, \qquad v = \frac{x_{14}^2 x_{23}^2}{x_{13}^2 x_{24}^2}.
$$

The conformal blocks encode the contribution of a primary $\mathcal{O}$ and all its descendants. They are eigenfunctions of the conformal Casimir operator [2,5].

Crossing symmetry (associativity of the OPE) requires equality of the $s$-channel and $t$-channel decompositions:

$$
\sum_{\mathcal{O}} f_{\phi\phi\mathcal{O}}^2\, g_{\Delta,\ell}(u,v) = \left(\frac{u}{v}\right)^{\Delta_\phi} \sum_{\mathcal{O}} f_{\phi\phi\mathcal{O}}^2\, g_{\Delta,\ell}(v,u).
$$

This is the **conformal bootstrap equation**. It is a powerful non-perturbative constraint on the spectrum $\{\Delta, \ell\}$ and OPE coefficients $f_{\phi\phi\mathcal{O}}$. Solutions to this equation define consistent CFTs.



## 4. Main Derivation: Conformal Ward Identities and Bootstrap

### 4.1 Conformal Ward Identity

The Ward identity for conformal transformations follows from the variation of the path integral under infinitesimal coordinate transformations $x^\mu \to x^\mu + \epsilon^\mu(x)$, where $\epsilon^\mu$ generates a conformal transformation. For a CFT with no anomaly, the trace of the stress tensor vanishes:

$$
T^\mu_{\ \mu} = 0.
$$

This is the defining local property of a CFT. The Ward identity for local insertions is

$$
\langle \partial_\mu T^{\mu\nu}(x) \mathcal{O}_1(x_1) \dots \mathcal{O}_n(x_n) \rangle = -i \sum_i \delta^{(d)}(x - x_i) \partial_{x_i}^\nu \langle \mathcal{O}_1(x_1) \dots \mathcal{O}_n(x_n) \rangle.
$$

Specializing to dilatations, the integrated Ward identity gives

$$
\sum_i (x_i \cdot \partial_{x_i} + \Delta_i) \langle \mathcal{O}_1(x_1) \dots \mathcal{O}_n(x_n) \rangle = 0,
$$

which is the origin of the scaling behavior of correlation functions.

### 4.2 Derivation of the Bootstrap Equation

Consider the four-point function $\langle \phi(x_1) \phi(x_2) \phi(x_3) \phi(x_4) \rangle$ in Euclidean CFT. Using conformal symmetry, we fix $x_1 = 0$, $x_2 = x$, $x_3 = 1$, $x_4 = \infty$ (a standard choice), after which the correlation function depends only on the cross-ratio $z$ (related to $u = z\bar{z}$, $v = (1-z)(1-\bar{z})$):

$$
G(z,\bar{z}) = \langle \phi(0) \phi(x) \phi(1) \phi(\infty) \rangle.
$$

Inserting the OPE in the $s$-channel (pairs (12)(34)) gives

$$
G(z,\bar{z}) = \sum_{\mathcal{O}} p_{\mathcal{O}}\, g_{\Delta,\ell}(z,\bar{z}), \quad p_{\mathcal{O}} = f_{\phi\phi\mathcal{O}}^2.
$$

Inserting the OPE in the $t$-channel (pairs (14)(23)) and using conformal transformations to map back to the same configuration yields

$$
G(z,\bar{z}) = \left( \frac{z\bar{z}}{(1-z)(1-\bar{z})} \right)^{\Delta_\phi} \sum_{\mathcal{O}} p_{\mathcal{O}}\, g_{\Delta,\ell}(1-z,1-\bar{z}).
$$

Equating the two expressions gives the crossing equation:

$$
\sum_{\mathcal{O}} p_{\mathcal{O}}\, g_{\Delta,\ell}(z,\bar{z}) = \left( \frac{z\bar{z}}{(1-z)(1-\bar{z})} \right)^{\Delta_\phi} \sum_{\mathcal{O}} p_{\mathcal{O}}\, g_{\Delta,\ell}(1-z,1-\bar{z}).
$$

This equation must hold for all $z,\bar{z}$. The program of solving this equation for the spectrum $\{\Delta,\ell\}$ and coefficients $p_{\mathcal{O}}$ is the **conformal bootstrap** [4,5].

### 4.3 Numerical Bootstrap

In practice, the bootstrap equation is turned into constraints using linear or semidefinite programming. For each putative spectrum, one constructs a linear functional $\alpha$ acting on the crossing equation such that

$$
\alpha\left[ g_{\Delta,\ell}(z,\bar{z}) - \left( \frac{z\bar{z}}{(1-z)(1-\bar{z})} \right)^{\Delta_\phi} g_{\Delta,\ell}(1-z,1-\bar{z}) \right] \geq 0
$$

for all operators in the spectrum. If such an $\alpha$ exists, the spectrum is ruled out. By scanning over $\Delta_\phi$, one can carve out the allowed space of CFT data. The most spectacular result is the determination of the 3D Ising model critical exponents: $\Delta_\sigma = 0.5181489(10)$ and $\Delta_\epsilon = 1.412625(10)$ [5].

## 5. Interpretation of the Main Equations

**The OPE and convergence.** The OPE in CFT is not an asymptotic series but a convergent expansion. Its convergence radius is the distance to the nearest other operator insertion. This follows from the state-operator correspondence: the OPE is equivalent to expanding a state in energy eigenstates on the cylinder.

**Crossing symmetry as dynamical principle.** The bootstrap equation encodes associativity of the OPE. It is the CFT analog of the S-matrix bootstrap in scattering theory. Crossing symmetry, combined with unitarity and the conformal algebra, is believed to determine CFT data uniquely.

**Unitarity bounds and the space of CFTs.** The unitarity bounds $\Delta \geq \frac{d-2}{2}$ for scalars carve out the allowed region in $\Delta$-space. Above these bounds lies the space of consistent CFTs; below them, the theory is non-unitary.



## 6. Consistency Checks and Limiting Cases

**Free scalar CFT.** A free massless scalar $\mathcal{L} = \frac12 (\partial\phi)^2$ in $d$ dimensions is a CFT with $\Delta_\phi = (d-2)/2$. The OPE coefficient for $\phi \times \phi$ is $f_{\phi\phi\phi^2} = 2$ and the bootstrap equation reduces to an identity involving hypergeometric functions. This provides an exact test of the bootstrap formalism.

**Mean field theory limit.** The large-$N$ limit of $O(N)$ models gives a generalized free field theory where all OPE coefficients factorize. The bootstrap equation reduces to analytic consistency conditions satisfied by the free-field conformal blocks.

**$d = 2$ and Virasoro symmetry.** In two dimensions, the conformal algebra is infinite-dimensional: the Virasoro algebra

$$
[L_n, L_m] = (n-m) L_{n+m} + \frac{c}{12} n(n^2-1)\delta_{n+m,0},
$$

with central charge $c$. The bootstrap in $d=2$ is solvable for minimal models $M(p,p')$ with $c = 1 - 6(p-p')^2/pp'$. The four-point functions can be expressed in terms of hypergeometric functions via the BPZ equations [6].

## 7. Discussion

### 7.1 Minimal Models

The simplest interacting CFTs in $d=2$ are the minimal models $M(p,p')$, classified by coprime integers $p,p' \geq 2$. Their spectrum of primary operators is finite, with dimensions

$$
\Delta_{r,s} = \frac{(pr - p's)^2 - (p - p')^2}{4pp'}, \quad 1 \leq r \leq p'-1, \; 1 \leq s \leq p-1.
$$

The Yang–Lee model $M(5,2)$ has central charge $c = -22/5$ and is the simplest non-unitary minimal model. The Ising model $M(4,3)$ has $c = 1/2$ and primaries: identity ($\Delta = 0$), spin $\sigma$ ($\Delta = 1/8$), and energy $\epsilon$ ($\Delta = 1$). The three-state Potts model $M(5,4)$ has $c = 4/5$.

### 7.2 The Bootstrap in $d > 2$

The modern numerical bootstrap has produced rigorous bounds on the space of CFTs. Key results include:

- **3D Ising model**: critical exponents determined to 6-7 decimal places, consistent with experimental measurements on fluids and lattice Monte Carlo.
- **$O(N)$ models**: bounds on the lowest operator dimensions for $N = 2,3,4$ show kinks that coincide with known critical points.
- **Conformal window**: the bootstrap has bounded the region in $(d,N)$ space where interacting fixed points exist.

### 7.3 AdS/CFT and Holography

The AdS/CFT correspondence [8] relates $d$-dimensional CFTs to (d+1)-dimensional quantum gravity in asymptotically anti-de Sitter space. The dictionary maps:

- CFT primary operator $\mathcal{O}$ with dimension $\Delta$ $\leftrightarrow$ bulk field with mass $m^2 = \Delta(\Delta-d)$.
- Stress tensor $T_{\mu\nu}$ $\leftrightarrow$ graviton.
- Global symmetry current $J_\mu$ $\leftrightarrow$ gauge field.
- CFT partition function $Z_{\mathrm{CFT}}$ $\leftrightarrow$ bulk path integral with boundary conditions.

The bootstrap equation in the CFT is dual to crossing symmetry of the bulk S-matrix. In the large-$N$ limit, the CFT becomes a generalized free theory dual to weakly coupled gravity.



## 8. Relation to the Theory of Everything

CFT is central to the search for a Theory of Everything for several reasons:

- **RG fixed points define fundamental theories.** A fundamental theory corresponds to a UV fixed point of the renormalization group. Understanding the space of CFTs is equivalent to understanding the possible UV completions of quantum field theories.

- **AdS/CFT provides a non-perturbative definition of quantum gravity.** The most precise formulation of string theory is as a CFT on the boundary of AdS. A complete ToE in asymptotically AdS spacetimes is a CFT — making the classification of CFTs a direct step toward classifying quantum gravity theories.

- **Critical phenomena and quantum phase transitions.** Many condensed matter systems near criticality are described by CFTs. The bootstrap program has determined their universal properties from first principles, demonstrating that CFT data is computable without a Lagrangian.

- **The conformal bootstrap as a non-perturbative method.** The bootstrap is the only known method for solving strongly coupled quantum field theories without relying on a small parameter. It is a candidate framework for studying quantum gravity non-perturbatively.

## 9. Common Pitfalls

1. **"Scale invariance always implies conformal invariance."** In unitary, Poincaré-invariant QFTs in $d=2$ and $d=4$, scale invariance generically implies conformal invariance, but there are known non-unitary counterexamples. In $d > 2$, the proof requires additional assumptions about the spectrum.

2. **"The OPE is an asymptotic expansion."** In CFT, the OPE converges within a finite radius set by the distance to the nearest other operator. This is not true in generic QFT, where the OPE is often asymptotic.

3. **"Conformal blocks are the same in all dimensions."** Conformal blocks depend on $d$ through the Casimir eigenvalues. Blocks in $d=2$ are hypergeometric functions; in $d=4$ they involve more complicated special functions.

4. **"The bootstrap only works in $d=2$."** While the two-dimensional bootstrap is exactly solvable for minimal models, the numerical bootstrap in $d=3,4$ has produced rigorous bounds and precise critical exponents.

5. **"All CFTs are Lagrangian."** Many CFTs — including the 3D Ising model — have no known Lagrangian description. The bootstrap defines and solves these theories without one.

## 10. Conclusion

Conformal field theory is one of the most powerful frameworks in modern theoretical physics. The combination of spacetime symmetry, the operator product expansion, and crossing symmetry yields a non-perturbative approach to quantum field theory at criticality. In two dimensions, the Virasoro algebra enables exact solvability and the classification of minimal models. In higher dimensions, the numerical bootstrap has produced precise results for the 3D Ising model and other physically relevant theories.

The connection to the renormalization group, critical phenomena, and the AdS/CFT correspondence makes CFT indispensable for the search for a Theory of Everything. As the bootstrap program continues to develop, it may provide the framework for defining quantum gravity itself.

## References

[1] A. M. Polyakov, "Conformal Symmetry of Critical Fluctuations," *JETP Lett.* 12, 381 (1970).

[2] S. Ferrara, A. F. Grillo, and R. Gatto, "Tensor Representations of Conformal Algebra and Conformally Covariant Operator Product Expansion," *Ann. Phys.* 76, 161 (1973).

[3] A. M. Polyakov, "Non-Hamiltonian Approach to Conformal Quantum Field Theory," *Zh. Eksp. Teor. Fiz.* 66, 23 (1974).

[4] R. Rattazzi, V. S. Rychkov, E. Tonni, and A. Vichi, "Bounding Scalar Operator Dimensions in 4D CFT," *JHEP* 12, 031 (2008).

[5] D. Poland, S. Rychkov, and A. Vichi, "The Conformal Bootstrap: Theory, Numerical Techniques, and Applications," *Rev. Mod. Phys.* 91, 015002 (2019).

[6] A. A. Belavin, A. M. Polyakov, and A. B. Zamolodchikov, "Infinite Conformal Symmetry in Two-Dimensional Quantum Field Theory," *Nucl. Phys. B* 241, 333 (1984).

[7] K. G. Wilson, "Non-Lagrangian Models of Current Algebra," *Phys. Rev.* 179, 1499 (1969).

[8] J. Maldacena, "The Large N Limit of Superconformal Field Theories and Supergravity," *Adv. Theor. Math. Phys.* 2, 231 (1998).

[9] P. Di Francesco, P. Mathieu, and D. Sénéchal, *Conformal Field Theory*, Springer, 1997.

[10] S. Rychkov, *EPFL Lectures on Conformal Field Theory in D >= 3 Dimensions*, Springer, 2017.
