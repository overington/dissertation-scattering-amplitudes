
# Elements of the Lorentz group

Here we will introduce some basic concepts: Groups, Algebras and Representations of the Lorentz Group

## Moving Beyond Galilean Mechanics

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

For small velocities, where \(\vec{x}\ll 1\), we can say:

\begin{equation}
  \label{eq:lagrange_smallapprox}
  \sqrt{1-\dvec{x}^2} \approx 1-\frac{\dvec{x}^2}{2} + \dots [\qq{Limit}]
\end{equation}

Using this approximation, we derive:

\begin{equation}
  H \to \frac{\vec{p}^2}{2m} = \frac{m\dvec{x}^2}{2}
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

\begin{equation}
  e_1 = [t,x,y,z]
\end{equation}


## Transformations:

<!-- begin:dissertation/log/2019.10.23.md -->

### Lorentz Transformations

Why \(x_{\dot{\alpha} \alpha}\)  What is this object?

For the Lorentz transformation:

<!-- #TODO: Write definition of Lorentz Group -->

\begin{definition}[Lorentz Transformations]
  \begin{equation}
    P^\mu \to \tensor{\Lambda}{^\mu_\nu} p^\nu \equiv p^{\prime \nu}
  \end{equation}

  Expanding on this, the can arrive at the following explanation:

  \begin{align}
    P_{\alpha \dot{\alpha}} &= \rho^{\mu}\sigma_{\mu \alpha \dot{\alpha}} \to MPM^\dagger
  \end{align}

  Using \(P^{\mu}\rho_\mu = \det p\), the following can be obtained:

  \begin{align}
    \det( MpM^\dagger ) &= \det(p)\\
    \det(M)\det(p)\det(M^\dagger) &= \det(p)\\
    \abs{\det( M )} &= 1
  \end{align}

  \begin{equation}
    \underbrace{SO(1,3)}_{\qq{group}} \to \underbrace{SL(2, \CC)\times SL(2,\CC)}_{\qq{group} \mathbb{Z_2}}
  \end{equation}

  The Lorentz Group \(SO(1,3) \) is isomorephic to \(SL(2,\CC)\cross SL(2,\CC) \)

\end{definition}

A transformation that is a representation of this group is are known as the **Spinor Transofrmations**:

<!-- #TODO: Write Spinor Transformation definition in words -->

\begin{definition}[Spinor Transformations]
The spinors transform as follows:

\(\alpha\)

\begin{align}
  \tensor{\Psi}{^{\prime}_\alpha} &= \tensor{M}{_\alpha^\beta}\tensor{\Psi}{_\beta}\\
  \tensor{\bar{\Psi}}{^{\prime}_{\dot{\alpha}}} &= \tensor{M}{_{\dot{\alpha}}^{\dot{\beta}}}\tensor{\bar{\Psi}}{_\beta}\\
\end{align}

Such that \(\tensor{M}{_\alpha^\beta}\) belongs to \(SL(2,\CC)\), i.e. with \(\det(M)=\one\)
\end{definition}

To build invariant spinors, we first need invariant tensors. The objects we will be working with are tensors of \(\rank 2\), so having an invariant tensor would give us a way of simplifying our equations, by giving us a principal invariant which equal to the coefficient of the characteristic polynomial (see definition: \ref{eq:characteristic_polynomial})

The principal invariants do not change under rotations of the coordinate system 
and satisfy the principle of material frame-indifference
and any function of the principal invariants is also objective.


\begin{definition}[Characteristic polynomials]

  For \(A\), which is a tensor of \(\rank 2\), the characteristic polynomial equation \(p\):

  \begin{equation}
    p(\lambda )=\det(A -\lambda \one)
    \label{eq:characteristic_polynomial}
  \end{equation}

  where \(\one\) is the identity matrix and \(\lambda _{i}\in \CC \) represent the polynomial's eigenvalues.


\end{definition}


When working with determinants, a common method of calculation and simplification is the Levi-Civita symbol.

\begin{definition}[Determinants]

  The determinant is a the reduction of a \(\rank n\) tensor to a \(\rank 0\) or scalar value. It is computed from each of the tensors elements, only if each of the number of elements are equal. For example, for an \(n=2\) ranked tensor, the corresponding matrix \(A_{ij}\) where there are \(i=j\) elements. The quantity of the determinant is used in understanding certain properties of the linear transformations.

\begin{equation}
  \det(A) = \abs{A} = \mdet{\xmat*{a}{2}{2}} = a_{11} a_{22} - a_{21}a_{12}
