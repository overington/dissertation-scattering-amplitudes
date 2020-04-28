
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
\label{fig:scattering_amplitude_single_loop}
\end{figure}



![Each Feynman diagram provides an intuitive way to visualize one possible way that particles might interact. The trouble is that there are countless other ways, too.  A quark-quark interaction might produce more than one gluon or involve more than one virtual-particle loop, or both. The calculations quickly become unmanageable.  [Figure taken from @Bern:2012aa]\label{fig:feynmandiagram_loops}](assets/sa-loops.pdf "Tree Level Loops"){ height=50% }


<!-- ## Feynman and BCFW recursion methods -->

In this paper, we will explore a method of calculating scattering amplitudes
called BCFW recursion [see @Britto:2005aa; @Britto:2005ab], this is a method
which is built up from the Feynman method, these methods build on using
a colour decomposition of the gauge theory amplitudes and on expressing them in
a spinor helicity basis particularly suited for massless particles (as outlined
in @Plefka:2014aa and other texts mentioned)


The Feynman method makes use of virtual-particles, so called because they are
gauge variant or off-shell (or off the mass shell) to keep tally of the
energy and momenta of all the paths the particles and interactions make, so
that an individual interaction may temporarily break the energy momentum
relations creating such a virtual particle with negative mass, or energy [see
@Hodges:2013aa; @Plefka:2014aa]. Although it allows for broken symmetries, each
virtual particle must cancel out by the final exiting interaction, ensuring
that the system as a whole is conservative and invariant and we are only left
with \textit{on-shell} particles at the boundaries.




The reason we use the virtual-particles of off-shell masses in Feynman diagrams
is that they can be a useful counting tool in simple particle interaction, to
balance out the entering and exiting particles, while keeping the whole
interaction on-shell. However; they quickly become problematic for computing
interactions involving numerous particles as the complexity of computation
quickly grows [see @Bern:2012aa] when you reach a loop level recursion (see
Figure \ref{fig:scattering_amplitude_single_loop}), the number of possible
diagrams that you have to calculate blow up in number the more complicated they
become, and the more loops you have in amplitude interaction, for example, see
Figure \ref{fig:feynmandiagram_loops}.


Using the BCFW method of calculation, we keep all masses on-shell which keeps
each individual interaction gauge invariant; therefore we don't need to use
virtual particles at all.


As an example; a quark-quark interaction might produce more than one gluon or
involve more than one virtual-particle loop, or both when calculating the
scattering amplitude using the Feynman method, and the calculations quickly
become unmanageable.  This is not the case when using BCFW recursion, as the
new method of calculating scattering amplitude only knows about on shell
degrees of freedom.


