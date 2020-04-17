## Transformations:

### Galilean to poincar`e

A velocity transformation

\begin{align}
  \dv{x'^0}(x') &= v &\implies \dd x' &= \gamma(\dd x + \beta \dd x^0)\\
  & &\implies \dd x'^0 &= \gamma(\dd x^0 + \beta \dd x)\\
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
