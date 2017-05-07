import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt

def fractal(points,n_max):
    if len(points)>=4**n_max+1:
        return
    for k in range(len(points)-1):
        i=4*k
        A=points[i]
        B=points[i+1]
        P=2.*A/3.+B/3.
        Q=A/3.+2*B/3.
        M=np.array([0.5*(B[0]-A[0])+0.288675*(A[1]-B[1]),
                   0.5*(B[1]-A[1])+0.288675*(B[0]-A[0])])
        M=M+A
        points.insert(i+1,Q)
        points.insert(i+1,M)
        points.insert(i+1,P)
    fractal(points,n_max)

points1=[np.array([0,0]),np.array([1.,0])]
points2=[np.array([1/2.,-0.866]),np.array([0,0])]
points3=[np.array([1.,0]),np.array([1/2.,-0.866])]
fractal(points1,5)
fractal(points2,5)
fractal(points3,5)

data1=np.array(points1).T
data2=np.array(points2).T
data3=np.array(points3).T
fig=plt.figure(figsize=[19.20,10.80])
plt.plot(data1[0],data1[1],"-",color="cornflowerblue")
plt.plot(data2[0],data2[1],"-",color="cornflowerblue")
plt.plot(data3[0],data3[1],"-",color="cornflowerblue")

plt.axis("off")
plt.axis("equal")
# plt.axis([-0.2,1.2,-1,0.4])
plt.savefig("/Users/qinglingzhang/Desktop/snowflake.png")
plt.show()
