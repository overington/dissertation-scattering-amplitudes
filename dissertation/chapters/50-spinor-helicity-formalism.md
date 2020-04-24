
# Spinor helicity formalism (null vectors)

## Spinor Helicity formalism and Pauli Matrices properties:

### Pauli Matrices

\begin{definition}[Pauli Matrices]
\begin{equation}
\label{eq:momentum_massless_particles}
p^2 = p_\mu p^mu = 0, \qq{and} p_0^2 - \vec{p}^2 = 0
\end{equation}


\begin{align}
\sigma^1 &= \pmqty{\pmat{1}} \\ 
\sigma^2 &= \pmqty{\pmat{2}} \\
\sigma^3 &= \pmqty{\pmat{3}}
\end{align}
\end{definition}

Squaring each of the pauli matrices produces the identity matrix:

\begin{equation}
  \label{eq:pauli_identity}
  \left(\sigma^i \right)^2 = \one
\end{equation}

Proof:

\begin{equation}
\left(\sigma^1 \right)^2 = \pmqty{\pmat{1}}^2 = \pmqty{\imat{2}}
\end{equation}

#### Multiplication \(\to\) identity matrix:

there is a recursive relation, when multiplying the \(i^{\text{th}}\) matrix by the \(j^{\text{th}}\):

\begin{equation}
  \label{eq:pauli_group}
  \sigma^i\sigma^j = \delta^{ij}\one +i\epsilon^{ijk}\sigma{k}
\end{equation}


#### commutation and anti commutation:

They have the following anti/commutator relations
\begin{equation}
  \label{eq:pauli_commutator}
  \commutator{\sigma^i}{\sigma^j} = i\epsilon^{ijk}\sigma^k = \anticommutator{\sigma^j}{\sigma^i}
\end{equation}

#### Trace of multiplication:

The trace of two pauli matrices multiplied together
\begin{equation}
  \label{eq:pauli_trace}
  \Tr \left(\sigma_i \sigma_j \right) = 2\delta^{ij}
\end{equation}
where

\begin{equation}
\sigma_i \sigma_j = \delta^{ij} \one_2 + i\epsilon^{ijk}\sigma^{k}
\end{equation}

<!-- aaabbbccc -->

## Spinor helicity formalism \(\vec{\rho} \to \vec{\rho}\cdot\vec{\sigma}\):

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

### Facts about \(\sigma_\mu\):

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

## Angular Momentum properties:

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

## Noethers Theorem

\begin{equation}
  \label{eq:noethers_theorem}
  I = \sum_r \pdv{\L}{\dot{q}_r}\delta q_r
\end{equation}


## \(SU\) Group:

### \(SU(2)\)

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

### Proofs:

\begin{align}
  U^{\dagger} U &= \one\\
  (U_1U_2)^\dagger(U_1U_2) &= \one\\
  U^\dagger_2 U^\dagger_1 U_1 U_2 & = \one
\end{align}



<!-- begin:2019.11.19.md -->

## Contraction using \(\left[ \quad  \right]\) and \(\langle \quad \rangle\) notation

 In order to move back and forth between our

 \begin{align}
   \agl{\lambda}{\chi} &\equiv& \lambda^\alpha \chi^\beta \epsilon_{\alpha\beta} &= \lambda^\alpha \chi_\alpha
   \\
   \ltd{\alpha}\tilde{\chi}^{\dot{\alpha}} &=& \epsilon_{\dot{\alpha}\beta}\ltu{\beta}\ltu{\alpha} &\equiv \sqr{\tilde{\lambda}}{\tilde{\chi}}
   \\
   2(p_i\cdot p_j) &\equiv& \tensor{{p_i}}{_{\alpha\dot{\alpha}}} \tensor{{p_i}}{^{\dot{\alpha}\alpha}} &= \agl{i}{j} \sqr{j}{i}
 \end{align}

\begin{definition}[Box operator]

\begin{equation}
  \Box \equiv \partial_\mu \partial^\mu \equiv \partial_0 \partial^0 +\partial_i \partial^i = \partial_j^2 - \nabla^2
  \label{eq:box_operator}
\end{equation}

\end{definition}

It has the following properties:

*   For massless particles: \(\left( \Box + m^2 \right) \phi = 0\)
*   Transform for \(\partial_\mu: \partial_\mu e^{ikx}\) for massless particles (i.e. where  \(k^2 = m^2\)):

### Weyl Spinors and equations

\begin{definition}[Weyl Equations]

\begin{align}
  i\partial_\mu \tensor{{\bar{\sigma}}}{^{\dot{\alpha}\alpha}} \Psi_{\alpha} = 0\\
  i\partial_\mu \tensor{\sigma}{_{\alpha \dot{\alpha}}} \tilde{\Psi}_{\alpha} = 0
\end{align}

Where \(\Psi_\alpha, \tilde{\Psi}_\alpha\) are Weyl spinors
\end{definition}

What do we need to solve \(\Psi_\alpha = \xi_\alpha e^{ikx}\):

\begin{align}
  i\partial^{\dot{\alpha}\alpha} \left( \xi_\alpha e^{ikx}\right) &= i^2 k^{\dot{\alpha}\alpha}\xi_\alpha e^{ikx} \\
  &= -\lu{\alpha} \ltu{\alpha} \xi_\alpha e^{ikx}
