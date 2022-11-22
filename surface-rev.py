from mpl_toolkits.mplot3d import Axes3D
from draw import drawApp
import matplotlib.pyplot as plt
import numpy as np

# Takes x and y data, representing a curve in xy-plane
# n is the number of points, proportional to resoultion
# returns x, y, and z data representing the surface generated
# by revolving the curve around the y-axis
def surface_rev(x, y, n):
    # parameterization from 0 to 2pi
    t = np.linspace(0, np.pi*2, n)

    # parameterize x,y for a circle
    # x -> r*cos(t)
    # y -> r*sin(t)
    # revolved around y-axis so x is radius of circles
    # numpy.outer computes outer product across numpy array
    xn = np.outer(x, np.cos(t))
    yn = np.outer(x, np.sin(t))

    # create empty array of shape of x-data/y-data
    zn = np.zeros_like(xn)

    # create values for z-data
    # copy y values of 2d plane for each circle of revolution
    for i in range(len(x)):
        zn[i:i+1,:] = np.full_like(zn[0,:], y[i])

    return [xn, yn, zn]

app = drawApp()
app.run()

n = len(app.coords)
x = [i[0] for i in app.coords]
y = [400-i[1] for i in app.coords]

x.reverse()
y.reverse()

fig = plt.figure(figsize=(12,6))
# 2D plot
ax1 = fig.add_subplot(121)
# 3D plot
ax2 = fig.add_subplot(122,projection='3d')

# First define function in xy-plane 
#y = np.linspace(0, 1, n)
#x = np.power(y, 3)

surface = surface_rev(x, y, n)

# plot curve in xy plane
ax1.plot(x, y)
# plot surface in xyz space
ax2.plot_surface(surface[0], surface[1], surface[2])
plt.show()
