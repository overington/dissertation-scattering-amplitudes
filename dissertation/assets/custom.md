$$
\require{physics}
$$
<!--
$$
\makeatletter
\newlength\xvec@height%
\newlength\xvec@depth%
\newlength\xvec@width%
\newcommand{\xvec}[2][]{%
  \ifmmode%
    \settoheight{\xvec@height}{$#2$}%
    \settodepth{\xvec@depth}{$#2$}%
    \settowidth{\xvec@width}{$#2$}%
  \else%
    \settoheight{\xvec@height}{#2}%
    \settodepth{\xvec@depth}{#2}%
    \settowidth{\xvec@width}{#2}%
  \fi%
  \def\xvec@arg{#1}%
  \def\xvec@dd{:}%
  \def\xvec@d{.}%
  \raisebox{.2ex}{\raisebox{\xvec@height}{\rlap{%
    \kern.05em
    \begin{tikzpicture}[scale=1]
    \pgfsetroundcap
    \draw (.05em,0)--(\xvec@width-.05em,0);
    \draw (\xvec@width-.05em,0)--(\xvec@width-.15em, .075em);
    \draw (\xvec@width-.05em,0)--(\xvec@width-.15em,-.075em);
    \ifx\xvec@arg\xvec@d%
      \fill(\xvec@width*.45,.5ex) circle (.5pt);%
    \else\ifx\xvec@arg\xvec@dd%
      \fill(\xvec@width*.30,.5ex) circle (.5pt);%
      \fill(\xvec@width*.65,.5ex) circle (.5pt);%
    \fi\fi%
    \end{tikzpicture}%
  }}}%
  #2%
}

\let\stdvec\vec
\renewcommand{\vec}[1]{\xvec[]{#1}}
$$
 -->
$$
\newcommand{\dvec}[1]{\dot{\vec{#1}}}
\newcommand{\ddvec}[1]{\ddot{\vec{#1}}}
\newcommand{\pdv}[1]{\frac{\partial #1}{\partial x}}
$$
$$
\makeatother
\newcommand{\udots}[1]{%
    \tikz[baseline=(todotted.base)]{
        \node[inner sep=1pt,outer sep=0pt] (todotted) {#1};
        \draw[densely dotted] (todotted.south west) -- (todotted.south east);
    }%
}%
\newcommand\eqq{\mathrel{\overset{\makebox[0pt]{\mbox{\small ?}}}{=}}}
\newcommand\abs[1]{\lvert #1 \rvert}
$$

$$
\newcommand{\agl}[2]{\langle#1 \, #2 \rangle} %%%% Some definition for the spinor braket in four and six dimensions %%%%%
\newcommand{\sqr}[2]{\lbrack #1 \, #2 \rbrack}
\newcommand{\aglb}[2]{\langle #1 \, #2 \rangle}
\newcommand{\sabrv}[2]{[#1\,#2\rangle}
\newcommand{\asbrv}[2]{\langle#1\,#2]}
\newcommand{\sabr}[4]{[#1_{\dot{#2}}\, #3_{#4}\rangle}
\newcommand{\asbr}[4]{\langle#1_{#2} \, #3_{\dot{#4}}]}
\newcommand{\afour}[8]{\langle#1_{#2}\, #3_{#4}\, #5_{#6}\, #7_{#8} \rangle}
\newcommand{\bfour}[8]{[#1_{\dot{#2}}\, #3_{\dot{#4}}\, #5_{\dot{#6}}\, #7_{\dot{#8}}]}
\newcommand{\lu}[1]{\lambda^{#1}}
\newcommand{\ltu}[1]{\tilde{\lambda}^{\dot{#1}}}
\newcommand{\lthd}[1]{\hat{\tilde{\lambda}}_{#1}}
\newcommand{\lh}{\hat{\lambda}}
\newcommand{\ld}[1]{\lambda_{#1}}
\newcommand{\lmt}{\tilde{\lambda}}
\newcommand{\lmtd}[1]{\tilde{\lambda}_{#1}}
\newcommand{\ltd}[1]{\tilde{\lambda}_{\dot{#1}}}
\newcommand{\muu}[1]{\mu^{#1}}
\newcommand{\mtu}[1]{\tilde{\mu}^{\dot{#1}}}
\newcommand{\mud}[1]{\mu_{#1}}
\newcommand{\mtd}[1]{\tilde{\mu}_{\dot{#1}}}
\renewcommand{\L}{\mathcal{L}} %%%% Some useful character %%%%
\newcommand{\Lg}{\text{L}}
\renewcommand{\H}{\hat{H}}
\newcommand{\sgn}{\text{sgn}}
\newcommand{\one}{\mathbb{1}}
\newcommand{\RR}{\mathbb{R}}
\newcommand{\CC}{\mathbb{C}}
\newcommand{\cA}{\mathcal{A}}
\newcommand{\cN}{\mathcal{N}}
\newcommand{\cL}{\mathcal{L}}
\newcommand{\cO}{\mathcal{O}}
\newcommand{\tb}{\tilde{b}}
\newcommand{\dij}{\delta_{ij}}
\newcommand{\sA}{\mathscr{A}}
\newcommand{\parallelsum}{\mathbin{/\mkern-5mu/}}
$$
<!--
$$
  \RR \dvec{x}
$$
-->