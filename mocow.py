import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
root = tk.Tk()
root.title("Moscow")
root.configure(bg="salmon1")
root.geometry('1400x800')
root.attributes('-fullscreen',True)

label1 = tk.Label(
    text = 'MOSCOW',
    bg = 'salmon1',
    fg = 'black',
    font = ('Comic Sans',50,'bold'),
)
label1.place(relx=0.5,rely=0.1,anchor='center')

label2 = tk.Label(
    text = "Moscow, on the Moskva River in western Russia, is the nation’s cosmopolitan \n capital. In its historic core is\
 the Kremlin, a complex that’s home to the president \n and tsarist treasures in the Armoury. Outside its walls \
is Red Square, Russia's \n symbolic center. It's home to Lenin’s Mausoleum, the State Historical Museum's comprehensive\
 collection \n and St. Basil’s Cathedral, known for its colorful, onion-shaped domes.",
    bg = 'salmon1',
    fg = 'grey35',
    font = ('Comic Sans',22,'bold italic'),
)
label2.place(relx=0.5,rely=0.28,anchor='center')

test1 = ImageTk.PhotoImage(Image.open('moscow-1.jpeg'))
labelimg1 = tk.Label(image=test1)
labelimg1.place(relx=0.9,rely=0.95,anchor='se')

test2 = ImageTk.PhotoImage(Image.open('moscow-2.jpeg'))
labelimg2 = tk.Label(image=test2)
labelimg2.place(relx=0.9,rely=0.7,anchor='se')

label = tk.Label(
    text = 'HOTELS (cost per night):',
    bg = 'salmon1',
    fg = 'grey22',
    font = ('Comic Sans',25,'bold'),
)
label.place(relx=0.02,rely=0.6,anchor='sw')

label3 = tk.Label(
    text = 'The Elite Royale (3.7) - Rs 19,293\n\
Hotel National, a Luxury Collection Hotel, Moscow(4.6) - Rs 13,618\n\
Four Seasons Hotel Moscow(4.7) - Rs 47,390',
    bg = 'salmon1',
    fg = 'grey22',
    font = ('Comic Sans',25),
)
label3.place(relx=0.02,rely=0.75,anchor='sw')

def nextpage():
    root.destroy()

button = tk.Button(
    text = 'Exit',
    bg = 'salmon1',
    fg = 'Black',
    font = ('Times',25,'bold'),
    command = nextpage,
).pack(side=tk.BOTTOM,pady=10)


root.mainloop()
