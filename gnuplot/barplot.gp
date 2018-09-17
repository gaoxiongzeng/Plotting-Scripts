set terminal pdf enhanced font 'Verdana,24’ persist
set output 'figures/barplot.pdf'
    
set boxwidth 0.9
set grid ytics
set yrange [0:500]
#set xrange [-1:4]
set auto x
set style data histogram
set style histogram cluster gap 1
set style fill border -1
set xlabel "Label X"
set ylabel "Label Y"
set key at graph 0.8, 0.96

plot "99_fct.txt" using 2:xtic(1) lc rgb 'blue' fillstyle pattern 3 title "Scheme 1" , \
            '' using 3 lc rgb 'orange' fillstyle pattern 2 title "Scheme 2" 