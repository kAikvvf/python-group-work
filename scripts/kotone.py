import csv
import tkinter as  tk
from tkinter.scrolledtext import ScrolledText


class Qestion:
    def __init__(self, q_num, csv_file):
        self.q_num = q_num
        self.csv_file = csv_file
        


root = tkinter.Tk()
root.geometry("500x600")
root.title("test")
textbox = tkinter.Text(root,bg="white",fg="red",height=88)
textbox.pack()
root.mainloop()
#def __init__(self):