\end{align}

\begin{definition}[Spin operator \(\hat{h}\)]

\begin{equation}
  \hat{h} = -\frac{1}{2}\lambda \pdv{\lambda} + \frac{1}{2} \pdv{\tilde{\lambda}} \tilde{\lambda}
\end{equation}

\end{definition}

## Creating Amplitudes for a three particle interaction:

\begin{figure}  
  \centering
  \input{assets/amplitude_3pointsimple.tex}
  \caption{Feynman diagram of a three particle interaction}
\end{figure}


\begin{equation}
  A(1,2,3) \approx \agl{1}{2} \agl{2}{3} \agl{3}{1}
\end{equation}

Mixing brackets for three particles doesn't work, for example a three particle "Scattering":

\begin{align}
  \agl{1}{2} \sqr{2}{3} \agl{3}{1} &\to p_1 + p_2 + p_3 = 0\\
  &\to p_1 = -(p_2 + p_3)
\end{align}

As we are looking at massless particles; here our equation goes:

\begin{align}
  p_1^2 &= 0\\
  & = p_2^2 + p_3^2 + 2(p_2 \cdot p_3)\\
  &= 2(p_2 \cdot p_3)\\
  \implies p_1 \cdot p_2 &= p_2 \cdot p_3 = p_3 \cdot p_1  = 0
\end{align}

And complex momenta:

\begin{align}
  2p_1 \cdot p_2 &= 2p_2 \cdot p_3 = 2p_3 \cdot p_1 \\
  \implies \agl{1}{2} \sqr{2}{1} &= 0\\
  \agl{2}{3} \sqr{3}{1} &= 0\\
  \agl{3}{1} \sqr{1}{3} &= 0\\
\end{align}

[@Plefka:2014aa, pp 17, section 1.11 Vanishing Tree Amplitudes]

We will use this and the following to explore a complex momenta:

\begin{align}
\qq{When} \agl{1}{2} &= 0
   \ld{1} &\parallel \ld{2}\\
   \tensor{{\ld{1}}}{_{\alpha}} &= a \tensor{{\ld{2}}}{_{\alpha}}\\
   A(1,2,3) &= \begin{cases} \overbrace{\agl{1}{2}}^{a_1} \overbrace{\agl{2}{3}}^{a_2} \overbrace{\agl{3}{1}}^{a_3}\\
     \underbrace{\sqr{1}{2}}_{\tilde{a_1}}
     \underbrace{\sqr{2}{3}}_{\tilde{a_3}}
     \underbrace{\sqr{3}{1}}_{\tilde{a_3}}
   \end{cases}
\end{align}


## Examples

### Simple using \(\sqr{\quad}{\ }\):

\begin{align}
  \frac{
    \sqr{1}{2}^3
    }{
    \sqr{2}{3} \sqr{3}{1}
    } &=
     &1: + \frac{1}{2}(3-1) &= +1\\
    &&2: + \frac{1}{2}(3-1) &= +1\\
    &&3: + \frac{1}{2}(0-2) &= -1\\
\end{align}

### Simple using \(\agl{\quad}{ }\):

\begin{align}
  \frac{
    \agl{1}{2}^3
    }{
    \agl{2}{3} \agl{3}{1}
    } &=
     &1: - \frac{1}{2}(3-1) &= -1\\
    &&2: - \frac{1}{2}(3-1) &= -1\\
    &&3: - \frac{1}{2}(0-2) &= +1\\
\end{align}

Note:

\begin{align}
  \agl{i}{j} &= - \frac{1}{2}(\qq{\(U_i\)} - \qq{\(D_j\)} )\\
  \sqr{i}{j} &= + \frac{1}{2}(\qq{\(U_i\)} - \qq{\(D_j\)} )
\end{align}


<!--
   - MHV examples:
   - a
   -->


<!-- end:2019.11.19.md -->

# Spinors and transformations

<!-- begin:dissertation/log/2020.01.21.md -->

## Symmetries

 - Spinor Helicity formalism -> Makes simplicity manifest
 - Dynamics: ie Why amplitudes are simple.
 - New methods are simple
 - what is the dot product in terms of spinors.

 ---

 1. Einstein Equation \(E^2 = (pc)^2 + (mc^2)^2\)
 2. Invariant quantities in relativity. What is the set of linear transformations that make the __metric__ invariant?

    - \(\eta \to \Lambda^T \eta \Lambda=\eta\)
    - Lorentz group definitions.

    \begin{equation}
      \overbrace{\mqty(\dmat{a,b})}^{+}  \overbrace{\mqty(\dmat{1,-1})}^{sp}  \overbrace{\mqty(\dmat{a,b})}^{+}
    \end{equation}

    - Transformation of velocity \(\to\) conclusion:

    \begin{equation}
      v' = \frac{\dd{x} + \beta \dd{x_0}}{\dd{x_0} + \beta \dd{x}}
    \end{equation} (Galilean transformation)

 3. Lorentz transformation \(SO(1,3) \to SL(2,\CC)\times SL(2,\CC)\). Arriving at Lorentz invariant transformation \(\agl{1}{\dot{2}} \equiv \tensor{\lambda}{_1^\alpha}\tensor{\lambda}{_{2\dot{\alpha}}}\)

 <!-- end:dissertation/log/2020.01.21.md -->
