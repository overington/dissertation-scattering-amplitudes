<!--
@import "assets/custom.md"
 -->

[@Plefka:2014aa, pp 35-39]

The BCFW recursion relations rely on an understanding of the behaviour of the function $A_n(z)$ in the complex $z$ plane.

The derivation proceeds in three steps.

* First, the locations of the poles of $A_n(z)$ are analyzed.]
* Then, it is shown that the residues of the poles correspond to products of lower-point tree amplitudes.
* Finally, the large $z$ behaviour of $A_n(z)$ is determined.


Using complex analysis, we want to inspect the amplitude $A_n(z)$. This is because the sum of tree-level Feynman diagrams are gauge invariant, and therefore when they are deformed by $z$, they remain unchanged. Therefore we can choose the Feynman gauge for the following discussion, without loss of generality. It is clear that $An(z)$ is a rational function of the $\ld{i}$,$\lmt_i$ and $z$. Moreover, $An(z = 0)$ can only have poles where the denominators of Feynman propagators become zero.

When inspecting a function using complex analysis, we try to simplify the function such that there is only one variable in which to take into the complex plane. Taking our scattering amplitude, we reduce it such that our only variable becomes the moment of a particle:

$$
  (p_i +p_{i+1} + p_{i+2} + \dots )^2 \equiv \ \dij
$$

Where we have the following quantities:

$$
\begin{aligned}
  S &= (p_1 + p_2)^2\\
  t &= (p_2 + p_3)^2\\
  u &= (p_1 + p_1)^2 \\
  p_4 &= -p_1 -p_2 -p_3 -p_4  \Rightarrow A(S,t,u)
\end{aligned}
$$

Gauge theory, n-point amplitudes. We now deform our amplitude in such a way that:

$$
\begin{aligned}
  A(p_1, \dots, p_n) &\to \begin{cases}
    p_i \to p_i(z)\\
    p_j \to p_j(z)\\
  \end{cases}\\
\end{aligned}
$$

Which leaves our amplitude in a state with only complexified momenta $p_i(z) \qq{and} p_i(z)$

$$
\begin{aligned}
  \sA(z) &= A(-p_1, p_2, \cdots, p_i(z), \cdots, p_j(z), \cdots  p_n  )\\
  \sA(0) &= A(-p_1, p_2, \cdots,  p_n  )
\end{aligned}
$$.

This process can be particularly useful when exploring massless particles $\left ( \sum p_i^2 = 0 \right )$; however this is not a constrain, and also works just as well with massive particles.

We are left with a transformation:
$$
\begin{aligned}
  \quad p_i^\mu(z) &= p_i^\mu(z)+z\eta^\mu\\
  \quad p_j^\mu(z) &= p_j^\mu(z)-z\eta^\mu\\
\end{aligned}
$$

With $\eta =$ new complex momentum and $z =$ its respective complex variable.

$$
\left .
\begin{aligned}
    p_i^2(z) &= 0\\
    p_j^2(z) &= 0
\end{aligned} \quad
\right \} \qquad \forall z
$$

This leads to:

$$
\left .
\begin{aligned}
  \quad p_i^2(z) &=& \cancelto{0}{p_i^2} +z^2\eta^2 + 2z(p_i \cdot \eta) & = 0\\
  \quad p_j^2(z) &=& \cancelto{0}{p_j^2} +z^2\eta^2 + 2z(p_j \cdot \eta) & = 0
\end{aligned}
\right \} \qquad \forall z
$$

This is useful for us, as we may thus choose $\eta$ to be any value we would like; so to simplify this equation, we choose $\eta = 0$, and we are left with:

$$
\begin{aligned}
  2(p_i \cdot \eta) &= 0 &\Leftrightarrow & \agl{i}{\eta} \sqr{\eta}{i} & =0\\
  2(p_j \cdot \eta) &= 0 &\Leftrightarrow & \agl{j}{\eta} \sqr{\eta}{j} & =0
\end{aligned}
$$

This is already a well known solution (from the 60s - find ref ), where we are keeping spacetime such that:

$$
  \lmt = \pm \lambda^*
$$

Real minkowski:

$$
  \agl{i}{\eta} = 0 \implies \sqr{i}{\eta} = 0 \qq{and:}
 \ld{\eta} \parallelsum \ld{i} \implies \lmtd{\eta} \parallelsum \lmtd{i}
$$

Taking complex Minkowski:
$$
\left .
\begin{aligned}
  \underline{\agl{i}{\eta}} \udots{$\sqr{\eta}{i}$} \to 0\\
  \udots{$\agl{j}{\eta}$} \underline{\sqr{\eta}{j}} \to 0\\
\end{aligned} \right \} \qq{2 options}
$$

$$
\begin{aligned}
  \eta &= \ld{i} \lmtd{j} && \qq{or} \eta &= \ld{j} \lmtd{i}
\end{aligned}
$$
Where implies that the we are left with:
$$
\begin{aligned}
  2(p_i\cdot \eta) &= 0\\
  2(p_j\cdot \eta) &= 0
\end{aligned}
$$

$$
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
$$

Leaving us with the two quantities:

\label{eq:shifted_amplitude}

