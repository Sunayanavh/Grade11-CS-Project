import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
root = tk.Tk()
root.title("Santorini")
root.configure(bg="bisque")
root.geometry('1400x800')
root.attributes('-fullscreen',True)

label1 = tk.Label(
    text = 'Santorini',
    bg = 'bisque',
    fg = 'black',
    font = ('Comic Sans',50,'bold'),
)
label1.place(relx=0.5,rely=0.1,anchor='center')

label2 = tk.Label(
    text = "Santorini is one of the Cyclades islands in the \
Aegean Sea. It was devastated  \n by a volcanic eruption in the 16th century\
BC, forever shaping its rugged landscape. \n  The whitewashed, \
cubiform houses of its 2 principal towns, Fira and Oia, cling\
to cliffs above an \nunderwater caldera (crater). They overlook the\
sea, small islands to the west and beaches\n made up of \
black, red and white lava pebbles.",
    bg = 'bisque',
    fg = 'grey35',
    font = ('Comic Sans',22,'bold italic'),
)
label2.place(relx=0.5,rely=0.28,anchor='center')

test1 = ImageTk.PhotoImage(Image.open('santa-1.jpeg'))
labelimg1 = tk.Label(image=test1)
labelimg1.place(relx=0.9,rely=0.95,anchor='se')

test2 = ImageTk.PhotoImage(Image.open('santa-2.jpeg'))
labelimg2 = tk.Label(image=test2)
labelimg2.place(relx=0.9,rely=0.7,anchor='se')

label = tk.Label(
    text = 'HOTELS (cost per night):',
    bg = 'bisque',
    fg = 'grey22',
    font = ('Comic Sans',25,'bold'),
)
label.place(relx=0.02,rely=0.6,anchor='sw')

label3 = tk.Label(
    text = 'Villa Manos(4.7) - Rs 5,293\n\
White Concept Caves(4.6) - Rs 7,618\n\
Rocabella Santorini(4.7) - Rs 8,390',
    bg = 'bisque',
    fg = 'grey22',
    font = ('Comic Sans',25),
)
label3.place(relx=0.02,rely=0.75,anchor='sw')

def nextpage():
    root.destroy()

button = tk.Button(
    text = 'Exit',
    bg = 'bisque',
    fg = 'Black',
    font = ('Times',25,'bold'),
    command = nextpage,
).pack(side=tk.BOTTOM,pady=10)

root.mainloop()
