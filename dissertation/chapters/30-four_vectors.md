# Four-vectors

Using our definition of an event from equation \ref{eq:event}, we would now
like to build up the Four-vector notation in a four-dimensional space. The
notation we will use will take the covariant form \(r_\alpha\) and a contravariant
form \(r^\alpha\), where the index \(\alpha \in 0,1,2,3\), where

\begin{align}
  r^0 &= ct\\
  r^1 &= x\\
  r^2 &= y\\
  r^3 &= z
\end{align}

Referring back to equation \ref{eq:vector_magnitude} and \ref{eq:s_spatial},
the square of the four-dimensional "length" of \(r^\alpha\) is given by:

\begin{equation}
(r^0)^2 - (r^1)^2 - (r^2)^2 - (r^3)^2 \label{eq:fourvector-squared-length}
\end{equation}

Using this notation, any set of four quantities \(X^0,X^1,X^2,X^3\) which can be measured using such a
four-dimensional coordinate system is called a four-vector, and their
respective values don't change under any rotations of the four-dimensional
coordinate system, in particular under Lorentz transformation:

\begin{align}
  X^0 &= \frac{ X\prime^0 + \frac{V}{c} X\prime^1 }{ \sqrt{ 1-\frac{V^2}{c^2} } } \\
  X^1 &= \frac{ X\prime^1 + \frac{V}{c} X\prime^0 }{ \sqrt{ 1-\frac{V^2}{c^2} } } \\
  X^2 &= X\prime^2\\
  X^3 &= X\prime^3\\
\end{align}

The covariant and contravariant vectors are related thus:

\begin{equation}
  X_0 = X^0, X_1 = -X^1, X_2 = -X^2, X_3 = -X^3
\end{equation}

And the square of this quantity \((X)^2\) is the summ:

\begin{equation}
  \sum_{\alpha = 0}^3 X^\alpha X_\alpha = X^0 X_0 + X^1 X_1 +X^2 X_2
\end{equation}

The four-vector has a time component: \(X^0\), and space components:
\(X^1,X^2,X^3\). And depending on the sign of its square:  when a four-vector
is positive; it is \textit{timelike}, when it is negative; its
\textit{spacelike}, or the null-vector and equal zero.

The four-vector can also take a form, separating out the time dimension, and with \(i\in 1,2,3\):

\begin{align}
  X^\alpha = (X^0, Xi^i)\\
  X^i = \begin{pmatrix}x\\y\\z\end{pmatrix}
  X_\alpha = (X^0, -X_i)\\
\end{align}

Using this form, the square of a four-vector can be written as:

\begin{equation}
  X^\alpha X_\alpha = (X^0)^2 - \vec{X}^2
\end{equation}

We can build on this notation to include more dimensions; creating a tensor. A
tensor is ranked. For example a vector is a rank 1 tensor, and a rank 2
four-tensor takes the form of a \(4\times 4\) array of values, and can be
compactly noted in three possible ways; a contravariant, covariant or mixed
tensor:

\begin{align}
  \qq{contravariant} &= \tensor{X}{^{\alpha \beta}}\\
  \qq{covariant}     &= \tensor{X}{_{\alpha \beta}}\\
  \qq{mixed}         &= \tensor{X}{^{\alpha}_{\beta}}\\
\end{align}

Where it needs to be noted that two tensor objects are not necisarily equal
when switching the covariant and contravarient indices around:

\begin{equation}
  \tensor{X}{_{\alpha}^{\beta}} \ne \tensor{X}{^{\alpha}_{\beta}}
\end{equation}

