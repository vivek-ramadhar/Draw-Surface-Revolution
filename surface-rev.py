from mpl_toolkits.mplot3d import Axes3D
from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
#from draw import drawApp

class drawApp:
    global coords
    global app
    global canvas
    global btn
    #global running

    def get_xy(event):
        global lasx, lasy
        lasx, lasy = event.x, event.y

    def draw(event, canvas, coords):
        global lasx, lasy
        canvas.create_line((lasx, lasy, event.x, event.y), fill='red', width=2)
        lasx, lasy = event.x, event.y
        coords.append([lasx, lasy])

    def run(self):

        # mainloop
        while self.running:
            self.app.update_idletasks()
            self.app.update()
    def close(self):
        self.running = False
        self.app.destroy()

    def __init__(self) -> None:
        app = Tk()
        canvas = Canvas(app, bg='black')
        app.geometry("600x600")

        self.coords = []
        self.app = app
        self.canvas = canvas
        self.running = True

        # set origin to top-left -> north-west
        # fill and expand stretch canvas to fill the entire window
        self.canvas.pack(anchor='nw', fill='both', expand=1)

        # when left clicking get initial cursor position
        self.canvas.bind("<Button-1>", drawApp.get_xy)
        # when left click is pressed and mouse is moved, call draw function
        self.canvas.bind("<B1-Motion>", lambda event: drawApp.draw(event, canvas=self.canvas, coords=self.coords))

        btn = Button(app, text="Generate Surface", width=15, height=1, bd='10', command=self.close)
        btn.place(x=445, y=55)

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

def moi(x, y, z):
    N = len(x)
    Ix = sum(y**2 + z**2)/N
    Iy = sum(x**2 + z**2)/N
    Iz = sum(x**2 + y**2)/N
    Ixy = sum(x*y)/N
    Iyz = sum(y*z)/N
    Ixz = sum(x*z)/N
    I = np.array([[Ix, Ixy, Ixz], [Ixy, Iy, Iyz],[Ixz, Iyz, Iz]])
    return I

def plot(app):
    n = len(app.coords)
    x = [i[0]/600 for i in app.coords]
    y = [(600-i[1])/600 for i in app.coords]

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
    #print(moi(surface[0], surface[1], surface[2]))
    plt.show()

while True:
    app = drawApp()
    app.run()
    plot(app)
