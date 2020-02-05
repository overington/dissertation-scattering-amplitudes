---
title: "test"
author: Samuel Overington | ID 170431121
numbersections: true
output:
  pdf_document:
    template: assets/template.tex
    path: "../thesis_output/test.pdf"
    toc: true
    toc_depth: 3
header-includes: |
  \usepackage{lmodern,mathrsfs}
  \usepackage{sectsty}
  \usepackage{yfonts}
  \usepackage{bbold}
  \usepackage{amssymb}
  \usepackage{amsmath}
  \usepackage{cancel}
  \usepackage[utf8]{inputenc}
  \usepackage{siunitx,physics}
  \usepackage{mattens}
  \usepackage{tensor}
  \usepackage[compat=1.0.0]{tikz-feynman}
  \usepackage{feynmp}
---

# FEYNMP

\begin{fmffile}{simple}
  \begin{fmfgraph}(40,25)
    \fmfleft{i1,i2}
    \fmfright{o1,o2}
    \fmf{fermion}{i1,v1,o1}
    \fmf{fermion}{i2,v2,o2}
    \fmf{photon}{v1,v2}
  \end{fmfgraph}
\end{fmffile}

# Testing `Tikz-Feynman` diagrams

\feynmandiagram [horizontal=a to d] {
  a -- [fermion,edge label=$N$] b [dot] -- [double,with arrow=0.5,edge label=$\mathcal{R}$] c -- [fermion,edge label=$N'$] d,
  i -- [charged boson,edge label=$W^i$] b,
  c -- [charged scalar,edge label=$\pi$] o,
};

<!--
\feynmandiagram [horizontal=a to b] {
  a -- [photon] b,
  i1 -- [fermion] a -- [fermion] i2,
  f1 -- [fermion] b -- [fermion] f2,
};
 -->
<!--
\feynmandiagram [horizontal=v1 to v2]{
  i1 -- [photon, momentum=$p_1$] v1,
  i2 -- [photon, momentum=$p_2$] v1,
  v1 -- [photon, momentum=$p_L$] v2,
  v2 -- [photon, momentum=$p_3$] o1,
  v2 -- [photon, momentum=$p_4$] o2,
};
 -->
<!--
i1 [particle=\(e^{-}\)] -- [fermion] a -- [fermion] i2 [particle=\(e^{+}\)],
a -- [photon, edge label=\(\gamma\)] b,
f1 [particle=\(\mu^{-}\)] -- [fermion] b -- [fermion] f2 [particle=\(\mu^{+}\)],  
 -->

# Testing abreviated brackets  

$$
  \lthd{i}(z) \equiv  \sabrv{i}{j}\\
  \sabr{\lambda}{i}{\psi}{j}
$$

Testing Underline:
$$
\begin{aligned}
  \underline{\agl{i}{\eta}} \udots{$\sqr{\eta}{i}$} \to 0
\end{aligned}
$$

<!--
  \underline{\agl{i}{\eta}} \udots{$\sqr{\eta}{i}$} \to 0
  \udots{$\agl{j}{\eta}$} \underline{\sqr{\eta}{j}} \to 0\\

  \underline{\agl{i}{\eta}} \dotuline{\sqr{\eta}{i}} \to 0\\
  \dotuline{\agl{j}{\eta}} \underline{\sqr{\eta}{j}} \to 0
-->


# testing cancel

$$
\left \{
\begin{aligned}
  \quad p_i^2(z) &=& \cancelto{0}{p_i^2} +z^2\eta^2 + 2z(p_i \cdot \eta) & = 0\\
  \quad p_j^2(z) &=& \cancelto{0}{p_j^2} +z^2\eta^2 + 2z(p_j \cdot \eta) & = 0
\end{aligned}
\right .
$$

$$
  testing \sA
$$

# ch 1
(@eqfirst) $E = mc^2$

$$
  \L
$$

\begin{equation}
  \label{eq:the_label}
  \gamma = \frac{1}{\sqrt{1-v^2/c^2}}
\end{equation}

# Section 2

$$
\begin{aligned}
  \L = this
\end{aligned}
$$

(@eqsecond) $\vec{a}\cdot\vec{b} = \abs{a}\abs{b}\cos(\theta)$

\begin{equation}
  \label{eq:the2_label}
  \gamma = \frac{1}{\sqrt{1-v^2/c^2}}
\end{equation}

\begin{equation}
  \label{eq:the3_label}
  \gamma = \frac{1}{\sqrt{1-v^2/c^2}}
\end{equation}

<!--
@import "assets/custom.md"
-->
