import tkinter as tk
from list import List

class Contents:
    def __init__(self,root):
        self.root = root
        self.list = List(self.root)

        self.list.canvas.bind("<Configure>",self.frame_canvas_width)
        self.frame_contents()
        self.desplay_label()






    #コンテンツ用フレーム１
    def frame_contents(self):
        self.frame1 = tk.Frame(self.list.canvas)
        self.canvas_window = self.list.canvas.create_window((0,100),window=self.frame1,anchor="nw")  

    #フレーム１自動調整
    def frame_canvas_width(self,event):
        self.list.canvas.itemconfig(self.canvas_window,width=event.width)

    #コンテンツ用メイン白色キャンバス
    def desplay_label(self):
        #スクロールバー
        self.scroll = tk.Scrollbar(self.frame1,orient=tk.VERTICAL)
        self.scroll.pack(side=tk.RIGHT,fill=tk.Y)
        
        #白色キャンバス
        self.canvas_back = tk.Canvas(self.frame1,bg="whitesmoke",yscrollcommand=self.scroll.set,height=1000)
        self.canvas_back.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)

        self.canvas_back.configure(scrollregion=(0,0,0,2000))
        self.canvas_back.configure(yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.canvas_back.yview)


    


    def label_frame(self):
        self.frame2 = tk.Frame(self.canvas_back)
        self.window2 = self.frame2.create_window((0,0),window=self.frame2,anchor="nw")
        self.frame2.bind("<Configure>",self.label_frame_width)
    
    def label_frame_width(self,event):
        self.canvas_back.itemconfig(self.window2,width=event.width)




class Quest:
    def __init__(self,root,index):
        self.root = root
        self.c = Contents(self.root)
        #self.question_label1()

        self.label1 = tk.Label(self.c.canvas_back,
                                text=f"{index},question\n \n目標回答時間：　分　　トピック：",
                                bg="white",
                                anchor=tk.W,
                                width=70)
        self.label1.pack(anchor="nw",pady=50)
        
        self.label1.bind("<Motion>",self.mouse_on1)
        self.label1.bind("<Leave>",self.mouse_leave1)

    def mouse_on1(self,event):
        self.label1["background"] = "slategray1"

    def mouse_leave1(self,event):
        self.label1["background"] = "white"


    def question_label2(self):
        self.label2 = tk.Label(self.c.canvas_back,
                                text="2,question\n \n目標回答時間：　分　　トピック：",
                                bg="white",
                                anchor=tk.W,
                                width=70)
        self.label2.pack(anchor="nw",pady=25)
        
        self.label2.bind("<Motion>",self.mouse_on2)
        self.label2.bind("<Leave>",self.mouse_leave2)

    def mouse_on2(self,event):
        self.label2["background"] = "slategray1"

    def mouse_leave2(self,event):
        self.label2["background"] = "white"

    def question_label3(self):
        self.label3 = tk.Label(self.c.canvas_back,
                                text="3,question\n \n目標回答時間：　分　　トピック：",
                                bg="white",
                                anchor=tk.W,
                                width=70)
        self.label3.pack(anchor="nw",pady=50)
        
        self.label3.bind("<Motion>",self.mouse_on3)
        self.label3.bind("<Leave>",self.mouse_leave3)

    def mouse_on3(self,event):
        self.label3["background"] = "slategray1"

    def mouse_leave3(self,event):
        self.label3["background"] = "white"


root = tk.Tk()
Contents(root)
root.mainloop()