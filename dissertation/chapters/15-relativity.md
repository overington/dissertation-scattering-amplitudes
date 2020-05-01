
<!-- ## Building a scattering amplitude / Relativity -->

# The Relativity Principle

In order to begin understanding such interactions, we must first understand the
rules by which we can describe an individual particles motion and then build up
a language for how these motions interact in a system of particles.  We open
here by exploring current methods available to us, in the forms of mathematical
formalisms, and how we might use certain properties to expand on this
knowledge, in order to represent systems, or groups of particles, and how they
interact.


## Maximum velocity of propagation



<!--
   - Frames of reference
  -->

We will begin by inspecting the systems and rules by which interactions between
free particles can be described, and build our theory from there.  We need to
have a system by which we make measurements, and that measurement will take
the same form, in all other inertial frames of reference. This is the principle
of relativity.

For example, taking a look at two frames of reference (see Figure
\ref{fig:frames_of_ref}); we have two frames \(G, G\prime\) with orthogonal
axes \(\vec{x},\vec{y},\vec{z}\) and
\(\vec{x}\prime,\vec{y}\prime,\vec{z}\prime\).

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
    \draw [thick,->]  (O) -- (X)  node[below]{\small $\vec{x}\x$}; % X
    \draw [thick,->]  (O) -- (Y)  node[above]{\small $\vec{y}\x$}; % Y
    \draw [thick,->]  (O) -- (Z)  node[left ]{\small $\vec{z}\x$}; % Z
    \draw [decorate,decoration={brace,amplitude=7}] (0.2+\r,0+\r) -- (2.2 + \r, 0 + \r) node [midway,above,yshift=7] {\small $\Delta \vec{x\x}$};
    \foreach \z in {0.2, 0.4,  ..., 6.9} {
      \draw (\z+\r, -\tick+\r) -- (\z+\r, \tick+\r);
    }
  }
\end{tikzpicture}
\end{center}
\caption{Two inertial frames of reference, \(G\) and \(G\prime\)}%
\label{fig:frames_of_ref}
\end{figure}




\begin{definition}[Inertial frame of reference]

  A moving body exists in an inertial reference frame, if does not have an
  external force acting upon it, and therefore moves with a constant velocity,
  which might be with a velocity of 0.  Any frame in constant motion with this frame is thus also
  an inertial frame of reference.

  The two inertial reference frames \(G\), and  \(G\prime\) from Figure \ref{fig:frames_of_ref} are related by:

  \begin{equation}
    \Delta \vec{x} = \vec{x}-\vec{x}\prime
  \end{equation}

  where \(\dv{x}{t}=0 \to x\) and \(x\prime\) have same inertial property.

\end{definition}



The equations expressing the laws of nature are invariant with respect to
transformations of coordinates and time from one inertial system to another.
This means that the equation describing any law of nature, when written in
terms of coordinates and time in different inertial reference systems, has one
and the same form. 

The laws of nature are identical in all inertial systems of reference.
Experiments show that instantaneous interactions interactions are impossible
principle of relativity is valid [See @Landau:1975aa]


In their classical form, the any changes or interactions which happen to a body
in an inertial frame, will happen instantaneously; for example the effects of
a gravitational field, or the electro-magnetic field. Changes to a body within
this frame will be propagated to all other bodies in this or any other inertial
frame instantaneously.

Experiments have shown [For example see @Einstein:1916aa; translation
@Bose:2016aa; @Abbott:2016aa ] that this is not the case, and that in fact the
effects of any such change or interaction must propagate out with a maximum
finite velocity, which we will refer to as the \textit{maximum velocity of
propagation}. This in turn implies that any such behaviour of freely moving
bodies within this frame will be limited to the same rules, and therefore must
also have a maximum velocity. This is a universal constant \(c\), the constant
velocity of light in a vacuum:


\begin{equation}
  c =  \SI{299792458}{\m\per\s} \label{eq:c_velocity}
\end{equation}


<!-- c is large numnber, therefore classical approximation c->intfy is good
approximation -->

Due to the fact that this velocity is such a large number, and that in our
every day dealings of velocities, it would be an irregular occurrence for
freely moving bodies to be travelling at such speeds; mostly we are dealing with
velocities where \(v \ll c \).  For such velocities, classical mechanics, or
the Newtonian limit is a fair approximation (where \(c \to \infty \)), and does
not need to take into account any changes needed to account for differences in
the mechanics of interactions, until the velocity of the freely moving body
approaches that order of magnitude i.e. where \(v \approx c\).  Such
differences were introduced in in the \textit{principle of relativity of Einstein} in
1905. Mechanics based on this principle are named \textit{Relativistic}.

We now turn our attention towards constructing a method of transforming between
any set of arbitrary coordinates, or any arbitrary frame of reference, such
that the choice of either is irrelevant of which frame of reference the
measurement was made, and "distances" are kept constant.  In order to do this,
we need to define what we mean by a distance, and then explore how we keep them
unchanged under certain types of transformation.


