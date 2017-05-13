import sys
from Sierpinski_triangle import *
n_max = int(sys.argv[1])

def rotate(point, theta):
	R = np.matrix([[np.cos(theta), -np.sin(theta)],
				   [np.sin(theta),  np.cos(theta)]])
	return np.array(np.dot(R, point))

fig, ax = plt.subplots(figsize=[19.2,10.8])
ax.set_axis_bgcolor('black')
ax.set_xticks([])
ax.set_yticks([])

p0 = rotate(np.array([0,1]),np.pi/6).flatten()
for i in range(6):
	p1 = rotate(p0, np.pi/3).flatten()
	points = np.array([np.array([0,0]), p0, p1])
	# points2 = np.array([p0+p1, p0, p1])
	fractal(points, n_max, ax, 0)
	# fractal(points2, n_max, ax, 0)
	p0 = p1

plt.axis("equal")
plt.axis([-1.2, 1.2, -np.sqrt(3)/2-0.2, np.sqrt(3)/2+0.2])
plt.ylim([-2,2])
plt.savefig("fig2.png", dpi=300)
plt.show()
