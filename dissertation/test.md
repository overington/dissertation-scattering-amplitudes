---
title: "test"
author: Samuel Overington | ID 170431121
numbersections: true
output:
  pdf_document:
    template: assets/template-eisvogel.latex
    path: ../thesis_output/test.pdf
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
---

# first
\[
  K = \frac{1}{2}mv^2
\]

# second
## point 1
\[
  K = \frac{1}{2}mv^2 \taglabel{eq:test}
\]


Here is a equation [\ref{eq:test}]
