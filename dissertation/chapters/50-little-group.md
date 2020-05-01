# Groups:

## \(SU(2)\)

\begin{align}
  SU(2) \to U(N) &= N\times N matrix\\
   &= U^\dagger U = \one \qq{Unitary}
\end{align}

\((SU(N)\) are a special subset of unitary matrices (\(\det(U)= \pm 1\))

Taylor expansion of \(U\):

\begin{align}
  U &= e^{iA}\\
  e^x &= 1 + \frac{x^2}{2} + \frac{x^3}{3} \dots
\end{align}

Impose the following conditions:

\begin{align}
  \det( e^{iA} ) = \one \implies \det( M ) &= e^{\Tr (\log{M})} \\
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

**Proofs**:

\begin{align}
  U^{\dagger} U &= \one\\
  (U_1U_2)^\dagger(U_1U_2) &= \one\\
  U^\dagger_2 U^\dagger_1 U_1 U_2 & = \one
\end{align}



<!-- begin:2019.11.19.md -->

<!-- begin:dissertation/log/2019.10.23.md -->

## \(SO(1,3)\) Lorentz Group

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

  The Lorentz Group \(SO(1,3) \) is isomorphic to \(SL(2,\CC)\cross SL(2,\CC) \)

\end{definition}

A transformation that is a representation of this group is are known as the
**spinor transformations**:

<!-- #TODO: Write Spinor Transformation definition in words -->

\begin{definition}[Spinor Transformations]
A spinor transforms as follows:

\begin{align}
  \tensor{\Psi}{^{\prime}_\alpha} &= \tensor{M}{_\alpha^\beta}\tensor{\Psi}{_\beta}\\
  \tensor{\bar{\Psi}}{^{\prime}_{\dot{\alpha}}} &= \tensor{M}{_{\dot{\alpha}}^{\dot{\beta}}}\tensor{\bar{\Psi}}{_\beta}
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

  The determinant is a the reduction of a \(\rank n\) tensor to a \(\rank 0\)
  or scalar value. It is computed from each of the tensors elements, only if
  each of the number of elements are equal. For example, for an \(n=2\) ranked
  tensor, the corresponding matrix \(A_{ij}\) where there are \(i=j\) elements.
  The quantity of the determinant is used in understanding certain properties
  of the linear transformations.

\begin{equation}
  \det(A) = \abs{A} = \mdet{\xmat*{a}{2}{2}} = a_{11} a_{22} - a_{21}a_{12}
\end{equation}


\end{definition}

Using the Levi-Civita symbol, we can calculate a determinant as such:



\begin{definition}[Levi Civita symbol]

The Levi-Civita symbol reduces a tensor of \(\rank n\) to one of \(\rank 0\) (a
scalar). It is denoted by \(\epsilon _{a_1, a_2, a_3,\cdots,a_n}\), where
\(\epsilon\) has \(n\) subscripts, each of which identifies one of the objects.

Depending on the reference order of its objects, the Levi-Civita symbol is
defined to be:

\begin{itemize}
  \item \(+1 \qq{if} a_1, a_2, a_3,\cdots,a_n \) represents an even permutation.
  \item \(−1 \qq{if} a_1, a_2, a_3,\cdots,a_n \) represents an odd permutation.
  \item \( 0 \qq{if} a_1, a_2, a_3,\cdots,a_n \) does not represent a permutation (i.e., contains duplicate of any of its entries).
\end{itemize}

\begin{equation}
 \epsilon _{a_1, a_2, a_3,\cdots,a_n}= \begin{cases}
 +1 &= \qq{if} a_1, a_2, a_3,\cdots,a_n \qq{even permutation}\\
 -1 &= \qq{if} a_1, a_2, a_3,\cdots,a_n \qq{odd permutation}\\
 0 &= \qq{otherwise}
 \end{cases}
 \label{eq:levi_civita}
\end{equation}

For a tensor or \(\rank 2\), which is our most common use case, this can be
represented by matrix as such:

\begin{equation}
    \epsilon_{\alpha \beta} = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}
     \label{eq:levi_civita_matrix}
\end{equation}

\end{definition}

Using definitions for the  Levi Civita tensor from equation \ref{eq:levi_citita}, we will now explore how this transforms with \(M\)

\begin{equation}
  \epsilon_{\alpha\beta} \to \\
  \tensor{M}{_\alpha^{\alpha^{\prime}}} \\
  \tensor{M}{_\beta^{\beta^{\prime}}}\\
  \epsilon_{\alpha^{\prime} \beta^{\prime}}= \det M\epsilon_{\alpha\beta}
\end{equation}

And this is precisely \(\epsilon_{\alpha\beta} \det(M) = \epsilon_{\alpha\beta}\) and therefore invariant if \(\det M )=1\)


*Side note*:

\begin{align}
  \epsilon =& \begin{pmatrix}0 & -1 \\ 1 & 0\end{pmatrix} = -i\sigma_2\\
  -\epsilon =& \begin{pmatrix}0 & 1 \\ -1 & 0\end{pmatrix} = \, \, \, i\sigma_2\\
  \sigma_2 =& \begin{pmatrix}0 & -i \\ i & 0\end{pmatrix}
\end{align}


<!-- end:dissertation/log/2019.10.23.md -->


## Little group and weights

In 1932, Eugene Paul Wigner presented a paper titled \textit{On unitary
representations of the inhomogeneous Lorentz group} [see @Wigner:1939aa pp
184-194 Section 6. REDUCTION OF THE REPRESENTATIONS OF THE INHOMOGENEOUS
LORENTZ GROUP TO REPRESENTATIONS OF A "LITTLE GROUP"], where he discusses a way
to classify elementary particles by their helicity / spin quantum numbers,
using the a new group he calls the \textit{Little Group}

\begin{definition}[Little group]

Wigner's Little group is defined as the subgroup of homogeneous Lorentz Group
that leaves the energy-momentum vector of a particle invariant:

\begin{equation}
  \tensor{W}{^\mu_\nu} = k^\mu
\end{equation}

\end{definition}


For massless particles (gluons) in 3+1 dimensions; the little group is the
euclidean group \(E(2)\), which is the semi direct product of \(SO)(2)\).

<!--
   - TODO: Is the euclidean group mentioned above, the same as Galilean mechanics?
   - If so, make a mention of what equation number we defined it in beforehand
   -->

One can obtain the Little Group as a particular limit of the rotation group
\(SO(3)\)


In 3+1 dimensions, the little group for a massive particle is the rotation group SO(3). On the other hand, for a massless particle, the little group is the Euclidean group E(2) which is a semi-direct product of SO(2) and T(2) - the group of translations in the 2-dimensional plane.


@Banerjee:2002aa


