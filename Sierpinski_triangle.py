#by Chen & Ling 
#05/13/2017

import numpy as np 
import matplotlib.pyplot as plt
import itertools as it

colors = ["red", "cyan", "yellow"]

'''
3 points of a triangle

'''
def fractal(points, n_max, ax, n=0): 
	if n >= n_max:
		return
	if n==0:
		draw_triangle(points, ax, colors[-1])

	middles = np.zeros([3,2],dtype=float)
	for i in range(3):
		middles[i] = (points[(i+1)%3]+points[(i+2)%3])/2.0
	color = colors[n%len(colors)]
	draw_triangle(middles, ax, color)

	for i in range(3):
		next_points = np.array([points[i], middles[(i+1)%3], middles[(i+2)%3]])
		fractal(next_points, n_max, ax, n+1)

def draw_triangle(points, ax, color):
	triplet = np.concatenate((points, np.array([points[0]])), axis=0)
	ax.plot(triplet[:,0], triplet[:,1], color=color, linewidth=2)


