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
	$(LATEXMK) $(LATEXMK_FLAGS) -jobname=ESM_1 supplementary.tex

clean:
	$(LATEXMK) -C main.tex
	$(LATEXMK) -C -jobname=ESM_1 supplementary.tex
	$(RM) paper/main.bbl paper/ESM_1.bbl paper/supplementary.aux paper/supplementary.bbl paper/supplementary.blg paper/supplementary.fdb_latexmk paper/supplementary.fls paper/supplementary.log paper/supplementary.out paper/supplementary.pdf
