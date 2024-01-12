import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
root = tk.Tk()
root.title("Andaman and Nicobar")
root.configure(bg="lavender blush")
root.geometry('1400x800')
root.attributes('-fullscreen',True)

label1 = tk.Label(
    text = 'ANDAMAN AND NICOBAR',
    bg = 'lavender blush',
    fg = 'black',
    font = ('Comic Sans',50,'bold'),
)
label1.place(relx=0.5,rely=0.1,anchor='center')

label2 = tk.Label(
    text = "The Andaman Islands are an Indian archipelago in \
the Bay of Bengal.\n These roughly 300 islands are known for their\
palm-lined, white-sand beaches, mangroves and \ntropical rainforests.\
Coral reefs supporting marine life such as sharks and rays make\
for popular\n diving and snorkeling sites. Indigenous Andaman Islanders \
inhabit the more remote islands,\n many of which are off limits to visitors",
    bg = 'lavender blush',
    fg = 'grey35',
    font = ('Comic Sans',22,'bold italic'),
)
label2.place(relx=0.5,rely=0.28,anchor='center')

test1 = ImageTk.PhotoImage(Image.open('andaman1.jpg'))
labelimg1 = tk.Label(image=test1)
labelimg1.place(relx=0.9,rely=0.95,anchor='se')

test2 = ImageTk.PhotoImage(Image.open('andaman2.jpg'))
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
    text = 'Welcomhotel Bay Island Port Blair (4.5) - Rs 20,060\n\
Sea Shell Samssara (5.0) - Rs 10,989\n\
Munjoh Ocean Resort (4.7) - Rs 12,026',
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
