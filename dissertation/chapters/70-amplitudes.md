\newpage

# Determination of three-point amplitudes of massless particles

<!-- begin:dissertation/log/2019.11.26.md -->

## Determining three point amplitudes

\begin{figure}
  \centering
  \input{assets/amplitude_3pointsimple2.tex}
  \caption{}
\end{figure}

The expression of the vertex is:

\begin{align}
  iV_{\mu_1, \mu_2, \mu_3}^{a_1, a_2, a_3} &= ig \left [
    (p_1-p_2)_{\mu_3} \eta_{\mu_1 \mu_2} +
    (p_2-p_3)_{\mu_1} \eta_{\mu_2 \mu_3} +
    (p_3-p_1)_{\mu_2} \eta_{\mu_3 \mu_1}
  \right ]f^{a_1 a_2 a_3}\\
  &=f^{a_1 a_2 a_3} V_{\mu_1 \mu_2 \mu_3}
\end{align}

Amplitude, using the polarisation vector \(\epsilon_{\alpha\dot{\alpha}}\):

\begin{equation}
\left .
\begin{aligned}
  V_{
    \mu_1 \mu_2 \mu_3
    } \evaluated{
      \epsilon_{(1)}^{\mu_1} \epsilon_{(2)}^{\mu_2} \epsilon_{(3)}^{\mu_3}
      }_{
        p_1^2 = p_2^2 = p_3^2 = 0
      }
= &\left [ \left( p_1 - p_2 \right) \cdot \epsilon_{(3)}\right ] \left( \epsilon_{(1)} \cdot \epsilon_{(2)} \right) +\\
  &\left [ \left( p_2 - p_3 \right) \cdot \epsilon_{(1)}\right ] \left( \epsilon_{(2)} \cdot \epsilon_{(3)} \right) +\\
  & \left [ \left( p_3 - p_1 \right) \cdot \epsilon_{(2)}\right ] \left( \epsilon_{(3)} \cdot \epsilon_{(1)} \right)
\end{aligned}
\qquad \right \}
[A]
\end{equation}

Here we also have to impose momentum conservation such that

\begin{equation}
  p_1 + p_2 + p_3 = 0
\end{equation}

