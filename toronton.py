import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
root = tk.Tk()
root.title("Toronto")
root.configure(bg="salmon1")
root.geometry('1400x800')
root.attributes('-fullscreen',True)

label1 = tk.Label(
    text = 'TORONTO',
    bg = 'salmon1',
    fg = 'black',
    font = ('Comic Sans',50,'bold'),
)
label1.place(relx=0.5,rely=0.1,anchor='center')

label2 = tk.Label(
    text = "Toronto is the most populous city in Canada and the capital city of the Canadian province of \n Ontario.\
With a recorded population of 2,794,356 in 2021 it is the fourth-most populous city \n in  North America.\
The city is the anchor  of the Golden Horseshoe, an urban agglomeration of \n people  surrounding \
the western end of  Lake Ontario.  Toronto is an international centre of \n business, arts, sports and\
culture, and is one of the most cosmopolitan cities in the world.",
    bg = 'salmon1',
    fg = 'grey35',
    font = ('Comic Sans',22,'bold italic'),
)
label2.place(relx=0.5,rely=0.28,anchor='center')

test1 = ImageTk.PhotoImage(Image.open('toronto-11.jpg'))
labelimg1 = tk.Label(image=test1)
labelimg1.place(relx=0.9,rely=0.95,anchor='se')

test2 = ImageTk.PhotoImage(Image.open('toronto-2.jpg'))
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
    text = 'Hilton Toronto (4.2) - Rs 16,000\n\
The Ritz-Carlton, Toronto(4.6) - Rs 5,22,00\n\
Four Seasons Hotel Toronto(4.7) - Rs 55,390',
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
