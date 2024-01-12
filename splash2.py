import tkinter as tk    
from tkinter import *
from PIL import ImageTk, Image
def nextpage():
    window.destroy()
    import page2

splash_root=Tk()
splash_root.title('splash screeeeen!!')
splash_root.geometry('1400x800')
splash_root.configure(bg = 'black')
splash_root.overrideredirect(True)   #to hide title bar
splash_label=Label(splash_root,text='~following the compass~',
                   font = ('Times',40,'bold italic'),
                   bg = 'black',
                   fg = 'white')
    
splash_label.pack(pady=20)

test = ImageTk.PhotoImage(Image.open('compass.jpeg'))
labelimg = tk.Label(width=500,
                    height=500,
                    image=test)
labelimg.place(relx=0.5,rely=0.5,anchor='center')

def main_window():
    splash_root.destroy()
    import page2
    
#timer
splash_root.after(1000, main_window)

mainloop()
