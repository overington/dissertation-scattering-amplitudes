---
title: 'On-Shell amplitude computation using loop level unitarity-based techniques'
author:
    - {name: 'Samuel Overington | ID 170431121', affiliation: "School of Physics and Astronomy,\nQueen Mary University of London\n"}
numbersections: true
fontsize: 12pt
geometry: margin=2cm
bibliography: bibliography-scattering_amplitudes.bib
abstract: '\input{dissertation/abstract.md}'
nocite: "@Henn:2014aa, @Hunter:2013ab, @Britto:2005ab, @Bern:2012aa, @Britto:2005aa, @Arkani-Hamed:2012aa, @Plefka:2014aa, @Landau:1975aa\n"
header-includes: "\\usepackage{lmodern,mathrsfs}\n\\usepackage{sectsty}\n\\usepackage{yfonts}\n\\usepackage{bbold}\n\\usepackage{amssymb}\n\\usepackage{amsmath}\n\\usepackage{cancel,ulem}\n\\usepackage[utf8]{inputenc}\n\\usepackage{siunitx,physics}\n\\usepackage{mattens}\n\\usepackage{tensor}\n\\usepackage{tikz}\n\\usepackage{tikz-feynman}\n"
output:
    pdf_document: {latex_engine: lualatex, template: assets/template.tex, path: ../thesis_output/amplitudes.pdf, toc: true, toc_depth: 3}
---  
  
  
\twocolumn
  
#  Introduction {#introduction }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
In Quantum Field Theory (QFT), a scattering amplitude is the mechanism for predicting and measuring fundamental particle interactions by mapping the energy and momentum associated with each entering particle to exiting particles while preserving Einsteins energy-momentum relationship of:
  
\begin{equation}
  \label{eq:einstein_energymomentum}
  E^2 = ( \vec{p} c )^2 + (mc^2)^2
\end{equation}
  
  
  
Traditionally, they have been computed using Feynman diagrams, which set the boundary conditions to the summed values of all entering particles and those exiting within the same interaction, such that they conserve this E-M relation between the entering and exiting particles at the macro level.
  
The Feynman method makes use of *virtual particles*, so called because they are gauge variant or **Off-Shell** (or off the mass shell) to keep tally of the energy and momenta of all the paths the particles and interactions make, so that an individual interaction may temporarily break the energy momentum relations creating such a virtual particle with negative mass, or energy [see @Hodges:2013aa; @Plefka:2014aa]. Although it allows for broken symmetries, each virtual particle must cancel out by the final exiting interaction, ensuring that the system as a whole is conservative and invariant and we are only left with **On-Shell** particles at the boundaries.
  
  
  
  
This method is flexible as it is gauge variant; a property which is useful for simple particle interactions, however it becomes problematic for computing interactions involving numerous particles as the complexity of computation quickly grows @Bern:2012aa. (For example a quark-quark interaction might produce more than one gluon or involve more than one virtual-particle loop, or both. The calculations quickly become unmanageable.)  The scattering amplitude on the other-hand is gauge invariant and only knows about on shell degrees of freedom.
  
  
Our aim will be to search for new symmetries, using the analytic structure found in the texts to probe tree level amplitudes in gauge theory. <!-- Loop level solutions will also be explored, and combined with the integral basis for one-loop Feynman integrals. --> The proposed strategy will explore scattering amplitudes between massless particles using restricted on-shell formalism where interactions and particles must be gauge invariant throughout, which is known as the *BCFW recursion relation* @Britto:2005ab, @Britto:2005aa.
  
These methods build on using a colour decomposition of the gauge theory amplitudes and on expressing them in a spinor helicity basis particularly suited for massless particles (as outlined in @Plefka:2014aa and other texts mentioned)
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
##  Outline: {#outline }
  
The outline for the proposed project will take the following form:
  
  
  
* Lagrangian / Relattivistic and non relatavistic mechanics
  * The Lagrangian and the action
  * Lagrangian Mechanics
    * Einstein Equation
  * Principal of relativity
    * Reference frames:
    * Intervals:
* Elements of the Lorentz group
  * Associative:
  * Unitary:
    * Invariance under transformation:
    * Metric:
  * Proper and Improper group
    * The Orthochronus group
  * Transformations:
  
  
* Four vectors
  * Angular Momentum properties:
  * Noethers Theorem
  * <img src="https://latex.codecogs.com/gif.latex?SU"/> Group:
    * <img src="https://latex.codecogs.com/gif.latex?SU(2)"/>
  * <img src="https://latex.codecogs.com/gif.latex?&#x5C;vec{&#x5C;rho}%20&#x5C;to%20&#x5C;vec{&#x5C;rho}&#x5C;cdot&#x5C;vec{&#x5C;sigma}"/>:
  
* Spinor helicity formalism (null vectors)
* Spinors and transformations
  * Spinor Helicity formalism and Pauli Matrices properties:
    * Multiplication <img src="https://latex.codecogs.com/gif.latex?&#x5C;to"/> identity matrix:
    * commutation and anti commutation:
    * Trace of multiplication:
  
* Little group and weights
* Determination of three-point amplitudes of massless particles
* Introduction to Feynman diagrams - reproducing amplitudes for Yang-Mills theory
* Three-point amplitudes and factorisation
* BCFW recursion relations in Yang-Mills and Gravity
  
  
  
  
  
---
  
  
\onecolumn
  
  
#  Relativity {#relativity }
  
  
In order to begin understanding scattering amplitudes, we behin at the fundamental rules of physical systems, and their Interactions.
  
The language we need to build up the form of relativistic interactions is bootstrapped from classical mechanics, which don't take into account things like the finite speed of light.
  
A working through the formalism to arrive at the relativistic formalisms for
  
Let us first take a look at the Lagrangian equation, and how they differ from their relativistic to non-relativistic formulations.
  
 - in order to account for rel physics, we need to introduce some changes. These changes are explored in the following:
  
##  The changes in the Lagrangian <img src="https://latex.codecogs.com/gif.latex?L"/> and Hamiltonian <img src="https://latex.codecogs.com/gif.latex?H"/> {#the-changes-in-the-lagrangian-l-and-hamiltonian-h }
  
Understanding interactions between free particles through, we inspect their classical form
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;begin{aligned}&#x5C;Lg_{&#x5C;text{NR}}%20&amp;=%20&#x5C;frac{1}{2}%20m&#x5C;dvec{x}%20&amp;&amp;&#x5C;to&amp;%20&#x5C;Lg_{&#x5C;text{Rel}}%20&amp;=%20-m&#x5C;sqrt{1-&#x5C;dvec{x}^2}&#x5C;&#x5C;%20%20H_{&#x5C;text{NR}}%20&amp;=%20&#x5C;frac{&#x5C;vec{p}^2}{2m}+V(x)%20&amp;&amp;&#x5C;to&amp;%20H_{Rel}%20&amp;=%20(something)&#x5C;end{aligned}"/></p>  
  
  
To calculate this relation, we inspect the Lagrangian relation between its two component measurables (in an unspecific basis, these can be any two variables <img src="https://latex.codecogs.com/gif.latex?&#x5C;vec{p},%20&#x5C;vec{q}"/>, but to relate them to the classical equations involving momentum and position, we will be calling them <img src="https://latex.codecogs.com/gif.latex?&#x5C;vec{p},%20&#x5C;vec{x}"/> )
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?p%20&#x5C;equiv%20&#x5C;pdv{&#x5C;Lg}{&#x5C;dvec{x}}%20=%20&#x5C;frac{m&#x5C;dvec{x}}{&#x5C;sqrt{1-&#x5C;dvec{x}^2}}"/></p>  
  
  
For small velocities, where <img src="https://latex.codecogs.com/gif.latex?&#x5C;vec{x}&#x5C;ll%201"/>, we can say:
\begin{equation}
  \label{eq:lagrange_smallapprox}
  \sqrt{1-\dvec{x}^2} \approx 1-\frac{\dvec{x}^2}{2} + \dots
