import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
root = tk.Tk()
root.title("abu dhabi")
root.configure(bg="LightBlue3")
root.geometry('1400x800')
root.attributes('-fullscreen',True)

label1 = tk.Label(
    text = 'ABU DHABI',
    bg = 'LightBlue3',
    fg = 'black',
    font = ('Comic Sans',50,'bold'),
)
label1.place(relx=0.5,rely=0.1,anchor='center')

label2 = tk.Label(
    text = "Abu Dhabi, the capital of the United \
Arab Emirates, sits off \n the mainland on an island in the Persian\
(Arabian) Gulf. Its focus on oil exports\n and commerce is \
reflected by the skyline’s modern towers and shopping megacenters \n\
such as Abu Dhabi and Marina malls. Beneath white-marble domes,\
the vast Sheikh \n Zayed Grand Mosque features an immense Persian \
carpet, crystal chandeliers and capacity\n for 41,000 worshipers",
    bg = 'LightBlue3',
    fg = 'grey35',
    font = ('Comic Sans',22,'bold italic'),
)
label2.place(relx=0.5,rely=0.28,anchor='center')

test1 = ImageTk.PhotoImage(Image.open('abudhabi1.jpg'))
labelimg1 = tk.Label(image=test1)
labelimg1.place(relx=0.9,rely=0.95,anchor='se')

test2 = ImageTk.PhotoImage(Image.open('abudhabi2.jpg'))
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
    text = 'Nurai Island (5.0) - Rs 1,29,051\n\
Al Wathba (4.5) - Rs 40,611\n\
Radisson Blu Hotel and Resort (4.6) - Rs 16,777',
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
