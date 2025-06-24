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
        self.canvas = tk.Canvas(self.root,bg="white")
        self.frame = tk.Frame(self.canvas)

        self.scrollbar = tk.Scrollbar(self.canvas,orient=tk.VERTICAL,command=self.canvas.yview)

        self.button = tk.Button(self.frame,text="Hello")

        self.canvas.configure(scrollregion=(0,0,900,900))
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side=tk.RIGHT,fill=tk.Y)
        self.canvas.pack(expand=True,fill=tk.BOTH)
        self.button.pack(expand=1)

        self.canvas.create_window((0,0),window=self.frame,anchor="nw",width=900,height=900)
        

        
        
root = tk.Tk()
game = list(root)
root.mainloop()