Momentum is always transverse to polarisation (see Definition \ref{def:polarisation_vec)

\begin{equation}
  p\cdot \epsilon(p) = 0
\end{equation}

The expression of the polarisation vectors

\begin{definition}[Polarisation Vector, reference spinor]

\begin{align}
  \epsilon^{+}_{\alpha\dot{\alpha}} & \equiv  \frac{\xi_{\alpha} \tilde{k}_{\dot{\alpha}}}{\agl{\xi}{k}} \sqrt{2}\\
  \epsilon^{-}_{\alpha\dot{\alpha}} & \equiv - \frac{\tilde{\xi}_{\dot{\alpha}} k_{\alpha}}{\sqr{\tilde{\xi}}{\tilde{k}}}\sqrt{2}
\end{align}
\label{def:polarisation_vecotr_ref}
\end{definition}

Simplifying \([A]\):

\begin{align}
  -p_2 &= p_1 + p_3\\
  &= (2p_1 +p_3)\cdot \epsilon_3\\
  &= 2(p_1 \cdot \epsilon_3)
\end{align}

Likewise, the remaining \(p_i\) can be found by cyclicly permutation.


We use the definition \ref{def:polarisation_vecotr_ref} to simplify the following case:

\begin{align}
  \tensor{{\epsilon_1}}{_{\alpha\dot{\alpha}}} \cdot \tensor{{\epsilon_2}}{^{\alpha\dot{\alpha}}} &= 2(\epsilon_1\cdot \epsilon_2)\\
  &= \left( - \sqrt{2} \right)^2 \frac{1_{\dot{\alpha}} k_{\alpha}}{ \agl{1}{k} } \frac{2^{\dot{\alpha}} k^\alpha}{ \agl{2}{k}}\\
  &= \sqr{1}{2} \agl{k}{k} = 0
\end{align}

Now here we illustrate the case for MHV (Maximum Helicity Violation), where we are choosing as many as possible combinations that can be reduced to 0 on inspection without further need to calculation:


\begin{definition}[MHV Amplitude]

A Maximally Helicity Violating Amplitude is an interaction between \(n\)
massless bosons, where \(n-2\) of the amplitude legs have a particular helicty,
and the remaining two particles have the opposite helicity.

  \begin{equation}
    A(1,2,3) = 2 \left [ (p_i \cdot \epsilon^3)(\epsilon^1 \cdot \epsilon^2) +
    (p_2 \cdot \epsilon^1)(\epsilon^2 \cdot \epsilon^3)
    (p_3 \cdot \epsilon^1)(\epsilon^1 \cdot \epsilon^3)
    \right ]
  \end{equation}
\end{definition}

### Worked example of an MHV Amplitude

Using

\begin{align}
  \epsilon_1^- &= \frac{\tilde{\xi}_{\dot{\alpha}} 1_{\alpha} }{ \sqr{\xi}{1}}\\
  \epsilon_2^- &= \frac{\tilde{\xi}_{\dot{\alpha}} 2_{\alpha} }{ \sqr{\xi}{2}}
\end{align}

We are now looking for \(\epsilon_1^{1^-} \cdot \epsilon_2^{2^-}\)

Deriving gluon three-point amplitudes from Feynman rules, colour order:

\begin{align}
  2 \cdot \epsilon_2 \epsilon_3 &= \tensor{{\epsilon_{(2)}}}{^{\dot{\alpha}\alpha}} \tensor{{\epsilon_{(3)}}}{_{\alpha \alpha}}\\
  &= \sqrt{2}\sqrt{2} \ 2^{\dot{\alpha}} \underbrace{\tensor{{k_3}}{_{\dot{\alpha}}} \tensor{{k_2}}{^{\alpha}} \tensor{3}{_{\alpha}}}_{contraction}\\
  &= -2\sqr{k_3}{2} \agl{k_2}{3}
\end{align}

Using the definition of the reference spinor

Aiming to find \(\perp \therefore \quad a \cdot  b = 0\), which gets rid of the interaction \(\Yup\). This makes the first and third term vanish:

\begin{equation}
  \epsilon_1 \cdot \epsilon_2 = 0, \qquad \epsilon_1 \cdot \epsilon_3 = 0
\end{equation}

Leaving us only with the second term:

\begin{align}
  \left[
  p_2 \epsilon_1^-
  \right] \left(
    \epsilon_2^- \cdot \epsilon_3^+
  \right) &=
  \tensor{ {p_2} }{_{\alpha\dot{\alpha}}} \left( -\sqrt{2} \right) \frac{
    \tilde{\xi}^{\dot{\alpha}} 1^{\alpha}
    }{
      \tensor{{\lambda_2}}{_{\dot{\alpha}}}
    } \\
  2(p_2 \cdot \epsilon_1^- ) &= - \sqrt{2} \frac{
    \agl{1}{2} \sqr{2}{\tilde{\xi}}
    }{
    \sqr{\tilde{\xi}}{1}
    }
\end{align}

end finally for \(\epsilon_3^{(+)}\):

\begin{align}
  \epsilon_3^{(+)} &= \frac{
    \tensor{{\lambda_1}}{_{\alpha}}
    \tensor{{\tilde{\lambda_3}}}{_{\dot{\alpha}}}
    }{
    \agl{1}{3}
    } \sqrt{2}\\
    \to 2\epsilon_2^- \epsilon_3^+ &= -(\sqrt{2})(\sqrt{2}) \frac{
    \agl{2}{1} \sqr{3}{\tilde{\xi}}
      }{
        \agl{1}{3} \sqr{\tilde{\xi}}{2}
      } \\
  &= -2 \frac{
    \agl{2}{1}
  }{
    \agl{1}{3}
  } \frac{
    \sqr{3}{\tilde{\xi} }
  }{
    \sqr{\tilde{\xi}}{2}
  }
\end{align}  

Now we simplify:

\begin{align}
  \frac{
    \agl{1}{2} \cancel{ \sqr{2}{\tilde{\xi}}}
    }{
      \agl{\xi}{1}
    } \frac{
      \agl{2}{1} \sqr{3}{ \tilde{\xi}}
    }{
      \cancel{ \sqr{2}{\tilde{\xi}}}
    } &= - \frac{ \agl{1}{2}^2 }{ \agl{1}{3} }
    \frac{ \sqr{3}{\tilde{\xi}} }{ \sqr{1}{\tilde{\xi}} } \\
    &= \frac{ \sqr{3}{\tilde{\xi}} }{ \sqr{1}{\tilde{\xi}} }
      \frac{ \agl{1}{2}^2 }{ \agl{3}{1} }
\end{align}

## Notation

\begin{align}
  p_{\alpha\dot{\alpha}} &= \ld{\alpha} \ld{\dot{\alpha}}\\
  p^\mu &= \# \bams{\lambda}{\mu}{\tilde{\lambda}} \\
  &= \# \lu{\alpha} \ltu{\alpha} \tensor{\sigma}{^\mu_{\alpha\dot{\alpha}}}
\end{align}

where we are using the identity:

\begin{equation}
  P_{\alpha\dot{\alpha}} = p^\mu \sigma_{\mu\alpha\dot{\alpha}}
\end{equation}

We can use the completeness relation to expand \(p^\mu\) further:

\begin{align}
    p^\mu &= \# \lu{\beta} \ltu{\beta} \underbrace{ { \tensor{\sigma}{^\mu_{\beta\dot{\beta}}} \tensor{\sigma}{_{\mu\alpha\dot{\alpha}}}
    }}_{\qq{Completeness relation}}
