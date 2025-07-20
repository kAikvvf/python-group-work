import tkinter as tk
from tkinter import messagebox
import datetime
from scripts import questDataHandler
from scripts.userDataHanlder import userDataHandler
from scripts.kotone import Question

class Quest:
    def __init__(self,master,username,quest_index,window_root,quest_list_page,answer_page,reload_func):

        self.root = master

        user_status_in_index = userDataHandler(username).getStatus(quest_index)
        status = '未回答'
        if user_status_in_index == 'True':
            status = '合格'
        if user_status_in_index == 'False' and not userDataHandler(username).getStartTime(quest_index) == 'null':
            status = '回答中'
        self.quest_choose_button = tk.Button(self.root,
                              text=f"{quest_index+1}, {questDataHandler.getTitle(quest_index)}    回答状況：{status}\n   目標回答時間：{questDataHandler.getEstimatedRequredTime(quest_index)} 分",
                              bg="white",
                              font=("メイリオ",12),
                              relief='groove',
                              justify="left",
                              )
        self.quest_choose_button.pack(padx=10,pady=5,fill='both',expand=True)

        self.quest_choose_button.bind("<Enter>",lambda e ,l=self.quest_choose_button:l.configure(bg="slategray1"))
        self.quest_choose_button.bind("<Leave>",lambda e ,l=self.quest_choose_button:l.configure(bg="white"))

        self.answering_page = ''
        def start_answring():
            self.answering_page = Question(answer_page,quest_index,username)
            quest_list_page.forget()
            answer_page.pack(fill='both',expand=True)

            def return_to_choose_page():
                self.answering_page.hide()
                answer_page.forget()
                quest_list_page.pack(fill='both',expand=True)
                reload_func()

            self.answering_page.return_button.config(command=return_to_choose_page)

        self.quest_choose_button.config(command=start_answring)


class Contents:
    def __init__(self,parent,username,window_root,quest_list_page,answer_page,reload_func):
        
        self.frame_contents = tk.Frame(parent)

        self.contents_canvas()
        
        self.contents_scroll = tk.Frame(self.cvs_contents)
        quest_button_list = []
        for i in range(questDataHandler.getNumOfQuest()):
            self.quest = Quest(self.contents_scroll,username,i,window_root,quest_list_page,answer_page,reload_func)
            quest_button_list.append(self.quest)
        self.contents_scroll.pack(fill="both",expand=True)

        scroll_region = 80*questDataHandler.getNumOfQuest()

        def getWindowWidth(e):
            window_width = int(window_root.winfo_width())-20
            self.cvs_contents.itemconfig(view_window,width=window_width)
            self.cvs_contents.config(height=window_width-30)
        
        window_root.bind("<Configure>",getWindowWidth)

        view_window = self.cvs_contents.create_window((0,0),window=self.contents_scroll,width=int(window_root.winfo_width()-20),height=scroll_region,anchor='nw')
        self.cvs_contents.configure(scrollregion=(0,0,0,scroll_region))

    def contents_canvas(self):
        self.scroll = tk.Scrollbar(self.frame_contents,orient=tk.VERTICAL)
        self.scroll.pack(side=tk.RIGHT,fill=tk.Y)

        self.cvs_contents = tk.Canvas(self.frame_contents,yscrollcommand=self.scroll.set)
        self.cvs_contents.pack(fill=tk.BOTH,expand=True)

        self.cvs_contents.configure(yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.cvs_contents.yview)
