---
title: "test"
author: Samuel Overington | ID 170431121
output:
  pdf_document:
    template: assets/template.tex
    path: ../thesis_output/test.pdf
header-includes: |
  \usepackage[T1]{fontenc}
  \usepackage{amsmath}
  \usepackage{tensor}
  \usepackage{physics}
  \usepackage{tikz}
---

$$
  \tensor{\L}{^\alpha_\beta}
$$

xvex:
$$
\xvec{x}
$$

$$
\pmqty{\pmat{1}}
$$

```latex {cmd=true}
\documentclass{standalone}
\begin{document}
  Hello world!
\end{document}
```
<!--
```latex {cmd:true, hide:true}
\documentclass{standalone}
\usepackage[siunitx]{tikz}
\begin{document}
\begin{tikzpicture}
  \draw (-1.5,0) -- (1.5,0);
  \draw (0,-1.5) -- (0,1.5);
\end{tikzpicture}
\end{document}
``` -->
