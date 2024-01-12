import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
root = tk.Tk()
root.title("Bangkok ")
root.configure(bg="salmon1")
root.geometry('1400x800')
root.attributes('-fullscreen',True)

label1 = tk.Label(
    text = 'Bangkok ',
    bg = 'salmon1',
    fg = 'black',
    font = ('Comic Sans',50,'bold'),
)
label1.place(relx=0.5,rely=0.1,anchor='center')

label2 = tk.Label(
    text = "Bangkok, Thailand’s capital, is a large city known for ornate shrines and vibrant street \n life. The boat-filled Chao \
Phraya River feeds its network of canals, flowing past \n the Rattanakosin royal district, home to opulent Grand Palace \
and its sacred Wat Phra Kaew \n Temple. Nearby is Wat Pho Temple with an enormous reclining Buddha and, on the opposite\
\n shore, Wat Arun Temple with its steep steps and Khmer-style spire. ",
    bg = 'salmon1',
    fg = 'grey35',
    font = ('Comic Sans',22,'bold italic'),
)
label2.place(relx=0.5,rely=0.28,anchor='center')

test1 = ImageTk.PhotoImage(Image.open('bk-1.jpeg'))
labelimg1 = tk.Label(image=test1)
labelimg1.place(relx=0.9,rely=0.95,anchor='se')

test2 = ImageTk.PhotoImage(Image.open('bk-2.jpg'))
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
    text = 'Bangkok palaca hotel (3.7) - Rs 2,293\n\
Hotel JC(4.6) - Rs 3,618\n\
Prince Hotel Bangkok (4.7) - Rs 47,390',
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
