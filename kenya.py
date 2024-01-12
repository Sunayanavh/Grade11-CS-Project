import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
root = tk.Tk()
root.title("kenya")
root.configure(bg="LightBlue3")
root.geometry('1400x800')
root.attributes('-fullscreen',True)

label1 = tk.Label(
    text = 'KENYA',
    bg = 'LightBlue3',
    fg = 'black',
    font = ('Comic Sans',50,'bold'),
)
label1.place(relx=0.5,rely=0.1,anchor='center')

label2 = tk.Label(
    text = "Kenya is a country in East Africa with coastline\
on the Indian Ocean. It encompasses\n savannah, lakelands, the\
dramatic Great Rift Valley and mountain highlands. It's \n also \
home to wildlife like lions, elephants and rhinos. From Nairobi,\
the capital,\n safaris visit the Maasai Mara Reserve, known for\
its annual wildebeest migrations,\n and Amboseli National Park, \
offering views of Tanzania's 5,895m Mt. Kilimanjaro",
    bg = 'LightBlue3',
    fg = 'grey35',
    font = ('Comic Sans',22,'bold italic'),
)
label2.place(relx=0.5,rely=0.28,anchor='center')

test1 = ImageTk.PhotoImage(Image.open('kenya1.jpg'))
labelimg1 = tk.Label(image=test1)
labelimg1.place(relx=0.9,rely=0.95,anchor='se')

test2 = ImageTk.PhotoImage(Image.open('kenya2.jpg'))
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
    text = 'Fairmont Mara Safari Club (4.6) - Rs 80,322\n\
Voyager Beach Resort (5.0) - Rs 18,247\n\
Turtle Bay Beach Club (4.5) - Rs 15,825',
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
