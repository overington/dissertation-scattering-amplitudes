<!--
@import "assets/custom.md"
-->
## Groups

### The Lorentz Group

[@Landau:1975aa, pp. 9-10] 
<!-- #TODO: Lorrentz Group definition get interesting points -->

>Our purpose is now to Obtain the formula of transformation from one inertial reference system to another, That is, A formula by means of which,Knowing the coordinates \(x,y,z,t,\) of a certain events in the system $K$, We can find the coordinates $x\prime,y\prime,z\prime,t\prime,$ of the same event in another inertial system $K\prime$

>In classical mechanics this question is resolved very simply. Because of the absolute nature of time we there have \(t = t\prime\); if, furthermore, the coordinate axes are chosen as usual (axes $X, X\prime$ coincident $Y, Z$ axes are parallel to $Y\prime, Z\prime$, motion along $X, X\prime$) then the coordinates $y,z$ clearly are equal to $y\prime,z\prime$, while the coordinates $x$ and $x\prime$ differ by the distance traversed by one system relative to the other. If the velocity of the $K\prime$ system relative to $K$ is $V$, then this distance is $Vt$. Thus:

\[
  x = x\prime +Vt,\qquad y = y\prime, \qquad z = z\prime, t=t\prime
  \taglabel{eq:galileotransoformation}
\]


>This formula (\ref{eq:galileotransoformation}) is called the *Galileo transformation*. It is easy to verify that this transformation, as was to be expected, does not satisfy the requirements of the theory of  relativity; it does not leave the interval between events invariant.

>We shall obtain the relativistic transformation precisely as a consequence of the requirement that it leaves the interval between events invariant

\begin{definition}[Lorentz Group]
The Lorentz group is the group of all transformations of Minkowski spacetime which leave the spacetime interval between any two events independent of the reference frame.  They are referred to as the \textit{Lorentz Transformation}

\textit{Minkowski spacetime} is the combination of three-dimensional Euclidean space and time into a four-dimensional manifold.

Lorentz transformations (\(G\)) that take the have the following properties:

\begin{align}
    \exists \quad A, B \in G &:&  A \otimes B &\in G\\
    && A(BC) &= (AB)C \\
  \exists \quad \one &:& A\otimes \one &= A \\
  \exists \quad A^{-1} &:& AA^{-1} &= A^{-1}A = A
\end{align}

\end{definition}

Additionally, let us inspect (???) group which leads us to the same conclusions as above:

\[
  \tensor{x}{^{\mu\prime}} \tensor{x}{_\mu^\prime} \equiv \tensor{x}{^\mu}\tensor{x}{_\mu} \to \Lambda^T \eta \Lambda = \eta \addtag
\]



#### Properties

#### Invariance under transformation:
Invariance of speed of light

\begin{align}
  x^\mu &= \left( x^0, +\vec{x} \right)\\
  x'^\mu &= \tensor{\Lambda}{^\mu_\nu}x^\nu
\end{align}

#### Metric:

\begin{align}
  \tensor{\eta}{_{\mu\nu}} = \begin{pmatrix}
    1 & 0 & 0 & 0\\
    0 & -1 & 0 & 0\\
    0 & 0 & -1 & 0\\
    0 & 0 & 0 & -1
  \end{pmatrix}
\end{align}

such that:

\begin{equation}
  x_\mu \equiv \tensor{\eta}{_{\mu\nu}}x^\nu = \left( x^0, -\vec{x} \right)
\end{equation}

with the important quantity in relativity:

\begin{equation}
  x^2 = x^\mu x_\mu
\end{equation}

### Unitary Group

### Proper and Improper group

Leaving us with the definition of the Lorentz group:

The condition \(\det(\Lambda) = \pm 1\) divides $\L$ into two disconnected components $\L\pm$ , called proper and improper Lorentz transformations.
\begin{equation}
  \label{eq:lorentzgroup}
  \Lambda^T \eta \Lambda = \eta
\end{equation}

or with indicies:

\begin{equation}
  \tensor{\Lambda}{^\mu_\rho} \tensor{\eta}{_{\mu\nu}} \tensor{\Lambda}{^\nu_\sigma} = \eta_{\rho \sigma}
\end{equation}


Here we have the following types of groups

\begin{definition}[Proper Group]
\label{eq:proper_group}
\[
  \det(\Lambda) = +1
\]
\end{definition}

\begin{definition}[Improper Group]
\label{eq:improper_group}
\[
  \det(\Lambda) = -1
\]
\end{definition}

>The condition \(\det(\Lambda) = \pm 1\) divides \(\L\) into two disconnected components \(\L\pm\) , called proper and improper Lorentz transformations.

### The Orthochronus group

