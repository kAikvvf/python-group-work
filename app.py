from tkinter import *
from scripts.prompt import prompt

root = Tk()
root.title("Python-Techful")

cmd_prompt = prompt(root_Tk=root,
                    width=40,row=10,
                    input_pack_padx=30,
                    input_pack_pady=30,
                    input_font_size=12
                    )

root.mainloop()