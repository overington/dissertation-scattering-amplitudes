<!-- @import "11-introduction.md" -->
<!-- @import "12-relativity.md" -->
<!-- @import "13-groups.md" -->



# Elements of the Lorentz group

Here we will introduce some basic concepts: Groups, Algebras and Representations of the Lorenz Group

## Moving Beyond Galilean Relativity

In order for us to begin understanding interactions between free particles, we
will first inspect their classical form and the systems by which such
interactions have been be described; using reference systems or co-ordinates.
This fist step will allow us to set a time and spatial dimensions of the
system, and allow us to compare two systems in relation to one another, and
measure the change in this relation as one of the systems evolves over time
in relation to the other.

### The changes in the Lagrangian \( \Lg \) and Hamiltonian \(H\)

\begin{align}
  \Lg_{\text{NR}} &= \frac{1}{2} m\dvec{x}^2\\
  \to \Lg_{\text{Rel}} &= -m\sqrt{1-\dvec{x}^2}\\
  H_{\text{NR}} &= \frac{\vec{p}^2}{2m}+V(x)\\
  \to H_{Rel} &= (something)
\end{align}

To calculate this relation, we inspect the Lagrangian relation between its two
component measurables (in an unspecific basis, these can be any two variables
\(\vec{p}, \vec{q}\), but to relate them to the classical equations involving
momentum and position, we will be calling them \(\vec{p}, \vec{x}\))

\begin{equation}
  p \equiv \pdv{\Lg}{\dvec{x}} = \frac{m\dvec{x}}{\sqrt{1-\dvec{x}^2}}
\end{equation}

### The time evolution of the system

Where
\begin{equation}
  H = H(\vec{q}, \vec{p},t)
\end{equation}

\begin{align}
  \dvec{p} &= \dv{\vec{p}}{t} &= -\pdv{H}{\vec{q}}\\
  \dvec{q} &= \dv{\vec{q}}{t} &= +\pdv{H}{\vec{p}}
\end{align}

Thus leaving us with the following set of equations:

\begin{align}
  H &= T+V
  &= \sum_i{\dvec{q}^i\pdv{L}{\dvec{q}^i} -L} = \sum_i{\dvec{q}^ip_i-L}
\end{align}

where

\begin{equation}
  p_i = \pdv{\L}{\dvec{q}^i}
\end{equation}

leading to

\begin{align}
  \H &= m\dvec{x}^2 - (-m\sqrt{1-\dvec{x}^2})\\
  &= \frac{m\dvec{x}}{\sqrt{1-\dvec{x}^2}}\dvec{x} +m\sqrt{1-\dvec{x}^2} \\
  &= \frac{\cancel{m\dvec{x}^2}+m-\cancel{m\dvec{x}^2}}{\sqrt{1-\dvec{x}^2}}\\
  &= \frac{m}{\sqrt{1-\dvec{x}^2}}
\end{align}

Using the approximation we showed above, we can show that

\begin{equation}
  H \to \frac{\vec{p}^2}{2m} = \frac{m\dvec{x}^2}{2}
\end{equation}

For small velocities, where \(\vec{x}\ll 1\), we can say:

\begin{equation}
  \label{eq:lagrange_smallapprox}
  \sqrt{1-\dvec{x}^2} \approx 1-\frac{\dvec{x}^2}{2} + \dots [\qq{Limit}]
\end{equation}


### Einstein Equation

Where we arrive at Einsteins formula, when setting c = 1
\begin{equation}
  \label{eq:einstein}
  H = E = \frac{m}{\sqrt{1-\dvec{x}^2}}
\end{equation}

This explains the principle of relatively according to Einsteins equations, and allows us to begin setting up the formalism for representing interactions which include relativistic properties.

### Principle of relativity

(Classical theory of fields, @Landau:1975aa )
Inertial reference frame in which a body moves in respect to and without any other force enacting on it, proceeds at constant velocity.


### Reference frames:

Two inertial reference frames are related by:

\begin{equation}
  \Delta x = x-x\prime
