from tkinter import *
from functools import partial
from input import KeyboardInput

def play(n1):
    text = str(n1.get())
    keyboard = KeyboardInput()
    keyboard.type_string(text, 5.0)
    return

window = Tk()

number1 = StringVar()  

txtfld = Entry(window, text="Digite o texto...", textvariable=number1, bd=5)
txtfld.place(x=80, y=30)
txtfld.grid_columnconfigure(1, weight=1)

play = partial(play, number1)  

btn = Button(window, text="Play", fg='blue', command=play)
btn.place(x=80, y=100)

window.title('Macro Typer')
window.geometry("300x200+10+10")
window.resizable(True, True) 
window.mainloop()