>The condition \(\sgn (\tensor{\Lambda}{_{00}}) = \pm 1\) divides \(\L\) into two disconnected components, which one denotes \(\L^\uparrow\) and \(\L^\downarrow\), and are called orthochronus and non-orthochronous. (jaff)

>The fundamental Lorentz transformations which we study are the restricted Lorentz group \(\L^\uparrow_+\). These are the Lorentz transformations that are both proper, \(\det \Lambda = +1\), and orthochronous, \(\Lambda_{00} \ge 1\). There are some elementary transformations in \(\L\) that map one component into another, and which have special names:

 - The Unit transformation \(\one: \Lambda^T \eta \Lambda = \eta\)
 - The parity transformation \(P : (x_0,\vec{x}) \mapsto (x_0,-\vec{x})\).
 <!-- - The time-reversal transformation \(T : (x_0,\vec{x}) \mapsto (-x_0,\vec{x})\).
 - The space-time-inversion transformation \(PT : (x_0,\vec{x}) \mapsto (-x_0,-\vec{x})\). -->


 The _proper group_ and _orthochronus group_: \(\tensor{\Lambda}{^0_0}>1\)

\begin{align}
  \tensor{(\Lambda \tilde{\Lambda})}{^0_0} &= \tensor{\Lambda}{^0_\mu} \tensor{\tilde{\Lambda}}{^\mu_0}\\
  &= \tensor{\Lambda}{^0_0} \tensor{\tilde{\Lambda}}{^0_0} + \tensor{\Lambda}{^0_1} \tensor{\tilde{\Lambda}}{^1_0} \ge 1
\end{align}

An example of this is the unit transformation:

\begin{align}
  \one &= \begin{pmatrix}
    1 & 0 & 0 & 0\\
    0 & 1 & 0 & 0\\
    0 & 0 & 1 & 0\\
    0 & 0 & 0 & 1
  \end{pmatrix} \\
\Lambda^T \eta \Lambda &= \eta
\end{align}

(Parity)

\begin{equation}
  P(x^0, \vec{x}) \mapsto ()
\end{equation}

The conditions for our transformation:

\begin{align}
  \Lambda^T \eta \Lambda &= \eta\\
  \begin{pmatrix}
    a & c\\ b & d
  \end{pmatrix} \begin{pmatrix}
    1 & 0 \\ 0 & -1
  \end{pmatrix} \begin{pmatrix}
    a & b \\ c & d
  \end{pmatrix} &= \begin{pmatrix}
    1 & 0 \\ 0 & -1
  \end{pmatrix}
\end{align}

The conditions for \(a, b, c\) & \(d\):

\begin{equation}
  \begin{pmatrix}
    \cosh \theta & \sinh \theta \\ sinh \theta & \cosh \theta
    \end{pmatrix} = \begin{pmatrix}
    \gamma & \gamma \beta \\ \gamma \beta & \gamma
  \end{pmatrix}
\end{equation}

and must satisfy \(R^TR = \one\):


\begin{equation}
  \begin{pmatrix}x_{00} & x_{10}\\x_{01} & x_{11}\end{pmatrix}
  \begin{pmatrix} \eta_{00} & \eta_{01}\\\eta_{10} & \eta_{11} \end{pmatrix}
  \begin{pmatrix} x_{00} & x_{01}\\x_{10} & x_{11} \end{pmatrix} =
  \begin{pmatrix} \eta_{00} & \eta_{01}\\\eta_{10} & \eta_{11} \end{pmatrix}
\end{equation}

\begin{equation}
=\left[
\begin{array}{c|c}
  \begin{aligned}
    x_{00} &\left(\eta_{00} x_{00} + \eta_{10} x_{10}\right) + \\
    x_{10} &\left(\eta_{01} x_{00} + \eta_{11} x_{10}\right)
  \end{aligned} & \begin{aligned}
    x_{01} &\left(\eta_{00} x_{00} + \eta_{10} x_{10}\right) + \\
    x_{11} &\left(\eta_{01} x_{00} + \eta_{11} x_{10}\right)
  \end{aligned} \\
  \hline
  \begin{aligned}
  x_{00} &\left(\eta_{00} x_{01} + \eta_{10} x_{11}\right) +\\
  x_{10} &\left(\eta_{01} x_{01} + \eta_{11} x_{11}\right) \
  \end{aligned} & \begin{aligned}
  x_{01} & \left(\eta_{00} x_{01} + \eta_{10} x_{11}\right) + \\
  x_{11} & \left(\eta_{01} x_{01} + \eta_{11} x_{11}\right)
\end{aligned}
\end{array} \right]
\end{equation}

## Transformations:

### What type of transformation is this?

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
