import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
root = tk.Tk()
root.title("Kanyakumari")
root.configure(bg="lavender blush")
root.geometry('1400x800')
root.attributes('-fullscreen',True)

label1 = tk.Label(
    text = 'KANYAKUMARI',
    bg = 'lavender blush',
    fg = 'black',
    font = ('Comic Sans',50,'bold'),
)
label1.place(relx=0.5,rely=0.1,anchor='center')

label2 = tk.Label(
    text = "Kanyakumari is a coastal town in the state of Tamil \
Nadu on India's southern tip. \nJutting into the Laccadive Sea, the \
town was known as Cape Comorin during British rule \nand is popular \
for watching sunrise and sunset over the ocean. It's also a noted \n\
pilgrimage site thanks to its Bagavathi Amman Temple, dedicated to\
a consort of Shiva,\n and its Our Lady of Ransom Church, a center \
of Indian Catholicism.",
    bg = 'lavender blush',
    fg = 'grey35',
    font = ('Comic Sans',22,'bold italic'),
)
label2.place(relx=0.5,rely=0.28,anchor='center')

test1 = ImageTk.PhotoImage(Image.open('kanyakumari1.jpg'))
labelimg1 = tk.Label(image=test1)
labelimg1.place(relx=0.9,rely=0.95,anchor='se')

test2 = ImageTk.PhotoImage(Image.open('kanyakumari2.jpg'))
labelimg2 = tk.Label(image=test2)
labelimg2.place(relx=0.9,rely=0.7,anchor='se')

label = tk.Label(
    text = 'HOTELS (cost per night):',
    bg = 'lavender blush',
    fg = 'grey22',
    font = ('Comic Sans',25,'bold'),
)
label.place(relx=0.02,rely=0.6,anchor='sw')

label3 = tk.Label(
    text = 'Anantya by The Lake (4.4) - Rs 11,563\n\
Isola DiCocco (4.5) - Rs 5,625\n\
Sparsa Kanyakumari (4.0) - Rs 4,704',
    bg = 'lavender blush',
    fg = 'grey22',
    font = ('Comic Sans',25),
)
label3.place(relx=0.02,rely=0.75,anchor='sw')

def nextpage():
    root.destroy()

button = tk.Button(
    text = 'Exit',
    bg = 'lavender blush',
    fg = 'Black',
    font = ('Times',25,'bold'),
    command = nextpage,
).pack(side=tk.BOTTOM,pady=10)

root.mainloop()