\end{align}

Using the Completeness Relation, our free index \(\mu\) is summed over:

\begin{equation}
\tensor{\sigma}{^\mu_{\beta\dot{\beta}} } \cdot \tensor{\sigma}{_{\mu\alpha\dot{\alpha}} } = -2 \epsilon_{\alpha\beta}\epsilon_{\dot{\alpha}\dot{\beta}}
\end{equation}

Which leads us to:

\begin{equation}
\epsilon^\mu = \frac{1}{\sqrt{2}} \frac{\bams{\xi}{\mu}{k}}{\baa{\xi}{k}}
\end{equation}

<!-- #TODO: notation reference p 18 Plefka -->

## Feynman Rule Vertex

We multiply polarisation by each vertex. Hence momentum is conserved

### Steps

choose helicities (for same) Polarisation vector:

\begin{align}
  \epsilon^{\alpha\dot{\alpha}}_+(\lambda) &= -\sqrt{2}\frac{\ltu \mu^{\alpha}}{\baa{\lambda}{\mu}} \\
  \epsilon^{\alpha\dot{\alpha}}_-(\lambda) &= \sqrt{2}\frac{\lu{\alpha} \tilde{\mu}^{\dot{\alpha}}}{\bss{\lambda}{\mu}}
\end{align}

From here, we choose \(\epsilon\) such that \(\epsilon_i \cdot \epsilon_j = 0\)

Here we now have two different ways of representing the Vertex:

\begin{align}
  \td[a]{\alpha} b_\alpha \tu[c]{\alpha} d^\alpha = \bss{a}{c}\baa{d}{b}
  2 a^\mu b_\mu &= 2(a \cdot b)\\
  &= a^{\alpha\dot{\alpha}} b_{\alpha\dot{\alpha}}\\
  &= a^\alpha \tu[a]{\alpha} b_\alpha \td[b]{\alpha}\\
  &= \baa{a}{b} \bss{b}{a}
\end{align}

The phenomenologist way of writing:

\begin{align}
  a^\mu &= \frac{1}{2} \bams{a}{\mu}{a} \equiv \frac{1}{2} a^\alpha \tilde{a}^{\dot{\alpha}}\tensor{{\sigma_mu}}{_{\alpha\dot{\alpha}}}\\
  2(a \cdot b) &= 2 \frac{1}{2} \frac{1}{2} \bams{a}{\mu}{a}\bams{b}{\mu}{b}\\
  &= 2 \baa{a}{b}\bss{b}{a}
