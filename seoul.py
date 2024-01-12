import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
root = tk.Tk()
root.title("Seoul")
root.configure(bg="bisque")
root.geometry('1400x800')
root.attributes('-fullscreen',True)

label1 = tk.Label(
    text = 'Seoul',
    bg = 'bisque',
    fg = 'black',
    font = ('Comic Sans',50,'bold'),
)
label1.place(relx=0.5,rely=0.1,anchor='center')

label2 = tk.Label(
    text = "Seoul, the capital of South Korea, is a huge metropolis\
where modern skyscrapers, high-tech \n subways and pop culture meet \
Buddhist temples, palaces and street markets. Notable \n attractions \
include futuristic Dongdaemun Design Plaza, a convention hall with \n \
curving architecture and a rooftop park; Gyeongbokgung Palace, which \
once had more than \n 7,000 rooms; and Jogyesa Temple, site of ancient \
locust and pine trees.",
    bg = 'bisque',
    fg = 'grey35',
    font = ('Comic Sans',22,'bold italic'),
)
label2.place(relx=0.5,rely=0.28,anchor='center')

test1 = ImageTk.PhotoImage(Image.open('Seoul-1.jpeg'))
labelimg1 = tk.Label(image=test1)
labelimg1.place(relx=0.9,rely=0.95,anchor='se')

test2 = ImageTk.PhotoImage(Image.open('Seoul-2.png'))
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
    text = 'Fairfield Mariott(4.0) - Rs 5,293\n\
WIbis Styles seoul(4.6) - Rs 6,618\n\
k-pop hotel tower(4.7) - Rs 18,390',
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
