import tkinter as tk

class list:
    def __init__(self,root):
        
        self.root = root
        self.root.title(" ")
        self.root.geometry("900x600")
        
        self.start_screen()
        
    def start_screen(self):
        
        self.canvas = tk.Canvas(self.root, bg="white")
        self.canvas.place(x=0, y=0, width=900, height=600)
        
        self.bar_y = tk.Scrollbar(self.canvas, orient=tk.VERTICAL)
        self.bar_y.pack(side=tk.RIGHT, fill=tk.Y)
        self.bar_y.config(command=self.canvas.yview)
        self.canvas.config(yscrollcommand=self.bar_y.set)

        self.canvas.config(scrollregion=(0, 0, 300, 900))
        
        

        
root = tk.Tk()
game = list(root)
root.mainloop()