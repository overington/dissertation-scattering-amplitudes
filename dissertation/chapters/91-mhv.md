
<!-- begin:dissertation/log/2020.02.18.md -->

## Deriving simplest 4-point MHV amplitude

Starting from a negative helicity amplitude, with a result of

\begin{equation}
  A_{MHV}(1^- 2^- 3^+ 4^+) = \frac{\ag{12}^4}{\ag{12}\ag{23}\ag{34}\ag{41}}
\end{equation}

### Special shifted:

\begin{equation}
Case [1]
\left \{
\begin{aligned}
  \hat \lambda_4 &= \lambda_4 - z \lambda_1\\
  \hat{\tilde{\lambda}}_1 &= \tilde{\lambda}_1 + z\tilde{\lambda}_4
\end{aligned}
\right \}
=\bas{4}{1}
\end{equation}

For this, it can be easily seen that the poles come from \(\ag{34}\)

\begin{align}
  \ag{\hat 4 1} &= \ag{41} - \cancelto{0}{ z\ag{11} }\\
  &= \ag{41}
\end{align}  

Of the \(\overline{MHV}\) and

\begin{figure}

\begin{subfigure}[t]{.5\linewidth}
  \centering
  \input{assets/mhv_4particle3.tex}
  \caption{\(\overline{MHV}\)  amplitude goes to zero, does not exist, as all LHS are + and all RHS are -}\label{fig:mhv_4particle3}
\end{subfigure}
\begin{subfigure}[t]{.5\linewidth}
  \centering
  \input{assets/mhv_4particle3_alt.tex}
  \caption{\(MHV\) amplitude }\label{fig:mhv_4particle3_alt}
\end{subfigure}
\caption{\(MHV\) amplitude calculations. One of these must go to zero, as there will only be one pole}
\end{figure}

The From the two amplitudes above ( \(\overline{MHV}\)  fig \ref{fig:mhv_4particle3}, and \(MHV\) fig \ref{fig:mhv_4particle3_alt})). We can immediately see that using the combinations of \(+\) and \(-\) on \(A_L\) and \(A_R\); only one of the objects is physically possible. We will now use this to calculate the position of the pole from the \(MHV\) amplitude:

\begin{align}
  z_p &= (p_3 + \hat{p}_4 (z_p))^2\\
  &= 0\\
  &= \ag{3 \hat{4}} \sq{\hat{4} 3}\\
  &= \ag{3 \hat{4}} \sq{4 3} & \qq{NB no hat}\\
  &= 0\\
  &\implies \ag{34} - z\ag{31} = 0\\
  \therefore & z_p = \frac{\ag{34}}{\ag{31}} & \qq{pole}
\end{align}

This is an important finding, and shows that momentum \(\hat p\), will not generally be on-shell, but using this method, it keeps it on-shell.

### \(\hat{p}\):

\begin{align}
  A_R &= \frac{\ag{12}^3}{\ag{2 \hat{p} } \ag{\hat p 1}} &= \frac{\ag{12}^2}{\ag{2\hat p} \ag{\hat p 1}}\\
  A_L &= \frac{\sq{3 \hat 4}^3}{\sq{\hat 4 \hat p} \sq{\hat p 3}} &= \frac{\sq{34}^3}{\sq{4 \hat p} \sq{\hat p 3}}
\end{align}

\begin{equation}
  \frac{i}{(p_3 + p_4)^2} = \frac{\ag{12}^3}{\ag{2 \hat p}\ag{\hat p 1}} \cdot \frac{i}{\ag{34}\sq{43}} \cdot \frac{\sq{34}^3}{\sq{4 \hat p} \sq{\hat p 3}}
\end{equation}

For this, we have a possible pairing:

\begin{align}
  \ag{\hat p 1} \sq{4 \hat p} &= \sq{4 \hat p}\sq{\hat p 1}\\
  &= \bsma{4}{\hat p}{1}
\end{align}

Here we are looking for a way to keep out particles on shell, so we use the complex momentum, and find the correct particles momentum to work allow for this calculation. In this case, we are choosing \(\hat p = \hat{\lambda}_1 + z\lambda_2\):

