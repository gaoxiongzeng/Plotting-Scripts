set terminal pdf enhanced font 'Verdana,24’ persist
set output 'figures/linechart.pdf'
set grid
#set key at graph 0.85, 0.9
set xtics font 'Verdana,24' 
set ytics font 'Verdana,24'

#set format x "10^{%L}"
set yrange [0:200]
set xrange [0:1]
set ylabel 'Label Y' font 'Verdana,32'
set xlabel 'Label X' font 'Verdana,32'
set style line 1 lc rgb 'blue' lt 1 lw 4 dashtype 2
set style line 2 lc rgb 'orange' lt 2 lw 4 

plot 'cachefollower_withoutaeolus_avg_fct_100k.txt' using 1:2 with linespoints ls 1 title '{/Times=30 Scheme 1}',\
     'cachefollower_withaeolus_avg_fct_100k.txt' using 1:2 with linespoints ls 2 title '{/Times=30 Scheme 2}',\
    
