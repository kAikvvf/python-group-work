from tkinter import *
from scripts.prompt import editor
from scripts import questDataExtracter

root = Tk()
root.title("Python-Techful")
root.geometry("1000x500")

# プロンプトの設定
cmd_prompt = editor(master=root,question_index=1)

quest_statement = Label(master=root,text=questDataExtracter.questStatement(quest_index=1))
quest_statement.pack(anchor="nw")

root.mainloop()