\end{align}


<!-- end:dissertation/log/2019.11.26.md -->


# BCFW recursion relations in Yang-Mills and Gravity

[@Plefka:2014aa, pp 35-39]

The BCFW recursion relations rely on an understanding of the behaviour of the
function \(A_n(z)\) in the complex \(z\) plane.

The derivation proceeds in three steps.

* First, the locations of the poles of \(A_n(z)\) are analyzed.
* Then, it is shown that the residues of the poles correspond to products of lower-point tree amplitudes.
* Finally, the large \(z\) behaviour of \(A_n(z)\) is determined.


Using complex analysis, we want to inspect the amplitude \(A_n(z)\). This is
because the sum of tree-level Feynman diagrams are gauge invariant, and
therefore when they are deformed by \(z\), they remain unchanged. Therefore we
can choose the Feynman gauge for the following discussion, without loss of
generality. It is clear that \(An(z)\) is a rational function of the
\(\ld{i}\),\(\lmt_i\) and \(z\). Moreover, \(An(z = 0)\) can only have poles where the
denominators of Feynman propagators become zero.

When inspecting a function using complex analysis, we try to simplify the
function such that there is only one variable in which to take into the complex
plane. Taking our scattering amplitude, we reduce it such that our only
variable becomes the moment of a particle:

\begin{equation}
  (p_i +p_{i+1} + p_{i+2} + \dots )^2 \equiv \ \dij
\end{equation}

Where we have the following quantities:


\begin{align}
  s &= (p_1 + p_2)^2\\
  t &= (p_2 + p_3)^2\\
  u &= (p_1 + p_1)^2 \\
  p_4 &= -p_1 -p_2 -p_3 -p_4  \Rightarrow A(S,t,u)
\end{align}

Gauge theory, n-point amplitudes. We now deform our amplitude in such a way that:

\begin{align}
  A(p_1, \dots, p_n) &\to \begin{cases}
    p_i \to p_i(z)\\
    p_j \to p_j(z)
  \end{cases}
\end{align}

Which leaves our amplitude in a state with only complexified momenta \(p_i(z) \qq{and} p_i(z)\)

\begin{align}
  \sA(z) &= A(-p_1, p_2, \cdots, p_i(z), \cdots, p_j(z), \cdots  p_n  )\\
  \sA(0) &= A(-p_1, p_2, \cdots,  p_n  )
\end{align}
.

This process can be particularly useful when exploring massless particles \(\left ( \sum p_i^2 = 0 \right )\); however this is not a constrain, and also works just as well with massive particles.

We are left with a transformation:

\begin{align}
  \quad p_i^\mu(z) &= p_i^\mu(z)+z\eta^\mu\\
  \quad p_j^\mu(z) &= p_j^\mu(z)-z\eta^\mu
\end{align}

With \(\eta =\) new complex momentum and \(z =\) its respective complex variable.

\begin{equation}
\left .
\begin{aligned}
    p_i^2(z) &= 0\\
    p_j^2(z) &= 0
\end{aligned} \quad
\right \} \qquad \forall z
\end{equation}

This leads to:

\begin{equation}
\left .
\begin{aligned}
  \quad p_i^2(z) &=& \cancelto{0}{p_i^2} +z^2\eta^2 + 2z(p_i \cdot \eta) & = 0\\
  \quad p_j^2(z) &=& \cancelto{0}{p_j^2} +z^2\eta^2 + 2z(p_j \cdot \eta) & = 0
\end{aligned}
\right \} \qquad \forall z
\end{equation}

This is useful for us, as we may thus choose \(\eta\) to be any value we would like; so to simplify this equation, we choose \(\eta = 0\), and we are left with:

\begin{align}
  2(p_i \cdot \eta) &= 0 \Leftrightarrow  \agl{i}{\eta} \sqr{\eta}{i}  =0\\
  2(p_j \cdot \eta) &= 0 \Leftrightarrow  \agl{j}{\eta} \sqr{\eta}{j}  =0
