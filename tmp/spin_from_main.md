<!-- aaabbbccc -->

# Spinor Helicity formalism and Pauli Matrices properties:

# Spinor helicity formalism \(\vec{\rho} \to \vec{\rho}\cdot\vec{\sigma}\):

<!--
>We shall now introduce the highly useful spinor helicity formalism for the description of scattering amplitudes of massless particles. It provides a uniform description of the on-shell degrees of freedom (momentum and polarization) for the scatter- ing states of all helicities (gluons, fermions, scalars) of massless particles. It also renders the analytic expressions of scattering amplitudes in an often much more compact form compared to the standard four-vector notation.
-->

The spinor helicity formalism is a very useful description of scattering amplitudes of massless particles, enabling us to use the on-shell degrees of freedom with respect to the particles momentum and polarisation to measure the scattering amplitude of massless particles of all helicities (gluons, fermions, scalars).

This method also simplifies the scattering amplitude, by rendering the analytic expressions in a form which does which is much more compact then the standard four-vector notation
[@Plefka:2014aa, pp 15]

\begin{align}
  \commutator{\frac{\sigma^i}{2}}{\frac{\sigma^j}{2}} & = i\epsilon^{ijk}\frac{\sigma^k}{2}
\end{align}


<!-- Properties \(SU(2)\): -->

\begin{align}
  \rho^\mu &= 2\times 2 \qq{matrix}\\
  \sigma^0 &= \one_2\\
  \sigma^i &= \qq{Pauli spin matrices}
\end{align}

\begin{equation}
  \label{eq:paulispin_innerprod}
  p^\mu \sigma_\mu \equiv \rho^0\sigma_0 + \vec{\rho}\cdot\vec{\sigma}
\end{equation}

where:

\begin{align}
  \det(p^\mu \sigma_\mu ) & \equiv \vec{p}^2 \\
  \qq{Where, for a massless particle} p^2 &= 0\\
  (\rho^0)^2 - (\vec{p})^2 &= 0
\end{align}

These relations here set the stage for being able to work with massless particles.

\begin{definition}[Spinor Helicity Formalism]
  \begin{equation}
    \label{eq:spinor_helicity_formalism}
    (p^\mu \sigma_\mu)_{\alpha \dot\alpha} = \lambda_\alpha \tilde{\lambda}_{\dot\alpha}
  \end{equation}
\end{definition}

<!-- New From Here 16th Feb 2020 -->

## Facts about \(\sigma_\mu\):

When using the  Minkowski spacetime metric, we represent as following:

\begin{align}
  \sigma^\mu_{\alpha\dot{\alpha}} &= \left(\one, \vec{\sigma} \right)\\
  \bar{\sigma}^{\mu\  \dot{\alpha}\beta} &= \left(\one, -\vec{\sigma} \right)\\
\end{align}

With the Euclidian metric, we represent as following:

\begin{align}
  \sigma^\mu_{\alpha\dot{\alpha}} &= \left(\one, i\vec{\sigma} \right)\\
  \bar{\sigma}^{\mu\  \dot{\alpha}\beta} &= \left(\one, -i\vec{\sigma} \right)\\
\end{align}

So that:

\begin{align}
    P_{\alpha \dot{\alpha}} &= p^\mu \sigma_{\mu\ \alpha \dot{\alpha}}\\
    \bar{P}^{\dot{\alpha} \alpha} &= p^\mu \bar{\sigma}_\mu^{\ \dot{\alpha}\alpha}
\end{align}   

Then \(\epsilon_{\alpha\beta}\) similar to Levi-Cevita.

\begin{equation}
  \epsilon_{12} = -\epsilon_{21}
\end{equation}

Introducing the baracket notation: \(\langle \quad \rangle\) and \([ \quad ]\)

\begin{align}
  \rho^\mu \sigma_\mu &= \rho^0 \sigma_0 + \vec{p}\cdot \vec{\sigma}\\
  \rho_{\alpha \dot{\alpha}}&= \ld{\alpha}\ltd{\alpha}
\end{align}


<!--
@import "/dissertation/assets/custom.md"
 -->

# Angular Momentum properties:

\begin{align}
  \vec{J} &= \vec{x} \times \vec{p}\\
  &= xp_y - yp_x
\end{align}

Using the a commutator:

\begin{align}
  \commutator{J^1}{J^2} &= \commutator{x^2p^3 - x^3p^2}{x^3p^1 - x^1p^3}\\
  &= (x^2p^3 - x^3p^2)(x^3p^1 - x^1p^3) - (x^3p^1 - x^1p^3)(x^2p^3 - x^3p^2)
\end{align}

(Only commutator with same index are non-zero)

\begin{align}
  \commutator{J_i}{J_i} &= 0\\
  \commutator{J_i}{J_j} &\ne 0\\
\end{align}

This leads to the formal relation of angular momentum:

\begin{equation}
  \label{eq:angmomentum_commutator}
  \commutator{J^i}{J^j} = i \hbar J^{ijk} \sigma^k J^k
\end{equation}

This related transformation and sum to Noethers theorem

# Noethers Theorem

\begin{equation}
  \label{eq:noethers_theorem}
  I = \sum_r \pdv{\L}{\dot{q}_r}\delta q_r
\end{equation}


# \(SU\) Group:

## \(SU(2)\)

\begin{align}
  SU(2) \to U(N) &= N\times N matrix\\
   &= U^\dagger U = \one \qq{Unitary}
\end{align}

\((SU(N)\) are a special subset of unitary matrices (\(\det U = \pm 1\))

Taylor expansion of \(U\):

\begin{align}
  U &= e^{iA}\\
  e^x &= 1 + \frac{x^2}{2} + \frac{x^3}{3} \dots
\end{align}

Impose the following conditions:

\begin{align}
  \det{e^{iA}} = \one \implies \det{M} &= e^{\Tr (\log{M})} \\
   &= e^{\Tr (\log{(\exp(iA) )} ) }\\
   &= e^{\Tr (iA)}\\
   &= e^{i \Tr (A)} \implies \Tr (A) = 0
\end{align}

Condition: \(U^\dagger U = \one\)
Special unitarity: add \(\det A = \pm 1 \to SU(N)\)

\begin{align}
  U &= e^{iA}\\
  A^\dagger &= A \qq{Unitary, hermitian}\\
  \Tr A &= 0
\end{align}

This implies we can write:

\begin{equation}
  \label{eq:unitary_group}
  U = e^{i\alpha^a \frac{\sigma^a}{2}}, \quad a = (1,2,3)
\end{equation}

where:

\begin{equation}
  e^{i\alpha^a \frac{\sigma^a}{2}} = \exp(\sum_{a=1}^3 i\alpha^a \frac{\sigma^a}{2})
\end{equation}

## Proofs:

\begin{align}
  U^{\dagger} U &= \one\\
  (U_1U_2)^\dagger(U_1U_2) &= \one\\
  U^\dagger_2 U^\dagger_1 U_1 U_2 & = \one
\end{align}
