import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
root = tk.Tk()
root.title("Tokyo")
root.configure(bg="bisque")
root.geometry('1400x800')
root.attributes('-fullscreen',True)

label1 = tk.Label(
    text = 'Tokyo', 
    bg = 'bisque',
    fg = 'black',
    font = ('Comic Sans',50,'bold'),
)
label1.place(relx=0.5,rely=0.1,anchor='center')

label2 = tk.Label(
    text = "Tokyo, Japan’s busy capital, mixes the ultramodern and the \
traditional, \n from \
neon-lit skyscrapers to historic\
temples. The opulent Meiji Shinto \n Shrine is known for \
its towering gate and surrounding woods. The Imperial Palace \
sits amid large\n public gardens. The citys many museums offer \
exhibits ranging from classical art (in the Tokyo \n\
National Museum) to a reconstructed kabuki theater",
    bg = 'bisque',
    fg = 'grey35',
    font = ('Comic Sans',22,'bold italic'),
)
label2.place(relx=0.5,rely=0.28,anchor='center')

test1 = ImageTk.PhotoImage(Image.open('tokyo-1.jpeg'))
labelimg1 = tk.Label(image=test1)
labelimg1.place(relx=0.9,rely=0.95,anchor='se')

test2 = ImageTk.PhotoImage(Image.open('tokyo-2.jpg'))
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
    text = 'Manga art hotel(3.9) - Rs 4,293\n\
One@ tokyo(4.6) - Rs 8,618\n\
Rembrandt(4.7) - Rs 7,390',
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
