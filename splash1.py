import tkinter as tk    
from PIL import ImageTk, Image

splash_window=tk.Tk()
splash_window.title('splash screeeeen!!')
splash_window.geometry('1400x800')
splash_window.configure(bg = 'black')
splash_window.overrideredirect(True)   #to hide title bar
splash_label=tk.Label(splash_window,text='~welcome to....',
                   font = ('Times',40,'bold italic'),
                   bg = 'black',
                   fg = 'white')

test = ImageTk.PhotoImage(Image.open('yaatra.jpeg'))
labelimg = tk.Label(width=1000,
                    height=600,
                    image=test)
labelimg.place(relx=0.5,rely=0.5,anchor='center')
    
splash_label.pack(pady=20)

def main_window():
    splash_window.destroy()
    import page2
    
#timer
splash_window.after(3000, main_window)

splash_window.mainloop()