\begin{align}
  &= \bsma{4}{\hat 1 + 2}{1}\\
  &= \bsma{4}{1 + 2}{1} = \overbrace{ \cancelto{0}{ \bsma{4}{1}{1} } }^{ \quad\text{Using }\sq{41}\ag{11} = 0 } + \bsma{4}{2}{1}\\
  \bsma{4}{2}{1} &= \sq{42}\ag{21}
\end{align}

What do we need? What are the spinors \(\lambda_p\) and \(\tilde{\lambda}_p\). We will change to a more systematic method of computation.

Only for the value of \(z_p\) should we keep the masses on shell.

\begin{equation}
  \hat p = \hat 1 + 2 = \lambda_p\tilde{\lambda}_p
\end{equation}

### \(\hat{1}\):

\begin{equation}
  \hat 1 + 2 = \lambda_1 (\underbrace{\tilde{\lambda}_1 + z_p \tilde{\lambda}_4}_{\substack{\text{Need to compute this.}\\ \text{Does it look like } \lambda \tilde{\lambda} ?} }) + \lambda_2 \tilde{\lambda}_2
\end{equation}

\begin{align}
  \tilde{\lambda}_1 + z_p \tilde{\lambda}_4 &= \tilde{\lambda}_1 + \frac{\ag{34}}{\ag{31}} \tilde{\lambda}_4\\
  &= \frac{\overbrace{\ag{31}\tilde{\lambda}_1}^{3} + \overbrace{\ag{34}\tilde{\lambda}_4}^{4}}{\ag{31}}\\
  &= \frac{
    \bra{3} (
      \overbrace{ p_1 + p+4}^{
        \substack{\text{Can look at}\\ \text{contributions from}\\ \text{other leg} }}
      )
      }{
        \ag{31}
      }
\end{align}

The momentum of each particle can also be seen as a sum from all the other contributing particles momenta. In this way we are able to write our legs in a different form: \(p_1 + p_4 = -p_2 -p_3\). And so continuing with this we substitute it back into the form we arrived at above:

\begin{align}
  (\tilde{\lambda}_1 + z_p \tilde{\lambda}_4 ) &= -\frac{\bra{3}(2+3)}{\ag{31}}\\
  &= \frac{-\ag{32}\tilde{\lambda}_2}{\ag{31}}
\end{align}

\(\hat p\) in a factorised form:

\begin{align}
  \hat p &= -\frac{\ag{32}}{\ag{31}}\lambda_1\tilde{\lambda}_2 +\lambda_2\tilde{\lambda}_2\\
  &= -\frac{\ag{32}}{\ag{31}}(\lambda_1 +\lambda_2)\tilde{\lambda}_2\\
  \ag{\hat p 1} &= \ag{21} \\
  \ag{2 \hat p} &= \underbrace{-\ag{21}}_{=\ag{12}} \frac{\ag{32}}{\ag{31}}
\end{align}

This leaves us with the following:

\begin{align}
  \sq{4 \hat p} &= \sq{42} \\
  \sq{\hat p 3} &= \sq{23}
\end{align}

Now putting everything together:

\begin{equation}
  \frac{
    \overbrace{\sq{34}^{\cancelto{2}{3}}}^{-} \overbrace{\ag{12}^{\cancelto{1}{3}}}^{-}
    }{
      \ag{34} \underbrace{\cancel{\sq{43}}}_{-} \sq{42} \sq{23} \cancel{\ag{12}} \frac{\ag{32}}{\ag{31}} \cancel{\ag{21}}
    } = \frac{
      \ag{12} \sq{34}^2 \ag{31}
      }{
        \ag{34} \sq{42} \sq{23} \ag{32}
      }
\end{equation}

This can be further simplified into our shifted pole:

\begin{equation}
  \bams{3}{4}{2} = \bams{3}{-1 - \cancelto{0}{2} - \cancelto{0}{3}}{2}
\end{equation}

Where we have used the face that \(\cancelto{0}{-2-3}\) because: \(\bams{3}{-2}{2} = 0\)

\begin{equation}
  \bams{3}{-1}{2} = -\ag{31} \sq{12}
\end{equation}

We then substitute this into the denominator to produce:

\begin{equation}
  \frac{
    \ag{12} \sq{34}^2 \cancel{\ag{31}}
    }{
      -\cancel{\ag{31}}\sq{12}\sq{23}\ag{32}
    }
\end{equation}

We can then group in the the terms in the denominator:

\begin{align}
  \sq{12} \ag{32} &= \sq{12}\ag{23} (-)\\
  &= \bsma{1}{2}{3}(-)\\
  &= \bsma{1}{-\cancel{1} - \cancel{3} -4}{3} (-)\\
  &= + \sq{14}\ag{43}
\end{align}

Multiplying both sides by \(\frac{\sq{34}}{\sq{34}}\)

<!-- #TODO: complete this equation, What does this mean here?? -->

\begin{equation}
  \ag{32}\sq{34} z\text{ bottom}
\end{equation}


\begin{align}
  &= -\ag{23} \sq{34}\\
  &= (-)(-) \ag{21} \sq{14}\\
  &= \frac{
    \cancelto{-}{\ag{12}} \sq{34}^2 \cancel{\ag{34}}\sq{34}
    }{
      - \cancel{\ag{31}} \sq{12} \sq{23} \cancel{\ag{21}} \sq{14}
    }\\
  \text{Finally } &= \frac{
    \sq{34}^3
    }{
    \sq{12}\sq{23}\sq{41}
    }
\end{align}

We can check this result in the other direction

\begin{align}
  \frac{\sq{34}^{\cancelto{2}{3}}
  }{
  \cancel{\sq{12}} \sq{23} \sq{41}
  } \cdot \frac{
    \ag{23} \cancel{\ag{34}} \ag{41}
    }{
    \ag{12}^{\cancelto{2}{3}}
    } \overset{?}{=} \pm \one
\end{align}

Now we pair up the legs with the momentum:

\begin{align}
  \sq{34} \ag{34} &= -2(p_3 \cdot p_4)\\
  \sq{12} \ag{12} &= -2(p_1 \cdot p_2) = -(p_1 + p_2)^2\\
  \sq{12} \ag{12} &= \sq{34} \ag{34}\\
  \ag{23} \sq{34} &= -\ag{21} \sq{14} = -\ag{12} \sq{41}\\
  \sq{34} \ag{41} &= -\sq{32} \ag{21} = -\sq{23} \ag{12}
\end{align}

Putting all this together:

\begin{align}
  = \frac{
    \ag{12} \sq{41} \sq{23} \ag{12}
    }{
    \ag{12}^2 \sq{23} \sq{41}
    } = \pm \one
\end{align}

<!--
   - ## Meeting Notes:
   - 
   - Slide equations:
   - 
   - \begin{align}
   -   p &= \lambda \tilde{\lambda}\\
   -   p_\mu \to p_{\alpha\dot{\alpha}} &= p_\mu \sigma^\mu\\
   -   \text{show } p_\mu p^\mu = 0\\
   -   p_{\alpha\dot{\alpha}} \equiv \lambda_\alpha \tilde{\lambda}_\alpha\\
   -   \det{(p_{\alpha\dot{\alpha}})} &= p^2
   - \end{align}  
   -->

<!-- end:dissertation/log/2020.02.18.md -->
## Deriving 3 point amplitudes
<!-- begin:dissertation/log/2020.03.11.md -->

<!--
   - - Derive \(\rm MHV\) amplitude
   - - Perform a shift for a 4-point amplitude.
   - - Negative helicity
   -->

\begin{equation}
  (\rm MHV) \to A(1^- 2^+ 3^- 4^+) = \frac{
    \ag{13}^4
  }{
    \ag{12}\ag{23}\ag{34} \ag{41}
  }
\end{equation}

We have the choice here:

\begin{equation}
\begin{cases}
  \hat{\tilde{\lambda}_i} &= \tilde{\lambda}_i + z \lambda_j\\
  \hat{\lambda}_j &= \lambda_j - z \lambda_i
\end{cases}
\end{equation}

Leaving us with:

\begin{equation}
  \ag{\hat 1 3} = \ag{13} + z\ag{23}
\end{equation}

We will now investigate the behaviour of this object at large \(z\), and begin by choosing \(i=1, j = 2\)

\begin{align}
  \hat{\tilde{\lambda}}_1 &= \tilde{\lambda}_1 + z \tilde{\lambda}_2\\
  \hat{\lambda}_2 &= \lambda_2 - z\lambda_1
\end{align}

Searching for the shift of \(\lambda_2\)

