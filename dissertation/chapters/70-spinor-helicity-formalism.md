# Spinor helicity formalism (null vectors)

## Pauli Matrices

We begin here exploring a special kind of matrix 

\begin{definition}[Pauli Matrices]
\label{def:pauli_matrices}
\begin{equation}
\label{eq:momentum_massless_particles}
p^2 = p_\mu p^\mu = 0, \qq{and} p_0^2 - \vec{p}^2 = 0
\end{equation}


\begin{align}
\sigma^1 &= \pmqty{\pmat{1}} \\ 
\sigma^2 &= \pmqty{\pmat{2}} \\
\sigma^3 &= \pmqty{\pmat{3}}
\end{align}
\end{definition}

Squaring each of the Pauli matrices produces the identity matrix:

\begin{equation}
  \label{eq:pauli_identity}
  \left(\sigma^i \right)^2 = \one
\end{equation}

Proof:

\begin{equation}
\left(\sigma^1 \right)^2 = \pmqty{\pmat{1}}^2 = \pmqty{\imat{2}}
\end{equation}

### Multiplication \(\to\) identity matrix:

there is a recursive relation, when multiplying the \(i^{\text{th}}\) matrix by the \(j^{\text{th}}\):

\begin{equation}
  \label{eq:pauli_group}
  \sigma^i\sigma^j = \delta^{ij}\one +i\epsilon^{ijk}\sigma^{k}
\end{equation}


### commutation and anti commutation:

They have the following anti/commutator relations
\begin{equation}
  \label{eq:pauli_commutator}
  \commutator{\sigma^i}{\sigma^j} = i\epsilon^{ijk}\sigma^k = \anticommutator{\sigma^j}{\sigma^i}
\end{equation}

### Trace of multiplication:

The trace of two Pauli matrices multiplied together
\begin{equation}
  \label{eq:pauli_trace}
  \Tr \left(\sigma_i \sigma_j \right) = 2\delta^{ij}
\end{equation}
where

\begin{equation}
\sigma_i \sigma_j = \delta^{ij} \one_2 + i\epsilon^{ijk}\sigma^{k}
\end{equation}

<!-- aaabbbccc -->


### Facts about \(\sigma_\mu\):

When using the  Minkowski spacetime metric, we represent as following:

\begin{align}
  \sigma^\mu_{\alpha\dot{\alpha}} &= \left(\one, \vec{\sigma} \right)\\
  \bar{\sigma}^{\mu\  \dot{\alpha}\beta} &= \left(\one, -\vec{\sigma} \right)
\end{align}

With the Euclidean metric, we represent as following:

\begin{align}
  \sigma^\mu_{\alpha\dot{\alpha}} &= \left(\one, i\vec{\sigma} \right)\\
  \bar{\sigma}^{\mu\  \dot{\alpha}\beta} &= \left(\one, -i\vec{\sigma} \right)
\end{align}

So that:

\begin{align}
    P_{\alpha \dot{\alpha}} &= p^\mu \sigma_{\mu\ \alpha \dot{\alpha}}\\
    \bar{P}^{\dot{\alpha} \alpha} &= p^\mu \bar{\sigma}_\mu^{\ \dot{\alpha}\alpha}
\end{align}

Then \(\epsilon_{\alpha\beta}\) similar to Levi-Civita.

\begin{equation}
  \epsilon_{12} = -\epsilon_{21}
\end{equation}

Introducing the bracket notation: \(\langle \quad \rangle\) and \([ \quad ]\)

\begin{align}
  \rho^\mu \sigma_\mu &= \rho^0 \sigma_0 + \vec{p}\cdot \vec{\sigma}\\
  \rho_{\alpha \dot{\alpha}}&= \ld{\alpha}\ltd{\alpha}
\end{align}



### Weyl Spinors and equations

\begin{definition}[Weyl Equations]

Using our definition from our box operator in equation \ref{eq:box_operator}, we combine this with the definition of the Pauli Matrices from \ref{def:pauli_matrices} we now define:
\begin{align}
  i\partial_\mu \tensor{{\bar{\sigma}}}{^{\dot{\alpha}\alpha}} \Psi_{\alpha} = 0\\
  i\partial_\mu \tensor{\sigma}{_{\alpha \dot{\alpha}}} \tilde{\Psi}_{\alpha} = 0
\end{align}

Where \(\Psi_\alpha, \tilde{\Psi}_\alpha\) are Weyl spinors
\end{definition}

