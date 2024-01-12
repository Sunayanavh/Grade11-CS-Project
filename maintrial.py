# https://realpython.com/python-gui-tkinter/

import tkinter as tk
from PIL import ImageTk, Image


#in command prompt upgrade pip3 and install pillow

window = tk.Tk()
window.title('travel planner')
window.geometry('1400x800')
window.attributes('-fullscreen',True)
window.configure(bg = 'honeydew2')

def nextpage():
    window.destroy()
    import splash2

label1 = tk.Label(
    text = '~Live your life by a compass not a clock~',
    bg = 'honeydew2',
    fg = 'gray40',
    font = ('comic sans',20,'bold italic')
).place(relx=0.5,rely=0.2,anchor='center')

#inserting image

test1 = ImageTk.PhotoImage(Image.open('beach2.jpeg'))
labelimg1 = tk.Label(width=350,
                    height=180,
                    image=test1)
labelimg1.place(relx=0.02,rely=0.1,anchor='nw')

test2 = ImageTk.PhotoImage(Image.open('waterfall1.jpeg'))
labelimg2 = tk.Label(width=350,
                    height=180,
                    image=test2)
labelimg2.place(relx=0.95,rely=0.95,anchor='se')

test3 = ImageTk.PhotoImage(Image.open('mountain1.jpeg'))
labelimg3 = tk.Label(width=320,
                    height=165,
                    image=test3)
labelimg3.place(relx=0.95,rely=0.1,anchor='ne')

test4 = ImageTk.PhotoImage(Image.open('snow1.jpeg'))
labelimg4 = tk.Label(width=330,
                    height=200,
                    image=test4)
labelimg4.place(relx=0.02,rely=0.95,anchor='sw')

label = tk.Label(
    text = 'Hello, my fellow traveller!\n\
    Need help finding the perfect spot for your vacation?\n\
    Simply enter a month of your choice and start planning your trip!',
    borderwidth = 10,
    bg = 'honeydew2',
    fg = 'black',
    font = ('Times',30,'bold italic'),
)
label.place(relx=0.5,rely=0.5,anchor='center')

label2 = tk.Label(
    text = 'select month:',
    bg = 'honeydew2',
    fg = 'black',
    font = ('Comic Sans',20),
)
label2.place(relx=0.5,rely=0.85,anchor='center')

text1 = tk.StringVar()
text1.set('choose here')
w = tk.OptionMenu(window,text1,
               'January','February','March','April','May',\
               'June','July','August','September','October',\
               'November','December',
)
w.place(relx=0.5,rely=0.9,anchor='center')

button = tk.Button(
    text = 'start planning!',
    bg = 'white',
    fg = 'black',
    font = ('Times',20,'bold'),
    command = nextpage,
).pack(side=tk.BOTTOM,pady=10)

window.mainloop()
