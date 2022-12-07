from tkinter import *

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
        app.geometry("400x400")

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
        btn.place(x=255, y=55)

if __name__ == "__main__":
    a = drawApp()
    a.run()