import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
root = tk.Tk()
root.title("New York")
root.configure(bg="LightBlue3")
root.geometry('1400x800')
root.attributes('-fullscreen',True)

label1 = tk.Label(
    text = 'NEW YORK',
    bg = 'LightBlue3',
    fg = 'black',
    font = ('Comic Sans',50,'bold'),
)
label1.place(relx=0.5,rely=0.1,anchor='center')

label2 = tk.Label(
    text = "New York City comprises 5 boroughs sitting where \
the Hudson River meets the Atlantic \n Ocean. At its core is Manhattan, \
a densely populated borough that’s among the world’s major\n commercial, \
financial and cultural centers. Its iconic sites include skyscrapers \
such as the\n Empire State Building and sprawling Central Park. \
Broadway theater is staged in neon-lit \nTimes Square.",
    bg = 'LightBlue3',
    fg = 'grey35',
    font = ('Comic Sans',22,'bold italic'),
)
label2.place(relx=0.5,rely=0.28,anchor='center')

test1 = ImageTk.PhotoImage(Image.open('newyork1.jpg'))
labelimg1 = tk.Label(image=test1)
labelimg1.place(relx=0.9,rely=0.95,anchor='se')

test2 = ImageTk.PhotoImage(Image.open('newyork2.jpg'))
labelimg2 = tk.Label(image=test2)
labelimg2.place(relx=0.9,rely=0.68,anchor='se')

label = tk.Label(
    text = 'HOTELS (cost per night):',
    bg = 'LightBlue3',
    fg = 'grey22',
    font = ('Comic Sans',25,'bold'),
)
label.place(relx=0.02,rely=0.6,anchor='sw')

label3 = tk.Label(
    text = 'The Plaza New York (4.6) - Rs 91,015\n\
Renaissance New York Times Square (4.5) - Rs 33,685\n\
Park Central Hotel (4.7) - Rs 19,152',
    bg = 'LightBlue3',
    fg = 'grey22',
    font = ('Comic Sans',25),
)
label3.place(relx=0.02,rely=0.75,anchor='sw')

def nextpage():
    root.destroy()

button = tk.Button(
    text = 'Exit',
    bg = 'LightBlue3',
    fg = 'Black',
    font = ('Times',25,'bold'),
    command = nextpage,
).pack(side=tk.BOTTOM,pady=10)

root.mainloop()
