import tkinter as tk
from contents_label import Contents
from list import List

class Score_status:
    def __init__(self,root):
        self.root = root
        self.screen = List(self.root)

        self.contents = Contents(self.root)
        self.contents.desplay_label()

        self.contents_button = tk.Button(self.root,text="コンテンツ",bg="white",)
        self.contents_button.place(x=10,y=50)

    def score(self):

        self.score_back = tk.Canvas(self.root,bg="whitesmoke")
        self.screen.canvas.create_window(280,550,window=self.score_back)


root = tk.Tk()
root.geometry('600x400')
Score_status(root)
root.mainloop()