$$
\begin{aligned}
  \lthd{i}(z) &\equiv \lmtd{i} + z\lmtd{j} \\
  \lh_j(z)    &\equiv \ld{j} - z\ld{i}
\end{aligned}
$$

Sometimes this is given the shorthand notation:

$$
\begin{aligned}
  \lthd{i}(z) &\equiv  \sabrv{i}{j}\\
  \lh_j(z) &\equiv \asbrv{i}{j}
\end{aligned}
$$

This leads us to being able to describe amplitudes in the simple form:

$$
  \frac{C_1}{z-z_1} + \frac{C_2}{z-z_2} + \dots+ \frac{C_L}{z-z_L}
$$

This has the simplification that there are no constant terms $(\cancelto{0}{C}+\cancelto{0}{d_1 z_1}+\cancelto{0}{d_2 z^2_2})$. This means that we only need to know pieces of information:

1. Position of poles: $(z_1, z_2, \dots, z_L )$
1. Residues $(L_1, L_2, \dots, L_L)$, leave us only with simple poles:
$$
  \frac{1}{(x-x_0)^3}
$$

This is referred to as the pole to third power.

## Feynman Diagrams
What are the singularities:

\begin{center}  
  \input{assets/feynman01.tex}
\end{center}

Using the above, such that $\vec{p}^2 = m^2$, and in the special massless case where $m = 0$

$$
  \vec{p} = -p_1 -p_2 -p_3
$$

When we complexify this, we get:
$$
\begin{aligned}
  \hat{p}(z) &= P + z\eta\\
  \hat{p}^2(z) =0 &= P^2 + 0 + 2z(P\cdot\eta)\\
  ??? \qquad \frac{z}{P}&= \frac{P^2}{2(P\cdot\eta)}
\end{aligned}
$$

rewriting this:

$$
\begin{aligned}
  \frac{1}{\hat{p}^2(z)} &= \frac{1}{p^2 + 2z(P\cdot z)}\\
  &= \frac{1}{2(p\cdot \eta)} \cdot \frac{1}{z+\underbrace{\frac{p^2}{2(p\cdot\eta)}}_{=\frac{1}{z-z_p}}}\\
  &= \sum_p \frac{C_p}{z-z_p}
\end{aligned}
$$

Where we have used the substitution: $z_p=\frac{p^2}{2(p\cdot\eta)}$

## Understanding Singularities

$$
  A(1,2,\cdots,n) \xrightarrow{\quad p^2\to 0 \quad} \sum_n A_L\frac{i}{p^2}A_R
$$


<!-- #TODO: Feynman diagram  -->
\begin{center}  
  \input{assets/feynman02.tex}
\end{center}

Where:
$$
\begin{aligned}
  P &= p_i +p_{i+1} + \cdots + p_{n} + p_1\\
  \hat{P} &= P + z\eta
\end{aligned}
$$

Then:
$$
\begin{aligned}
  z \to z_p &\equiv \frac{-p^2}{2(p\cdot \eta)}\\
  \hat{p}^2(z) &\to 0\\
  \therefore \frac{1}{\hat{p}^2(x)} &= \frac{1}{2(p\cdot \eta)[z-z_p]}\\
\end{aligned}
$$

$$
\begin{aligned}
  C_p \lim_{z\to z_p} \sA(z) &=  \cancel{z-z_p} \sum_h A_L (\hat{1}(z), \hat{p}^h, i, i+1, \cdots)  \frac{i}{2(p\cdot\eta)\cancel{(z-z_p)}} A_R(\hat{p}^h, \hat{2}(z), \cdots)\\
  & = A_L(\hat{i}, \hat{p}, \cdots)A_R(-\hat{p},\cdots) \\
  &= A_L(\hat{1}(z_p), \hat{p}, \cdots)A_R(-\hat{P},^{-h}, 2(z_p), \cdots)\\
  &= \sum_h \frac{A_L(1(z_p), \hat{p}^h) A_R(-\hat{p}^{-h},2(z(p)))}{2(p\eta)}\\
  &\equiv C_p
\end{aligned}
$$

$$
\begin{aligned}
  A(1,2,\cdots,n) &= \sum_n A_L \frac{i}{p^2} A_R\\
  \sA(0) &= \sum_p \sum_h \frac{A_L^h(z_p) A_R^{-h}(z_p)}{s(p\cdot\eta)(\cancel{z}-z_p)} i \\
  &= \sum_p \sum_h A_L^h(z_p)\frac{i}{p^2}A_R^{-h}(z_p) = A
\end{aligned}
$$

For example:

<!-- #TODO: Feynman Diagrams -->
\begin{center}  
  \input{assets/feynman03.tex}
\end{center}

$$
\begin{aligned}
  P &= p_4 + p_1, z = \frac{-1p^2}{2(p\cdot\eta)}\\
  P^2 &= (p_4 + p_1)^2 = \agl{4}{1}\sqr{1}{4}
\end{aligned}
$$

$$
  2p\eta \qq{such that}\eta : \begin{cases}
    \ld{1}\lmtd{2} \to 2(p\cdot \eta) &= \left < 1 | p | 2 \right ] \\
    \ld{2}\lmtd{1} \to 2(p\cdot \eta) &= \left < 2 | p | 1 \right ] \\
  \end{cases}
$$
