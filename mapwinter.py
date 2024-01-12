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

marker_1 = mapwidget.set_marker(46.0207, 7.7491, text="Zermatt, Swizz")
marker_2 = mapwidget.set_marker(32.2432, 77.1892, text="Manali")
marker_3 = mapwidget.set_marker(40.7128, -74.0060, text="New York")
marker_4 = mapwidget.set_marker(51.5072, 0.1276, text="London")
marker_5 = mapwidget.set_marker(48.8566, 2.3522, text="Paris")

def nextpage():
    root.destroy()
    import Zermatt

button = tk.Button(
    text = 'Zermatt, Swizz',
    bg = 'white',
    fg = 'black',
    font = ('Times',15,'bold'),
    command = nextpage,
).place(relx=0.02,rely=0.1,anchor='nw')

def nextpage():
    root.destroy()
    import Manali

button = tk.Button(
    text = 'Manali',
    bg = 'white',
    fg = 'black',
    font = ('Times',15,'bold'),
    command = nextpage,
).place(relx=0.02,rely=0.2,anchor='nw')

def nextpage():
    root.destroy()
    import NewYork

button = tk.Button(
    text = 'New York',
    bg = 'white',
    fg = 'black',
    font = ('Times',15,'bold'),
    command = nextpage,
).place(relx=0.02,rely=0.3,anchor='nw')

def nextpage():
    root.destroy()
    import London

button = tk.Button(
    text = 'London',
    bg = 'white',
    fg = 'black',
    font = ('Times',15,'bold'),
    command = nextpage,
).place(relx=0.02,rely=0.4,anchor='nw')

def nextpage():
    root.destroy()
    import Paris

button = tk.Button(
    text = 'Paris',
    bg = 'white',
    fg = 'black',
    font = ('Times',15,'bold'),
    command = nextpage,
).place(relx=0.02,rely=0.5,anchor='nw')

root.mainloop()  
