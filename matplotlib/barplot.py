"""
Bar plot demo with pairs of bars grouped for easy comparison.
"""
import numpy as np
import matplotlib.pyplot as plt

n_groups = 5
dataa = (1968, 1940, 55, 64, 1269)
datab = (8021, 8060, 9945, 9936, 8731)
datac = (8027, 8060, 9945, 9936, 8731)

fig, ax = plt.subplots(figsize=(10,5))

index = np.arange(n_groups)
bar_width = 0.3

#error_config = {'ecolor': '0.3'}

rects1 = plt.bar(index, dataa, bar_width,
                 alpha=0.9,
				 color=(0.33,0.56,0.84),
                 #yerr=,
                 #error_kw=error_config,
				 hatch='.',
                 label='L1')

rects2 = plt.bar(index + bar_width, datab, bar_width,
                 alpha=1,
                 color=(0.75,0.31,0.3),
                 #yerr=,
                 #error_kw=error_config,
				 hatch='x',
                 label='L2')

rects3 = plt.bar(index + 2*bar_width, datac, bar_width,
                 alpha=0.9,
                 color=(0.61,0.73,0.35),
                 #yerr=,
                 #error_kw=error_config,
				 hatch='o',
                 label='L3')
				 
plt.xlabel('', fontsize=20)
plt.ylabel('Label Y', fontsize=20, fontweight='bold')
plt.yticks(fontsize=18)
plt.xticks(index + bar_width, 
    ('Case A', 'Case B', 'Case C', 'Case D', 'Case E'),
    fontsize=20) 
plt.setp(ax.get_xticklabels(), rotation=12)
plt.legend(fontsize=20, loc=2, ncol=3, columnspacing=0.8, 
    handletextpad=0.4)

def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., height+1,
                '%d' % int(height), ha='center', va='bottom',
				fontsize=18, color='black')

#autolabel(rects1)
#autolabel(rects2)
#autolabel(rects3)

plt.tight_layout()
plt.show()