What do we need to solve \(\Psi_\alpha = \xi_\alpha e^{ikx}\):

\begin{align}
  i\partial^{\dot{\alpha}\alpha} \left( \xi_\alpha e^{ikx}\right) &= i^2 k^{\dot{\alpha}\alpha}\xi_\alpha e^{ikx} \\
  &= -\lu{\alpha} \ltu \xi_\alpha e^{ikx}
\end{align}

<!-- Properties \(SU(2)\): -->

\begin{align}
  \rho^\mu &= 2\times 2 \qq{matrix}\\
  \sigma^0 &= \one_2\\
  \sigma^i &= \qq{Pauli spin matrices}
\end{align}

\begin{equation}
  \label{eq:paulispin_innerprod}
  p^\mu \sigma_\mu \equiv \rho^0\sigma_0 + \vec{\rho}\cdot\vec{\sigma}
\end{equation}

where:

\begin{align}
  \det(p^\mu \sigma_\mu ) & \equiv \vec{p}^2 \\
  \qq{Where, for a massless particle} p^2 &= 0\\
  (\rho^0)^2 - (\vec{p})^2 &= 0
\end{align}

These relations here set the stage for being able to work with massless particles.


 3. Lorentz transformation \(SO(1,3) \to SL(2,\CC)\times SL(2,\CC)\). Arriving at Lorentz invariant transformation \(\agl{1}{\dot{2}} \equiv \tensor{\lambda}{_1^\alpha}\tensor{\lambda}{_{2\dot{\alpha}}}\)

 <!-- end:dissertation/log/2020.01.21.md -->




## Helicity

Helicity (see equation \ref{eq:helicity}) is the projection of a massless
particles' spin \(\vec{S}\) onto the the momentum \(\vec{p}\), which is then
normalised. This quantity is invariant under Lorentz transformation.
[@Plefka:2014aa, pp 15]

\begin{definition}[Helicity]

\begin{equation}
    h := \frac{\vec{p} \cdot \vec{S}}{\abs{\vec{p}}} \label{eq:helicity}
\end{equation}

\end{definition}

## Spinors

\begin{definition}[Spinors]
  Raising and lowering spinor indices

\begin{align}
  \ld{\alpha} &= \epsilon_{\alpha\beta} \lu{\beta} \\
  \lu{\alpha} &\equiv \epsilon^{\alpha\beta} \ld{\beta} \\
  \lmtd[\alpha] &= \epsilon_{\dot{\alpha}\dot{\beta}} \ltu[\beta] \\
  \ltu &\equiv \epsilon^{\dot{\alpha}\dot{\beta}} \lmtd[\beta]
  \label{eq:spinors}
\end{align}
\end{definition}

