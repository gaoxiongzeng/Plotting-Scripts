set terminal pdf enhanced font 'Verdana,24'
set output 'figures/cdf.pdf'
set grid
set key at graph 0.99, 0.3
set xtics font 'Verdana,24’
set ytics font 'Verdana,24’

#set format x "10^{%L}"
#set logscale x
set yrange [0:1]
set xrange [1:300]
set xtics 100
set ylabel 'CDF' font 'Verdana,30’
set xlabel 'Label X' font 'Verdana,30’
set style line 1 lc rgb 'blue' lt 1 lw 4 dashtype 2
set style line 2 lc rgb 'green' lt 2 lw 3
set style line 3 lc rgb 'orange' lt 3 lw 4

plot 'scheme1.txt' using 2:1 with lines ls 1 title '{/Times=30 Scheme 1}',\
     'scheme2.txt' using 2:1 with lines ls 3 title '{/Times=30 Scheme 2}',\
