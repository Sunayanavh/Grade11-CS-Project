import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
root = tk.Tk()
root.title("Paris")
root.configure(bg="LightBlue3")
root.geometry('1400x800')
root.attributes('-fullscreen',True)

label1 = tk.Label(
    text = 'PARIS',
    bg = 'LightBlue3',
    fg = 'black',
    font = ('Comic Sans',50,'bold'),
)
label1.place(relx=0.5,rely=0.1,anchor='center')

label2 = tk.Label(
    text = "Paris, France's capital, is a major European \
city and a global center for art, fashion, gastro- \n nomy and \
culture. Its 19th-century cityscape is crisscrossed by \
wide boulevards and the\n River Seine. Beyond such landmarks\
as the Eiffel Tower and the 12th-century, Gothic Notre- \nDame \
cathedral, the city is known for its cafe culture and \
designer boutiques along the \nRue du Faubourg Saint-Honoré.",
    bg = 'LightBlue3',
    fg = 'grey35',
    font = ('Comic Sans',22,'bold italic'),
)
label2.place(relx=0.5,rely=0.28,anchor='center')

test1 = ImageTk.PhotoImage(Image.open('paris1.jpg'))
labelimg1 = tk.Label(image=test1)
labelimg1.place(relx=0.88,rely=0.95,anchor='se')

test2 = ImageTk.PhotoImage(Image.open('paris2.jpg'))
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
    text = 'Hotel Barriere Fouquets Paris (4.5) - Rs 1,13,347\n\
West End Hotel (4.3) - Rs 41,128\n\
Citadines Tour Eiffel Paris (4.6) - Rs 18,189',
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
