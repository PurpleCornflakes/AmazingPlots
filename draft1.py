
import sys
from Sierpinski_triangle import *
n_max = int(sys.argv[1])

ps = np.array([[0.0,2.0],[-np.sqrt(3),-1.0],[np.sqrt(3),-1.0]])
fig, ax = plt.subplots(figsize=[19.2,10.8])
ax.set_axis_bgcolor('black')
ax.set_xticks([])
ax.set_yticks([])

ps1 = np.array([[0.0,2.0],[-np.sqrt(3),-1.0],[-2*np.sqrt(3),2.0]])
ps2 = np.array([[0.0,2.0],[2*np.sqrt(3),2.0],[np.sqrt(3),-1.0]])

fractal(ps, n_max, ax, 0)
fractal(ps2, n_max, ax, 0)

plt.axis("equal")
plt.ylim([-1.7,2.7])
plt.savefig("/Users/qinglingzhang/Desktop/fig2.png", dpi=200)
plt.show()
