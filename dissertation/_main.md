---
title: "Computating On-Shell amplitude using BCFW"
author:
  - name: Samuel Overington | ID 170431121
    affiliation: |
      School of Physics and Astronomy,
      Queen Mary University of London
numbersections: true
fontsize: 12pt
geometry: margin=2cm
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
output:
  pdf_document:
    latex_engine: lualatex
    template: /Users/samuel/Documents/devices/2019-20/project/dissertation/assets/template.tex
    path: /thesis_output/amplitudes.pdf
    toc: true
    toc_depth: 3
---
<!--
\twocolumn
# Introduction

@import "00.introduction.md"

\onecolumn


# Relativity
@import "02.relativity.md"
 -->
# Groups

@import "03.groups.md"


# Four vectors



# Spinors and transformations
# Spinor helicity formalism (null vectors)
@import "01.spinor.md"

# Little group and weights
@import "01.angular_momentum.md"

# Determination of three-point amplitudes of massless particles

# Introduction to Feynman diagrams  - reproducing amplitudes for Yang-Mills theory

# Three-point amplitudes and factorisation
# BCFW recursion relations in Yang-Mills and Gravity

@import "99.bcfw.md"

# Bibliography
