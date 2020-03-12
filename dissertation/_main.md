---
title: "(DRAFT) Scattering Amplitudes"
subtitle:  Novel new methods of calculation, using BCFW recursion
date: \today
institute: |
  School of Physics and Astronomy,
  Queen Mary University of London
numbersections: true
titlepage: true,
titlepage-text-color: "FFFFFF"
titlepage-rule-color: "360049"
titlepage-rule-height: 0
titlepage-background: "assets/background.pdf"
logo: assets/qmullogo-white.eps
# fontsize: 12pt
# geometry: margin=2cm
bibliography: bibliography-scattering_amplitudes.bib
abstract:  \input{abstract}
nocite: |
  @Henn:2014aa, @Hunter:2013ab, @Britto:2005ab, @Bern:2012aa, @Britto:2005aa, @Arkani-Hamed:2012aa, @Plefka:2014aa, @Landau:1975aa
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
  \input{assets/custom-commands}
output:
  pdf_document:
    latex_engine: lualatex
    template: assets/template-eisvogel.latex
    path: /thesis_output/draft-amplitudes.pdf
    toc: true
    toc_depth: 3
---
\twocolumn
# Introduction

@import "00.introduction.md"

\onecolumn


# Relativity
@import "02.relativity.md"

# Groups
@import "03.groups.md"


# Four vectors

# Pauli Matrices
@import "40.pauli_matrices.md"


# Spinors and transformations
@import "50.spinor.md"

# Spinor helicity formalism (null vectors)

# Little group and weights
<!-- Working on -->
@import "51.angular_momentum.md"
<!-- LOGS from here -->
# 23rd October 2019
@import "/dissertation/log/2019.10.23.md"

# 29th October 2019
@import "/dissertation/log/2019.10.29.md"


# Tues, 19th November 2019
@import "/dissertation/log/2019.11.19.md"

# Tues, 26 November 2019
@import "/dissertation/log/2019.11.26.md"
<!-- logs end here -->
<!--
# Determination of three-point amplitudes of massless particles

# Introduction to Feynman diagrams  - reproducing amplitudes for Yang-Mills theory

# Three-point amplitudes and factorisation
# BCFW recursion relations in Yang-Mills and Gravity
 -->
@import "99.bcfw.md"

# Bibliography
