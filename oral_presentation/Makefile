tmp_file = _tmp
main_file = presentation.md
local_config = _config.yaml
m4config = ~/.config/m4config

default: FORCE
	make preprocess
	make main.pdf
	make clean

o: FORCE
	make
	open main.pdf

beamer: 
	make preprocess
	make presentation.pdf

ob:
	make beamer
	open presentation.pdf

latex:
	make preprocess
	make main.latex

doc:
	make preprocess
	make main.docx
	make clean
	open main.docx

mdfiles = **/*/*.md

pandoc_in = pandoc -s -i $(tmp_file) $(local_config)
pandoc_args_pdf = --pdf-engine=pdflatex
eisvogel_template = --template "template-eisvogel.latex" --listings
pandoc_template = -V theme:metropolis

preprocess: $(local_config) FORCE
	m4 $(m4config) -I./ $(main_file) > $(tmp_file);

clean: $(tmp_file) FORCE
	rm $<

main.pdf: $(mdfiles) $(tmp_file) FORCE
	$(pandoc_in) --from markdown $(pandoc_args_pdf) $(pandoc_template) --to pdf -o $@

main.latex: $(mdfiles) $(tmp_file) FORCE
	$(pandoc_in) --from markdown --to latex -o $@

presentation.pdf: $(mdfiles) $(tmp_file) FORCE
	$(pandoc_in) $(pandoc_template) --to beamer --from markdown -o $@

main.docx: $(mdfiles) $(tmp_file) FORCE
	$(pandoc_in) --from markdown $(pandoc_template) -o $@
	# make main.latex
	# rm $(tmp_file)
	# mv main.latex $(tmp_file)
	# $(pandoc_in) $(pandoc_template) --from latex -o $@

FORCE:

