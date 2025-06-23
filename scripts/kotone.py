import csv
import tkinter as tk
from tkinter import scrolledtext

"""
class Myscrolledtext(tk.Frame):
    def __init__(self,parent,**kwargs):
        super().__init__(parent,**kwargs)
        #self.use_frame = use_frame
        #self.text1 = text1
        self.scrolledtext()

    def scrolledtext(self):
        self.scrolledtext = tk.Frame(self.use_frame)
        self.x_scroll = tk.Scrollbar(self.scrolledtext, orient="horizontal")
        self.y_scroll = tk.Scrollbar(self.scrolledtext, orient="vertical")
        self.x_scroll.pack(side="bottom", fill="x")
        self.y_scroll.pack(side="right", fill="y")

        self.textbox = tk.Text(self.scrolledtext, 
                               font=("メイリオ", 22), 
                               wrap="none", 
                               xscrollcommand=self.x_scroll.set, 
                               yscrollcommand=self.y_scroll.set)
        self.textbox.insert('1.0', self.text1)
        self.textbox.config(state="disabled")
        self.textbox.pack(side="left", fill="y", expand=True)
        self.textbox.pack()
        
        self.x_scroll.config(command=self.textbox.xview)
        self.y_scroll.config(command=self.textbox.yview)
       
        #self.scrolledtext.pack()

"""

