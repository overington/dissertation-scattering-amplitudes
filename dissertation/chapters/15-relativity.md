<!-- ## Building a scattering amplitude / Relativity -->
## The Principle of Relativity

In order to begin understanding them, we must first understand the
rules by which we can describe an individual particles motion and then build up
a language for how these motions interact in a system of particles.  We open
here by exploring current methods available to us, in the forms of mathematical
formalisms, and how we might use certain properties to expand on this
knowledge, in order to represent systems, or groups of particles, and how they
interact.

 - in order to account for relativistic physics, we need to introduce some changes. These changes are explored in the following:



<!--
   - Frames of reference
  -->

We will begin by inspecting the systems and rules by which interactions between
free particles can be described, and build our theory from there.  We need to
have a system by which we make measurements , and that measurement will take
the same form, in all other inertial frames of reference. This is the principle
of relativity.

For example, taking a look at two frames of reference (see Figure
\ref{fig:frames_of_ref}); we have two frames \(K, K\prime\) with orthogonal
axes \(\vec{x},\vec{y},\vec{z}\) and
\(\vec{x\prime},\vec{y\prime},\vec{z\prime}\).

\begin{figure}
\begin{center}
\begin{tikzpicture}
\def\tick{0.05}
\def\th{205}
 \foreach \x [count = \ra] in {,'}{
    \def\r{\ra};
    \coordinate(O) at (0+\r, 0+\r);
    \coordinate(X) at ((7 + \r, 0 + \r);
    \coordinate(Y) at (\r, 3+\r);
    \coordinate(Z) at ({3 * cos(\th) + \r}, {3 * sin(\th) + \r});
    \draw [thick,->]  (O) -- (X) node[below]{\small $\vec{x\x}$}; % X
    \draw [thick,->]  (O) -- (Y)  node[above]{\small $\vec{y\x}$}; % Y
    \draw [thick,->]  (O) -- (Z)  node[left]{\small $\vec{z\x}$}; % Z
    \draw [decorate,decoration={brace,amplitude=7}] (0.2+\r,0+\r) -- (2.2 + \r, 0 + \r) node [midway,above,yshift=7] {\small $\Delta \vec{x\x}$};
    \foreach \z in {0.2, 0.4,  ..., 6.9} {
      \draw (\z+\r, -\tick+\r) -- (\z+\r, \tick+\r);
    }
  }
\end{tikzpicture}
\end{center}
\caption{Two inertial frames of reference, \(K\) and \(k\prime\)}%
\label{fig:frames_of_ref}
\end{figure}

Experiments show that the principle of relativity is valid; that 

> the laws of nature are identical in all inertial systems of reference. 

## Transformations

groups of
particles; such that their positions and velocities may be described by
coordinates. Next we must ensure two things:


This is to ensure that the equations describing the laws of physics have the
same form in all admissible frames of reference.

This will ensure that there is no special place in space or time by which
we can make the measurement that will be different from any other. It will also
ensure that distances between points remain unchanged before and after this
transformation. 


 under a closed group of transformations acting on them.

We will also make sure that this system of measurement and
group of transformations remain unchanged when comparing 



as well as in any other system out side of the current system.


classical mechanics, moving between intertial reference frames is relatively
simple becuase of the static nature of time, events int the two reference
frames can be calcuculated  The Galileo Transformation [see @Landau:1975aa] 

### Relative distances







## Spacetime intervals

## Spacetime transformations


## Moving Beyond Galilean Mechanics



using reference systems or co-ordinates.  This fist step will allow us to set a
time and spatial dimensions of the system, and allow us to compare two systems
in relation to one another, and measure the change in this relation as one of
the systems evolves over time in relation to the other.

### Principle of relativity


[@Landau:1975aa]

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


<!-- Interactions -->
At the heart of an interaction between free particles, is the Einsteins
conservative energy and momentum associated with each entering particle to
exiting particles using *De Broglie dispersion relations*, which connects the
energy, momentum, and mass of particles through relativistic dispersion
relation:

\begin{equation}
  \label{eq:einstein_energymomentum}
  E^2 = ( \vec{p} c )^2 + (mc^2 )^2
\end{equation}


currently available to us for exploring interactions from their fundamental
rules in physical systems and building up the language we need in order to
model how they interact. From this, we explore further formalisms which

<!-- TODO:discussion of einstein energy momentum dispersion relation -->

form of relativistic interactions, which themselves have been bootstrapped from
classical mechanics.

setting out the notation for which we will use throughout the duration of this
paper, in order to be able to concisely explain

In order to take into account relativistic effects, we begin here by working
through the formalism of the Lorentz Group to arrive at the relativistic
formalisms for

the a special group called the Lorentz Group,

Let us first take a look at the Lagrangian equation, and how they differ from
their relativistic to non-relativistic formulations.

