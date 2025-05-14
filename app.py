from tkinter import *
from tkinter import ttk
from libraries.codeDebugger import codeDebugger

root = Tk()
root.title("Hello World")

input_area = Text(root,width=30)
input_area.pack(padx= 20,pady=10)

def confirm_prog():
    prog = input_area.get("1.0",END)
    print(prog)
    print(type(prog))
    debug = codeDebugger.debug(prog)
    print(debug)

confirm_button = Button(command=confirm_prog)
confirm_button.pack()

root.mainloop()