\end{equation}
  
  
##  The time evolution of the system {#the-time-evolution-of-the-system }
  
Where <img src="https://latex.codecogs.com/gif.latex?&#x5C;H%20=%20&#x5C;H(&#x5C;vec{q},%20&#x5C;vec{p},t)"/>
  
\begin{equation}
  \label{eq:lagrangian_timeevolutionp}
  \dv{\vec{p}}{t} = -\pdv{\H}{\vec{q}}
\end{equation}
  
\begin{equation}
  \label{eq:lagrangian_timeevolutionq}
  \dv{\vec{q}}{t} = +\pdv{\H}{\vec{p}}
\end{equation}
  
Thus leaving us with the following set of equations:
  
<img src="https://latex.codecogs.com/gif.latex?&#x5C;H%20=%20T+V"/>:
  
\begin{equation}
  \label{eq:hamiltonian_lagrangian_basic}
  \frac{p^2}{2m} + \frac{1}{2}mv^2
\end{equation}
  
  
\begin{equation}
  \label{eq:hamiltonian_lagrangian}
  \H = \sum_i{\dvec{q}^i\pdv{\L}{\dvec{q}^i} -\L} = \sum_i{\dvec{q}^ip_i-\L}
\end{equation}
  
where
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?p_i%20=%20&#x5C;pdv{&#x5C;L}{&#x5C;dvec{q}^i}"/></p>  
  
  
leading to
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;begin{aligned}%20%20&#x5C;H%20&amp;=%20m&#x5C;dvec{x}^2%20-%20(-m&#x5C;sqrt{1-&#x5C;dvec{x}^2})&#x5C;&#x5C;%20%20&amp;=%20&#x5C;frac{m&#x5C;dvec{x}}{&#x5C;sqrt{1-&#x5C;dvec{x}^2}}&#x5C;dvec{x}%20+m&#x5C;sqrt{1-&#x5C;dvec{x}^2}%20&#x5C;&#x5C;%20%20&amp;=%20&#x5C;frac{m&#x5C;dvec{x}+m-m&#x5C;dvec{x}^2}{&#x5C;sqrt{1-&#x5C;dvec{x}^2}}&#x5C;end{aligned}"/></p>  
  
  
###  Einstein Equation {#einstein-equation }
  
Where we arrive at Einsteins formula, when setting c = 1
\begin{equation}
  \label{eq:einstein}
  \H = E = \frac{m}{\sqrt{1-\dvec{x}^2}}
\end{equation}
  
This explains the principal of relatively according to Einsteins equations, and allows us to begin setting up the formalism for representing interactions which include relativistic properties.
  
##  Principal of relativity {#principal-of-relativity }
  
(Classical theory of fields, @Landau:1975aa )
Inertial reference frame in which a body moves in respect to and without any other force enacting on it, proceeds at constant velocity.
  
  
###  Reference frames: {#reference-frames }
  
Two inertial reference frames are related by:
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;Delta%20x%20=%20x-x&#x27;"/></p>  
  
  
where <img src="https://latex.codecogs.com/gif.latex?&#x5C;dv{x}{t}=0%20&#x5C;to%20x"/> and <img src="https://latex.codecogs.com/gif.latex?x&#x27;"/> have same property of inertiality.
  
  
###  Intervals: {#intervals }
  
Event: described by the place where it occured and times
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;begin{aligned}%20%20e_1%20&amp;=%20[t,x,y,z]&#x5C;&#x5C;%20%20&#x5C;text{worldline%20}&amp;=%20[t&#x5C;to%20t&#x27;,%20f(x,y,z)-f&#x27;(x,y,z)]&#x5C;end{aligned}"/></p>  
  
  
Invariance of speed of light
  
  
#  Elements of the Lorentz group {#elements-of-the-lorentz-group }
  
  
##  Lorentz group {#lorentz-group }
  
The lorentz group is defined as being:
  
###  Associative: {#associative }
  
 <p align="center"><img src="https://latex.codecogs.com/gif.latex?A(BC)%20=%20(AB)C"/></p>  
  
  
###  Unitary: {#unitary }
  