\end{equation}

where \(\dv{x}{t}=0 \to x\) and \(x\prime\) have same inertial property.


### Intervals:

Event: described by the place where it occurred and times

\begin{align}
  e_1 &= [t,x,y,z]\\
  \text{worldline }&= [t\to t\prime, f(x,y,z)-f\prime(x,y,z)]
\end{align}


## Transformations:

### Galilean to Poincaré

A velocity transformation

\begin{align}
  \dv{x'^0}(x')     &= v\\
  \implies \dd x'   &= \gamma(\dd x + \beta \dd x^0)\\
  \implies \dd x'^0 &= \gamma(\dd x^0 + \beta \dd x)
\end{align}

For small velocities:

\begin{align}
S &= -mc^2 \int \dd t \sqrt{1-\frac{\dvec{x}^2}{c^2}}\\
 &\simeq \frac{1- \dvec{x}^2 }{\left(2c^2\right)^2}
\end{align}


Using \(p^2 = m^2\):

\begin{equation}
  E(\dvec{x}) = \frac{m}{\sqrt{1-\dvec{x}^2}} \to m+m\frac{\dvec{x}^2}{2}
\end{equation}


Claim:

\begin{align}
  (E, \vec{p}) &= \qq{4-momentum}\\
  &= \qq{4-velocity}
\end{align}

There exists these two values

\begin{align}
  p^\mu &\to \tensor{\Lambda}{^\mu_\nu} p^\nu \\
  x^\mu &\to \tensor{\Lambda}{^\mu_\nu} x^\nu
\end{align}

To prove that this quantity os a 4-vector:

\begin{align}
  v^\mu &= \dv{x^\mu}{\tau} \to  \dv{x^\mu}{x} \\
  \dv{x^\mu}{t} \dv{t}{\tau} &= \dv{x}{t}
\end{align}



Lagrangian using the following Taylor expansion:

\begin{align}
  \sqrt{1+\epsilon} &\sim 1+\frac{\epsilon}{2} \\
  \frac{1}{1+\epsilon} &\sim 1-\epsilon
\end{align}

Combined:

\begin{equation}
  \frac{1}{\sqrt{1-\epsilon}} = 1+ \frac{\epsilon}{2}
\end{equation}


(Fundamentally we are searching for a massless particles, where \(p^2 = m^2 = 0\))

### Pauli Matrices

\begin{equation}
  \label{eq:momentum_massless_particles}
  p^2 = p_\mu p^mu = 0, \qq{and} p_0^2 - \vec{p}^2 = 0
\end{equation}


\begin{align}
  \sigma^1 &= \pmqty{\pmat{1}},
  \sigma^2 &= \pmqty{\pmat{2}},
  \sigma^3 &= \pmqty{\pmat{3}}
\end{align}

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


## Spinor Helicity formalism and Pauli Matrices properties:

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
  \sigma^i &= \qq{Pauli spin matrices}\\
\end{align}

\begin{equation}
  \label{eq:paulispin_innerprod}
  p^\mu \sigma_\mu \equiv \rho^0\sigma_0 + \vec{\rho}\cdot\vec{\sigma}
\end{equation}

where:

\begin{align}
  \det(p^\mu \sigma_\mu ) & \equiv \vec{p}^2 \\
  \qq{Where, massless particles} p^2 &= 0\\
  (\rho^0)^2 - (\vec(p))^2 &= 0
\end{align}

These relations here set the stage for being able to work with massless particles.


\begin{equation}
  \label{eq:spinor_helicity_formalism}
  (p^\mu \sigma_\mu)_{\alpha \dot\alpha} = \lambda_\alpha \tilde{\lambda}_{\dot\alpha}
\end{equation}

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

\begin{(SU(N)\end{(} are a special subset of unitary matrices (\(\det U = \pm 1\))

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
  U^dagger U &= \one\\
  (U_1U_2)^\dagger(U_1U_2) &= \one\\
  U^\dagger_2 U^\dagger_1 U_1 U_2 & = \one
\end{align}   