In classical mechanics, the "distance" between two points depend only on the
spatial distance between them being kept constant; so a distance in this sense
is purely spatially dependant.  In relativistic physics, this distance relies
on both spatial and time coordinates being kept constant, and is referred to as
a spacetime \textit{interval}.


\begin{figure}
\begin{center}
\begin{tikzpicture}[scale=1]
\def\tick{0.05};
\coordinate(O) at (0, 0, 0);
\coordinate(X) at (7, 0, 0);
\coordinate(Y) at (0, 3, 0);
\coordinate(Z) at (0, 0, 3);
\coordinate(r0) at (-1,2,2);
\coordinate(r1) at (2,1,-2);
\draw [thick,->]  (O) -- (X)  node[below]{\small $\vec{x}$}; % X
\draw [thick,->]  (O) -- (Y)  node[above]{\small $\vec{y}$}; % Y
\draw [thick,->]  (O) -- (Z)  node[left]{\small $\vec{z}$}; % Z
\draw [thick](r0) -- (r1) node[midway, above]{\(\vec{r}\)};
\draw [color=ImperialRed, -{Latex}] (O) -- (r0) node[above left]{\small \(\vec{r}_0\)};
\draw [dashed,color=BitterSweet] (0,0,0)
    -- (-1,0,0)  node[midway,below]{\small \(r_{0x}\)}
    -- (-1,2,0)  node[midway,right]{\small \(r_{0y}\)}
    -- (r0)      node[midway,above]{\small \(r_{0z}\)};
\draw [PrussianBlue, -{Latex}] (O) -- (r1) node[above right]{\small \(\vec{r}_1\)};
\draw [dashed,SteelBlue] (0,0,0)
    -- (0,0,-2)  node[midway,above]{\small \(r_{1z}\)}
    -- (2,0,-2)  node[midway,below]{\small \(r_{1x}\)}
    -- (r1)      node[midway, right,left]{\small \(r_{1y}\)};
\end{tikzpicture}
\end{center}
\caption{Distance \(\vec{r} = \vec{r_1} - \vec{r_0}\), broken into their respective components \((r_{0x},r_{0y},r_{0z})\) and \( (r_{1x},r_{1y},r_{1z})\)}%
\label{fig:vec_addition}
\end{figure}

These two differences between classical and relativistic mechanics can be
summed up in the the following two topics (**space**, and **time**)

 - **Space**: the classical definition of distances between points only takes
 on a meaning when we properly specify which from which system we have made
 that reference. In classical mechanics, we can absolute distances between two
 points by vector addition (See Figure \ref{fig:vec_addition}), where the
 distance \(\vec{r}\) between any two points \(\vec{r_0}\) and \(\vec{r_1}\)
 can be calculated using the vector sum as in the following equation:

\begin{align}
  \vec{r} &= \vec{r_1} - \vec{r_0} \label{eq:vector_addition}\\
  \vec{r_{0}} &= \vec{r_{0x}} + \vec{r_{0y}} + \vec{r_{0z}} \\
  \vec{r_{1}} &= \vec{r_{1x}}+ \vec{r_{1y}}+ \vec{r_{1z}}
\end{align}

  This is made possible through Pythagorean or vector addition. Where the
  magnitudes or length of each vector can be found using each scalar value like
  so for \(\vec{r_0}\), (and likewise for \(\vec{r_1}\) ):

\begin{equation}
  \abs{\vec{r_0}} = \sqrt{r_{0x}^2 + r_{0y}^2 + r_{0z}^2} \label{eq:vector_magnitude}
\end{equation}

 - **Time**: in classical mechanics time is an absolute property of the
  universe; and is independent of the frame of reference, as well as the
  coordinate system in which an event is measured; meaning that two independent
  events which happen simultaneously in one frame of reference; the even will
  occur like this in all other frames; this is given the term \textit{absolute
  time}, which was predicted to not be the case by Einstein's principal of
  relativity, and since then, has has been proved incorrect by experimental and
  observed data.

Here we turn to the changes in some property over time, and explore the
principle that of simultaneous changes, and how they might effect one another.
Accordingly; these effects in classical mechanics would be propagated
immediately, which contradicts our previous findings: the universal maximum
velocity of preparation we arrived at in equation \ref{eq:c_velocity}. So we
infer from this that there is no \textit{absolute time}, and that the
measurement of a time interval is different depending on the frame of reference
by which we have made the measurement. This also has an impact on simultaneity
of events, meaning that measuring two events happening at the same time in one
frame, would not necessarily happen simultaneously in all others.


## Spacetime intervals

In order for us to preserve our maximum velocity of preparation within
Einstein's Relativity, we will now explore the invariance of \(c\). To begin
with, we will introduce some new definitions:

\textit{Intervals} are described as the distance between two \textit{events},
where an event is a \textit{point}, which is described by both spatial and
temporal coordinates.  Using the coordinate system from Figures
\ref{fig:vec_addition} and \ref{fig:frames_of_ref}, this would be \(x, y, z\)
with \(t\) for time.

\begin{equation}
  e = (x,y,z,t) \label{eq:event}
\end{equation}

When a collection of points corresponding to the same body form sequential
events, they are called \textit{world points}, and taken to its limit, i.e.
\(\in [-\infty, \infty]\), then this describes the body at all points in time,
and is called a \textit{world line}.

The velocity at which any event can make an effect on any other body, both
withing the frame or any other frame must not exceed \(c\). By incorporating
the temporal coordinates of the event \(e\) from equation \ref{eq:event}. Here
we may build on our equation for vector addition \ref{eq:vector_addition}, by
adding the distance that would be traveled in time\(t\). Here we will simplify
things,  by assuming that the body is travelling the maximum velocity possible
\(c\), so that the whole "distance" \(s\) the body will travel is:

\begin{align}
  \vec{r} &= \vec{r_1} - \vec{r_0}\\
  \vec{r_0} &= (r_{0x}, r_{0y}, r_{0z}, r_{0t})\\
  \vec{r_1} &= (r_{1x}, r_{1y}, r_{1z}, r_{1t})\\
  s &= \sqrt{ (r_{1x} - r_{0x})^2 + (r_{1y} - r_{0y})^2 + (r_{1z} - r_{0z})^2} \label{eq:s_spatial}\\
  &= \sqrt{c^2 (r_{1t} - r_{0t})^2} \label{eq:s_temporal}
\end{align}

If we combine the two equations \ref{eq:s_spatial} and \ref{eq:s_temporal}, we
see that they are equal and therefore by taking one from the other \((s_s -
s_t)\); we get the null sum:


\begin{equation}
  0 =  (r_{1x} - r_{0x})^2 + (r_{1y} - r_{0y})^2 + (r_{1z} - r_{0z})^2 - 
    c^2 (r_{1t} - r_{0t})^2
\end{equation}

If taking the same measurement from a different frame of reference (For example
see Figure \ref{fig:frames_of_ref}), this becomes

\begin{equation}
  0 =  (r\prime_{1x} - r\prime_{0x})^2 + (r\prime_{1y} - r\prime_{0y})^2 + (r\prime_{1z} - r\prime_{0z})^2 - 
    c^2 (r\prime_{1t} - r\prime_{0t})^2
\end{equation}

If this is generalised to any vectors, such that we can define the interval:

\begin{equation}
  \vec{s} = \sqrt{ c^2 (r\prime_{1t} - r\prime_{0t})^2 - (r\prime_{1x} - r\prime_{0x})^2 + (r\prime_{1y} - r\prime_{0y})^2 + (r\prime_{1z} - r\prime_{0z})^2 } \label{eq:4d_interval}
\end{equation}

and in its infinitesimal form:

\begin{equation}
\dd[2]{\vec{s}} = c^2 \dd[2]{\vec{r_t}} - \dd[2]{\vec{r_{x}}} - \dd[2]{\vec{r_{y}}} - \dd[2]{\vec{r_{z}}} \label{eq:minkowski_metric}
\end{equation}


\begin{figure}
\begin{center}
\begin{tikzpicture}[scale=1, transform shape, every text node part/.style={align=center}]
  \fill [pattern=north east lines] (-2,2) -- (0,0) -- (-2,-2) -- (2,-2) -- (0,0) -- (2,2);
  \draw [thick,<->] (-3, 0) node[text width=3cm, right]{Absolutely Seperated} -- (3,0) node[below left]{$x$} node[text width=3cm, left]{Absolutely Seperated};
  \draw [thick,<->] (0, -2.2) node[below]{Absolute Past} -- (0,2.2);
  \draw (0,2.2) node[right]{$t$} +(0,0.3)node[above]{Absolute Future};
  \draw [thick] (-2,-2) -- (0,0)  -- (2,2);
  \draw [thick] (2,-2) -- (0,0) -- (-2, 2);
\end{tikzpicture}
\end{center}
\caption{Spacetime diagram, showing light cone}%
\label{fig:light_cone}
\end{figure}


Another important observation to point due to the maximum velocity of
propagation \(c\); any event can only effect another only if the interval between
them is time-like, that is: xxx; this follows immediately from the fact that no interaction
can propagate at a velocity greater than our maximum velocity of propagation
\(c\),




# TOEDIT:

## Spacetime transformations


### Transformations

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

#### Relative distances


### Moving Beyond Galilean Mechanics



Using reference systems or co-ordinates.  This fist step will allow us to set a
time and spatial dimensions of the system, and allow us to compare two systems
in relation to one another, and measure the change in this relation as one of
the systems evolves over time in relation to the other.






#### Einsteins dispersion relation

<!-- previously this section was named Interactions -->

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