\begin{align}
  \ag{12} \to \ag{1 \hat 2} &= \ag{1 \lambda_2 - z\lambda_1}\\
  &= \ag{12} - \cancelto{0}{z\ag{11}} \\
  &= \ag{12}
\end{align}

The other leg:

\begin{equation}
  \ag{\hat 2 3} = \ag{23} - z\ag{13}
\end{equation}

This leaves us with the following amplitudes:

\begin{figure}

\begin{subfigure}[t]{.5\linewidth}
  \centering
  \input{assets/mhv_4particle4.tex}
  \caption{\,}\label{fig:mhv_4particle4}
\end{subfigure}
\begin{subfigure}[t]{.5\linewidth}
  \centering
  \input{assets/mhv_4particle4_alt.tex}
  \caption{\,}\label{fig:mhv_4particle4_alt}
\end{subfigure}
\caption{Amplitude example}
\end{figure}

 - In real Minkowski, three point doesn't exist
 - Only angle or square brackets can be zero, but not at the same time.
 - Two particle invariance (2 half + 3 squares )

Referring to Figure \ref{fig:mhv_4particle4}, we can see that it is null at the polling \(z\), and therefore the product of the brackets must go to zero:

\begin{equation}
 \underbrace{
    \ag{\hat 2 3 }
   }_{\text{Must equal }0} \sq{32} = 0 = (\hat{p}_2 + p_3)^2
\end{equation}

 The angle brackets (\(\ag{\hat 2 3}\)) must be equal to zero because of the line between the two shells. The condition for blobs to be on-shell are zero

 This means that the right hand leg in Figure \ref{fig:mhv_4particle4} must go to zero:

\begin{equation}
 \frac{
   \ag{3 \hat p }^3
   }{
     \ag{\hat 2 3}\ag{\hat p 2}
   } = \frac{0^3}{0^2}
\end{equation}

 This shows us that the amplitude found in Figure \ref{fig:mhv_4particle4} is
 not physically possible, as the amplitude is only made of square brackets
 (\(+-+\)). This could be zero if square is 0, but square brackets can't be
 zero. Because we are shifting the particle \(\lambda_2\). \(\rm MHV\) \(2^-
 1^+\) means angle brackets. One of these will always go to zero.

##  Example \(\rm MHV\) diagram with brackets


\begin{figure}
  \centering
  \input{assets/mhv_4particle4_alt.tex}
  \caption{Non vanishing Diagram}\label{fig:mhv_4particle4_alt_nonvanishing}
\end{figure}

To write this amplitude using the bracket notation of \ref{def:bracket_notation}:

\begin{align}
A_L &= \frac{
    \ag{\hat 1 \hat p}^3
    }{
      \ag{\hat p 4} \ag{4 \hat 1}
    } \underbrace{
      = \frac{ \ag{1 \hat p}^3 }{ \ag{\hat p 4} \ag{4 1} }
      }_{
       \text{because \(\lambda_1\) is not shifted}
       }
\end{align}

And the amplitude on the right is \(\overline{\rm MHV}\):

\begin{equation}
  A_R = \frac{
    \sq{\hat{p} \hat{2}}^3
    }{
      \sq{3 \hat p} \sq{\hat 2 p}
    } = \frac{
      \sq{\hat p 2}
      }{
        \sq{3 \hat p} \sq{23}
      }
\end{equation}

\begin{equation}
  A(1^- 2^+ 3^- 4^+) = \frac{
    \ag{1 \hat p}^3
  }{
    \ag{\hat p 3} \ag{41}
} \frac{i}{p^2_{23}}
\frac{
  \sq{\hat p 2}
  }{
    \sq{3 \hat p} \sq{23}
  }
\end{equation}

Where \(p_{23}\) is the momentum between \(A_L\) and \(A_R\)

\begin{equation}
  p_{23}^2 = (p_2 + p_3)^2 = \ag{23}\sq{32}
\end{equation}

Putting this all together, all we need to understand is \(\hat{p}\)

We have to find the spinors of \(\hat{p}\) at the positions of the poles:

\begin{equation}
  \hat{p} = \lambda_{\hat{p}}\tilde{\lambda}_{\hat{p}}
\end{equation}

The position of the pole in z is found by requiring \(\hat{p}\) to be on-shell.