The connection between raising or lowering an index is a change in sign of the
spatial coordinate (ie \(X^i, i\in 1,2,3\); as an illustration:

\begin{equation}
  \tensor{X}{_{00}} = \tensor{X}{^{00}}, \qquad \tensor{X}{_{01}} = \tensor{-X}{^{01}}
\end{equation}

A property of a tensor which will become useful later on is its symmetry: and
can be easily observed through inspection.

A symmetric tensor:

\begin{equation}
  \tensor{X}{^{\alpha \beta}} = \tensor{X}{^{\beta \alpha}}
\end{equation}

An antisymmetric tensor:

\begin{equation}
  \tensor{X}{^{\alpha \beta}} = - \tensor{X}{^{\beta \alpha}}
\end{equation}

A side product of a tensor being antisymmetric, is that all its diagonal components are equal to zero:

\begin{equation}
  \tensor{X}{^{\alpha \beta}} = - \tensor{X}{^{\beta \alpha}} =  \mqty(\dmat{0,0,0,0})
\end{equation} 

The unit four-tensor satisfies:

\begin{equation}
\delta^\alpha_\beta X^\alpha = X^\beta
\end{equation}

where we have the Kronecker delta:

\begin{align}
\delta^\alpha_\beta &= \begin{cases}1, \qq{if} \alpha = \beta \\ 0, \qq{if} \alpha \ne \beta \end{cases}\\
  \Trace{\delta^\alpha_\beta} &= 4
\end{align}

There is a special tensor \(g\), called the \textit{metric tensor}, which has the property:

\begin{equation}
\tensor{g}{^{\alpha \beta}} = \tensor{g}{_{\alpha \beta}} = \mqty(\dmat[0]{1,-1,-1,-1}) 
\end{equation}


We may use this quantity to raise and lower indices in any four-vector like so:

\begin{equation}
  \tensor{g}{_{\alpha \beta}}X^\beta = X_\alpha, \tensor{g}{^{\alpha \beta}}X_\beta = X^\alpha
\end{equation}

and from this we can see that we can form a scalar product:

\begin{equation}
  X^\alpha X_\alpha = g_{\alpha \beta} X^\alpha X^\beta =  g^{\alpha \beta} X_\alpha X_\beta
\end{equation}


<!-- begin:2019.10.29.md -->

<!-- #TODO: link to previous def that I have written  / Write definition of invariance -->

\begin{definition}[Invariance]

Take the following:


\begin{align}
  \lu{\alpha}\mud{\alpha} = \agl{\lambda}{\mu} &= \lu{\alpha}\muu{\beta}\tensor{\epsilon}{_{\alpha\beta}}\\
  \lmtd \mtu{\alpha} &= \sqr{\lmt}{\tilde\mu}
\end{align}

Both of these are antisymmetric:

\begin{align}
  \sqr{\lmt}{\tilde\mu} = \mtd{\alpha}\ltu{\alpha} &= \epsilon_{\dot{\alpha}\dot{\beta}}\mtu{\beta}\lu{\dot\alpha}\\
  &= \mtu{\beta}(-\epsilon_{\dot{\beta}\dot{\alpha}} \ltu)\\
  &= -\ltd{\beta}\mtu{\beta}
\end{align}

Where \(\lambda, \lmt\) are two types of spinors:

\begin{align}
  \qq{Undotted:}& \lu{\alpha},   \ld{\alpha}\\
  \qq{Dotted:}& \mu_{\dot\alpha}, \mu^{\dot\alpha}
\end{align}
\end{definition}

## Dot product:

\begin{definition}[Box operator]

\begin{equation}
  \Box \equiv \partial_\mu \partial^\mu \equiv \partial_0 \partial^0 +\partial_i \partial^i = \partial_j^2 - \nabla^2
  \label{eq:box_operator}
\end{equation}

It has the following properties:

\begin{itemize}
  \item Using our equation for the \(\Box\) operator in equation \ref{eq:box_operator}, massless particles have the following property: \(\left( \Box + m^2 \right) \phi = 0\)
  \item Transform for \(\partial_\mu: \partial_\mu e^{ikx}\) for massless particles (i.e. where  \(k^2 = m^2\)):
\end{itemize}

\end{definition}
<!-- #UPTO: 14th april 10:52  -->

## Tranformation of velocy

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



## Lorentz invariance using the covariant form of Maxwell's Equations of electrodynamics

<!-- https://www.ippp.dur.ac.uk/~krauss/Lectures/QuarksLeptons/QED/GaugeInvariance_1.html -->

We can now explore this gauge invariance using Maxwell equations; taking us
from a classical form to our new form, while continuing to be gauge invariant.
Starting from the classical form of the Maxwell equations:

\begin{align}
  \vec{\nabla} \cdot \vec{E} &= \rho \\
  \vec{\nabla}\cdot\vec{B} &=0 \taglabel{eq:maxwell_divB}\\
  \vec{\nabla}\times \vec{E} &= -\pdv{\vec{B}}{t} \taglabel{eq:maxwell_curlE}\\
  \vec{\nabla}\times \vec{B}&=\vec{J}+\pdv{\vec{E}}{t}
\end{align}

Taking a closer look at equation ~\ref{eq:maxwell_divB}, we can set see that this suggests that there is a vector potential

\begin{equation}
  \vec{B} = \left(  \vec{\nabla} \times \vec{A}\right)
\end{equation}

The \(\vec{B}\) field remains unchanged when the gradient of an arbitrary scalar field \( \left( \vec{\nabla}\Lambda \right)\) is added:

\begin{equation}
  \vec{A} \to \vec{A}+\vec{\nabla}\Lambda
\end{equation}

Similarily, with eq ~\ref{eq:maxwell_curlE} it follows that:

\begin{equation}
  \vec{\nabla}\times \vec{E} = -\pdv{\vec{B}}{t}
\end{equation}

Which suggests we could have a scalar potential \(\phi\), which would satisfy:

\begin{equation}
  -\vec{\nabla}\phi-\pdv{\vec{A}}{t} = \vec{E}
\end{equation}

And we can therefore add any arbitrary scalar field's \(\Lambda\) time
derivative to the scalar potential \(\phi\), while keeping the \(\vec{E}\) field
unchanged.

\begin{equation}
  \phi\to \phi-\pdv{\Lambda}{t}
\end{equation}

alternatively, this can be written in a more compact form as:

\begin{equation}
  \vec{\nabla}\times \left( E+ \pdv{\vec{A}}{t} \right) = \vec{0}
\end{equation}

Maxwell's equations can be recast as

\begin{equation}
  A^\mu = (\phi, \vec{A})
\end{equation}

Where, using the covariant notation, there is a symmetry in gauge invariance
with the field-strength tensor:

\begin{align}
  \partial_\mu F^{\mu\nu} &= J^\nu\\
  F^{\mu\nu} &= \partial^\mu A^\nu - \partial^\nu A^\mu
\end{align}

Therefore if we set the following, it will lead to is a symmetry in gauge
invariance.

Using

\begin{align}
  \vec{A}\times (\vec{B}\times \vec{C}) &= \vec{B}(\vec{A}\cdot\vec{C}) - \vec{C} (\vec{A}\cdot \vec{B})\\
  (\vec{a}\times \vec{b})^i = \epsilon^{ijk}a^j b^k
\end{align}

Where \(\epsilon^{ijk}\) is Levi Civita symbol we define in equation ~\ref{eq:levi_civita}.

Combing the above mentioned expansions, we will now find a different way to write the Maxwell equations:

### A new method of deriving \(J, \rho\) and \(F\)

\begin{align}
  \vec{\nabla}(\underbrace{\vec{\nabla}\times A}_{=\vec{B}}) &= J \pdv{t}(\underbrace{-\vec{\nabla}A^0 - \pdv{\vec{A}}{t} }_{=E})\\
  &= \vec{\nabla}(\vec{\nabla}\cdot\vec{A}) - \vec{\nabla}^2\vec{A}\\
  &= \vec{\nabla}(\vec{\nabla}\cdot\vec{A}) - \vec{\nabla}^2\vec{A}\\
  &= \left( \pdv[2]{t} - \vec{\nabla}^2 \right)\vec{A} +\vec{\nabla}\left(\vec{\nabla}\cdot\vec{A}+ \pdv{A^0}{t}  \right) = \vec{J}
\end{align}

\begin{align}
  \vec{\nabla}\cdot\left(- \vec{\nabla}\cdot\vec{A}- \pdv{A}{t} \right) &= \rho\\
  \left( \pdv[2]{t} - \vec{\nabla}^2 \right)A^0 - \pdv{t} \left( \vec{\nabla}\cdot \vec{A} + \pdv{A^0}{t} \right) &= \rho
\end{align}

This leads us to our new Box operator '\(\Box\)' which we defined in equation ~\ref{eq:box_operator} for a four-vector, defined as:

\begin{equation}
  \Box A^\mu = \partial^\mu \left( \partial_\nu A^\nu \right) = J^\mu
\end{equation}



\begin{align}
  F^{\mu\nu} &= \partial^\mu A^\nu - \partial^\nu A^\mu\\
  \partial_\mu F^{\mu\nu} &= J^\nu
\end{align}

\begin{definition}[Gauge redundancy]

\begin{align}
  A^\mu &\to A^\mu + \partial^\mu \Lambda\\
  F^{\mu\nu}&\to F_{\mu\nu}
\end{align}

\end{definition}

<!-- end:2019.10.29.md -->
