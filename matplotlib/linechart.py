"""
Line chart demo.
"""
import matplotlib.pyplot as plt

dataa = (162, 186, 256, 438)
datab = (200, 217, 251, 310)
datac = (161, 185, 233, 298)
datad = (89, 98, 107, 116)

fig, ax = plt.subplots(figsize=(8,5))

x = (1, 2, 3, 4)
xticks = ('Case A', 'Case B', 'Case C', 'Case D')

plt.plot(x, dataa, 'o-', markersize=14, color=(0.93,0.49,0.19), 
	linewidth=5, label='Legend A')
plt.plot(x, datab, 's-', markersize=14, color=(0.36,0.61,0.84), 
	linewidth=5, label='Legend B')
plt.plot(x, datac, 'D-', markersize=14, color=(1,0.75,0), 
	linewidth=5, label='Legend C')
plt.plot(x, datad, 'v-', markersize=14, color=(0.5,0.5,0.5), 
	linewidth=5, label='Legend D')

plt.xlabel('', fontsize=20)
plt.ylabel('Label Y', fontsize=20, fontweight='bold')
plt.xticks(x, xticks, fontsize=20)
plt.yticks(fontsize=18)
plt.ylim(ymin=0)
plt.setp(ax.get_xticklabels(), rotation=5)
plt.legend(fontsize=18, loc=2)

plt.tight_layout()
plt.show()
