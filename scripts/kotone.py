from tkinter import *
from scripts.prompt import editor
from scripts.samplePage import sampleDisplay
from scripts import questDataHandler
from scripts.scoringPage import scoringDisplay
from scripts.userDataHanlder import userDataHandler

class Question:
    def __init__(self,master,question_index,username):
        self.root = Canvas(master=master)
        self.root.pack(fill="both",expand=1)
        self.question_index = question_index
        self.username = username

        self.user_data_handeler = userDataHandler(self.username)

        if userDataHandler(self.username).getStartTime(self.question_index+1) == 'null':
            self.user_data_handeler.setStartTime(self.question_index+1)

        #タブ切り替えボタン
        self.tab = Frame(master=self.root)
        self.tab.place(relheight=1.0,relwidth=0.5)
        
        self.button_frame = Frame(master=self.tab)
        self.button_frame.pack(anchor='nw')

        self.return_button = Button(master=self.button_frame,text="<-戻る")
        self.quest_tab_button = Button(master=self.button_frame,text="問題",command=self.showQuestTab)
        self.debug_tab_button = Button(master=self.button_frame,text="サンプル",command=self.showSampleTab)
        self.result_tab_button = Button(master=self.button_frame,text="結果",command=self.showResultTab)
        
        self.return_button.pack(side='left',padx=5,pady=5)
        self.quest_tab_button.pack(side='left',padx=5,pady=5)
        self.debug_tab_button.pack(side='left',padx=5,pady=5)
        self.result_tab_button.pack(side='left',padx=5,pady=5)

        self.editor = editor(master=self.root,question_index=self.question_index)
        self.editor.sample_debug_button.config(command=self.debug)

        #---問題文 タブ設定---
        self.quest_tab = Frame(master=self.tab)
        self.y_scroll = Scrollbar(self.quest_tab, orient="vertical")
        self.y_scroll.pack(side="right", fill="y")

        self.textbox = Text(self.quest_tab, 
                               font=("メイリオ", 12), 
                               wrap="word", 
                               xscrollcommand=self.y_scroll.set)
        self.textbox.insert('1.0', questDataHandler.getQuestStatement(question_index).replace('\\n','\n'))
        self.textbox.config(state="disabled")
        self.textbox.pack(side="left", fill="y", expand=True)
        self.textbox.pack()

        #---サンプル タブ設定---
        self.sample_tab = Frame(master=self.tab)
        self.sampleDisplay = sampleDisplay(master=self.sample_tab,quest_index=self.question_index,result=[{'result':'','matches':'none'},{'result':'','matches':'none'},{'result':'','matches':'none'},{'result':'','matches':'none'},{'result':'','matches':'none'},{'result':'','matches':'none'},{'result':'','matches':'none'},{'result':'','matches':'none'}])

        #---結果 タブ設定---
        self.result_tab = Frame(master=self.tab)
        self.score_display = scoringDisplay(self.result_tab,question_index,result=[{'result':'','matches':'none'},{'result':'','matches':'none'},{'result':'','matches':'none'},{'result':'','matches':'none'},{'result':'','matches':'none'},{'result':'','matches':'none'},{'result':'','matches':'none'},{'result':'','matches':'none'}],username=self.username,prog='')
        if self.user_data_handeler.getStatus(self.question_index+1) == 'none':
            self.score_display = scoringDisplay(self.result_tab,question_index,result=[{'result':'','matches':'none'},{'result':'','matches':'none'},{'result':'','matches':'none'},{'result':'','matches':'none'},{'result':'','matches':'none'},{'result':'','matches':'none'},{'result':'','matches':'none'},{'result':'','matches':'none'}],username=self.username,prog='')
            self.showQuestTab()
        elif self.user_data_handeler.getStatus(self.question_index+1) == 'True':
            self.editor.type_area.insert('1.0',self.user_data_handeler.getProgStatement(self.question_index+1).replace('\\n','\n'))
            self.setScore()
            self.debug()
            self.disable_buttons()
            self.showResultTab()
        else:
            self.showQuestTab()
        self.editor.scoring_button.config(command=self.setScore)
        #------

 
    def debug(self):
        self.showSampleTab()
        self.sampleDisplay.hide()

        self.editor.sampleDebug()
        result = []
        for i in range(len(self.editor.entire_result)):
            currnet_result = self.editor.entire_result[i]
            result.append(currnet_result)

        self.sampleDisplay = sampleDisplay(master=self.sample_tab,quest_index=self.question_index,result=result)

    def setScore(self):
        self.showResultTab()

        self.editor.sampleDebug()
        result = []
        for i in range(len(self.editor.entire_result)):
            currnet_result = self.editor.entire_result[i]
            result.append(currnet_result)
        self.score_display.hide()
        self.score_display = scoringDisplay(self.result_tab,self.question_index,result=result,username=self.username,prog=self.editor.prog)
        if self.user_data_handeler.getStatus(self.question_index+1) == 'True':
            self.disable_buttons()

    def disable_buttons(self):
        self.editor.scoring_button.config(state='disabled')
        self.editor.sample_debug_button.config(state='disabled')

    def showQuestTab(self):
        self.quest_tab_button.config(state='disabled')
        self.debug_tab_button.config(state='normal')
        self.result_tab_button.config(state='normal')

        self.quest_tab.pack(fill='both',expand=1)
        self.sample_tab.forget()
        self.result_tab.forget()

    def showSampleTab(self):
        self.quest_tab_button.config(state='normal')
        self.debug_tab_button.config(state='disabled')
        self.result_tab_button.config(state='normal')

        self.quest_tab.forget()
        self.sample_tab.pack(fill='both',expand=1)
        self.result_tab.forget()

    def showResultTab(self):
        self.quest_tab_button.config(state='normal')
        self.debug_tab_button.config(state='normal')
        self.result_tab_button.config(state='disabled')
        
        self.quest_tab.forget()
        self.sample_tab.forget()
        self.result_tab.pack(fill="both",expand=1)
    
    def hide(self):
        self.root.forget()