\end{align}

This is already a well known solution (from the 60s - find ref ), where we are keeping spacetime such that:

\begin{equation}
  \lmt = \pm \lambda^*
\end{equation}

Real minkowski:

\begin{equation}
  \agl{i}{\eta} = 0 \implies \sqr{i}{\eta} = 0 \qq{and:}
 \ld{\eta} \parallelsum \ld{i} \implies \lmtd{\eta} \parallelsum \lmtd{i}
\end{equation}

Taking complex Minkowski:

\begin{equation}
\left .
\begin{aligned}
  \underline{\agl{i}{\eta}} \udots{\(\sqr{\eta}{i}\)} \to 0\\
  \udots{\(\agl{j}{\eta}\)} \underline{\sqr{\eta}{j}} \to 0\\
\end{aligned} \right \} \qq{2 options}
\end{equation}

\begin{align}
  \qq{either} \eta &= \ld{i} \lmtd{j} \\
  \qq{or} \eta &= \ld{j} \lmtd{i}
\end{align}

Where implies that the we are left with:

\begin{align}
  2(p_i\cdot \eta) &= 0\\
  2(p_j\cdot \eta) &= 0
\end{align}

\[
\begin{aligned}
p_i \to p_i(z) &= p_i +z \eta\\
  &= \ld{i}\lmtd{i} + z\ld{i}\lmtd{j}\\
  &= \ld{i}(\lmtd{i} + z\lmtd{j})\\
  &\equiv \ld{i} \lthd{i}(z)\\
\end{aligned}
\qquad \qquad
\begin{aligned}
p_j \to p_j(z) &= p_j -z \eta\\
  &= \ld{j}\lmtd{j} - z\ld{i}\lmtd{j}\\
  &= (\ld{j} - z\ld{i})\lmtd{j}\\
  &\equiv \lh_j \lmtd{j}(z)
\end{aligned}
\taglabel{eq:complexmomentum}
\]

Leaving us with the two quantities:

\label{eq:shifted_amplitude}

\begin{align}
  \lthd{i}(z) &\equiv \lmtd{i} + z\lmtd{j} \\
  \lh_j(z)    &\equiv \ld{j} - z\ld{i}
\end{align}

Sometimes this is given the shorthand notation:

\begin{align}
  \lthd{i}(z) &\equiv  \sabrv{i}{j}\\
  \lh_j(z) &\equiv \asbrv{i}{j}
\end{align}

This leads us to being able to describe amplitudes in the simple form:

\begin{equation}
  \frac{C_1}{z-z_1} + \frac{C_2}{z-z_2} + \dots+ \frac{C_L}{z-z_L}
\end{equation}

This has the simplification that there are no constant terms \((\cancelto{0}{C}+\cancelto{0}{d_1 z_1}+\cancelto{0}{d_2 z^2_2})\). This means that we only need to know pieces of information:

1. Position of poles: \((z_1, z_2, \dots, z_L )\)
1. Residues \((L_1, L_2, \dots, L_L)\), leave us only with simple poles:

\begin{equation}
  \frac{1}{(x-x_0)^3}
\end{equation}

This is referred to as the pole to third power.

## Feynman Diagrams

What are the singularities:

\begin{center}  
  \input{assets/feynman01.tex}
\end{center}

Using the above, such that \(\vec{p}^2 = m^2\), and in the special massless case where \(m = 0\)

\begin{equation}
  \vec{p} = -p_1 -p_2 -p_3
\end{equation}

When we complexify this, we get:

\begin{align}
  \hat{p}(z) &= P + z\eta\\
  \hat{p}^2(z) =0 &= P^2 + 0 + 2z(P\cdot\eta)\\
  ??? \qquad \frac{z}{P}&= \frac{P^2}{2(P\cdot\eta)}
\end{align}

rewriting this:

