from tkinter import *
from scripts.prompt import editor
from scripts.samplePage import sampleDisplay
from scripts import questDataExtracter

class Question:
    def __init__(self,master,question_index):
        self.root = Canvas(master=master)
        self.root.pack(fill="both",expand=1)
        self.question_index = question_index

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
        self.textbox.insert('1.0', questDataExtracter.questStatement(self.question_index))
        self.textbox.config(state="disabled")
        self.textbox.pack(side="left", fill="y", expand=True)
        self.textbox.pack()

        #---サンプル タブ設定---
        self.sample_tab = Frame(master=self.tab)
        self.sampleDisplay = sampleDisplay(master=self.sample_tab,quest_index=self.question_index,result=['','','','','','','','','',''])

        #---結果 タブ設定---
        self.result_tab = Frame(master=self.tab)
        self.x_scroll = Scrollbar(self.result_tab, orient="horizontal")
        self.y_scroll = Scrollbar(self.result_tab, orient="vertical")
        self.x_scroll.pack(side="bottom", fill="x")
        self.y_scroll.pack(side="right", fill="y")

        self.textbox = Text(self.result_tab, 
                               font=("メイリオ", 12), 
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
        #------

        self.showQuestTab()

    def debug(self):
        self.showSampleTab()
        self.sampleDisplay.hide()

        self.editor.sampleDebug()
        result = []
        for i in range(len(self.editor.entire_result)):
            currnet_result = self.editor.entire_result[i]['result']
            result.append(currnet_result)
        self.sampleDisplay = sampleDisplay(master=self.sample_tab,quest_index=self.question_index,result=result)

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