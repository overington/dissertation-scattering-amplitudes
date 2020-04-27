# Introduction

<!-- Abstract -->
<!-- # General outline
* How have they been calculated using Feynman diagrams
* (How do they relate to Gauge theory)
* Problem with current method of computation (using Feynman diagrams)
* difference between On-shell and Off-shell
* Aim: To find and produce generators using the 'On-Shell' methods.
Guage theories and spinnor matricies for Gluons and massless particles were
-->


In Quantum Field Theory (QFT), a scattering amplitude is the mechanism for
measuring and modelling the properties of fundamental particles and how they
interact.  

<!-- ## Feynman Diagrams -->

Traditionally, they have been computed using Feynman diagrams, which set the
boundary conditions to the summed values of all entering particles and those
exiting within the same interaction, such that they conserve this E-M relation
between the entering and exiting particles at the macro level.

\begin{figure}
\begin{center}
\feynmandiagram [horizontal=a to d] {
  l1 -- [fermion] a -- [fermion] l2,
  a -- [photon] d,
  r2 -- [fermion] d -- [fermion] r1,
};
\end{center}
\caption{Feynman diagram of a simple four leg scattering amplitude}%
\label{fig:scattering_amplitude_simpple}
\end{figure}

The Feynman method makes use of *virtual particles*, so called because they are
gauge variant or **Off-Shell** (or off the mass shell) to keep tally of the
energy and momenta of all the paths the particles and interactions make, so
that an individual interaction may temporarily break the energy momentum
relations creating such a virtual particle with negative mass, or energy [see
@Hodges:2013aa; @Plefka:2014aa]. Although it allows for broken symmetries, each
virtual particle must cancel out by the final exiting interaction, ensuring
that the system as a whole is conservative and invariant and we are only left
with **On-Shell** particles at the boundaries.

\begin{figure}
\begin{center}
\feynmandiagram [horizontal=a to d] {
  l1 -- [fermion] a -- [fermion] l2,
  a -- [photon] b -- [half left,fermion] c -- [half left, fermion] b,
  c -- [photon] d,
  r2 -- [fermion] d -- [fermion] r1,
};
\end{center}
\caption{Scattering amplitude with loop}%
\label{fig:scattering_amplitude_loop}
\end{figure}



The problem with calculations using purley Feynman methods of calculation, is
that when you reach a loop level recursion (see Figure
\ref{fig:scattering_amplitude_loop}), the number of possible diagrams that you
have to calculate blow up in number the more complicated they become, and the
more loops you have in amplitude interaction, for example, see Figure
\ref{fig:feynmandiagram_loops}.


![Each Feynman diagram provides an intuitive way to visualize one possible way that particles might interact. The trouble is that there are countless other ways, too.  A quark-quark interaction might produce more than one gluon or involve more than one virtual-particle loop, or both. The calculations quickly become unmanageable.  [Figure taken from @Bern:2012aa]\label{fig:feynmandiagram_loops}](assets/sa-loops.pdf "Tree Level Loops"){ height=45% }


<!-- ## BCFW recursion relation -->

This method is flexible as it is gauge invariant; a property which is useful for
simple particle interactions, however it becomes problematic for computing
interactions involving numerous particles as the complexity of computation
quickly grows @Bern:2012aa. (For example a quark-quark interaction might
produce more than one gluon or involve more than one virtual-particle loop, or
both. The calculations quickly become unmanageable.)  The scattering amplitude
on the other-hand is gauge invariant and only knows about on shell degrees of
freedom.


Our aim will be to search for new symmetries, using the analytic structure
found in the texts to probe tree level amplitudes in gauge theory.

<!-- ## Building a scattering amplitude / Relativity -->

In order to begin understanding them, we must first understand the
rules by which we can describe an individual particles motion and then build up
a language for how these motions interact in a system of particles.  We open
here by exploring current methods available to us, in the forms of mathematical
formalisms, and how we might use certain properties to expand on this
knowledge, in order to represent systems, or groups of particles, and how they
interact.

 - in order to account for relativistic physics, we need to introduce some changes. These changes are explored in the following:


<!-- Loop level solutions will also be explored, and combined with the integral basis for one-loop Feynman integrals. -->


The proposed strategy will explore scattering amplitudes between massless
particles using restricted on-shell formalism where interactions and particles
must be gauge invariant throughout, which is known as the *BCFW recursion
relation* [see @Britto:2005ab; also @Britto:2005aa].

These methods build on using a colour decomposition of the gauge theory
amplitudes and on expressing them in a spinor helicity basis particularly
suited for massless particles (as outlined in @Plefka:2014aa and other texts
mentioned)


<!-- The New Method: -->
<!-- Thinking about the analytic structure of tree level amplitudes leads to novel on-shell recursion relations. They allow the analytic construction of tree-level amplitudes from atomistic three-point ones. -->
<!-- At loop level unitarity-based techniques, combined with the knowledge of an integral basis for one-loop Feynman integrals, may be used to construct loop amplitudes from tree- level amplitudes. In summary, all amplitudes follow from the on-shell three-point vertices, and no reference to the complicated form of the Lagrangian, gauge fixing terms and ghosts is necessary. -->


<!-- >We present new recursion relations for tree amplitudes in gauge theory that give very compact formulas. Our relations give any tree amplitude as a sum over terms constructed from products of two amplitudes of fewer particles multiplied by a Feynman propagator. -->


## Principle of Relativity

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

