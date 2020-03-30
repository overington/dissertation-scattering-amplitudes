## Spinor Helicity formalism and Pauli Matrices properties:
## Spinor helicity formalism $\vec{\rho} \to \vec{\rho}\cdot\vec{\sigma}$:

<!--
>We shall now introduce the highly useful spinor helicity formalism for the description of scattering amplitudes of massless particles. It provides a uniform description of the on-shell degrees of freedom (momentum and polarization) for the scatter- ing states of all helicities (gluons, fermions, scalars) of massless particles. It also renders the analytic expressions of scattering amplitudes in an often much more compact form compared to the standard four-vector notation.
-->

The spinor helicity formalism is a very useful description of scattering amplitudes of massless particles, enabling us to use the on-shell degrees of freedom with respect to the particles momentum and polarisation to measure the scattering amplitude of massless particles of all helicities (gluons, fermions, scalars).

This method also simplifies the scattering amplitude, by rendering the analytic expressions in a form which does which is much more compact then the standard four-vector notation
[@Plefka:2014aa, pp 15]

$$
\begin{aligned}
  \commutator{\frac{\sigma^i}{2}}{\frac{\sigma^j}{2}} & = i\epsilon^{ijk}\frac{\sigma^k}{2}
\end{aligned}
$$


<!-- Properties $SU(2)$: -->

$$
\begin{aligned}
  \rho^\mu &= 2\times 2 \qq{matrix}\\
  \sigma^0 &= \one_2\\
  \sigma^i &= \qq{Pauli spin matrices}\\
\end{aligned}
$$

\begin{equation}
  \label{eq:paulispin_innerprod}
  p^\mu \sigma_\mu \equiv \rho^0\sigma_0 + \vec{\rho}\cdot\vec{\sigma}
\end{equation}

where:

$$
\begin{aligned}
  \det(p^\mu \sigma_\mu ) & \equiv \vec{p}^2 \\
  \qq{Where, massless particles} p^2 &= 0\\
  (\rho^0)^2 - (\vec(p))^2 &= 0
\end{aligned}
$$

These relations here set the stage for being able to work with massless particles.


\begin{equation}
  \label{eq:spinor_helicity_formalism}
  (p^\mu \sigma_\mu)_{\alpha \dot\alpha} = \lambda_\alpha \tilde{\lambda}_{\dot\alpha}
\end{equation}

<!-- New From Here 16th Feb 2020 -->

### Facts about $\sigma_\mu$:

When using the  Minkowski spacetime metric, we represent as following:
$$
\begin{aligned}
  \sigma^\mu_{\alpha\dot{\alpha}} &= \left(\one, \vec{\sigma} \right)\\
  \bar{\sigma}^{\mu\  \dot{\alpha}\beta} &= \left(\one, -\vec{\sigma} \right)\\
\end{aligned}
$$

With the Euclidian metric, we represent as following:

$$
\begin{aligned}
  \sigma^\mu_{\alpha\dot{\alpha}} &= \left(\one, i\vec{\sigma} \right)\\
  \bar{\sigma}^{\mu\  \dot{\alpha}\beta} &= \left(\one, -i\vec{\sigma} \right)\\
\end{aligned}
$$

So that:

$$
\begin{aligned}
    P_{\alpha \dot{\alpha}} &= p^\mu \sigma_{\mu\ \alpha \dot{\alpha}}\\
    \bar{P}^{\dot{\alpha} \alpha} &= p^\mu \bar{\sigma}_\mu^{\ \dot{\alpha}\alpha}
\end{aligned}   
$$

Then $\epsilon_{\alpha\beta}$ similar to Levi-Cevita.
$$
  \epsilon_{12} = -\epsilon_{21}
$$

Introducing the baracket notation: $\langle \quad \rangle$ and $[ \quad ]$

$$
\begin{aligned}
  \rho^\mu \sigma_\mu &= \rho^0 \sigma_0 + \vec{p}\cdot \vec{\sigma}\\
  \rho_{\alpha \dot{\alpha}}&= \ld{\alpha}\ltd{\alpha}
\end{aligned}
$$
