cd src

pdflatex all_small.tex
pdflatex all_small.tex
./clean.sh
cp output/all_small.pdf ..
cp output/all_small.toc ..