Proof:
\begin{align}
  \lu{\alpha\prime} &= \epsilon^{\alpha\beta}\tensor{M}{_\beta^\gamma}\ld{\gamma}\\
  &= \underbrace{\epsilon^{\alpha\beta} \tensor{M}{_\beta^\gamma}}_{ \tensor{\left [ \left( M^T \right)^{-1} \right ]}{^{\alpha}_{\delta}} \lu{\delta}} \epsilon_{\gamma\delta} \lu{\delta}\\
  \to \lu{\alpha'} &= \lu{\delta} \tensor{\left( M^{-1} \right)}{_{\delta} ^{\alpha}}\\
  \tensor{\epsilon}{^{\alpha\beta}}\tensor{M}{_\beta^\gamma}\tensor{\epsilon}{_{\gamma\delta}} &\eqq \tensor{ \left( M^{-1} \right) }{_\delta^\alpha}
\end{align}


Calculating a Spinor, we have a consistency condition:

\begin{equation}
  \tensor{\epsilon}{^{\alpha\beta}} \tensor{\epsilon}{_{\beta\rho}} \equiv \tensor{\delta}{^\alpha_\rho}
\end{equation}

## \(\vec{\rho} \to \vec{\rho}\cdot\vec{\sigma}\):

We introduce here the new Spinor Helicity formalism that has the
following properties:

 - Makes simplicity manifest
 - Enables us to perform one operation for all massless particles with different helicities (gluons, fermions, scalars)
 - Drastically simplifies the expression of scattering amplitudes by providing a compact form, while keeping the invariance of the four-vector form.
 - The dispersion equation from \ref{eq:einstein_energymomentum} remains invariant  under transformation  by the use of a metric. Using the spinor helicity formalism, we are able to keep the dispersion relation equivalently invariant (see Definition \ref{def:spinor_invariance}).

<!--
   -     - \(\eta \to \Lambda^T \eta \Lambda=\eta\)
   -     - Lorentz group definitions.
   - 
   -     \begin{equation}
   -           \overbrace{\mqty(\dmat{a,b})}^{+}  \overbrace{\mqty(\dmat{1,-1})}^{sp}  \overbrace{\mqty(\dmat{a,b})}^{+}
   -     \end{equation}
   - 
   -     - Transformation of velocity \(\to\) conclusion:
   - 
   -     \begin{equation}
   -       v' = \frac{\dd{x} + \beta \dd{x_0}}{\dd{x_0} + \beta \dd{x}}
   -     \end{equation} (Galilean transformation)
   -->

\begin{definition}[Spinor Helicity Formalism]
  \begin{equation}
    \label{eq:spinor_helicity_formalism}
    (p^\mu \sigma_\mu)_{\alpha \dot\alpha} = \lambda_\alpha \tilde{\lambda}_{\dot\alpha}
  \end{equation}
\end{definition}

\begin{definition}[Spin operator \(\hat{h}\)]

\begin{equation}
  \hat{h} = -\frac{1}{2}\lambda \pdv{\lambda} + \frac{1}{2} \pdv{\tilde{\lambda}} \tilde{\lambda}
\end{equation}

\end{definition}

\begin{definition}[Spinor Invariance]
  \label{def:spinor_invariance}
Take the following:

\begin{align}
  \lu{\alpha}\mud{\alpha} = \agl{\lambda}{\mu} &= \lu{\alpha}\muu{\beta}\tensor{\epsilon}{_{\alpha\beta}}\\
  \lmtd \mtu{\alpha} &= \sqr{\lmt}{\tilde\mu}
\end{align}

Both of these are antisymmetric:

\begin{align}
  \sqr{\lmt}{\tilde\mu} = \mtd{\alpha}\ltu &= \epsilon_{\dot{\alpha}\dot{\beta}}\mtu{\beta}\lu{\dot\alpha}\\
  &= \mtu{\beta}(-\epsilon_{\dot{\beta}\dot{\alpha}} \ltu)\\
  &= -\ltd{\beta}\mtu{\beta}
\end{align}

Where \(\lambda, \lmt\) are two types of spinors:

\begin{align}
  \qq{Undotted:}& \lu{\alpha},   \ld{\alpha}\\
  \qq{Dotted:}& \mu_{\dot\alpha}, \mu^{\dot\alpha}
\end{align}
\end{definition}

<!-- New From Here 16th Feb 2020 -->

<!-- #TODO: write definition for spinors -->

## Polarisation vectors for massless particles

We now examine the way to calculate the polarisation vector for gluons. This process can also be used in the calculation of any particle with similar properties. They have the following properties:

 - Massless
 - Spin 1
 - Two states of polarisation: helicity \(h=\pm 1\)

\begin{definition}[Polarisation vector \(\vec{\epsilon}\)]
  \label{def:polarisation_vector}

A polarisation vector \(\vec{\epsilon}\) may be found from a momentum vector
\(\vec{k} =\) such that they are orthogonal as in:

\begin{equation}
  \vec{\epsilon} ( \vec{k} ) \cdot \vec{k}=0 \label{eq:polarisation_vector_ref}
\end{equation}

\begin{figure}
  \centering
  \begin{tikzpicture}[]
    \coordinate (origin) at (0,0);
    \coordinate (x) at (0,1);
    \coordinate (y) at (1,0);
    \coordinate (z) at ({0.7*cos(210)}, {0.7*sin(210)} );
    \draw[->] (origin) -- (x) node[anchor=south] {\(\vec{k}\)};
    \draw[->] (origin) -- (y) node[anchor=west] {\(\vec{\epsilon}^{\small -}\)};
    \draw[->] (origin) -- (z) node[anchor=north east] {\(\vec{\epsilon}^{\small +}\)};
  \end{tikzpicture}
\end{figure}

\begin{align}
  \vec{k} &= \abs{\vec{k}} (0,0,1)\\
  \epsilon^{+} &= \frac{1}{\sqrt{2}}(1,i,0)\\
  \epsilon^{-} &= \frac{1}{\sqrt{2}}(1,-i,0)
\end{align}

In four-vector notation this becomes:

\begin{align}
  \epsilon^\mu(\vec{k}^{\pm})
\end{align}

We will use covariant 4-vector notation with \(\mu\) index to represent in \(\alpha\dot{\alpha}\) form:

\begin{align}
  \epsilon^{(+)}_{\alpha\dot{\alpha}}(k) &= \sqrt{2} (\text{something } B)\\
  \epsilon^{(-)}_{\alpha\dot{\alpha}}(k) &= \sqrt{2} (\text{something } A)
\end{align}

Here we need to introduce the reference spinor (\(\mu, \tilde{\mu}\)), such that the corresponding \(\lambda\) or \(\tilde\lambda\) are not parallel:

\begin{align}
  \tilde\mu \not\parallel \tilde\lambda: \qquad
    (A)&=&\frac{\ld{\alpha}\mtd{\alpha}}{\sqr{\tilde\lambda}{\tilde\mu}} \\
  \mu \not\parallel \lambda: \qquad
    (B)&=&\frac{\lmtd \mud{\alpha}}{\agl{\lambda}{\mu}}
\end{align}

\end{definition}

We don't want denominator to vanish such that \(\frac{\#}{\agl{\lambda}{\lambda}\to 0}\), as this would cause it to divide by zero.

So we will use:

\begin{equation}
\mud{\alpha} \to \mu^{'} = a \mu_\alpha + b \lambda_\alpha
\end{equation}

Therefore we choose \(\epsilon^{(+)}_{\alpha\dot{\alpha}}\) leaving us with:

\begin{align}
  \epsilon^{(+)}_{\alpha\dot{\alpha}} - \frac{
    \ltd{\alpha} ( a \mu_\alpha + b \lambda_\alpha )
  }{
    a \agl{\lambda}{\mu} + \cancel{b \agl{\lambda}{\lambda}}
  }
\end{align}

Where this is a gauge freedom:

\begin{equation}
  \epsilon^{(+)}_{\alpha\dot{\alpha}}  + \# \ld{\alpha} \lmtd = \epsilon
\end{equation}


## Spinors and transformations

\begin{definition}[Dot Product]

In order to do a dot product using this convention:

\begin{align}
  \tensor{{p_1}}{^{\dot{\alpha}\alpha}} \tensor{{p_2}}{_{\dot{\alpha}\alpha}}
    &= \tensor{{\tilde{\lambda_1}}}{^{\dot{\alpha}}}
    \tensor{{\lambda_1}}{^\alpha}
    \tensor{{\lambda_2}}{_\alpha}
    \tensor{{\tilde{\lambda_2}}}{_{\dot{\alpha}}} \\
  &= \agl{1}{2} \sqr{2}{1} = 2(p_1p_2)
\end{align}

and

\[
  \begin{aligned}
    \agl{1}{2} &\equiv \tensor{{\lambda_1}}{^\alpha} \tensor{{\lambda_2}}{_\alpha}\\
    \sqr{1}{2} &\equiv \tensor{{\lambda_1}}{_{\dot{\alpha}}} \tensor{{\lambda_2}}{^{\dot{\alpha}}}
  \end{aligned} \qquad
  \begin{aligned}
    \lu{\alpha} &= \epsilon^{\alpha\beta}\ld{\beta} \\
    \ld{\alpha} &= \epsilon_{\alpha\beta}\lu{\beta} \\
  \end{aligned}
\]

Hence we define:

\begin{align}
  \lu{\alpha} &= \epsilon^{\alpha\beta}\ld{\beta}\\
  \ld{\alpha} &= \epsilon_{\alpha\beta}\lu{\beta}
\end{align}

Similar to dotted spinors:

\begin{align}
  \tensor{{\sigma_\mu}}{_{\alpha\dot{\alpha}}} &\equiv
    \left( \one, \vec{\sigma} \right)_{\alpha\dot{\alpha}}\\
  \tensor{{\overline{\sigma}^{\mu}}}{^{\dot{\alpha}\alpha}} &\equiv
    \left( \one, -\vec{\sigma} \right)^{\dot{\alpha} \alpha}
      \equiv \epsilon^{\alpha \beta}\epsilon^{\dot{\alpha}\dot{\beta}}\tensor{{\sigma_\mu}}{_{\beta \dot{\beta}}}
\end{align}

\end{definition}



## Contraction using \(\left[ \quad  \right]\) and \(\langle \quad \rangle\) notation

In order to move back and forth between a four-vector and a spinor, we introduce a new notation, called the bracket notation:

\begin{definition}[Square and Angle Bracket Notation]
  \label{def:bracket_notation}
  \begin{align}
    \agl{\lambda}{\chi} &\equiv& \lambda^\alpha \chi^\beta \epsilon_{\alpha\beta} &= \lambda^\alpha \chi_\alpha
    \\
    \ltd{\alpha}\tilde{\chi}^{\dot{\alpha}} &=& \epsilon_{\dot{\alpha}\beta}\ltu[\beta]\ltu &\equiv \sqr{\tilde{\lambda}}{\tilde{\chi}}
    \\
    2(p_i\cdot p_j) &\equiv& \tensor{{p_i}}{_{\alpha\dot{\alpha}}} \tensor{{p_i}}{^{\dot{\alpha}\alpha}} &= \agl{i}{j} \sqr{j}{i}
  \end{align}
\end{definition}

## Creating Amplitudes for a three particle interaction:

Let us now begin using our bracket notation from Definition \ref{def:bracket_notation}, to create a simple three particle interaction.

\begin{figure}
  \centering
  \input{assets/amplitude_3pointsimple.tex}
  \caption{Feynman diagram of a three particle interaction}
\end{figure}


\begin{equation}
  A(1,2,3) \approx \agl{1}{2} \agl{2}{3} \agl{3}{1}
\end{equation}

Mixing brackets for three particles doesn't work, for example a three particle "Scattering":

\begin{align}
  \agl{1}{2} \sqr{2}{3} \agl{3}{1} &\to p_1 + p_2 + p_3 = 0\\
  &\to p_1 = -(p_2 + p_3)
\end{align}

As we are looking at massless particles; here our equation goes:

\begin{align}
  p_1^2 &= 0\\
  & = p_2^2 + p_3^2 + 2(p_2 \cdot p_3)\\
  &= 2(p_2 \cdot p_3)\\
  \implies p_1 \cdot p_2 &= p_2 \cdot p_3 = p_3 \cdot p_1  = 0
\end{align}

And complex momenta [@Plefka:2014aa]:

\begin{align}
  2p_1 \cdot p_2 &= 2p_2 \cdot p_3 = 2p_3 \cdot p_1 \\
  \implies \agl{1}{2} \sqr{2}{1} &= 0\\
  \agl{2}{3} \sqr{3}{1} &= 0\\
  \agl{3}{1} \sqr{1}{3} &= 0
\end{align}


We will use this and the following to explore a complex momenta:

\begin{align}
\qq{When} \agl{1}{2} &= 0\\
   \ld{1} &\parallel \ld{2}\\
   \tensor{{\ld{1}}}{_{\alpha}} &= a \tensor{{\ld{2}}}{_{\alpha}}\\
   A(1,2,3) &= \begin{cases} \overbrace{\agl{1}{2}}^{a_1} \overbrace{\agl{2}{3}}^{a_2} \overbrace{\agl{3}{1}}^{a_3}\\
     \underbrace{\sqr{1}{2}}_{\tilde{a_1}}
     \underbrace{\sqr{2}{3}}_{\tilde{a_3}}
     \underbrace{\sqr{3}{1}}_{\tilde{a_3}}
   \end{cases}
\end{align}


## Examples

### Simple using \(\sqr{\quad}{\ }\):

\begin{align}
  \frac{
    \sqr{1}{2}^3
    }{
    \sqr{2}{3} \sqr{3}{1}
    } &=
     &1: + \frac{1}{2}(3-1) &= +1\\
    &&2: + \frac{1}{2}(3-1) &= +1\\
    &&3: + \frac{1}{2}(0-2) &= -1
\end{align}

### Simple using \(\agl{\quad}{ }\):

\begin{align}
  \frac{
    \agl{1}{2}^3
    }{
    \agl{2}{3} \agl{3}{1}
    } &=
     &1: - \frac{1}{2}(3-1) &= -1\\
    &&2: - \frac{1}{2}(3-1) &= -1\\
    &&3: - \frac{1}{2}(0-2) &= +1
\end{align}

Note:

\begin{align}
  \agl{i}{j} &= - \frac{1}{2}(\qq{\(U_i\)} - \qq{\(D_j\)} )\\
  \sqr{i}{j} &= + \frac{1}{2}(\qq{\(U_i\)} - \qq{\(D_j\)} )
\end{align}


<!--
   - MHV examples:
   - a
   -->


<!-- end:2019.11.19.md -->