class Qestion:
    def __init__(self, q_num):
        
        self.q_num = q_num #問題番号

        #メインウィンドウの作成
        self.root = tk.Tk()
        self.root.title("問題文")
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight() - 100
        self.root.geometry(f"{self.screen_width}x{self.screen_height}+0+0")

        #csvファイルからデータを読み込む
        self.csv_file()

        #フレーム
        self.left_frame()
        self.button_frame()
        self.return_frame()
        self.quest_frame()
        self.sample_frame()
        self.result_frame()

        #消すフレームをまとめた
        self.frames = {"return": self.return_frame,
                       "quest": self.quest_frame, 
                       "sample": self.sample_frame, 
                       "result": self.result_frame}
      
        self.root.mainloop()


    def csv_file(self):
        with open('quest-data.csv', 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i == self.q_num:
                    self.text = "\n".join(row)
                    break
        return self.text
                   

    #戻る    
    def return_click(self):
        for frame in self.frames.values():
            frame.pack_forget()
        self.return_frame.pack(side="left", fill="both", expand=True)
      

    #問題文
    def qest_click(self):
        for frame in self.frames.values():
            frame.pack_forget()
        self.quest_frame.pack(side="left", fill="both", expand=True)
       
        
    #サンプルケース
    def sample_click(self):
        for frame in self.frames.values():
            frame.pack_forget()
        self.sample_frame.pack(side="left", fill="both", expand=True)
     

    #結果
    def result_click(self):
        for frame in self.frames.values():
            frame.pack_forget()
        self.result_frame.pack(side="left", fill="both", expand=True)
      

    #フレームを乗せるフレーム
    def left_frame(self):
        self.left_frame =tk.Frame(self.root,width=self.screen_width/2)
        self.left_frame.pack(side="left", fill="y")
        self.left_frame.pack_propagate(False)

    
    #ボタンを置くフレーム
    def button_frame(self):
        #フレーム作成
        self.button_frame = tk.Frame(self.left_frame)

        #戻るボタン
        button1 = tk.Button(self.button_frame, text="<-戻る", command=self.return_click)
        button1.pack(side="left", padx=5, pady=5)

        #問題文ボタン
        button2 = tk.Button(self.button_frame, text="問題文", command=self.qest_click)
        button2.pack(side="left", padx=5, pady=5)

        #サンプルケースボタン
        button3 = tk.Button(self.button_frame, text="サンプルケース", command=self.sample_click)
        button3.pack(side="left", padx=5, pady=5)

        #結果ボタン
        button4 = tk.Button(self.button_frame, text="結果", command=self.result_click)
        button4.pack(side="left",padx=5, pady=5)

        self.button_frame.pack(side="top", anchor="nw")


    #----------ボタン押したら出てくるフレーム----------#
    def return_frame(self):
        #ここのは全部消す
        self.return_frame = tk.Frame(self.left_frame)
        a = "本当はまなみちゃんが作ったフレームを入れる"
        scrolledText = scrolledtext.ScrolledText(self.return_frame)
        scrolledText.insert('1.0', a)
        scrolledText.config(state="disabled")
        scrolledText.pack(side="left", fill="both", expand=True)
            
    
    def quest_frame(self):
        self.quest_frame = tk.Frame(self.left_frame)
        self.x_scroll = tk.Scrollbar(self.quest_frame, orient="horizontal")
        self.y_scroll = tk.Scrollbar(self.quest_frame, orient="vertical")
        self.x_scroll.pack(side="bottom", fill="x")
        self.y_scroll.pack(side="right", fill="y")

        self.textbox = tk.Text(self.quest_frame, 
                               font=("メイリオ", 15), 
                               wrap="none", 
                               xscrollcommand=self.x_scroll.set, 
                               yscrollcommand=self.y_scroll.set)
        self.textbox.insert('1.0', self.text)
        self.textbox.config(state="disabled")
        self.textbox.pack(side="left", fill="y", expand=True)
        self.textbox.pack()
        
        self.x_scroll.config(command=self.textbox.xview)
        self.y_scroll.config(command=self.textbox.yview)
        """
        self.quest_frame = tk.Frame(self.left_frame)
        scrolledText1 = scrolledtext.ScrolledText(self.quest_frame, font=("メイリオ", 12))
        scrolledText1.insert('1.0', self.text)
        scrolledText1.config(state="disabled")
        scrolledText1.pack(side="left", fill="both", expand=True)
        """
      

    def sample_frame(self):
        self.sample_frame = tk.Frame(self.left_frame)
        self.x_scroll = tk.Scrollbar(self.sample_frame, orient="horizontal")
        self.y_scroll = tk.Scrollbar(self.sample_frame, orient="vertical")
        self.x_scroll.pack(side="bottom", fill="x")
        self.y_scroll.pack(side="right", fill="y")

        self.textbox = tk.Text(self.sample_frame, 
                               font=("メイリオ", 15), 
                               wrap="none", 
                               xscrollcommand=self.x_scroll.set, 
                               yscrollcommand=self.y_scroll.set)
        a = "サンプルケース\nここにCSVで書かれた文を入れたい。\nけど、やり方が分からない…。\nもっと頑張らなきゃ。"
        self.textbox.insert('1.0', a)
        self.textbox.config(state="disabled")
        self.textbox.pack(side="left", fill="y", expand=True)
        self.textbox.pack()
        
        self.x_scroll.config(command=self.textbox.xview)
        self.y_scroll.config(command=self.textbox.yview)
        """
        self.sample_frame = tk.Frame(self.left_frame)
        a = "サンプルケース\nここにCSVで書かれた文を入れたい。\nけど、やり方が分からない…。\nもっと頑張らなきゃ。"
        scrolledText2 = scrolledtext.ScrolledText(self.sample_frame)
        scrolledText2.insert('1.0', a)
        scrolledText2.config(state="disabled")
        scrolledText2.pack(side="left", fill="both", expand=True)
        """
      

    def result_frame(self):
        self.result_frame = tk.Frame(self.left_frame)
        self.x_scroll = tk.Scrollbar(self.result_frame, orient="horizontal")
        self.y_scroll = tk.Scrollbar(self.result_frame, orient="vertical")
        self.x_scroll.pack(side="bottom", fill="x")
        self.y_scroll.pack(side="right", fill="y")

        self.textbox = tk.Text(self.result_frame, 
                               font=("メイリオ", 15), 
                               wrap="none", 
                               xscrollcommand=self.x_scroll.set, 
                               yscrollcommand=self.y_scroll.set)
        a = "結果\nここにCSVで書かれた文を入れたい。\nけど、やり方が分からない…。\nもっと頑張らなきゃ。"
        self.textbox.insert('1.0', a)
        self.textbox.config(state="disabled")
        self.textbox.pack(side="left", fill="y", expand=True)
        self.textbox.pack()
        
        self.x_scroll.config(command=self.textbox.xview)
        self.y_scroll.config(command=self.textbox.yview)
        """
        self.result_frame = tk.Frame(self.left_frame)
        a = "結果\nここにCSVで書かれた文を入れたい。\nけど、やり方が分からない…。\nもっと頑張らなきゃ。"
        scrolledText3 = scrolledtext.ScrolledText(self.result_frame)
        scrolledText3.insert('1.0', a)
        scrolledText3.config(state="disabled")
        scrolledText3.pack(side="left", fill="both", expand=True)
        """

        #--------------------#
     

Qestion(0)     


#次までに全部フレームに入れて、フレームごと消せるように。サンプルけして、問題文表示みたいな






