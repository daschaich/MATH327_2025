# ------------------------------------------------------------------
# Fermi--Dirac average occupation number distribution for various temperatures
gnuplot
set terminal epslatex color
set out "temp.tex"
set key top right
set xlabel "{\\Large $E / \\mu$}"
set ylabel "{\\Large $F(E)$}" rotate by 0
set xr [0:5]
set yr [0:1.1]
f(x) = 1.0 / (1.0 + exp(1.0 * (x - 1.0)))
g(x) = 1.0 / (1.0 + exp(2.0 * (x - 1.0)))
h(x) = 1.0 / (1.0 + exp(10.0 * (x - 1.0)))
k(x) = 1.0 / (1.0 + exp(100.0 * (x - 1.0)))
plot f(x) w l lt 1 lc 7 lw 4 t "$T = \\mu$", \
     g(x) w l dt 2 lc 2 lw 4 t "$T = \\mu / 2$", \
     h(x) w l dt 3 lc 6 lw 4 t "$T = \\mu / 10$", \
     k(x) w l lt 1 lc -1 lw 4 t "$T = \\mu / 100$"
quit
cp ~/.gnuplot-out.tex gnuplot-out.tex
latex gnuplot-out
dvips -Ppdf gnuplot-out.dvi -o unit08_dist.ps
ps2pdf unit08_dist.ps
pdfcrop --margins 5 unit08_dist.pdf
mv -f unit08_dist-crop.pdf unit08_dist.pdf
rm gnuplot-out.* temp* unit08_dist.ps
# ------------------------------------------------------------------
