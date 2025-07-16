import tkinter as tk

class List:
    def __init__(self,root):
        
        self.root = root
        self.root.title(" ")
        self.screen_width = self.root.winfo_screenwidth() -1000
        self.screen_height = self.root.winfo_screenheight() - 300
        self.root.geometry(f"{self.screen_width}x{self.screen_height}")
        
        self.frame()

        self.canvas = tk.Canvas(self.frame, bg="skyblue3")   
        self.canvas.pack(fill=tk.BOTH,expand=True) 

    

        #self.scrollbar()
        self.title()
    
        
    def scrollbar(self):
        
        self.scrollbar = tk.Scrollbar(self.canvas,orient=tk.VERTICAL,command=self.canvas.yview)

        self.canvas.configure(scrollregion=(0,0,self.root.winfo_screenwidth(),2000))
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.pack(expand=True,fill=tk.BOTH)
        self.scrollbar.pack(side=tk.RIGHT,fill=tk.Y)

        

    def title(self):
        #各メイン画面用のframeを作る
        self.frame_title = tk.Frame(self.canvas,bg="skyblue3")
        self.canvas.create_window((0,0),window=self.frame_title,anchor="nw")  

        #３つのメイン画面切り替えのボタン配置
        self.contents_b =tk.Button(self.frame_title,text="コンテンツ")
        self.contents_b.pack(side="left",pady=50,padx=15)  

        self.score_b = tk.Button(self.frame_title,text="解答状況")    
        self.score_b.pack(side="left",padx=15)

        self.code_b = tk.Button(self.frame_title,text="コード提出履歴")
        self.code_b.pack(side="left",padx=15)


    def frame(self):
        self.frame = tk.Frame(self.root)
        #self.frame.pack(side="left", fill="y")
        self.frame.pack(fill=tk.BOTH,expand=True)    