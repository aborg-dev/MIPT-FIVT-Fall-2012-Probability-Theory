cd src

pdflatex all.tex
pdflatex all.tex
./clean.sh
cp output/all.pdf ..

pdflatex all_small.tex
pdflatex all_small.tex
./clean.sh
cp output/all_small.pdf ..
