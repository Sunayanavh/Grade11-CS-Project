import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
root = tk.Tk()
root.title("Zermatt")
root.configure(bg="LightBlue3")
root.geometry('1400x800')
root.attributes('-fullscreen',True)

label1 = tk.Label(
    text = 'ZERMATT',
    bg = 'LightBlue3',
    fg = 'black',
    font = ('Comic Sans',50,'bold'),
)
label1.place(relx=0.5,rely=0.1,anchor='center')

label2 = tk.Label(
    text = "Zermatt, in southern Switzerland’s Valais canton, is\
a mountain resort renowned for skiing, \n climbing and hiking. The \
town, at an elevation of around 1,600m, lies below the iconic, \n\
pyramid-shaped Matterhorn peak. Its main street, Bahnhofstrasse \
is lined with\n boutique shops, hotels and restaurants, and also \
has a lively après-ski scene. There\n are public outdoor \
rinks for ice-skating and curling",
    bg = 'LightBlue3',
    fg = 'grey35',
    font = ('Comic Sans',22,'bold italic'),
)
label2.place(relx=0.5,rely=0.28,anchor='center')

test1 = ImageTk.PhotoImage(Image.open('zermatt1.jpg'))
labelimg1 = tk.Label(image=test1)
labelimg1.place(relx=0.9,rely=0.95,anchor='se')

test2 = ImageTk.PhotoImage(Image.open('zermatt2.jpg'))
labelimg2 = tk.Label(image=test2)
labelimg2.place(relx=0.9,rely=0.7,anchor='se')

label = tk.Label(
    text = 'HOTELS (cost per night):',
    bg = 'LightBlue3',
    fg = 'grey22',
    font = ('Comic Sans',25,'bold'),
)
label.place(relx=0.02,rely=0.6,anchor='sw')

label3 = tk.Label(
    text = 'Mont Cervin Palace (4.5) - Rs 1,33,240\n\
Hotel Firefly (5.0) - Rs 86,423\n\
Hotel Bellerive (5.0) - Rs 30,886',
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
