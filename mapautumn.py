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
mapwidget.set_position(41.9028, 12.4964, text="rome")
mapwidget.set_zoom(2)
mapwidget.pack()

marker_1 = mapwidget.set_marker(56.1304, -106.3468, text="Toronto")
marker_2 = mapwidget.set_marker(55.7558, 37.6173, text="Moscow")
marker_3 = mapwidget.set_marker(41.9028, 12.4964, text="Rome")
marker_4 = mapwidget.set_marker(32.7157, -117.1611, text="San Diego, California")
marker_5 = mapwidget.set_marker(13.7563, 100.5018, text="Bangkok")

def nextpage():
    root.destroy()
    import toronton

button = tk.Button(
    text = 'Toronto',
    bg = 'white',
    fg = 'black',
    font = ('Times',15,'bold'),
    command = nextpage,
).place(relx=0.02,rely=0.1,anchor='nw')

def nextpage():
    root.destroy()
    import moscow

button = tk.Button(
    text = 'Moscow',
    bg = 'white',
    fg = 'black',
    font = ('Times',15,'bold'),
    command = nextpage,
).place(relx=0.02,rely=0.2,anchor='nw')

def nextpage():
    root.destroy()
    import rome

button = tk.Button(
    text = 'Rome',
    bg = 'white',
    fg = 'black',
    font = ('Times',15,'bold'),
    command = nextpage,
).place(relx=0.02,rely=0.3,anchor='nw')

def nextpage():
    root.destroy()
    import Sandiego

button = tk.Button(
    text = 'San Diego, California',
    bg = 'white',
    fg = 'black',
    font = ('Times',15,'bold'),
    command = nextpage,
).place(relx=0.02,rely=0.4,anchor='nw')

def nextpage():
    root.destroy()
    import Bangkok

button = tk.Button(
    text = 'Bangkok',
    bg = 'white',
    fg = 'black',
    font = ('Times',15,'bold'),
    command = nextpage,
).place(relx=0.02,rely=0.5,anchor='nw')

root.mainloop()
