
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

\begin{align}
  \ld{\alpha} &= \epsilon_{\alpha\beta} \lu{\beta} \\
  \lu{\alpha} &\equiv \epsilon^{\alpha\beta} \ld{\beta} \\
  \lmtd[\alpha] &= \epsilon_{\dot{\alpha}\dot{\beta}} \ltu[\beta] \\
  \ltu &\equiv \epsilon^{\dot{\alpha}\dot{\beta}} \lmtd[\beta]
  \label{eq:spinors}
\end{align}
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

