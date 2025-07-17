import tkinter as tk
import datetime
from scripts import questDataHandler
from scripts.userDataHanlder import userDataHandler
from scripts.kotone import Question

class Quest:
    def __init__(self,master,username,quest_index,window_root,quest_list_page,answer_page):

        self.root = master

        user_status_in_index = userDataHandler(username).getStatus(quest_index)
        status = '未達成'
        if user_status_in_index == 'True':
            status = '合格'
        self.quest_choose_button = tk.Button(self.root,
                              text=f"{quest_index+1}, {questDataHandler.getTitle(quest_index)}    回答状況：{status}\n 目標回答時間：{questDataHandler.getEstimatedRequredTime(quest_index)} 分",
                              bg="white",
                              font=("メイリオ",12),
                              relief='groove',
                              justify="left",
                              activebackground="#44BBFF",
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

            self.answering_page.return_button.config(command=return_to_choose_page)

        self.quest_choose_button.config(command=start_answring)


class Contents:
    def __init__(self,parent,username,window_root,quest_list_page,answer_page):
        
        self.frame_contents = tk.Frame(parent)

        self.contents_canvas()
        
        self.contents_scroll = tk.Frame(self.cvs_contents)
        quest_button_list = []
        for i in range(questDataHandler.getNumOfQuest()):
            self.quest = Quest(self.contents_scroll,username,i,window_root,quest_list_page,answer_page)
            quest_button_list.append(self.quest)
        self.contents_scroll.pack(fill="both",expand=True)

        scroll_region = 80*questDataHandler.getNumOfQuest()
        self.cvs_contents.create_window((0,0),window=self.contents_scroll,width=400,height=scroll_region,anchor='nw')
        self.cvs_contents.configure(scrollregion=(0,0,0,scroll_region))

    def contents_canvas(self):
        self.scroll = tk.Scrollbar(self.frame_contents,orient=tk.VERTICAL)
        self.scroll.pack(side=tk.RIGHT,fill=tk.Y)

        self.cvs_contents = tk.Canvas(self.frame_contents,bg="skyblue3",yscrollcommand=self.scroll.set)
        self.cvs_contents.pack(fill=tk.BOTH,expand=True)

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
    def __init__(self,parent,username):
        self.frame_code = tk.Frame(parent)      

        self.username = username

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
        for i in range(questDataHandler.getNumOfQuest()):
            status = '未回答'
            required_time = '-'
            if userDataHandler(self.username).getStatus(i) == 'True':
                required_time = userDataHandler(self.username).getEndTime(i) - userDataHandler(self.username).getStartTime(i)
                status = f'合格済 (スコア：{userDataHandler(self.username).getScore(i)} , 所要時間：{required_time} , 提出日時：{userDataHandler(self.username).getEndTime(i)})'
            elif userDataHandler(self.username).getStatus(i) == 'false' and not userDataHandler(self.username).getStartTime(i) == 'null':
                status = '回答中'

            self.label2 = tk.Label(self.cvs_code,text=f"{i+1}, ステータス：{status}",bg="white",font=("メイリオ",12))
            self.cvs_code.create_window(50,50*i,window=self.label2,anchor="nw")

    
    

class Main:
    def __init__(self,root,username,answe_page):

        self.root = root

        self.frame_main = root
        self.main_canvas()    
        self.button() 

        self.contents = Contents(self.frame_main,username,root,self.frame_main,answe_page)
        self.score = Score(self.frame_main)
        self.code = Code(self.frame_main,username)

        self.contents.frame_contents.pack(fill=tk.BOTH,expand=True)

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