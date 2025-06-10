import tkinter as tk

class list:
    def __init__(self,root):
        
        self.root = root
        self.root.title(" ")
        self.root.geometry("900x600")
        
        self.start_screen()
        
    def start_screen(self):
        
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