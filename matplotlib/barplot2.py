%matplotlib inline

import matplotlib as mpl
import matplotlib.pylab as plt
import numpy as np
import os

# Changing default matplotlib settings
mpl.rcParams['hatch.linewidth'] = 2.4
mpl.rcParams['font.family'] = 'Times New Roman'

# Number of Groups
n_groups = 1

# Figures folder if not exists
if os.name == 'posix':
    output_folder = 'temp'
else:
    output_folder = "d:\\temp"


# data to draw
raw_data_1 = [
          # avg (us)
          (120), # Scheme1

          (103), # Scheme2

          (79), # Scheme3
    
          (29), # Scheme4

          (59), # Scheme5

          (89), # Scheme6

          (57), # Scheme7 
      ]

def preprocessing (data):
    new_data = []
    for d in data:
        new_data.append (d)
    return new_data
        
def draw_one_group( data, title, its_xticks, data_size=7, legend_or_not=0):
    data = preprocessing (data)
    fig, ax = plt.subplots()
    
    index = np.arange(n_groups)
    bar_width = 0.05

    opacity = 0.4
    
    interval_between_bar = 0.2
    
    colors = ['#cccccc','#999999', '#333333', '#00ffff', '#0080ff', '#0000ff', '#ff00ff']
    hatches= ['-', 'x', '//', '.', '\\', '+', '//']
    labels = ['Scheme1','Scheme2','Scheme3','Scheme4','Scheme5','Scheme6','Scheme7']
    
    for i in range(data_size):
        plt.bar(index + (1 + i + interval_between_bar*i)*bar_width, data[i], bar_width,
                 fill=True,
                 color=colors[i],
                 hatch=hatches[i],
                 label=labels[i],
                 edgecolor='black')

    plt.ylabel('Y Label (unit)', fontsize=25, fontweight='bold')
    plt.xlabel(its_xticks, fontsize=25, fontweight='bold')
    
    ax.yaxis.grid(alpha=.6)
    if legend_or_not:
        plt.legend(loc=2, fontsize=18, ncol=2)
        ax.set_ylim([0, int (2.5 * max([d for d in data]))])
    else:
        ax.set_ylim([0, int (1.2 * max([d for d in data]))])
    
    plt.tick_params(axis='y',labelsize=22)
    plt.tick_params(
        axis='x',          # changes apply to the x-axis
        which='both',      # both major and minor ticks are affected
        bottom='off',      # ticks along the bottom edge are off
        top='off',         # ticks along the top edge are off
        labelbottom='off') # labels along the bottom edge are off
    plt.tight_layout()
    plt.savefig(output_folder + os.sep + title+'.pdf', format='pdf') # save as pdf
    plt.show()

    
draw_one_group(raw_data_1, "barplot2", ("X Label"), 7, 1)