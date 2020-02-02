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
header-includes:
  - \usepackage{amssymb}
  - \usepackage{amsmath}
  - \usepackage[utf8]{inputenc}
  - \usepackage{siunitx,physics}
  - \usepackage{pgfplots,pgfplotstable}
  - \pgfplotsset{compat=1.13}
---


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