\begin{figure}[t]
  \centering
  \input{assets/mhv_4particle4_altnonvanishing.tex}
  \caption{Non vanishing Diagram}\label{fig:mhv_4particle4_alt_nonvanishing}
\end{figure}

Where we have two equivalent conditions:

\begin{align}
  \ag{\hat 2 3}\sq{32} &= 0\\
  \ag{41} \sq{\hat 1 4} &= 0
\end{align}

From these two equations, we have two possibilities:

\begin{align}
  \ag{\hat 2 3} &= 0 \implies &\ag{23} - z\ag{13} = 0\\
  \sq{\hat 1 4} &= 0 \implies &\sq{14} + z\sq{s4} = 0
\end{align}

And solving these two equations simultaneously:

\begin{equation}
  z = \frac{\ag{23}}{\ag{13}} \qquad z = \frac{-\sq{14}}{\sq{24}}
\end{equation}

Here the two \(z\) are the same, so we have found two equations that are equal.  When two mathematical objects are equal, we can divide one by the other and their ratio must equal one:

\begin{equation}
  - \frac{\ag{23}}{\ag{13}} \cdot \frac{\sq{24}}{\sq{14}} \eqq 1
\end{equation}

Let us interrogate the ratio a little further, and we can replace with the momenta \(p\)

\begin{align}
  &\frac{(-) \bsma{4}{2}{3}
  }{
      \bsma{4}{
        \underbrace{ 1 }_{p_1} }{3}
    } &= - \frac{
    \bsma{4}{2}{3}
    }{
      (-)\bsma{4}{2+ 3+4}{3}
    }\\
   &\qquad p_1 = -p_2 -p_3 - p_4   
  &&(-)\bsma{4}{2+ \cancel{3}+\cancel{4}}{3}
\end{align}

Summary:
We have two values of \(z\), which look different, but are actually the same. We now have to find \(\ag{\,}\sq{\,}\)

\begin{align}
  \hat{p} &= \hat{p}_2 + p_3 &= \lambda_2\tilde{\lambda}_2 - z\lambda_1\tilde{\lambda}_2 + \lambda_3 \tilde{\lambda}_3\\
  &= (\lambda_2 - z\lambda_1)\tilde{\lambda}_2+ \lambda_3\tilde{\lambda}_3
\end{align}

Using in our \(z = -\frac{\sq{14}}{\sq{24}}\), and \(\hat{\lambda}_2=\lambda_2 + \frac{\sq{14}}{\sq{24}}\lambda_1\)

\begin{align}
  \hat{\lambda}_2 &= \lambda_2 + \frac{\sq{14}}{\sq{24}}\lambda_1\\
  &= \frac{
    \lambda_2\sq{24} + \lambda_1 \sq{14}
    }{
      \sq{24}
    }\\
  \text{which is the same as } &= \frac{
    (p_2 + p_1)|\, 4\, ]
    }{
      \sq{24}
    }\\
    \text{with momentum conservation }& = \frac{
      -(p_3 + p_4) |\, 4\, ]
      }{
        \sq{24}
      } \qq{(\(p_4\) next to 4 gives 0)}\\
      \text{becoming } &= -\lambda_3 \frac{\sq{34}}{\sq{24}}
\end{align}

Finally:

\begin{equation}
  \hat{\lambda}_2 = \lambda_3 \frac{\sq{34}}{\sq{24}}
\end{equation}

Plugging this back into the original expression, this becomes:

\begin{align}
  \hat{p} &= \underbrace{
    \lambda_3
    }_{\lambda_{\hat{p}}}
       \underbrace{
      \left [
        -\frac{\sq{34}}{\sq{24}} \tilde{\lambda}_2 + \tilde{\lambda}_3
      \right ]
        }_{\tilde{\lambda}_{\hat{p}}}\\
  \lambda_{\hat{p}} &= \lambda_3\\
  \tilde{\lambda}_{\hat{p}} &= \tilde{\lambda}_3 - \frac{\sq{34}}{\sq{24}} \tilde{\lambda}_2
\end{align}


Collecting the terms we arrive at our expected result:

\begin{align}
  i \frac{
    \ag{13}^4
  }{
    \ag{12}\ag{23}\ag{34}\ag{41}
  }
\end{align}

<!--
   - --- 
   - Taking these spinors written in BCFW form:
   -->

<!-- end:dissertation/log/2020.03.11.md -->
