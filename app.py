from tkinter import *
from scripts import questDataExtracter
from scripts.editorPage import editorPage

root = Tk()
root.title("Python-Techful")
root.geometry("1000x500")

editorPage(master=root,question_index=1)

quest_statement = Label(master=root,text=questDataExtracter.questStatement(quest_index=1))
quest_statement.pack(anchor="nw")

root.mainloop()