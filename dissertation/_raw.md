---
title: "DRAFT: raw Computating On-Shell amplitude using BCFW"
author:
  - name: Samuel Overington | ID 170431121
    affiliation: |
      School of Physics and Astronomy,
      Queen Mary University of London
numbersections: true
fontsize: 12pt
geometry: margin=2cm
bibliography: bibliography-scattering_amplitudes.bib
header-includes: |
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
  \usepackage{tikz}
  \usepackage{tikz-feynman}
output:
  pdf_document:
    latex_engine: lualatex
    template: /Users/samuel/Documents/devices/2019-20/project/dissertation/assets/template.tex
    path: /thesis_output/draft_raw_amplitudes.pdf
    toc: true
    toc_depth: 3
---
<!--
@import "assets/custom.md"
 -->

Why $x_{\dot{\alpha}\alpha}$? What is this object?

For the Lorenz transformation $P^\mu \to \tensor{\Lambda}{^\mu_\nu} \rho^\nu \equiv \rho^{\prime \nu}$:
$$
\begin{aligned}
  P_{\alpha \dot{\alpha}} &= x \rho^{\mu}\sigma_{\mu \alpha \dot{\alpha}}\\
  &= MpM^\dagger
\end{aligned}
$$

Using $P^mu\rho_\mu = \det{p}$, the following can be obtained:
$$
\begin{aligned}
  \det{MpM^\dagger} &= \det{p}\\
  \det{M}\det{p}\det{M^\dagger} &= \det{p}\\
  \det{M} &= 1
\end{aligned}
$$

Expanding on this, the can arrive at the following explanation:
$$
  P_{\alpha \dot{\alpha}} = \ld{\alpha}\ld{\dot{\alpha}} = \begin{pmatrix}
    \rho^0 +\rho^3 & \rho^1 - i\rho^2\\
    \rho^1 + i\rho^2 & \rho^0 - \rho^2
\end{pmatrix},
  \rho^0 = \rho_{1\dot{1}}
$$

This makes the ($\lambda_{\alpha \dot{\alpha}}$) an operation.

$$
  \underbrace{SO(1,3)}_{\qq{group}} \to \underbrace{SL(2, \CC)\times SL(2,\CC)}_{\qq{group} \mathbb{Z_2}}
$$

A transformation is a representation of this group; **Spinors**:

\begin{definition}[Spinor Group]
The spinor group is a transformation as follows:
$$
\begin{aligned}
  \tensor{\Psi}{^{\prime}_\alpha} &= \tensor{M}{_\alpha^\beta}\tensor{\Psi}{_\beta}\\
  \tensor{\bar{\Psi}}{^{\prime}_{\dot{\alpha}}} &= \tensor{M}{_{\dot{\alpha}}^{\dot{\beta}}}\tensor{\bar{\Psi}}{_\beta}\\
\end{aligned}
$$

Such that $\tensor{M}{^0_0}$ belongs to $SL(2,\CC)$, with $\det{M}=\one$
\end{definition}

The object which do not transform under $\tensor{\Psi}{^{\prime}_\alpha}, \tensor{\bar{\Psi}}{^{\prime}_{\dot{\alpha}}}$ build the objects which are invariant under Lorenz group.

# Levi Cevita symbol:

$$ \epsilon_{\alpha \beta} = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} $$

How does this transform with $M$

$$
  \epsilon_{\alpha\beta} \to \\
  \tensor{M}{_\alpha^{\alpha^{\prime}}} \\
  \tensor{M}{_\beta^{\beta^{\prime}}}\\
  \epsilon_{\alpha^{\prime} \beta^{\prime}}
$$