There exists an object such that:
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?U&#x5C;cdot%20U^{-1}%20=%20&#x5C;one"/></p>  
  
  
####  Invariance under transformation: {#invariance-under-transformation }
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;begin{aligned}%20%20x^&#x5C;mu%20&amp;=%20&#x5C;left(%20x^0,%20-&#x5C;vec{x}%20&#x5C;right)&#x5C;&#x5C;%20%20x&#x27;^&#x5C;mu%20&amp;=%20&#x5C;tensor{&#x5C;Lambda}{^&#x5C;mu_&#x5C;nu}x^&#x5C;nu&#x5C;end{aligned}"/></p>  
  
  
####  Metric: {#metric }
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;tensor{&#x5C;eta}{_{&#x5C;mu&#x5C;nu}}%20=%20&#x5C;begin{pmatrix}%20%201%20&amp;%200%20&amp;%200%20&amp;%200&#x5C;&#x5C;%20%200%20&amp;%20-1%20&amp;%200%20&amp;%200&#x5C;&#x5C;%20%200%20&amp;%200%20&amp;%20-1%20&amp;%200&#x5C;&#x5C;%20%200%20&amp;%200%20&amp;%200%20&amp;%20-1%20%20&#x5C;end{pmatrix}"/></p>  
  
  
such that:
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;tensor{&#x5C;eta}{_{&#x5C;mu&#x5C;nu}}x^&#x5C;nu%20=%20&#x5C;left(%20x^0,%20-&#x5C;vec{x}%20&#x5C;right)"/></p>  
  
  
with the important quantity in relativity:
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;begin{aligned}%20%20x^2%20&amp;=%20&#x5C;vec{x}&#x5C;cdot%20&#x5C;vec{x}%20%20&amp;=%20x^&#x5C;mu%20x_&#x5C;mu&#x5C;end{aligned}"/></p>  
  
  
###  Proper and Improper group {#proper-and-improper-group }
  
Leaving us with the definition of the Lorentz group:
  
The condition <img src="https://latex.codecogs.com/gif.latex?&#x5C;det(&#x5C;Lambda)%20=%20&#x5C;pm%201"/> divides <img src="https://latex.codecogs.com/gif.latex?&#x5C;L"/> into two disconnected components <img src="https://latex.codecogs.com/gif.latex?&#x5C;L&#x5C;pm"/> , called proper and improper Lorentz transformations.
\begin{equation}
  \label{eq:lorentzgroup}
  \Lambda^T \eta \Lambda = \eta
\end{equation}
  
or with indicies:
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;tensor{&#x5C;Lambda}{^&#x5C;mu_&#x5C;rho}%20&#x5C;tensor{&#x5C;eta}{_{&#x5C;mu&#x5C;nu}}%20&#x5C;tensor{&#x5C;Lambda}{^&#x5C;nu_&#x5C;sigma}%20=%20&#x5C;eta_{&#x5C;rho%20&#x5C;sigma}"/></p>  
  
  
Here we have the following types of groups
  
proper group:
\begin{equation}
  \label{eq:proper_group}
  \det(\Lambda) = +1
\end{equation}
  
and the improper group
\begin{equation}
  \label{eq:improper_group}
  \det(\Lambda) = -1
\end{equation}
  
>The condition <img src="https://latex.codecogs.com/gif.latex?&#x5C;det(&#x5C;Lambda)%20=%20&#x5C;pm%201"/> divides <img src="https://latex.codecogs.com/gif.latex?&#x5C;L"/> into two disconnected components <img src="https://latex.codecogs.com/gif.latex?&#x5C;L&#x5C;pm"/> , called proper and improper Lorentz transformations.
  
####  The Orthochronus group {#the-orthochronus-group }
  
>The condition <img src="https://latex.codecogs.com/gif.latex?&#x5C;sgn%20(&#x5C;tensor{&#x5C;Lambda}{_{00}})%20=%20&#x5C;pm%201"/> divides <img src="https://latex.codecogs.com/gif.latex?&#x5C;L"/> into two disconnected components, which one denotes <img src="https://latex.codecogs.com/gif.latex?&#x5C;L^&#x5C;uparrow"/> and <img src="https://latex.codecogs.com/gif.latex?&#x5C;L^&#x5C;downarrow"/>, and are called orthochronus and non-orthochronous. (jaff)
  
>The fundamental Lorentz transformations which we study are the restricted Lorentz group <img src="https://latex.codecogs.com/gif.latex?&#x5C;L^&#x5C;uparrow_+"/>. These are the Lorentz transformations that are both proper, <img src="https://latex.codecogs.com/gif.latex?&#x5C;det%20&#x5C;Lambda%20=%20+1"/>, and orthochronous, <img src="https://latex.codecogs.com/gif.latex?&#x5C;Lambda_{00}%20&#x5C;ge%201"/>. There are some elementary transformations in <img src="https://latex.codecogs.com/gif.latex?&#x5C;L"/> that map one component into another, and which have special names:
  
 - The Unit transformation <img src="https://latex.codecogs.com/gif.latex?&#x5C;one:%20&#x5C;Lambda^T%20&#x5C;eta%20&#x5C;Lambda%20=%20&#x5C;eta"/>
 - The parity transformation <img src="https://latex.codecogs.com/gif.latex?P%20:%20(x_0,&#x5C;vec{x})%20&#x5C;mapsto%20(x_0,-&#x5C;vec{x})"/>.
 <!-- - The time-reversal transformation <img src="https://latex.codecogs.com/gif.latex?T%20:%20(x_0,&#x5C;vec{x})%20&#x5C;mapsto%20(-x_0,&#x5C;vec{x})"/>.
 - The space-time-inversion transformation <img src="https://latex.codecogs.com/gif.latex?PT%20:%20(x_0,&#x5C;vec{x})%20&#x5C;mapsto%20(-x_0,-&#x5C;vec{x})"/>. -->
  
  
 The _proper group_ and _orthochronus group_: <img src="https://latex.codecogs.com/gif.latex?&#x5C;tensor{&#x5C;Lambda}{^0_0}&gt;1"/>
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;begin{aligned}%20%20&#x5C;tensor{(&#x5C;Lambda%20&#x5C;tilde{&#x5C;Lambda})}{^0_0}%20&amp;=%20&#x5C;tensor{&#x5C;Lambda}{^0_&#x5C;mu}%20&#x5C;tensor{&#x5C;tilde{&#x5C;Lambda}}{^&#x5C;mu_0}&#x5C;&#x5C;%20%20&amp;=%20&#x5C;tensor{&#x5C;Lambda}{^0_0}%20&#x5C;tensor{&#x5C;tilde{&#x5C;Lambda}}{^0_0}%20+%20&#x5C;tensor{&#x5C;Lambda}{^0_1}%20&#x5C;tensor{&#x5C;tilde{&#x5C;Lambda}}{^1_0}%20&#x5C;ge%201&#x5C;end{aligned}"/></p>  
  
  
An example of this is the unit transformation:
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;begin{aligned}%20%20&#x5C;one%20&amp;=%20&#x5C;begin{pmatrix}%20%20%20%201%20&amp;%200%20&amp;%200%20&amp;%200&#x5C;&#x5C;%20%20%20%200%20&amp;%201%20&amp;%200%20&amp;%200&#x5C;&#x5C;%20%20%20%200%20&amp;%200%20&amp;%201%20&amp;%200&#x5C;&#x5C;%20%20%20%200%20&amp;%200%20&amp;%200%20&amp;%201%20%20&#x5C;end{pmatrix}%20&#x5C;&#x5C;&#x5C;Lambda^T%20&#x5C;eta%20&#x5C;Lambda%20&amp;=%20&#x5C;eta&#x5C;end{aligned}"/></p>  
  
  
(Parity)
<p align="center"><img src="https://latex.codecogs.com/gif.latex?P(x^0,%20&#x5C;vec{x})%20&#x5C;mapsto%20()"/></p>  
  
  
The conditions for our transformation:
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;begin{aligned}%20%20&#x5C;Lambda^T%20&#x5C;eta%20&#x5C;Lambda%20&amp;=%20&#x5C;eta&#x5C;&#x5C;%20%20&#x5C;begin{pmatrix}%20%20%20%20a%20&amp;%20c&#x5C;&#x5C;%20b%20&amp;%20d%20%20&#x5C;end{pmatrix}%20&#x5C;begin{pmatrix}%20%20%20%201%20&amp;%200%20&#x5C;&#x5C;%200%20&amp;%20-1%20%20&#x5C;end{pmatrix}%20&#x5C;begin{pmatrix}%20%20%20%20a%20&amp;%20b%20&#x5C;&#x5C;%20c%20&amp;%20d%20%20&#x5C;end{pmatrix}%20&amp;=%20&#x5C;begin{pmatrix}%20%20%20%201%20&amp;%200%20&#x5C;&#x5C;%200%20&amp;%20-1%20%20&#x5C;end{pmatrix}&#x5C;end{aligned}"/></p>  
  
  
The conditions for <img src="https://latex.codecogs.com/gif.latex?a,%20b,%20c"/> & <img src="https://latex.codecogs.com/gif.latex?d"/>:
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;begin{pmatrix}%20%20&#x5C;cosh%20&#x5C;theta%20&amp;%20&#x5C;sinh%20&#x5C;theta%20&#x5C;&#x5C;%20sinh%20&#x5C;theta%20&amp;%20&#x5C;cosh%20&#x5C;theta&#x5C;end{pmatrix}%20=%20&#x5C;begin{pmatrix}%20%20&#x5C;gamma%20&amp;%20&#x5C;gamma%20&#x5C;beta%20&#x5C;&#x5C;%20&#x5C;gamma%20&#x5C;beta%20&amp;%20&#x5C;gamma&#x5C;end{pmatrix}"/></p>  
  
  
and must satisfy <img src="https://latex.codecogs.com/gif.latex?R^TR%20=%20&#x5C;one"/>:
  
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;begin{pmatrix}x_{00}%20&amp;%20x_{10}&#x5C;&#x5C;x_{01}%20&amp;%20x_{11}&#x5C;end{pmatrix}&#x5C;begin{pmatrix}%20&#x5C;eta_{00}%20&amp;%20&#x5C;eta_{01}&#x5C;&#x5C;&#x5C;eta_{10}%20&amp;%20&#x5C;eta_{11}%20&#x5C;end{pmatrix}&#x5C;begin{pmatrix}%20x_{00}%20&amp;%20x_{01}&#x5C;&#x5C;x_{10}%20&amp;%20x_{11}%20&#x5C;end{pmatrix}%20=&#x5C;begin{pmatrix}%20&#x5C;eta_{00}%20&amp;%20&#x5C;eta_{01}&#x5C;&#x5C;&#x5C;eta_{10}%20&amp;%20&#x5C;eta_{11}%20&#x5C;end{pmatrix}"/></p>  
  
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?=&#x5C;left[&#x5C;begin{array}{c|c}%20%20&#x5C;begin{aligned}%20%20%20%20x_{00}%20&amp;&#x5C;left(&#x5C;eta_{00}%20x_{00}%20+%20&#x5C;eta_{10}%20x_{10}&#x5C;right)%20+%20&#x5C;&#x5C;%20%20%20%20x_{10}%20&amp;&#x5C;left(&#x5C;eta_{01}%20x_{00}%20+%20&#x5C;eta_{11}%20x_{10}&#x5C;right)%20%20&#x5C;end{aligned}%20&amp;%20&#x5C;begin{aligned}%20%20%20%20x_{01}%20&amp;&#x5C;left(&#x5C;eta_{00}%20x_{00}%20+%20&#x5C;eta_{10}%20x_{10}&#x5C;right)%20+%20&#x5C;&#x5C;%20%20%20%20x_{11}%20&amp;&#x5C;left(&#x5C;eta_{01}%20x_{00}%20+%20&#x5C;eta_{11}%20x_{10}&#x5C;right)%20%20&#x5C;end{aligned}%20&#x5C;&#x5C;%20%20&#x5C;hline%20%20&#x5C;begin{aligned}%20%20x_{00}%20&amp;&#x5C;left(&#x5C;eta_{00}%20x_{01}%20+%20&#x5C;eta_{10}%20x_{11}&#x5C;right)%20+&#x5C;&#x5C;%20%20x_{10}%20&amp;&#x5C;left(&#x5C;eta_{01}%20x_{01}%20+%20&#x5C;eta_{11}%20x_{11}&#x5C;right)%20&#x5C;%20%20&#x5C;end{aligned}%20&amp;%20&#x5C;begin{aligned}%20%20x_{01}%20&amp;%20&#x5C;left(&#x5C;eta_{00}%20x_{01}%20+%20&#x5C;eta_{10}%20x_{11}&#x5C;right)%20+%20&#x5C;&#x5C;%20%20x_{11}%20&amp;%20&#x5C;left(&#x5C;eta_{01}%20x_{01}%20+%20&#x5C;eta_{11}%20x_{11}&#x5C;right)&#x5C;end{aligned}&#x5C;end{array}%20&#x5C;right]"/></p>  
  
  
###  Transformations: {#transformations }
  
A velocity transformation
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;begin{aligned}%20%20&#x5C;dv{x&#x27;^0}(x&#x27;)%20&amp;=%20v%20&amp;&#x5C;implies%20&#x5C;dd%20x&#x27;%20&amp;=%20&#x5C;gamma(&#x5C;dd%20x%20+%20&#x5C;beta%20&#x5C;dd%20x^0)&#x5C;&#x5C;%20%20&amp;%20&amp;&#x5C;implies%20&#x5C;dd%20x&#x27;^0%20&amp;=%20&#x5C;gamma(&#x5C;dd%20x^0%20+%20&#x5C;beta%20&#x5C;dd%20x)&#x5C;&#x5C;&#x5C;end{aligned}"/></p>  
  
  
For small velocities:
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;begin{aligned}S%20&amp;=%20-mc^2%20&#x5C;int%20&#x5C;dd%20t%20&#x5C;sqrt{1-&#x5C;frac{&#x5C;dvec{x}^2}{c^2}}&#x5C;&#x5C;%20&amp;&#x5C;simeq%20&#x5C;frac{1-%20&#x5C;dvec{x}^2%20}{&#x5C;left(2c^2&#x5C;right)^2}&#x5C;end{aligned}"/></p>  
  
  
  
Using <img src="https://latex.codecogs.com/gif.latex?p^2%20=%20m^2"/>:
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?E(&#x5C;dvec{x})%20=%20&#x5C;frac{m}{&#x5C;sqrt{1-&#x5C;dvec{x}^2}}%20&#x5C;to%20m+m&#x5C;frac{&#x5C;dvec{x}^2}{2}"/></p>  
  
  
  
Claim:
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;begin{aligned}%20%20(E,%20&#x5C;vec{p})%20&amp;=%20&#x5C;qq{4-momentum}&#x5C;&#x5C;%20%20&amp;=%20&#x5C;qq{4-velocity}&#x5C;end{aligned}"/></p>  
  
  
There exists these two values
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;begin{aligned}%20%20p^&#x5C;mu%20&amp;&#x5C;to%20&#x5C;tensor{&#x5C;Lambda}{^&#x5C;mu_&#x5C;nu}%20p^&#x5C;nu%20&#x5C;&#x5C;%20%20x^&#x5C;mu%20&amp;&#x5C;to%20&#x5C;tensor{&#x5C;Lambda}{^&#x5C;mu_&#x5C;nu}%20x^&#x5C;nu&#x5C;end{aligned}"/></p>  
  
  
To prove that this quantity os a 4-vector:
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;begin{aligned}%20%20v^&#x5C;mu%20&amp;=%20&#x5C;dv{x^&#x5C;mu}{&#x5C;tau}%20&#x5C;to%20%20&#x5C;dv{x^&#x5C;mu}{x}%20&#x5C;&#x5C;%20%20&#x5C;dv{x^&#x5C;mu}{t}%20&#x5C;dv{t}{&#x5C;tau}%20&amp;=%20&#x5C;dv{x}{t}&#x5C;end{aligned}"/></p>  
  
  
  
  
Lagrangian using the following Taylor expansion:
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;begin{cases}%20%20&#x5C;sqrt{1+&#x5C;epsilon}%20&amp;&#x5C;sim%201+&#x5C;frac{&#x5C;epsilon}{2}%20&#x5C;&#x5C;%20%20&#x5C;frac{1}{1+&#x5C;epsilon}%20&amp;&#x5C;sim%201-&#x5C;epsilon&#x5C;end{cases}"/></p>  
  
  
Combined:
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;frac{1}{&#x5C;sqrt{1-&#x5C;epsilon}}%20=%201+%20&#x5C;frac{&#x5C;epsilon}{2}"/></p>  
  
  
  
(Fundamentally we are alloking at massless particles, where <img src="https://latex.codecogs.com/gif.latex?p^2%20=%20m^2%20=%200"/>)
  
  
  
#  Four vectors {#four-vectors }
  
  
  
#  Spinors and transformations {#spinors-and-transformations }
#  Spinor helicity formalism (null vectors) {#spinor-helicity-formalism-null-vectors }
  
##  Spinor Helicity formalism and Pauli Matrices properties: {#spinor-helicity-formalism-and-pauli-matrices-properties }
  
\begin{equation}
  \label{eq:momentum_massless_particles}
  p^2 = p_\mu p^mu = 0, \qq{and} p_0^2 - \vec{p}^2 = 0
\end{equation}
  
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;sigma^1%20=%20&#x5C;pmqty{&#x5C;pmat{1}},%20%20&#x5C;sigma^2%20=%20&#x5C;pmqty{&#x5C;pmat{2}},%20%20&#x5C;sigma^3%20=%20&#x5C;pmqty{&#x5C;pmat{3}}"/></p>  
  
  
Squaring each of the pauli matrices produces the identity matrix:
  
\begin{equation}
  \label{eq:pauli_identity}
  \left(\sigma^i \right)^2 = \one
\end{equation}
  
Proof:
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;left(&#x5C;sigma^1%20&#x5C;right)^2%20=%20&#x5C;pmqty{&#x5C;pmat{1}}^2%20=%20&#x5C;pmqty{&#x5C;imat{2}}"/></p>  
  
  
###  Multiplication <img src="https://latex.codecogs.com/gif.latex?&#x5C;to"/> identity matrix: {#multiplication-to-identity-matrix }
  
there is a recursive relation, when multiplying the <img src="https://latex.codecogs.com/gif.latex?i^{&#x5C;text{th}}"/> matrix by the <img src="https://latex.codecogs.com/gif.latex?j^{&#x5C;text{th}}"/>:
  
\begin{equation}
  \label{eq:pauli_group}
  \sigma^i\sigma^j = \delta^{ij}\one +i\epsilon^{ijk}\sigma{k}
\end{equation}
  
  
###  commutation and anti commutation: {#commutation-and-anti-commutation }
They have the following anti/commutator relations
\begin{equation}
  \label{eq:pauli_commutator}
  \commutator{\sigma^i}{\sigma^j} = i\epsilon^{ijk}\sigma^k = \anticommutator{\sigma^j}{\sigma^i}
\end{equation}
  
###  Trace of multiplication: {#trace-of-multiplication }
The trace of two pauli matrices multiplied together
\begin{equation}
  \label{eq:pauli_trace}
  \Tr \left(\sigma_i \sigma_j \right) = 2\delta^{ij}
\end{equation}
where
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;sigma_i%20&#x5C;sigma_j%20=%20&#x5C;delta^{ij}%20&#x5C;one_2%20+%20i&#x5C;epsilon^{ijk}&#x5C;sigma^{k}"/></p>  
  
  
  
#  Little group and weights {#little-group-and-weights }
  
##  Angular Momentum properties: {#angular-momentum-properties }
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;begin{aligned}%20%20&#x5C;vec{J}%20&amp;=%20&#x5C;vec{x}%20&#x5C;times%20&#x5C;vec{p}&#x5C;&#x5C;%20%20&amp;=%20xp_y%20-%20yp_x&#x5C;&#x5C;&#x5C;end{aligned}"/></p>  
  
  
Using the a commutator:
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;begin{aligned}%20%20&#x5C;commutator{J^1}{J^2}%20&amp;=%20&#x5C;commutator{x^2p^3%20-%20x^3p^2}{x^3p^1%20-%20x^1p^3}&#x5C;&#x5C;%20%20&amp;=%20(x^2p^3%20-%20x^3p^2)(x^3p^1%20-%20x^1p^3)%20-%20(x^3p^1%20-%20x^1p^3)(x^2p^3%20-%20x^3p^2)&#x5C;end{aligned}"/></p>  
  
  
(Only commutator with same index are non-zero)
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;begin{aligned}%20%20&#x5C;commutator{J_i}{J_i}%20&amp;=%200&#x5C;&#x5C;%20%20&#x5C;commutator{J_i}{J_j}%20&amp;&#x5C;ne%200&#x5C;&#x5C;&#x5C;end{aligned}"/></p>  
  
  
This leads to the formal relation of angular momentum:
  
\begin{equation}
  \label{eq:angmomentum_commutator}
  \commutator{J^i}{J^j} = i \hbar J^{ijk} \sigma^k J^k
\end{equation}
  
This related transformation and sum to Noethers theorem
  
##  Noethers Theorem {#noethers-theorem }
  
\begin{equation}
  \label{eq:noethers_theorem}
  I = \sum_r \pdv{\L}{\dot{q}_r}\delta q_r
\end{equation}
  
  
##  <img src="https://latex.codecogs.com/gif.latex?SU"/> Group: {#su-group }
###  <img src="https://latex.codecogs.com/gif.latex?SU(2)"/> {#su2 }
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;begin{aligned}%20%20SU(2)%20&#x5C;to%20U(N)%20&amp;=%20N&#x5C;times%20N%20matrix&#x5C;&#x5C;%20%20%20&amp;=%20U^&#x5C;dagger%20U%20=%20&#x5C;one%20&#x5C;qq{Unitary}&#x5C;end{aligned}"/></p>  
  
  
<img src="https://latex.codecogs.com/gif.latex?SU(N)"/> are a special subset of unitary matrices (<img src="https://latex.codecogs.com/gif.latex?&#x5C;det%20U%20=%20&#x5C;pm%201"/>)
  
Taylor expansion of <img src="https://latex.codecogs.com/gif.latex?U"/>:
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;begin{aligned}%20%20U%20&amp;=%20e^{iA}&#x5C;&#x5C;%20%20e^x%20&amp;=%201%20+%20&#x5C;frac{x^2}{2}%20+%20&#x5C;frac{x^3}{3}%20&#x5C;dots&#x5C;end{aligned}"/></p>  
  
  
Impose the following conditions:
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;begin{aligned}%20%20&#x5C;det{e^{iA}}%20=%20&#x5C;one%20&#x5C;implies%20&#x5C;det{M}%20&amp;=%20e^{&#x5C;Tr%20(&#x5C;log{M})}%20&#x5C;&#x5C;%20%20%20&amp;=%20e^{&#x5C;Tr%20(&#x5C;log{(&#x5C;exp(iA)%20)}%20)%20}&#x5C;&#x5C;%20%20%20&amp;=%20e^{&#x5C;Tr%20(iA)}&#x5C;&#x5C;%20%20%20&amp;=%20e^{i%20&#x5C;Tr%20(A)}%20&#x5C;implies%20&#x5C;Tr%20(A)%20=%200&#x5C;end{aligned}"/></p>  
  
  
Condition: <img src="https://latex.codecogs.com/gif.latex?U^&#x5C;dagger%20U%20=%20&#x5C;one"/>
Special unitarity: add <img src="https://latex.codecogs.com/gif.latex?&#x5C;det%20A%20=%20&#x5C;pm%201%20&#x5C;to%20SU(N)"/>
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;begin{aligned}%20%20U%20&amp;=%20e^{iA}&#x5C;&#x5C;%20%20A^&#x5C;dagger%20&amp;=%20A%20&#x5C;qq{Unitary,%20hermitian}&#x5C;&#x5C;%20%20&#x5C;Tr%20A%20&amp;=%200&#x5C;end{aligned}"/></p>  
  
  
This implies we can write:
  
\begin{equation}
  \label{eq:unitary_group}
  U = e^{i\alpha^a \frac{\sigma^a}{2}}, \quad a = (1,2,3)
\end{equation}
  
where:
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;begin{aligned}%20%20e^{i&#x5C;alpha^a%20&#x5C;frac{&#x5C;sigma^a}{2}}%20=%20&#x5C;exp(&#x5C;sum_{a=1}^3%20i&#x5C;alpha^a%20&#x5C;frac{&#x5C;sigma^a}{2})&#x5C;end{aligned}"/></p>  
  
  
###  Proofs: {#proofs }
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;begin{aligned}%20%20U^dagger%20U%20&amp;=%20&#x5C;one&#x5C;&#x5C;%20%20(U_1U_2)^&#x5C;dagger(U_1U_2)%20&amp;=%20&#x5C;one&#x5C;&#x5C;%20%20U^&#x5C;dagger_2%20U^&#x5C;dagger_1%20U_1%20U_2%20&amp;%20=%20&#x5C;one&#x5C;end{aligned}"/></p>  
  
  
##  <img src="https://latex.codecogs.com/gif.latex?&#x5C;vec{&#x5C;rho}%20&#x5C;to%20&#x5C;vec{&#x5C;rho}&#x5C;cdot&#x5C;vec{&#x5C;sigma}"/>: {#vecrho-to-vecrhocdotvecsigma }
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;begin{aligned}%20%20&#x5C;commutator{&#x5C;frac{&#x5C;sigma^i}{2}}{&#x5C;frac{&#x5C;sigma^j}{2}}%20&amp;%20=%20i&#x5C;epsilon^{ijk}&#x5C;frac{&#x5C;sigma^k}{2}&#x5C;end{aligned}"/></p>  
  
  
###  Properties: {#properties }
<img src="https://latex.codecogs.com/gif.latex?SU(2)"/>
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;begin{aligned}%20%20&#x5C;rho^&#x5C;mu%20&amp;=%202&#x5C;times%202%20&#x5C;qq{matrix}&#x5C;&#x5C;%20%20&#x5C;sigma^0%20&amp;=%20&#x5C;one_2&#x5C;&#x5C;%20%20&#x5C;sigma^i%20&amp;=%20&#x5C;qq{Pauli%20spin%20matrices}&#x5C;&#x5C;&#x5C;end{aligned}"/></p>  
  
  
\begin{equation}
  \label{eq:paulispin_innerprod}
  p^\mu \sigma_\mu \equiv \rho^0\sigma_0 + \vec{\rho}\cdot\vec{\sigma}
\end{equation}
  
where:
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;begin{aligned}%20%20&#x5C;det(p^&#x5C;mu%20&#x5C;sigma_&#x5C;mu%20)%20&amp;%20&#x5C;equiv%20&#x5C;vec{p}^2%20&#x5C;&#x5C;%20%20&#x5C;qq{Where,%20massless%20particles}%20p^2%20&amp;=%200&#x5C;&#x5C;%20%20(&#x5C;rho^0)^2%20-%20(&#x5C;vec(p))^2%20&amp;=%200&#x5C;end{aligned}"/></p>  
  
  
These relations here set the stage for being able to work with massless particles.
  
  
\begin{equation}
  \label{eq:spinor_helicity_formalism}
  (p^\mu \sigma_\mu)_{\alpha \dot\alpha} = \lambda_\alpha \tilde{\lambda}_{\dot\alpha}
\end{equation}
  
  
#  Determination of three-point amplitudes of massless particles {#determination-of-three-point-amplitudes-of-massless-particles }
  
#  Introduction to Feynman diagrams  - reproducing amplitudes for Yang-Mills theory {#introduction-to-feynman-diagrams-reproducing-amplitudes-for-yang-mills-theory }
  
#  Three-point amplitudes and factorisation {#three-point-amplitudes-and-factorisation }
#  BCFW recursion relations in Yang-Mills and Gravity {#bcfw-recursion-relations-in-yang-mills-and-gravity }
  
  
  
  
  
[@Plefka:2014aa, pp 35-39]
  
The BCFW recursion relations rely on an understanding of the behaviour of the function <img src="https://latex.codecogs.com/gif.latex?A_n(z)"/> in the complex <img src="https://latex.codecogs.com/gif.latex?z"/> plane.
  
The derivation proceeds in three steps.
  
* First, the locations of the poles of <img src="https://latex.codecogs.com/gif.latex?A_n(z)"/> are analyzed.]
* Then, it is shown that the residues of the poles correspond to products of lower-point tree amplitudes.
* Finally, the large <img src="https://latex.codecogs.com/gif.latex?z"/> behaviour of <img src="https://latex.codecogs.com/gif.latex?A_n(z)"/> is determined.
  
  
Using complex analysis, we want to inspect the amplitude <img src="https://latex.codecogs.com/gif.latex?A_n(z)"/>. This is because the sum of tree-level Feynman diagrams are gauge invariant, and therefore when they are deformed by <img src="https://latex.codecogs.com/gif.latex?z"/>, they remain unchanged. Therefore we can choose the Feynman gauge for the following discussion, without loss of generality. It is clear that <img src="https://latex.codecogs.com/gif.latex?An(z)"/> is a rational function of the <img src="https://latex.codecogs.com/gif.latex?&#x5C;ld{i}"/>,<img src="https://latex.codecogs.com/gif.latex?&#x5C;lmt_i"/> and <img src="https://latex.codecogs.com/gif.latex?z"/>. Moreover, <img src="https://latex.codecogs.com/gif.latex?An(z%20=%200)"/> can only have poles where the denominators of Feynman propagators become zero.
  
When inspecting a function using complex analysis, we try to simplify the function such that there is only one variable in which to take into the complex plane. Taking our scattering amplitude, we reduce it such that our only variable becomes the moment of a particle:
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?(p_i%20+p_{i+1}%20+%20p_{i+2}%20+%20&#x5C;dots%20)^2%20&#x5C;equiv%20&#x5C;%20&#x5C;dij"/></p>  
  
  
Where we have the following quantities:
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;begin{aligned}%20%20S%20&amp;=%20(p_1%20+%20p_2)^2&#x5C;&#x5C;%20%20t%20&amp;=%20(p_2%20+%20p_3)^2&#x5C;&#x5C;%20%20u%20&amp;=%20(p_1%20+%20p_1)^2%20&#x5C;&#x5C;%20%20p_4%20&amp;=%20-p_1%20-p_2%20-p_3%20-p_4%20%20&#x5C;Rightarrow%20A(S,t,u)&#x5C;end{aligned}"/></p>  
  
  
Gauge theory, n-point amplitudes. We now deform our amplitude in such a way that:
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;begin{aligned}%20%20A(p_1,%20&#x5C;dots,%20p_n)%20&amp;&#x5C;to%20&#x5C;begin{cases}%20%20%20%20p_i%20&#x5C;to%20p_i(z)&#x5C;&#x5C;%20%20%20%20p_j%20&#x5C;to%20p_j(z)&#x5C;&#x5C;%20%20&#x5C;end{cases}&#x5C;&#x5C;&#x5C;end{aligned}"/></p>  
  
  
Which leaves our amplitude in a state with only complexified momenta <img src="https://latex.codecogs.com/gif.latex?p_i(z)%20&#x5C;qq{and}%20p_i(z)"/>
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;begin{aligned}%20%20&#x5C;sA(z)%20&amp;=%20A(-p_1,%20p_2,%20&#x5C;cdots,%20p_i(z),%20&#x5C;cdots,%20p_j(z),%20&#x5C;cdots%20%20p_n%20%20)&#x5C;&#x5C;%20%20&#x5C;sA(0)%20&amp;=%20A(-p_1,%20p_2,%20&#x5C;cdots,%20%20p_n%20%20)&#x5C;end{aligned}"/></p>  
.
  
This process can be particularly useful when exploring massless particles <img src="https://latex.codecogs.com/gif.latex?&#x5C;left%20(%20&#x5C;sum%20p_i^2%20=%200%20&#x5C;right%20)"/>; however this is not a constrain, and also works just as well with massive particles.
  
We are left with a transformation:
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;begin{aligned}%20%20&#x5C;quad%20p_i^&#x5C;mu(z)%20&amp;=%20p_i^&#x5C;mu(z)+z&#x5C;eta^&#x5C;mu&#x5C;&#x5C;%20%20&#x5C;quad%20p_j^&#x5C;mu(z)%20&amp;=%20p_j^&#x5C;mu(z)-z&#x5C;eta^&#x5C;mu&#x5C;&#x5C;&#x5C;end{aligned}"/></p>  
  
  
With <img src="https://latex.codecogs.com/gif.latex?&#x5C;eta%20="/> new complex momentum and <img src="https://latex.codecogs.com/gif.latex?z%20="/> its respective complex variable.
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;left%20.&#x5C;begin{aligned}%20%20%20%20p_i^2(z)%20&amp;=%200&#x5C;&#x5C;%20%20%20%20p_j^2(z)%20&amp;=%200&#x5C;end{aligned}%20&#x5C;quad&#x5C;right%20&#x5C;}%20&#x5C;qquad%20&#x5C;forall%20z"/></p>  
  
  
This leads to:
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;left%20.&#x5C;begin{aligned}%20%20&#x5C;quad%20p_i^2(z)%20&amp;=&amp;%20&#x5C;cancelto{0}{p_i^2}%20+z^2&#x5C;eta^2%20+%202z(p_i%20&#x5C;cdot%20&#x5C;eta)%20&amp;%20=%200&#x5C;&#x5C;%20%20&#x5C;quad%20p_j^2(z)%20&amp;=&amp;%20&#x5C;cancelto{0}{p_j^2}%20+z^2&#x5C;eta^2%20+%202z(p_j%20&#x5C;cdot%20&#x5C;eta)%20&amp;%20=%200&#x5C;end{aligned}&#x5C;right%20&#x5C;}%20&#x5C;qquad%20&#x5C;forall%20z"/></p>  
  
  
This is useful for us, as we may thus choose <img src="https://latex.codecogs.com/gif.latex?&#x5C;eta"/> to be any value we would like; so to simplify this equation, we choose <img src="https://latex.codecogs.com/gif.latex?&#x5C;eta%20=%200"/>, and we are left with:
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;begin{aligned}%20%202(p_i%20&#x5C;cdot%20&#x5C;eta)%20&amp;=%200%20&amp;&#x5C;Leftrightarrow%20&amp;%20&#x5C;agl{i}{&#x5C;eta}%20&#x5C;sqr{&#x5C;eta}{i}%20&amp;%20=0&#x5C;&#x5C;%20%202(p_j%20&#x5C;cdot%20&#x5C;eta)%20&amp;=%200%20&amp;&#x5C;Leftrightarrow%20&amp;%20&#x5C;agl{j}{&#x5C;eta}%20&#x5C;sqr{&#x5C;eta}{j}%20&amp;%20=0&#x5C;end{aligned}"/></p>  
  
  
This is already a well known solution (from the 60s - find ref ), where we are keeping spacetime such that:
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;lmt%20=%20&#x5C;pm%20&#x5C;lambda^*"/></p>  
  
  
Real minkowski:
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;agl{i}{&#x5C;eta}%20=%200%20&#x5C;implies%20&#x5C;sqr{i}{&#x5C;eta}%20=%200%20&#x5C;qq{and:}%20&#x5C;ld{&#x5C;eta}%20&#x5C;parallelsum%20&#x5C;ld{i}%20&#x5C;implies%20&#x5C;lmtd{&#x5C;eta}%20&#x5C;parallelsum%20&#x5C;lmtd{i}"/></p>  
  
  
Taking complex Minkowski:
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;left%20.&#x5C;begin{aligned}%20%20&#x5C;underline{&#x5C;agl{i}{&#x5C;eta}}%20&#x5C;udots{<img src="https://latex.codecogs.com/gif.latex?&amp;#x5C;sqr{&amp;#x5C;eta}{i}"/>}%20&#x5C;to%200&#x5C;&#x5C;%20%20&#x5C;udots{<img src="https://latex.codecogs.com/gif.latex?&amp;#x5C;agl{j}{&amp;#x5C;eta}"/>}%20&#x5C;underline{&#x5C;sqr{&#x5C;eta}{j}}%20&#x5C;to%200&#x5C;&#x5C;&#x5C;end{aligned}%20&#x5C;right%20&#x5C;}%20&#x5C;qq{2%20options}"/></p>  
  
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;begin{aligned}%20%20&#x5C;eta%20&amp;=%20&#x5C;ld{i}%20&#x5C;lmtd{j}%20&amp;&amp;%20&#x5C;qq{or}%20&#x5C;eta%20&amp;=%20&#x5C;ld{j}%20&#x5C;lmtd{i}&#x5C;end{aligned}"/></p>  
  
Where implies that the we are left with:
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;begin{aligned}%20%202(p_i&#x5C;cdot%20&#x5C;eta)%20&amp;=%200&#x5C;&#x5C;%20%202(p_j&#x5C;cdot%20&#x5C;eta)%20&amp;=%200&#x5C;end{aligned}"/></p>  
  
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;begin{aligned}p_i%20&#x5C;to%20p_i(z)%20&amp;=%20p_i%20+z%20&#x5C;eta&#x5C;&#x5C;%20%20&amp;=%20&#x5C;ld{i}&#x5C;lmtd{i}%20+%20z&#x5C;ld{i}&#x5C;lmtd{j}&#x5C;&#x5C;%20%20&amp;=%20&#x5C;ld{i}(&#x5C;lmtd{i}%20+%20z&#x5C;lmtd{j})&#x5C;&#x5C;%20%20&amp;&#x5C;equiv%20&#x5C;ld{i}%20&#x5C;lthd{i}(z)&#x5C;&#x5C;&#x5C;end{aligned}&#x5C;qquad%20&#x5C;qquad&#x5C;begin{aligned}p_j%20&#x5C;to%20p_j(z)%20&amp;=%20p_j%20-z%20&#x5C;eta&#x5C;&#x5C;%20%20&amp;=%20&#x5C;ld{j}&#x5C;lmtd{j}%20-%20z&#x5C;ld{i}&#x5C;lmtd{j}&#x5C;&#x5C;%20%20&amp;=%20(&#x5C;ld{j}%20-%20z&#x5C;ld{i})&#x5C;lmtd{j}&#x5C;&#x5C;%20%20&amp;&#x5C;equiv%20&#x5C;lh_j%20&#x5C;lmtd{j}(z)&#x5C;end{aligned}"/></p>  
  
  
Leaving us with the two quantities:
  
\label{eq:shifted_amplitude}
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;begin{aligned}%20%20&#x5C;lthd{i}(z)%20&amp;&#x5C;equiv%20&#x5C;lmtd{i}%20+%20z&#x5C;lmtd{j}%20&#x5C;&#x5C;%20%20&#x5C;lh_j(z)%20%20%20%20&amp;&#x5C;equiv%20&#x5C;ld{j}%20-%20z&#x5C;ld{i}&#x5C;end{aligned}"/></p>  
  
  
Sometimes this is given the shorthand notation:
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;begin{aligned}%20%20&#x5C;lthd{i}(z)%20&amp;&#x5C;equiv%20%20&#x5C;sabrv{i}{j}&#x5C;&#x5C;%20%20&#x5C;lh_j(z)%20&amp;&#x5C;equiv%20&#x5C;asbrv{i}{j}&#x5C;end{aligned}"/></p>  
  
  
This leads us to being able to describe amplitudes in the simple form:
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;frac{C_1}{z-z_1}%20+%20&#x5C;frac{C_2}{z-z_2}%20+%20&#x5C;dots+%20&#x5C;frac{C_L}{z-z_L}"/></p>  
  
  
This has the simplification that there are no constant terms <img src="https://latex.codecogs.com/gif.latex?(&#x5C;cancelto{0}{C}+&#x5C;cancelto{0}{d_1%20z_1}+&#x5C;cancelto{0}{d_2%20z^2_2})"/>. This means that we only need to know pieces of information:
  
1. Position of poles: <img src="https://latex.codecogs.com/gif.latex?(z_1,%20z_2,%20&#x5C;dots,%20z_L%20)"/>
1. Residues <img src="https://latex.codecogs.com/gif.latex?(L_1,%20L_2,%20&#x5C;dots,%20L_L)"/>, leave us only with simple poles:
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;frac{1}{(x-x_0)^3}"/></p>  
  
  
This is referred to as the pole to third power.
  
##  Feynman Diagrams {#feynman-diagrams }
What are the singularities:
  
\begin{center}  
  \input{assets/feynman01.tex}
\end{center}
  
Using the above, such that <img src="https://latex.codecogs.com/gif.latex?&#x5C;vec{p}^2%20=%20m^2"/>, and in the special massless case where <img src="https://latex.codecogs.com/gif.latex?m%20=%200"/>
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;vec{p}%20=%20-p_1%20-p_2%20-p_3"/></p>  
  
  
When we complexify this, we get:
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;begin{aligned}%20%20&#x5C;hat{p}(z)%20&amp;=%20P%20+%20z&#x5C;eta&#x5C;&#x5C;%20%20&#x5C;hat{p}^2(z)%20=0%20&amp;=%20P^2%20+%200%20+%202z(P&#x5C;cdot&#x5C;eta)&#x5C;&#x5C;%20%20???%20&#x5C;qquad%20&#x5C;frac{z}{P}&amp;=%20&#x5C;frac{P^2}{2(P&#x5C;cdot&#x5C;eta)}&#x5C;end{aligned}"/></p>  
  
  
rewriting this:
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;begin{aligned}%20%20&#x5C;frac{1}{&#x5C;hat{p}^2(z)}%20&amp;=%20&#x5C;frac{1}{p^2%20+%202z(P&#x5C;cdot%20z)}&#x5C;&#x5C;%20%20&amp;=%20&#x5C;frac{1}{2(p&#x5C;cdot%20&#x5C;eta)}%20&#x5C;cdot%20&#x5C;frac{1}{z+&#x5C;underbrace{&#x5C;frac{p^2}{2(p&#x5C;cdot&#x5C;eta)}}_{=&#x5C;frac{1}{z-z_p}}}&#x5C;&#x5C;%20%20&amp;=%20&#x5C;sum_p%20&#x5C;frac{C_p}{z-z_p}&#x5C;end{aligned}"/></p>  
  
  
Where we have used the substitution: <img src="https://latex.codecogs.com/gif.latex?z_p=&#x5C;frac{p^2}{2(p&#x5C;cdot&#x5C;eta)}"/>
  
##  Understanding Singularities {#understanding-singularities }
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?A(1,2,&#x5C;cdots,n)%20&#x5C;xrightarrow{&#x5C;quad%20p^2&#x5C;to%200%20&#x5C;quad}%20&#x5C;sum_n%20A_L&#x5C;frac{i}{p^2}A_R"/></p>  
  
  
\begin{center}  
  TODO
  \input{assets/feynman02.tex}
\end{center}
  
Where:
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;begin{aligned}%20%20P%20&amp;=%20p_i%20+p_{i+1}%20+%20&#x5C;cdots%20+%20p_{n}%20+%20p_1&#x5C;&#x5C;%20%20&#x5C;hat{P}%20&amp;=%20P%20+%20z&#x5C;eta&#x5C;end{aligned}"/></p>  
  
  
Then:
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;begin{aligned}%20%20z%20&#x5C;to%20z_p%20&amp;&#x5C;equiv%20&#x5C;frac{-p^2}{2(p&#x5C;cdot%20&#x5C;eta)}&#x5C;&#x5C;%20%20&#x5C;hat{p}^2(z)%20&amp;&#x5C;to%200&#x5C;&#x5C;%20%20&#x5C;therefore%20&#x5C;frac{1}{&#x5C;hat{p}^2(x)}%20&amp;=%20&#x5C;frac{1}{2(p&#x5C;cdot%20&#x5C;eta)[z-z_p]}&#x5C;&#x5C;&#x5C;end{aligned}"/></p>  
  
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;begin{aligned}%20%20C_p%20&#x5C;lim_{z&#x5C;to%20z_p}%20&#x5C;sA(z)%20&amp;=%20%20&#x5C;cancel{z-z_p}%20&#x5C;sum_h%20A_L%20(&#x5C;hat{1}(z),%20&#x5C;hat{p}^h,%20i,%20i+1,%20&#x5C;cdots)%20%20&#x5C;frac{i}{2(p&#x5C;cdot&#x5C;eta)&#x5C;cancel{(z-z_p)}}%20A_R(&#x5C;hat{p}^h,%20&#x5C;hat{2}(z),%20&#x5C;cdots)&#x5C;&#x5C;%20%20&amp;%20=%20A_L(&#x5C;hat{i},%20&#x5C;hat{p},%20&#x5C;cdots)A_R(-&#x5C;hat{p},&#x5C;cdots)%20&#x5C;&#x5C;%20%20&amp;=%20A_L(&#x5C;hat{1}(z_p),%20&#x5C;hat{p},%20&#x5C;cdots)A_R(-&#x5C;hat{P},^{-h},%202(z_p),%20&#x5C;cdots)&#x5C;&#x5C;%20%20&amp;=%20&#x5C;sum_h%20&#x5C;frac{A_L(1(z_p),%20&#x5C;hat{p}^h)%20A_R(-&#x5C;hat{p}^{-h},2(z(p)))}{2(p&#x5C;eta)}&#x5C;&#x5C;%20%20&amp;&#x5C;equiv%20C_p&#x5C;end{aligned}"/></p>  
  
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;begin{aligned}%20%20A(1,2,&#x5C;cdots,n)%20&amp;=%20&#x5C;sum_n%20A_L%20&#x5C;frac{i}{p^2}%20A_R&#x5C;&#x5C;%20%20&#x5C;sA(0)%20&amp;=%20&#x5C;sum_p%20&#x5C;sum_h%20&#x5C;frac{A_L^h(z_p)%20A_R^{-h}(z_p)}{s(p&#x5C;cdot&#x5C;eta)(&#x5C;cancel{z}-z_p)}%20i%20&#x5C;&#x5C;%20%20&amp;=%20&#x5C;sum_p%20&#x5C;sum_h%20A_L^h(z_p)&#x5C;frac{i}{p^2}A_R^{-h}(z_p)%20=%20A&#x5C;end{aligned}"/></p>  
  
  
For example:
  
\begin{center}  
  TODO
  \input{assets/feynman03.tex}
\end{center}
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;begin{aligned}%20%20P%20&amp;=%20p_4%20+%20p_1,%20z%20=%20&#x5C;frac{-1p^2}{2(p&#x5C;cdot&#x5C;eta)}&#x5C;&#x5C;%20%20P^2%20&amp;=%20(p_4%20+%20p_1)^2%20=%20&#x5C;agl{4}{1}&#x5C;sqr{1}{4}&#x5C;end{aligned}"/></p>  
  
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?2p&#x5C;eta%20&#x5C;qq{such%20that}&#x5C;eta%20:%20&#x5C;begin{cases}%20%20%20%20&#x5C;ld{1}&#x5C;lmtd{2}%20&#x5C;to%202(p&#x5C;cdot%20&#x5C;eta)%20&amp;=%20&#x5C;left%20&lt;%201%20|%20p%20|%202%20&#x5C;right%20]%20&#x5C;&#x5C;%20%20%20%20&#x5C;ld{2}&#x5C;lmtd{1}%20&#x5C;to%202(p&#x5C;cdot%20&#x5C;eta)%20&amp;=%20&#x5C;left%20&lt;%202%20|%20p%20|%201%20&#x5C;right%20]%20&#x5C;&#x5C;%20%20&#x5C;end{cases}"/></p>  
  
  
  
  
  
  
  
  
#  Bibliography {#bibliography }
  