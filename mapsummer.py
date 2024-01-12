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
#mapwidget.place(relx=0.5, rely=0.1, anchor='ne')
mapwidget.pack()

marker_1 = mapwidget.set_marker(11.3493, 142.1996, text="Maldives")
marker_2 = mapwidget.set_marker(19.8987, -155.6659, text="Hawaii")
marker_3 = mapwidget.set_marker(8.0844, 77.5495, text="Kanyakumari")
marker_4 = mapwidget.set_marker(-8.4095, 115.1889, text="Bali")
marker_5 = mapwidget.set_marker(10.7449, 92.5000, text="Andaman and Nicobar")

def nextpage():
    root.destroy()
    import maldives

button = tk.Button(
    text = 'Maldives',
    bg = 'white',
    fg = 'black',
    font = ('Times',15,'bold'),
    command = nextpage,
).place(relx=0.02,rely=0.1,anchor='nw')

def nextpage():
    root.destroy()
    import hawaii

button = tk.Button(
    text = 'Hawaii',
    bg = 'white',
    fg = 'black',
    font = ('Times',15,'bold'),
    command = nextpage,
).place(relx=0.02,rely=0.2,anchor='nw')

def nextpage():
    root.destroy()
    import kanyakumari

button = tk.Button(
    text = 'Kanyakumari',
    bg = 'white',
    fg = 'black',
    font = ('Times',15,'bold'),
    command = nextpage,
).place(relx=0.02,rely=0.3,anchor='nw')

def nextpage():
    root.destroy()
    import bali

button = tk.Button(
    text = 'Bali',
    bg = 'white',
    fg = 'black',
    font = ('Times',15,'bold'),
    command = nextpage,
).place(relx=0.02,rely=0.4,anchor='nw')

def nextpage():
    root.destroy()
    import andaman

button = tk.Button(
    text = 'Andaman and Nicobar',
    bg = 'white',
    fg = 'black',
    font = ('Times',15,'bold'),
    command = nextpage,
).place(relx=0.02,rely=0.5,anchor='nw')

root.mainloop()  