\begin{align}
  \frac{1}{\hat{p}^2(z)} &= \frac{1}{p^2 + 2z(P\cdot z)}\\
  &= \frac{1}{2(p\cdot \eta)} \cdot \frac{1}{z+\underbrace{\frac{p^2}{2(p\cdot\eta)}}_{=\frac{1}{z-z_p}}}\\
  &= \sum_p \frac{C_p}{z-z_p}
\end{align}

Where we have used the substitution:

\begin{equation}
  z_p=\frac{p^2}{2(p\cdot\eta)}
\end{equation}

## Understanding Singularities

\begin{equation}
  A(1,2,\cdots,n) \xrightarrow{\quad p^2\to 0 \quad} \sum_n A_L\frac{i}{p^2}A_R
\end{equation}


<!-- #TODO: Feynman diagram  -->
\begin{center}  
  \input{assets/feynman02.tex}
\end{center}

Where:

\begin{align}
  P &= p_i +p_{i+1} + \cdots + p_{n} + p_1\\
  \hat{P} &= P + z\eta
\end{align}

Then:

\begin{align}
  z \to z_p &\equiv \frac{-p^2}{2(p\cdot \eta)}\\
  \hat{p}^2(z) &\to 0\\
  \therefore \frac{1}{\hat{p}^2(x)} &= \frac{1}{2(p\cdot \eta)[z-z_p]}
\end{align}

\begin{align}
  C_p \lim_{z\to z_p} \sA(z) &=  \cancel{z-z_p} \sum_h A_L (\hat{1}(z), \hat{p}^h, i, i+1, \cdots)  \frac{i}{2(p\cdot\eta)\cancel{(z-z_p)}} A_R(\hat{p}^h, \hat{2}(z), \cdots)\\
  & = A_L(\hat{i}, \hat{p}, \cdots)A_R(-\hat{p},\cdots) \\
  &= A_L(\hat{1}(z_p), \hat{p}, \cdots)A_R(-\hat{P},^{-h}, 2(z_p), \cdots)\\
  &= \sum_h \frac{A_L(1(z_p), \hat{p}^h) A_R(-\hat{p}^{-h},2(z(p)))}{2(p\eta)}\\
  &\equiv C_p
\end{align}

\begin{align}
  A(1,2,\cdots,n) &= \sum_n A_L \frac{i}{p^2} A_R\\
  \sA(0) &= \sum_p \sum_h \frac{A_L^h(z_p) A_R^{-h}(z_p)}{s(p\cdot\eta)(\cancel{z}-z_p)} i \\
  &= \sum_p \sum_h A_L^h(z_p)\frac{i}{p^2}A_R^{-h}(z_p) = A
\end{align}

For example:

<!-- #TODO: Feynman Diagrams -->
\begin{center}  
  \input{assets/feynman03.tex}
\end{center}

\begin{align}
  P &= p_4 + p_1, z = \frac{-1p^2}{2(p\cdot\eta)}\\
  P^2 &= (p_4 + p_1)^2 = \agl{4}{1}\sqr{1}{4}
\end{align}

\begin{equation}
  2p\eta \qq{such that}\eta : \begin{cases}
    \ld{1}\lmtd{2} \to 2(p\cdot \eta) &= \bams{1}{p}{2} \\
    \ld{2}\lmtd{1} \to 2(p\cdot \eta) &= \bams{2}{p}{1}
  \end{cases}
\end{equation}

# Three-point amplitudes and factorisation


<!-- begin:dissertation/log/2020.02.11.md -->

[@Plefka:2014aa, pp 15]

## General Notes:

 - \(\agl{\quad}{} \sqr{\quad}{}\)
 - \(\RR\) Minkowski implies vanishing of one implies vanishing of other

## Example of shifted poles

Looking at all possible diagrams:
(continued from last amplitude).

\begin{equation}
  A_{MHV} = (1^- 2^- 3^+ 4^+ 5^+) = \frac{
    \agl{1}{2}^4
  }{
    \agl{1}{2} \agl{2}{3} \agl{3}{4} \agl{4}{5} \agl{5}{1}
  }
\end{equation}

Special shifted movement.