"""
class Score:
    def __init__(self,parent,username):
        self.frame_score = tk.Frame(parent)
        self.username = username
        self.user_data_handler = userDataHandler(self.username)

        self.score_canvas()
        self.chart()

    def score_canvas(self):
        total_score = 0
        for i in range(questDataHandler.getNumOfQuest()):
            total_score += int(self.user_data_handler.getScore(i))
        
        tk.Label(self.frame_score,text=f'合計スコア : {total_score}',font=("メイリオ",12)).pack(fill="x")
        
        self.scrolly = tk.Scrollbar(self.frame_score,orient=tk.VERTICAL)
        self.scrolly.pack(side=tk.RIGHT,fill=tk.Y)

        self.cvs_score = tk.Canvas(self.frame_score,bg="skyblue3",yscrollcommand=self.scrolly.set)
        self.cvs_score.pack(fill=tk.BOTH,expand=True)

        self.cvs_score.configure(scrollregion=(0,0,0,28*questDataHandler.getNumOfQuest()))
        self.cvs_score.configure(yscrollcommand=self.scrolly.set)
        self.scrolly.config(command=self.cvs_score.yview)

    def chart(self):
        self.score_scroll_frame = tk.Frame(self.cvs_score)
        tk.Label(self.score_scroll_frame,text="#",font=("メイリオ",12),padx=5,pady=2).grid(column=0,row=0)
        tk.Label(self.score_scroll_frame,text="問題",font=("メイリオ",12),padx=5,pady=2).grid(column=1,row=0)
        tk.Label(self.score_scroll_frame,text="合否",font=("メイリオ",12),padx=5,pady=2).grid(column=2,row=0)
        tk.Label(self.score_scroll_frame,text="スコア",font=("メイリオ",12),padx=5,pady=2).grid(column=3,row=0)

        for i in range(questDataHandler.getNumOfQuest()):
            tk.Label(self.score_scroll_frame,text=f"{i+1}",font=("メイリオ",12),padx=5,pady=2).grid(column=0,row=i+1)
            tk.Label(self.score_scroll_frame,text=questDataHandler.getTitle(i),font=("メイリオ",12),padx=5,pady=2).grid(column=1,row=i+1)
            status = '未回答'
            score = '-'
            if self.user_data_handler.getStatus(i) == 'False' and self.user_data_handler.getStartTime(i) == True:
                status = '回答中'
            elif self.user_data_handler.getStatus(i) == 'True':
                status = '合格済'
                score = self.user_data_handler.getScore(i)
            tk.Label(self.score_scroll_frame,text=status,font=("メイリオ",12),padx=5,pady=2).grid(column=2,row=i+1)
            tk.Label(self.score_scroll_frame,text=score,font=("メイリオ",12),padx=5,pady=2).grid(column=3,row=i+1)
        
        def getWindowWidth(e):
            window_width = int(self.frame_score.winfo_width())-20
            self.cvs_score.itemconfig(view_window,width=window_width)
            self.cvs_score.config(height=window_width-30)
        
        self.frame_score.bind("<Configure>",getWindowWidth)
        view_window = self.frame_score.create_window(0,0,window=self.score_scroll_frame,anchor="nw",width=int(self.frame_score.winfo_width()-20),height=28*questDataHandler.getNumOfQuest())
"""
class Code:
    def __init__(self,parent,username):
        self.frame_code = tk.Frame(parent)      

        self.username = username

        self.code_canvas()
        self.chart()

    def code_canvas(self):
        self.scrolly = tk.Scrollbar(self.frame_code,orient=tk.VERTICAL)
        self.scrollx = tk.Scrollbar(self.frame_code,orient=tk.HORIZONTAL)
        self.scrolly.pack(side=tk.RIGHT,fill='y')
        self.scrollx.pack(side=tk.BOTTOM,fill='x')

        self.cvs_code = tk.Canvas(self.frame_code,yscrollcommand=self.scrolly.set,xscrollcommand=self.scrollx.set)
        self.cvs_code.pack(fill=tk.BOTH,expand=True)

        self.cvs_code.configure(scrollregion=(0,0,800,800))
        self.scrolly.config(command=self.cvs_code.yview)
        self.scrollx.config(command=self.cvs_code.xview)

    def chart(self):
        for i in range(questDataHandler.getNumOfQuest()):
            status = '未回答'
            required_time = '-'
            if userDataHandler(self.username).getStatus(i) == 'True':
                required_time = userDataHandler(self.username).getEndTime(i) - userDataHandler(self.username).getStartTime(i)
                status = f'合格済 (スコア：{userDataHandler(self.username).getScore(i)} , 所要時間：{required_time} , 提出日時：{userDataHandler(self.username).getEndTime(i)})'
            elif userDataHandler(self.username).getStatus(i) == 'False' and not userDataHandler(self.username).getStartTime(i) == 'null':
                status = '回答中'

            self.label2 = tk.Label(self.cvs_code,text=f"{i+1}, ステータス：{status}",bg="white",font=("メイリオ",12))
            self.cvs_code.create_window(30,50*i,window=self.label2,anchor="nw")

    
    

