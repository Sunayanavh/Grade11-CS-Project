import tkinter as tk
from tkinter import *
import tkintermapview
root = tk.Tk()
root.geometry('800x600')
root.title("map_view_example.py")
root.configure(bg="darkgrey")

mylabel=LabelFrame(root)
mylabel.pack(pady=20)
mapwidget = tkintermapview.TkinterMapView(mylabel,
                                           width=800,
                                           height=600,
                                           corner_radius=0)
mapwidget.set_position(36.393, 25.4615, text="santorini")
mapwidget.set_zoom(2)
mapwidget.pack()

marker_1 = mapwidget.set_marker(35.6764, 139.6500, text="Tokyo")
marker_2 = mapwidget.set_marker(52.3676,4.9041, text="Amsterdam")
marker_3 = mapwidget.set_marker(36.393, 25.4615, text="Santorini")
marker_4 = mapwidget.set_marker(37.5519, 126.9918, text="Seoul")
marker_5 = mapwidget.set_marker(39.5501, -105.7821, text="Colorado")

def nextpage():
    root.destroy()
    import tokyo

button = tk.Button(
    text = 'Tokyo',
    bg = 'white',
    fg = 'black',
    font = ('Times',15,'bold'),
    command = nextpage,
).place(relx=0.02,rely=0.1,anchor='nw')

def nextpage():
    root.destroy()
    import Amsterdam

button = tk.Button(
    text = 'Amsterdam',
    bg = 'white',
    fg = 'black',
    font = ('Times',15,'bold'),
    command = nextpage,
).place(relx=0.02,rely=0.2,anchor='nw')

def nextpage():
    root.destroy()
    import Santorini

button = tk.Button(
    text = 'Santorini',
    bg = 'white',
    fg = 'black',
    font = ('Times',15,'bold'),
    command = nextpage,
).place(relx=0.02,rely=0.3,anchor='nw')

def nextpage():
    root.destroy()
    import seoul

button = tk.Button(
    text = 'Seoul',
    bg = 'white',
    fg = 'black',
    font = ('Times',15,'bold'),
    command = nextpage,
).place(relx=0.02,rely=0.4,anchor='nw')

def nextpage():
    root.destroy()
    import Colorado

button = tk.Button(
    text = 'Colorado',
    bg = 'white',
    fg = 'black',
    font = ('Times',15,'bold'),
    command = nextpage,
).place(relx=0.02,rely=0.5,anchor='nw')

root.mainloop()  
