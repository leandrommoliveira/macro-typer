from tkinter import *
from functools import partial
from input import KeyboardInput

def play(textValue, delayValue):
    text = str(textValue.get())

    delay = float(delayValue.get())

    keyboard = KeyboardInput()
    keyboard.type_string(text, delay)
    return

window = Tk()

textValue = StringVar()
delayValue = IntVar()

txtfld = Entry(window, text="Digite o texto...", textvariable=textValue, bd=5)
txtfld.place(x=80, y=30)
txtfld.grid_columnconfigure(1, weight=1)

spin = Spinbox(window, from_= 0, to = 25, state="readonly", textvariable=delayValue)
spin.place(x=80, y = 70)  
spin.grid_columnconfigure(1, weight=1)

play = partial(play, textValue, delayValue)  

btn = Button(window, text="Play", fg='blue', command=play)
btn.place(x=80, y=100)

window.title('Macro Typer')
window.geometry("300x200+10+10")
window.resizable(True, True) 
window.mainloop()