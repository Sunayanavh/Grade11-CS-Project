import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
root = tk.Tk()
root.title("Colorado")
root.configure(bg="bisque")
root.geometry('1400x800')
root.attributes('-fullscreen',True)

label1 = tk.Label(
    text = 'Colorado',
    bg = 'bisque',
    fg = 'black',
    font = ('Comic Sans',50,'bold'),
)
label1.place(relx=0.5,rely=0.1,anchor='center')

label2 = tk.Label(
    text = "Colorado, a western U.S. state, has a diverse landscape of arid desert, river canyons \n and snow-covered Rocky Mountains,\
 which are partly protected by Rocky Mountain\n  National Park. Elsewhere, Mesa Verde National Park features Ancestral\
 Puebloan cliff dwellings. \n Perched a mile above sea level, Denver, Colorado’s capital and largest city, features a\ vibrant \n downtown area.",
    bg = 'bisque',
    fg = 'grey35',
    font = ('Comic Sans',22,'bold italic'),
)
label2.place(relx=0.5,rely=0.28,anchor='center')

test1 = ImageTk.PhotoImage(Image.open('colo-1.jpeg'))
labelimg1 = tk.Label(image=test1)
labelimg1.place(relx=0.9,rely=0.95,anchor='se')

test2 = ImageTk.PhotoImage(Image.open('colo-2.jpeg'))
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
    text = 'Hotel Colorado(4.0) - Rs 10,293\n\
Kinship Landing(4.6) - Rs 16,618\n\
hotel Glenwood Colorado(4.7) - Rs 8,390',
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
