<!-- Abstract -->
<!-- # General outline
* A definition of Scattering amplitudes
* How have they been calculated using Feynman diagrams
* (How do they relate to Gauge theory)
* Problem with current method of computation (using Feynman diagrams)
* difference between On-shell and Off-shell
* Aim: To find and produce generators using the 'On-Shell' methods.
Guage theories and spinnor matricies for Gluons and massless particles were
-->

<!-- Course page notes

Please submit a title and abstract of your project in a single 1-page PDF document.

The abstract should include a Purpose / Problem Statement, a description of your approach or methods used, as well as a description of your results (obtained or anticipated) and their expected impact on other researchers.

Undergraduate Research Conference Applications

This abstract could be developed into an application to participate in an undergraduate research conferences (e.g., the British Conference on Undergraduate Research, the IoP Conference of Astronomy and Physics Students).  Please discuss this with your project supervisor if you are interested in participating and submitting an abstract.  
-->



<!-- ## Scattering Amplitudes -->

In Quantum Field Theory (QFT), a scattering amplitude is the mechanism for predicting and measuring fundamental particle interactions by mapping the energy and momentum associated with each entering particle to exiting particles while preserving Einsteins energy-momentum relationship of $E^2 = (pc)^2 + (mc^2)^2$.

<!-- ## Feynman Diagrams -->
Traditionally, they have been computed using Feynman diagrams, which set the boundary conditions to the summed values of all entering particles and those exiting within the same interaction, such that they conserve this E-M relation between the entering and exiting particles at the macro level.

The Feynman method makes use of *virtual particles*, so called because they are gauge variant or **Off-Shell** (or off the mass shell) to keep tally of the energy and momenta of all the paths the particles and interactions make, so that an individual interaction may temporarily break the energy momentum relations creating such a virtual particle with negative mass, or energy @Hodges:2013aa, @Plefka:2014aa. Although it allows for broken symmetries, each virtual particle must cancel out by the final exiting interaction, ensuring that the system as a whole is conservative and invariant and we are only left with **On-Shell** particles at the boundaries.

<!-- Graph that out and you get a parabolic surface for massive particles, and a cone for massless particles, like photons. This is known as the mass shell. The momentum of a real particle can be represented by a vector lying along the shells’ surface. The point is that real particles have momentum vectors that are on the shell – not inside it, but on it. -->

This method is flexible as it is gauge variant; a property which is useful for simple particle interactions, however it becomes problematic for computing interactions involving numerous particles as the complexity of computation quickly grows @Bern:2012aa. (For example a quark-quark interaction might produce more than one gluon or involve more than one virtual-particle loop, or both. The calculations quickly become unmanageable.)  The scattering amplitude on the other-hand is gauge invariant and only knows about on shell degrees of freedom.


Our aim will be to search for new symmetries, using the analytic structure found in the texts to probe tree level amplitudes in gauge theory. <!-- Loop level solutions will also be explored, and combined with the integral basis for one-loop Feynman integrals. --> The proposed strategy will explore scattering amplitudes between massless particles using restricted on-shell formalism where interactions and particles must be gauge invariant throughout, which is known as the *BCFW recursion relation* @Britto:2005ab, @Britto:2005aa.

These methods build on using a colour decomposition of the gauge theory amplitudes and on expressing them in a spinor helicity basis particularly suited for massless particles (as outlined in @Plefka:2014aa and other texts mentioned)



<!-- The New Method: -->
<!-- Thinking about the analytic structure of tree level amplitudes leads to novel on-shell recursion relations. They allow the analytic construction of tree-level amplitudes from atomistic three-point ones. -->
<!-- At loop level unitarity-based techniques, combined with the knowledge of an integral basis for one-loop Feynman integrals, may be used to construct loop amplitudes from tree- level amplitudes. In summary, all amplitudes follow from the on-shell three-point vertices, and no reference to the complicated form of the Lagrangian, gauge fixing terms and ghosts is necessary. -->


<!-- >We present new recursion relations for tree amplitudes in gauge theory that give very compact formulas. Our relations give any tree amplitude as a sum over terms constructed from products of two amplitudes of fewer particles multiplied by a Feynman propagator. -->

<!-- * Generalised Unitarity -->