In order to calculate this MHV amplitude, we need to find a way of simplifying this, by using the methods that we have been building up to so far. Lets try by first choosing vertexes \(5\) and \(1\) make a complex shift. We now have two choices:

\begin{equation}
\text{case }[1]
\begin{cases}
  \hat{\lambda}_5 &= \lambda_5 + z\lambda_1\\
  \hat{\tilde\lambda}_1 &= \tilde \lambda_1 - z\tilde \lambda_5\\
\end{cases}
\end{equation}

\begin{equation}
\text{case } [2]
\begin{cases}
  \hat{\lambda}_1 &= \lambda_1 + z\lambda_5\\
  \hat{\tilde\lambda}_5 &= \tilde \lambda_5 - z\tilde \lambda_1\\
\end{cases}
\end{equation}

### Case [1]:

First shift:

\begin{align}
  \agl{\hat 1}{2} &= \agl{1}{2} &\text{(Same)}\\
  \agl{2}{3}      &= \agl{2}{3}      &\text{(Same)}\\
  ...&& \text{(Same)}\\
  \underbrace{ \agl{4}{\hat 5} }_{\substack{\text{Changed to}\\ \text{give a pole}}}
  &= \agl{\lambda_4}{\lambda_5 + z\lambda_1} = \agl{4}{5} + z\agl{4}{1}\\
  \agl{\hat 5}{\hat 1} &= \agl{\hat 5}{1} =  \agl{5}{1} + z\agl{1}{1}\\
  &= \agl{\lambda_5+\lambda_1}{\lambda_1} = \agl{5}{1} +\cancelto{0}{\agl{1}{1}}\\
  &= \agl{5}{1}
\end{align}
This leaves us with the new shifted amplitude:

\begin{align}
  \sA(z) = \frac{ \agl{1}{2}^4
    }{
      \agl{1}{2} \cdots \agl{3}{4}\left (\agl{4}{5} + z\agl{5}{1} \right )\agl{5}{1}
    }
\end{align}

And this is precisely a simple pole:

\begin{align}
  \inv{\ag{4 \hat 5}} &= \inv{\ag{45} + z\ag{41}} = \inv{\ag{41}} \cdot \underbrace{
      \inv{z+ \frac{\ag{45}}{\ag{41}} }
    }_{
      \text{Position of the pole } z_p
    } \\
      z_p &= -\frac{\ag{45} }{ \ag{41} }
\end{align}

\begin{figure}

\begin{subfigure}[t]{.5\linewidth}
  \centering
  \input{assets/mhv_5particle1.tex}
  \caption{Amplitude corresponding to simple pole \(z_p\)}
\end{subfigure}
\begin{subfigure}[t]{.5\linewidth}
  \centering
  \input{assets/mhv_5particle1_alt.tex}
  \caption{Alternative possible arrangement, which goes to zero}
\end{subfigure}
\caption{Two possible MHV amplitudes for complex shifted system}
\end{figure}

### Case [2]:
Looking at the second shift:

\begin{align}
  \ag{\hat 1 2} &= \ag{12} + z\ag{52}\\
  ... (unchanged)\\
  \ag{\hat 5 \hat 1} &= \ag{5\hat 1} = \ag{51} + z\cancelto{0}{\ag{11}}\\
  &= \ag{51}
\end{align}

This leaves us with an Amplitude \(\sA(z) \approx z^3\), which at large \(z: (z-z_p)^3 \approx z^3\)

This example turns out to have no poles, and no physical coefficients, and we therefore cannot perform the recursion relation.

## Helicities:

\begin{figure}

\begin{subfigure}[t]{.5\linewidth}
  \centering
  \input{assets/mhv_5particle2.tex}
  \caption{Goes to zero, does not exist}
\end{subfigure}
\begin{subfigure}[t]{.5\linewidth}
  \centering
  \input{assets/mhv_5particle2_alt.tex}
  \caption{Goes to zero, why (next time)}
\end{subfigure}
\caption{MHV amplitude calculations when taking helicities into account}
\end{figure}

<!-- end:dissertation/log/2020.02.11.md -->
