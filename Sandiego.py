import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
root = tk.Tk()
root.title("San Diego")
root.configure(bg="salmon1")
root.geometry('1400x800')
root.attributes('-fullscreen',True)

label1 = tk.Label(
    text = 'San Diego',
    bg = 'salmon1',
    fg = 'black',
    font = ('Comic Sans',50,'bold'),
)
label1.place(relx=0.5,rely=0.1,anchor='center')

label2 = tk.Label(
    text = "SanDiego is a city on the Pacific coast of California known for its beaches, parks \n and warm climate. Immense \
Balboa Park is the site of the renowned San Diego Zoo,\n as well as numerous art galleries, artist studios, museums \
and gardens. A deep harbor \n is home to a large active naval fleet, with the USS Midway, an aircraft-carrier-turned-\
museum, \n open to the public.",
    bg = 'salmon1',
    fg = 'grey35',
    font = ('Comic Sans',22,'bold italic'),
)
label2.place(relx=0.5,rely=0.28,anchor='center')

test1 = ImageTk.PhotoImage(Image.open('sandi-1.jpg'))
labelimg1 = tk.Label(image=test1)
labelimg1.place(relx=0.9,rely=0.95,anchor='se')

test2 = ImageTk.PhotoImage(Image.open('sandi-2.jpeg'))
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
    text = ' courtyard Maeiott (3.9) - Rs 19,293\n\
Hotel Hilton Mission Valley(3.6) - Rs 13,618\n\
Paciffic Terrace Hotel (4.7) - Rs 1,47,390',
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