\end{equation}


\end{definition}

Using the Levi-Civita symbol, we can calculate a determinant as such:



\begin{definition}[Levi Civita symbol]

The Levi-Civita symbol reduces a tensor of \(\rank n\) to one of \(\rank 0\) (a scalar). It is denoted by \(\epsilon _{a_1, a_2, a_3,\cdots,a_n}\), where \(\epsilon\) has \(n\) subscripts, each of which identifies one of the objects.

Depending on the reference order of its objects, the Levi-Civita symbol is defined to be:
 - \(+1 \qq{if} a_1, a_2, a_3,\cdots,a_n \) represents an even permutation.
 - \(−1 \qq{if} a_1, a_2, a_3,\cdots,a_n \) represents an odd permutation.
 - \( 0 \qq{if} a_1, a_2, a_3,\cdots,a_n \) does not represent a permutation (i.e., contains duplicate of any of its entries).

 \begin{equation}
 \epsilon _{a_1, a_2, a_3,\cdots,a_n}= \begin{cases}
 +1 &= \qq{if} a_1, a_2, a_3,\cdots,a_n \qq{even permutation}\\
 -1 &= \qq{if} a_1, a_2, a_3,\cdots,a_n \qq{odd permutation}\\
 0 &= \qq{otherwise}
 \end{cases}
 \label{eq:levi_civita}
 \end{equation}

 For a tensor or \(\rank 2\), which is our most common use case, this can be reprenented by matrix as such:
  \begin{equation}
    \epsilon_{\alpha \beta} = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}
     \label{eq:levi_civita_matrix}
  \end{equation}

\end{definition}

How does this transform with \(M\)

\begin{equation}
  \epsilon_{\alpha\beta} \to \\
  \tensor{M}{_\alpha^{\alpha^{\prime}}} \\
  \tensor{M}{_\beta^{\beta^{\prime}}}\\
  \epsilon_{\alpha^{\prime} \beta^{\prime}}= \det M\epsilon_{\alpha\beta}
\end{equation}

And this is precisely \(\epsilon_{\alpha\beta} \det(M) = \epsilon_{\alpha\beta}\) and therefore invariant if \(\det M )=1\)


\begin{definition}[Spinors]
  Raising and lowering spinor indices

\begin{align*}
  \ld{\alpha} &= \epsilon_{\alpha\beta} \lu{\beta} &
  \lu{\alpha} &\equiv \epsilon^{\alpha\beta} \ld{\beta} \\
  \lmtd{\dot\alpha} &= \epsilon_{\dot{\alpha}\dot{\beta}} \ltu{\beta} &
  \ltu{\alpha} &\equiv \epsilon^{\dot{\alpha}\dot{\beta}} \lmtd{\dot\beta}
  \label{eq:spinors}
\end{align*}
\end{definition}

Proof:
\begin{align}
  \lu{\alpha\prime} &= \epsilon^{\alpha\beta}\tensor{M}{_\beta^\gamma}\ld{\gamma}\\
  &= \underbrace{\epsilon^{\alpha\beta} \tensor{M}{_\beta^\gamma}}_{ \tensor{\left [ \left( M^T \right)^{-1} \right ]}{^{\alpha}_{\delta}} \lu{\delta}} \epsilon_{\gamma\delta} \lu{\delta}\\
  \to \lu{\alpha'} &= \lu{\delta} \tensor{\left( M^{-1} \right)}{_{\delta} ^{\alpha}}\\
  \tensor{\epsilon}{^{\alpha\beta}}\tensor{M}{_\beta^\gamma}\tensor{\epsilon}{_{\gamma\delta}} &\eqq \tensor{ \left( M^{-1} \right) }{_\delta^\alpha}
\end{align}

*Side note*:

\begin{align}
  \epsilon =& \begin{pmatrix}0 & -1 \\ 1 & 0\end{pmatrix} = -i\sigma_2\\
  -\epsilon =& \begin{pmatrix}0 & 1 \\ -1 & 0\end{pmatrix} = \, \, \, i\sigma_2\\
  \sigma_2 =& \begin{pmatrix}0 & -i \\ i & 0\end{pmatrix}
\end{align}

Calculating a Spinor, we have a consistency condition:

\begin{equation}
  \tensor{\epsilon}{^{\alpha\beta}} \tensor{\epsilon}{_{\beta\rho}} \equiv \tensor{\delta}{^\alpha_\rho}
\end{equation}

<!-- end:dissertation/log/2019.10.23.md -->
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

To prove that this quantity of a 4-vector:

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
