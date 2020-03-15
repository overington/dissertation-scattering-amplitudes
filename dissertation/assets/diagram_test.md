---
title: "Feynman diagrams"
author: Samuel Overington | ID 170431121
abstract: |
  Experiment results
output:
  pdf_document:
    latex_engine: lualatex
    path: "/tmp/diagrams.pdf"
    toc: false
header-includes:
  \usepackage{lmodern,mathrsfs}
  \usepackage{sectsty}
  \usepackage[skipabove=\topskip,skipbelow=\topskip]{mdframed}
  \usepackage{yfonts}
  \usepackage{bbold}
  \usepackage{amssymb}
  \usepackage{amsmath}
  \usepackage{cancel,ulem}
  \usepackage[utf8]{inputenc}
  \usepackage{siunitx,physics}
  \usepackage{mattens}
  \usepackage{tensor}
  \usepackage{subcaption}
  \usepackage{tikz}
  \usepackage{tikz-feynman}
  \usepackage{subcaption}
  \input{custom-commands}
---

## mhv_5particle.tex

\begin{subfigure}[t]{.5\linewidth}
  \centering
  \input{assets/mhv_5particle2.tex}
  \caption{Amplitude corresponding to simple pole $z_p$}
\end{subfigure}
\begin{subfigure}[t]{.5\linewidth}
  \centering
  \input{assets/mhv_5particle2_alt.tex}
  \caption{Alternative possible arrangement, which goes to zero}
\end{subfigure}
\caption{Two possible MHV amplitudes for complex shifted system}
\end{figure}

<!--
\begin{subfigure}[t]{.5\linewidth}
  \centering
  \input{assets/mhv_5particle1.tex}
  \caption{Amplitude corresponding to simple pole $z_p$}
\end{subfigure}
\begin{subfigure}[t]{.5\linewidth}
  \centering
  \input{assets/mhv_5particle1_alt.tex}
  \caption{Alternative possible arrangement, which goes to zero}
\end{subfigure}
\caption{Two possible MHV amplitudes for complex shifted system}
\end{figure}
-->

## feynman01.tex
\input{feynman01.tex}
\input{feynman02.tex}
\input{feynman03.tex}
