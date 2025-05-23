from tkinter import *
from scripts.prompt import prompt

root = Tk()
root.title("Python-Techful")
root.geometry("600x400")

# プロンプトの設定
cmd_prompt = prompt(root_Tk=root,
                    input_font_size=12
                    )
cmd_prompt.show() #プロンプトを表示するプログラム

hide_but = Button(master=root,text="hide",command=cmd_prompt.hide)
show_but = Button(master=root,text="show",command=cmd_prompt.show)

hide_but.pack(side=LEFT)
show_but.pack(side=LEFT)

root.mainloop()