class Main:
    def __init__(self,root,username,answe_page,window_root):

        self.root = root
        self.username = username
        self.answer_page = answe_page
        self.window_root = window_root

        self.frame_main = root
        self.frame_main.pack(fill="both",expand=True)
        self.main_canvas()    
        self.button() 

        self.contents = Contents(self.frame_main,username,window_root,self.frame_main,answe_page,self.reload)
        #self.score = Score(self.frame_main,username)
        self.code = Code(self.frame_main,username)

        self.contents.frame_contents.pack(fill=tk.BOTH,expand=True)

    def main_canvas(self):
        self.cvs_main = tk.Canvas(self.frame_main,bg="white")
        self.cvs_main.pack(fill=tk.X)

    def button(self):
        self.btn_contents = tk.Button(self.cvs_main,text="コンテンツ",command=self.contents_btn)
        self.btn_contents.pack(side=tk.LEFT,padx=7,pady=10)

        #self.btn_score = tk.Button(self.cvs_main,text="解答状況",command=self.score_btn)
        #self.btn_score.pack(side=tk.LEFT,padx=15)

        self.btn_score = tk.Button(self.cvs_main,text="コード提出履歴",command=self.code_btn)
        self.btn_score.pack(side=tk.LEFT,padx=7)

        def how_to_use():
            messagebox.showinfo('使い方','[コンテンツ] ボタン :\n\t押すと問題選択するページが表示される。\n[コード提出履歴] ボタン :\n\t押すとすべての問題の回答状況・提出履歴が表示される。\n問題の解答方法 :\n\t① まず [コンテンツ] ボタンを押して問題選択のページを開く\n\t② 表示されている問題を選択する。\n\t③ 問題文を読んで右のエディターにプログラムを記入する。\n\t④ サンプル実行を押すとプログラムが実行される。\n\t    [サンプル] タブで実行結果を表示する。\n\t    もし、各サンプルケースの表示が青かったら、成功\n\t⑤ もし、プログラムがあっていると思ったら、[採点] ボタンを押す。\n\n-----採点基準-----\n- どれだけ目標回答時間内にとけたか\n- 採点回数\n----------')

        self.how_to_use_button = tk.Button(self.cvs_main,text='使い方',command=how_to_use)
        self.how_to_use_button.pack(side=tk.RIGHT,padx=7)

        total_score = 0
        for i in range(questDataHandler.getNumOfQuest()):
            total_score += int(userDataHandler(self.username).getScore(i))
        tk.Label(self.cvs_main,text=f'合計スコア : {total_score}',font=("メイリオ",12)).pack(side=tk.RIGHT,padx=7)

    def contents_btn(self):
        #self.score.frame_score.pack_forget()        
        self.contents.frame_contents.pack(fill=tk.BOTH,expand=True)
        self.code.frame_code.pack_forget()
  
    def score_btn(self):
        self.contents.frame_contents.pack_forget()
        #self.score.frame_score.pack(fill=tk.BOTH,expand=True)
        self.code.frame_code.pack_forget()

    def code_btn(self):
        self.contents.frame_contents.pack_forget()
        #self.score.frame_score.pack_forget()
        self.code.frame_code.pack(fill=tk.BOTH,expand=True)
    
    def reload(self):
        self.frame_main.destroy()
        self.root = tk.Frame(self.window_root)
        self.root.pack(fill="both",expand=True)
        self.__init__(self.root,self.username,self.answer_page,self.window_root)