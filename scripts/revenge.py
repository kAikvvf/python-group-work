import tkinter as tk

class Quest:
    def __init__(self,canvas):

        self.canvas = canvas
        self.label_list()


    def frame_label(self):
        self.frame = tk.Frame()
        self.frame.pack()

    def label_list(self):
        label_area = tk.Frame(master=self.canvas)
        for i in range(1,11):
            self.label = tk.Label(label_area,
                                  text=f"{i},Question\n 目標回答時間：　分　　トピック ",
                                  bg="white",
                                  font=("メイリオ",12),
                                  )
            self.label.pack(padx=10,pady=5,fill='both',expand=True)

            self.label.bind("<Enter>",lambda e ,l=self.label:l.configure(bg="slategray1"))
            self.label.bind("<Leave>",lambda e ,l=self.label:l.configure(bg="white"))

        self.canvas.create_window(0,0,window=label_area,anchor="nw")


class Contents:
    def __init__(self,parent):
        
        self.frame_contents = tk.Frame(parent)


        self.contents_canvas()
        
        self.quest = Quest(self.cvs_contents)

    def contents_canvas(self):
        self.scroll = tk.Scrollbar(self.frame_contents,orient=tk.VERTICAL)
        self.scroll.pack(side=tk.RIGHT,fill=tk.Y)

        self.cvs_contents = tk.Canvas(self.frame_contents,bg="skyblue3",yscrollcommand=self.scroll.set)
        self.cvs_contents.pack(fill=tk.BOTH,expand=True)

        self.cvs_contents.configure(scrollregion=(0,0,0,650))
        self.cvs_contents.configure(yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.cvs_contents.yview)

class Score:
    def __init__(self,parent):
        self.frame_score = tk.Frame(parent)      

        self.score_canvas()
        self.chart()

    def score_canvas(self):
        self.scroll1 = tk.Scrollbar(self.frame_score,orient=tk.VERTICAL)
        self.scroll1.pack(side=tk.RIGHT,fill=tk.Y)

        self.cvs_score = tk.Canvas(self.frame_score,bg="skyblue3",yscrollcommand=self.scroll1.set)
        self.cvs_score.pack(fill=tk.BOTH,expand=True)

        self.cvs_score.configure(scrollregion=(0,0,0,2000))
        self.cvs_score.configure(yscrollcommand=self.scroll1.set)
        self.scroll1.config(command=self.cvs_score.yview)

    def chart(self):
        self.label_title = tk.Label(self.cvs_score,text="# 問題　合否　スコア")
        self.cvs_score.create_window(50,0,window=self.label_title,anchor="nw")

        for i in range(1,11):
            self.label1 = tk.Label(self.cvs_score,text=f"{i}",bg="white",font=("メイリオ",12))
            self.cvs_score.create_window(50,30*i,window=self.label1,anchor="nw")
    

class Code:
    def __init__(self,parent):
        self.frame_code = tk.Frame(parent)      

        self.code_canvas()
        self.chart()

    def code_canvas(self):
        self.scroll1 = tk.Scrollbar(self.frame_code,orient=tk.VERTICAL)
        self.scroll1.pack(side=tk.RIGHT,fill=tk.Y)

        self.cvs_code = tk.Canvas(self.frame_code,bg="skyblue3",yscrollcommand=self.scroll1.set)
        self.cvs_code.pack(fill=tk.BOTH,expand=True)

        self.cvs_code.configure(scrollregion=(0,0,0,2000))
        self.cvs_code.configure(yscrollcommand=self.scroll1.set)
        self.scroll1.config(command=self.cvs_code.yview)

    def chart(self):
        for i in range(1,11):
            self.label2 = tk.Label(self.cvs_code,text=f"{i},所要時間",bg="white",font=("メイリオ",12))
            self.cvs_code.create_window(50,50*i,window=self.label2,anchor="nw")

    
    

class Main:
    def __init__(self,root):

        self.root = root
        root.title(" ")
        screen_width = root.winfo_screenwidth() -1000
        screen_height = root.winfo_screenheight() - 300
        root.geometry(f"{screen_width}x{screen_height}")   


        self.main_frame()
        self.main_canvas()    
        self.button() 

        self.contents = Contents(self.frame_main)
        self.score = Score(self.frame_main)
        self.code = Code(self.frame_main)

        self.contents.frame_contents.pack(fill=tk.BOTH,expand=True)
        

    def main_frame(self):
        self.frame_main = tk.Frame()
        self.frame_main.pack(fill=tk.BOTH,expand=True)

    def main_canvas(self):
        self.cvs_main = tk.Canvas(self.frame_main,bg="white")
        self.cvs_main.pack(fill=tk.X)

    def button(self):
        self.btn_contents = tk.Button(self.cvs_main,text="コンテンツ",command=self.contents_btn)
        self.btn_contents.pack(side=tk.LEFT,padx=30,pady=25)

        self.btn_score = tk.Button(self.cvs_main,text="解答状況",command=self.score_btn)
        self.btn_score.pack(side=tk.LEFT,padx=30)

        self.btn_score = tk.Button(self.cvs_main,text="コード提出履歴",command=self.code_btn)
        self.btn_score.pack(side=tk.LEFT,padx=30)

    def contents_btn(self):
        self.score.frame_score.pack_forget()        
        self.contents.frame_contents.pack(fill=tk.BOTH,expand=True)
        self.code.frame_code.pack_forget()
  

    def score_btn(self):
        self.contents.frame_contents.pack_forget()
        self.score.frame_score.pack(fill=tk.BOTH,expand=True)
        self.code.frame_code.pack_forget()

    def code_btn(self):
        self.contents.frame_contents.pack_forget()
        self.score.frame_score.pack_forget()
        self.code.frame_code.pack(fill=tk.BOTH,expand=True)


root = tk.Tk()
Main(root)
root.mainloop()
