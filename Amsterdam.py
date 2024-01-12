import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
root = tk.Tk()
root.title("Amsterdam")
root.configure(bg="bisque")
root.geometry('1400x800')
root.attributes('-fullscreen',True)

label1 = tk.Label(
    text = 'Amsterdam',
    bg = 'bisque',
    fg = 'black',
    font = ('Comic Sans',50,'bold'),
)
label1.place(relx=0.5,rely=0.1,anchor='center')

label2 = tk.Label(
    text = "Amsterdam is the Netherlands’ capital, known for its \
artistic heritage, elaborate canal \n system and narrow houses with gabled \
facades, legacies of the  city’s 17th-century Golden Age. \n Its Museum \
District houses the Van Gogh Museum, works by Rembrandt and Vermeer at \n\
the Rijksmuseum, and modern art at the Stedelijk. Cycling is key to the \
city’s character, and \n there are numerous bike paths.",
    bg = 'bisque',
    fg = 'grey35',
    font = ('Comic Sans',22,'bold italic'),
)
label2.place(relx=0.5,rely=0.28,anchor='center')

test1 = ImageTk.PhotoImage(Image.open('ams-1.jpeg'))
labelimg1 = tk.Label(image=test1)
labelimg1.place(relx=0.9,rely=0.95,anchor='se')

test2 = ImageTk.PhotoImage(Image.open('ams-2.jpg'))
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
    text = 'meininiger hotel Amsterdam(4.2) - Rs 4,293\n\
Parh Inn(4.0) - Rs 8,618\n\
Mariott(4.2) - Rs 8,390',
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
