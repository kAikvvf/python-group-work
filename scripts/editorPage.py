from tkinter import *
from prompt import editor
from samplePage import sampleDisplay

class editorPage:
    def __init__(self,master,question_index):
        self.root = Canvas(master=master)
        self.root.pack(fill="both",expand=1)
        self.question_index = question_index

        #タブ切り替えボタン
        self.tab = Canvas(master=self.root)
        self.tab.place(relheight=1.0,relwidth=0.5)

        self.quest_tab_button = Button(master=self.tab,text="問題",command=self.showQuestTab)
        self.debug_tab_button = Button(master=self.tab,text="サンプル",command=self.showDebugTab)
        self.result_tab_button = Button(master=self.tab,text="結果",command=self.showResultTab)
        
        self.quest_tab_button.pack(anchor="nw")
        self.debug_tab_button.pack(anchor="nw")
        self.result_tab_button.pack(anchor="nw")

        self.editor = editor(master=self.root,question_index=self.question_index)
        self.editor.sample_debug_button.config(command=self.debug)

        #サンプルタブ設定
        self.sample_tab = Canvas(master=self.tab)
        self.sample_tab.pack(fill='both',expand=1)
        self.sampleDisplay = sampleDisplay(master=self.sample_tab,quest_index=self.question_index,result=['','','','','','','','','',''])

    def debug(self):
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

        self.sample_tab.pack_forget()

    def showDebugTab(self):
        self.quest_tab_button.config(state='normal')
        self.debug_tab_button.config(state='disabled')
        self.result_tab_button.config(state='normal')

        self.sample_tab.pack(fill='both',expand=1)

    def showResultTab(self):
        self.quest_tab_button.config(state='normal')
        self.debug_tab_button.config(state='normal')
        self.result_tab_button.config(state='disabled')
        self.sample_tab.pack_forget()

root = Tk()
root.title("test")
root.geometry("600x400")
Label(text='test').pack()
editorPage(master=root,question_index=1)
root.mainloop()