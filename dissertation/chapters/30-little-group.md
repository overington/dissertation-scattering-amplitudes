# Little group and weights

In 1932, Eugene Paul Wigner presented a paeper titled \textit{On unitary
representations of the inhomogeneous Lorentz group} [see @Wigner:1939aa pp
184-194 Section 6. REDUCTION OF THE REPRESENTATIONS OF THE INHOMOGENEOUS
LORENTZ GROUP TO REPRESENTATIONS OF A "LITTLE GROUP"], where he discusses a way
to classify elementary particles by their helicity / spin quantum numbers,
using the a new group he calls the \textit{Little Group}

\begin{definition}[Little group]

Wigners Little group is defined as the subgroup of homogeneous Lorentz Group
that leaves the energy-momentum verctor of a particle invariant:

\begin{equation}
  \tensor{W}{^\mu_\nu} = k^\mu
\end{equation}

\end{definition}


For massless particles (gluons) in 3+1 dimensions; the little group is the
euclidian group \(E(2)\), which is the semi direct product of \(SO)(2)\).

<!--
   - TODO: Is the euclidian group mentioned above, the same as Galilean mechanics?
   - If so, make a mention of what eqation numner we defined it in beforehand
   -->

One can obtain the Little Group as a particular limit of the rotation group
\(SO(3)\)


In 3+1 dimensions, the little group for a massive particle is the rotation group SO(3). On the other hand, for a massless particle, the little group is the Euclidean group E(2) which is a semi-direct product of SO(2) and T(2) - the group of translations in the 2-dimensional plane.


@Banerjee:2002aa


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

