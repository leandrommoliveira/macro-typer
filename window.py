from tkinter import *
from functools import partial
from input import KeyboardInput

def play(textValue, delayValue, selectValue):
    text = str(textValue.get())

    delay = float(delayValue.get())

    keyboard = KeyboardInput()
    if selectValue.get():
        text = text.upper()

    keyboard.type_string(text, delay)
    return

window = Tk()

textValue = StringVar()
delayValue = IntVar()
selectValue = BooleanVar()

txtfld = Entry(window, text="Digite o texto...", textvariable=textValue, bd=5)
txtfld.place(x=80, y=30)
txtfld.grid_columnconfigure(1, weight=1)

spin = Spinbox(window, from_= 0, to = 25, state="readonly", textvariable=delayValue)
spin.place(x=80, y = 70)  
spin.grid_columnconfigure(1, weight=1)

radio = BooleanVar()  
lbl = Label(text = "Escolha como o texto deve ser digitado:")  
lbl.pack() 
lbl.place(x=80, y = 100) 
R1 = Radiobutton(window, text="upper", variable=radio, value=TRUE)  
R1.place(x=80, y = 120) 
  
R2 = Radiobutton(window, text="original", variable=radio, value=FALSE) 
R2.place(x=80, y = 150)  

play = partial(play, textValue, delayValue, radio) 

btn = Button(window, text="Play", fg='blue', command=play)
btn.place(x=80, y=180)

  

window.title('Macro Typer')
window.geometry("400x220+10+10")
window.resizable(True, True) 
window.mainloop()
