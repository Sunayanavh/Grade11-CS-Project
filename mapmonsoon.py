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
mapwidget.set_position(12.9121, 77.6446, text="current location")
mapwidget.set_zoom(2)
mapwidget.pack()

marker_1 = mapwidget.set_marker(24.4539, 54.3773, text="Abu Dhabi")
marker_2 = mapwidget.set_marker(45.440, 12.3155, text="Venice")
marker_3 = mapwidget.set_marker(41.3874, -2.1686, text="Barcelona")
marker_4 = mapwidget.set_marker(0.0236, 37.9062, text="Kenya")
marker_5 = mapwidget.set_marker(11.4102, 76.6950, text="Ooty")

def nextpage():
    root.destroy()
    import abudhabi

button = tk.Button(
    text = 'Abu Dhabi',
    bg = 'white',
    fg = 'black',
    font = ('Times',15,'bold'),
    command = nextpage,
).place(relx=0.02,rely=0.1,anchor='nw')

def nextpage():
    root.destroy()
    import venice

button = tk.Button(
    text = 'Venice',
    bg = 'white',
    fg = 'black',
    font = ('Times',15,'bold'),
    command = nextpage,
).place(relx=0.02,rely=0.2,anchor='nw')

def nextpage():
    root.destroy()
    import barcelona

button = tk.Button(
    text = 'Barcelona',
    bg = 'white',
    fg = 'black',
    font = ('Times',15,'bold'),
    command = nextpage,
).place(relx=0.02,rely=0.3,anchor='nw')

def nextpage():
    root.destroy()
    import kenya

button = tk.Button(
    text = 'Kenya',
    bg = 'white',
    fg = 'black',
    font = ('Times',15,'bold'),
    command = nextpage,
).place(relx=0.02,rely=0.4,anchor='nw')

def nextpage():
    root.destroy()
    import ooty

button = tk.Button(
    text = 'Ooty',
    bg = 'white',
    fg = 'black',
    font = ('Times',15,'bold'),
    command = nextpage,
).place(relx=0.02,rely=0.5,anchor='nw')

root.mainloop()
