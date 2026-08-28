TEXLIVE_IMAGE ?= ghcr.io/xu-cheng/texlive-alpine:latest
LATEXMK = docker run --rm \
	--user "$$(id -u):$$(id -g)" \
	-e HOME=/tmp \
	-e TEXINPUTS=/work/template: \
	-v "$(CURDIR):/work" \
	-w /work/paper \
	--entrypoint /opt/texlive/bin/latexmk \
	$(TEXLIVE_IMAGE)
LATEXMK_FLAGS = -pdf -file-line-error -halt-on-error -interaction=nonstopmode

.PHONY: paper main supplement clean

paper: main supplement

main:
	$(LATEXMK) $(LATEXMK_FLAGS) main.tex

supplement:
	$(LATEXMK) $(LATEXMK_FLAGS) supplementary.tex

clean:
	$(LATEXMK) -C main.tex
	$(LATEXMK) -C supplementary.tex
	$(RM) paper/main.bbl paper/supplementary.bbl
