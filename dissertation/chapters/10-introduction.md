  <!-- Abstract -->
<!-- # General outline
* How have they been calculated using Feynman diagrams
* (How do they relate to Gauge theory)
* Problem with current method of computation (using Feynman diagrams)
* difference between On-shell and Off-shell
* Aim: To find and produce generators using the 'On-Shell' methods.
Guage theories and spinnor matricies for Gluons and massless particles were
-->


# Introduction

<!-- Introduction outline -->

* A definition of Scattering amplitudes
* Why are SAs used?
*



In Quantum Field Theory (QFT), a scattering amplitude is the mechanism for
measuring and modelling the properties of fundamental particles and how they
interact.


In order to begin understanding a scattering amplitude, we must first
understand the rules by which we can describe an individual particles motion
and then build up a langauge for how these motions interact in a system of
particles.  We open here by exploring current methods available to us, in the
forms of mathematical formalisms, and how we might use certain properties to
expand on this knowledge, to 

certain properties when joining one or more individual things, in order to
represent systems, or groups of particles, and how they interact.

We begin by mapping the Einsteins conservative energy and momentum associated
with each entering particle to exiting particles using *De Broglie dispersion
relations*, which connects the energy, momentum, and mass of particles through
relativistic dispersion relation:

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

 - in order to account for relativistic physics, we need to introduce some changes. These changes are explored in the following:

<!-- ## Feynman Diagrams -->

Traditionally, they have been computed using
Feynman diagrams, which set the boundary conditions to the summed values of all
entering particles and those exiting within the same interaction, such that
they conserve this E-M relation between the entering and exiting particles at
the macro level.

The Feynman method makes use of *virtual particles*, so called because they are
gauge variant or **Off-Shell** (or off the mass shell) to keep tally of the
energy and momenta of all the paths the particles and interactions make, so
that an individual interaction may temporarily break the energy momentum
relations creating such a virtual particle with negative mass, or energy [see
@Hodges:2013aa; @Plefka:2014aa]. Although it allows for broken symmetries, each
virtual particle must cancel out by the final exiting interaction, ensuring
that the system as a whole is conservative and invariant and we are only left
with **On-Shell** particles at the boundaries.

<!-- Graph that out and you get a parabolic surface for massive particles, and a cone for massless particles, like photons. This is known as the mass shell. The momentum of a real particle can be represented by a vector lying along the shells’ surface. The point is that real particles have momentum vectors that are on the shell – not inside it, but on it. -->

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

<!-- Loop level solutions will also be explored, and combined with the integral basis for one-loop Feynman integrals. -->


The proposed strategy will explore scattering amplitudes between massless
particles using restricted on-shell formalism where interactions and particles
must be gauge invariant throughout, which is known as the *BCFW recursion
relation* [see @Britto:2005ab, @Britto:2005aa].

These methods build on using a colour decomposition of the gauge theory
amplitudes and on expressing them in a spinor helicity basis particularly
suited for massless particles (as outlined in @Plefka:2014aa and other texts
mentioned)



<!-- The New Method: -->
<!-- Thinking about the analytic structure of tree level amplitudes leads to novel on-shell recursion relations. They allow the analytic construction of tree-level amplitudes from atomistic three-point ones. -->
<!-- At loop level unitarity-based techniques, combined with the knowledge of an integral basis for one-loop Feynman integrals, may be used to construct loop amplitudes from tree- level amplitudes. In summary, all amplitudes follow from the on-shell three-point vertices, and no reference to the complicated form of the Lagrangian, gauge fixing terms and ghosts is necessary. -->


<!-- >We present new recursion relations for tree amplitudes in gauge theory that give very compact formulas. Our relations give any tree amplitude as a sum over terms constructed from products of two amplitudes of fewer particles multiplied by a Feynman propagator. -->

<!-- * Generalised Unitarity -->

<!--
## Outline:

The outline for the proposed project will take the following form:

@import "outline.md"
 -->

<!--
Original from Gabrielle
*   Elements of the Lorentz group
*   Four vectors
*   Spinors and transformations
*   Spinor helicity formalism (null vectors)
*   Little group and weights
*   Determination of three-point amplitudes of massless particles
*   Introduction to Feynman diagrams  - reproducing amplitudes for Yang-Mills theory
*   Three-point amplitudes and factorisation
*   BCFW recursion relations in Yang-Mills and Gravity
-->

