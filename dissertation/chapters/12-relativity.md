<!-- 
@import "assets/custom.md"
 -->
## Relativity

### The changes in the Lagrangian \( \Lg \) and Hamiltonian \(H\)

Understanding interactions between free particles through, we inspect their classical form

\begin{align}
  \Lg_{\text{NR}} &= \frac{1}{2} m\dvec{x} &&\to& \Lg_{\text{Rel}} &= -m\sqrt{1-\dvec{x}^2}\\
  H_{\text{NR}} &= \frac{\vec{p}^2}{2m}+V(x) &&\to& H_{Rel} &= (something)
\end{align}

To calculate this relation, we inspect the Lagrangian relation between its two component measurables (in an unspecific basis, these can be any two variables \(\vec{p}, \vec{q}\), but to relate them to the classical equations involving momentum and position, we will be calling them \(\vec{p}, \vec{x}\))

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

For small velocities, where $\vec{x}\ll 1$, we can say:

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
