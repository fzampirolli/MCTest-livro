# para rodar
# chmod +x runAll.sh
# ./runAll livro

# livro digital
pdflatex --shell-escape $1.tex
bibtex $1
pdflatex --shell-escape $1.tex
pdflatex --shell-escape $1.tex
#open $1.pdf

# converter para html
pdf2htmlEX $1.pdf

# livro para impressao 12pt
pdflatex --shell-escape $1-impressao12pt.tex
bibtex $1-impressao12pt
pdflatex --shell-escape $1-impressao12pt.tex
pdflatex --shell-escape $1-impressao12pt.tex

# livro para impressao 11pt
pdflatex --shell-escape $1-impressao11pt.tex
bibtex $1-impressao11pt
pdflatex --shell-escape $1-impressao11pt.tex
pdflatex --shell-escape $1-impressao11pt.tex


# capa
pdflatex --shell-escape $1-capa21x29.7.tex
pdflatex --shell-escape $1-capa21x29.7orelha.tex

# converter para epub - tem muitos erros de formatação
#tex4ebook -f epub3 $1 mathml
tex4ebook -f epub3 $1.tex --shell-scape

'''
latexml --dest=$1.xml $1.tex
latexmlpost -dest=$1.html $1.xml
ebook-convert $1.html $1.epub --language en --no-default-epub-cover

# para mover para o github
git commit -am "2ed"
git push origin main

'''

rm -rf *.aux */*.aux livro-epub* *.bbl *.lof *.log *.blg *.lol *.maf *.mtc* *.out *.ptc *.toc *.xhtml *.css *.dvi *.tmp *.xref *.idv *.lg *.ncx *.pyg *.4* _min* *.opf *.png 

cp livro*.pdf /Users/fz/PycharmProjects/mctest/book/2ed-br
cp *.html /Users/fz/PycharmProjects/mctest/book/2ed-br
cp *.epub /Users/fz/PycharmProjects/mctest/book/2ed-br

cp livro.pdf ~/Desktop

# pdflatex --shell-escape livro.tex ; cp livro.pdf ~/Desktop
# bibtex livro
