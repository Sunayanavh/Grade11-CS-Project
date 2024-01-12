import tkinter as tk
from tkinter import ttk
from maintrial import text1

window = tk.Tk()
window.title('travel planner')
window.geometry('1400x800')
window.configure(bg = 'honeydew2')
window.attributes('-fullscreen',True)

def prevpage():
    window.destroy()
    import maintrial

#def nextpage():
    #window.destroy()

    
#months display
v1=text1.get()
if v1=='November' or v1=='December' or v1=='January':
    label1 = tk.Label(
            text = 'Winter months...',
            bg = 'honeydew2',
            fg = 'gray40',
            font = ('comic sans',20,'bold italic')
        ).place(relx=0.5,rely=0.2,anchor='center')
    label = tk.Label(
        text = 'check out suitable places on the map',
        borderwidth = 10,
        bg = 'honeydew2',
        fg = 'black',
        font = ('Times',30,'bold italic'),
    )
    label.place(relx=0.5,rely=0.5,anchor='center')
    def nextpage():
        window.destroy()
        import mapwinter

elif v1=='February' or v1=='March':
    label1 = tk.Label(
            text = 'Spring months...',
            bg = 'honeydew2',
            fg = 'gray40',
            font = ('comic sans',20,'bold italic')
        ).place(relx=0.5,rely=0.2,anchor='center')
    label = tk.Label(
        text = 'check out suitable places on the map',
        borderwidth = 10,
        bg = 'honeydew2',
        fg = 'black',
        font = ('Times',30,'bold italic'),
    )
    label.place(relx=0.5,rely=0.5,anchor='center')
    def nextpage():
        window.destroy()
        import mapspring

elif v1=='April' or v1=='May' or v1=='June':
    label1 = tk.Label(
        text = 'Summer months...',
        bg = 'honeydew2',
        fg = 'gray40',
        font = ('comic sans',20,'bold italic')
    ).place(relx=0.5,rely=0.2,anchor='center')
    label = tk.Label(
        text = 'check out suitable places on the map',
        borderwidth = 10,
        bg = 'honeydew2',
        fg = 'black',
        font = ('Times',30,'bold italic'),
    )
    label.place(relx=0.5,rely=0.5,anchor='center')
    def nextpage():
        window.destroy()
        import mapsummer
    
    
elif v1=='July' or v1=='August':
    label1 = tk.Label(
            text = 'Autumn months...',
            bg = 'honeydew2',
            fg = 'gray40',
            font = ('comic sans',20,'bold italic')
        ).place(relx=0.5,rely=0.2,anchor='center')
    label = tk.Label(
        text = 'check out suitable places on the map',
        borderwidth = 10,
        bg = 'honeydew2',
        fg = 'black',
        font = ('Times',30,'bold italic'),
    )
    label.place(relx=0.5,rely=0.5,anchor='center')
    def nextpage():
        window.destroy()
        import mapautumn

elif v1=='September' or v1=='October':
    label1 = tk.Label(
            text = 'Monsoon months...',
            bg = 'honeydew2',
            fg = 'gray40',
            font = ('comic sans',20,'bold italic')
        ).place(relx=0.5,rely=0.2,anchor='center')
    label = tk.Label(
        text = 'check out suitable places on the map',
        borderwidth = 10,
        bg = 'honeydew2',
        fg = 'black',
        font = ('Times',30,'bold italic'),
    )
    label.place(relx=0.5,rely=0.5,anchor='center')
    def nextpage():
        window.destroy()
        import mapmonsoon

button = tk.Button(
    text = 'MAP',
    bg = 'white',
    fg = 'black',
    font = ('Times',20,'bold'),
    command = nextpage,
).pack(side=tk.BOTTOM,pady=10)

window.mainloop()
