cd src

pdflatex all.tex
pdflatex all.tex
./clean.sh
cp output/all.pdf ..
cp output/all.toc ..

