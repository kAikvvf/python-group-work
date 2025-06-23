import tkinter as tk

class List:
    def __init__(self,root):
        
        self.root = root
        self.root.title(" ")
        self.root.geometry("600x400")
        
        self.start_screen()
        
    def start_screen(self):
        
        self.canvas = tk.Canvas(self.root, bg="skyblue3")
        self.canvas.place(x=0, y=0, width=600, height=400)
        

        self.bar_y = tk.Scrollbar(self.canvas, orient=tk.VERTICAL)
        self.bar_y.pack(side=tk.RIGHT, fill=tk.Y)
        self.bar_y.config(command=self.canvas.yview)
        self.canvas.config(yscrollcommand=self.bar_y.set)

        self.canvas.config(scrollregion=(0, 0, 300, 900))  