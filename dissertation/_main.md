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
  \usepackage{subcaption}
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

<!-- import "chapters/00-introduction.md" -->


# Some Basic Concepts: Groups, Algebras and Representations
@import "chapters/10-groups_algebras_reprs.md"




# Bibliography
