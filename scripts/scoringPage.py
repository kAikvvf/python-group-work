from tkinter import *
from scripts import questDataHandler
from scripts.userDataHanlder import userDataHandler
import datetime

class scoringDisplay:
    def __init__(self,master,quest_index,result,username,prog,disable_button_prog):
        self.master = master
        self.root = Frame(master=master)
        self.quest_index = quest_index
        self.result = [str(result[i]['matches']) for i in range(len(result))]
        self.username = username

        self.user_data_handeler = userDataHandler(self.username)

        self.user_data_handeler.setProgStatement(self.quest_index,prog)
        self.user_data_handeler.addNumOfConfirm(self.quest_index)

        quest_start_time = self.user_data_handeler.getStartTime(self.quest_index)

        if not self.user_data_handeler.getStatus(self.quest_index) == 'True':
            self.user_data_handeler.setEndTime(self.quest_index)
        quest_end_time = self.user_data_handeler.getEndTime(self.quest_index)

        self.time_required = '-'

        if not quest_start_time == 'null' and not quest_start_time == 'null':
            self.time_required= quest_end_time - quest_start_time

        Label(master=self.root,text='採点結果',font=11).pack()
        required_time_label = Label(master=self.root,text=f'所要時間：{self.time_required}')
        required_time_label.pack()

        score_list_frame = Frame(master=self.root)
        score_list_frame.pack()

        self.pass_or_not = True

        for i in range(len(result)):
            single_score_frame = Canvas(master=score_list_frame,highlightbackground='black',highlightthickness=1)
            if self.result[i] == 'True':
                Label(master=single_score_frame,text=f'ケース {i+1}　　正解',fg="blue",font=12).pack(padx=5,pady=2)
            elif self.result[i] == 'False':
                Label(master=single_score_frame,text=f'ケース {i+1}　　不正解',fg="red",font=12).pack(padx=5,pady=2)
                self.pass_or_not = False
            elif self.result[i] == 'none':
                Label(master=single_score_frame,text=f'ケース {i+1}　　未回答',fg="red",font=12).pack(padx=5,pady=2)
                self.pass_or_not = False
            single_score_frame.pack()

        if self.pass_or_not == True:
            score_basis = self.time_required.total_seconds() / (questDataHandler.getEstimatedRequredTime(quest_index)*60)
            score = int(7/score_basis)-int(self.user_data_handeler.getNumOfConfirm(self.quest_index))

            if score >= 25:
                score = 25
            score_label = Label(master=score_list_frame,text=f'最終スコア：{score}',font=20)
            self.user_data_handeler.setScore(self.quest_index,score)
            score_label.pack(pady=20)
            passed_label = Label(master=self.root,text='☆☆☆ 合格 ☆☆☆',highlightthickness=2,highlightbackground='black',fg="#000000",bg="#FF00EE",font=('arial',17,'bold'))
            passed_label.pack(fill='x',pady=5)

            disable_button_prog()

            self.user_data_handeler.setStatus(self.quest_index,True)

        self.root.pack(fill='both',expand=True)

    def show(self):
        self.root.pack(fill='both',expand=True)
    def hide(self):
        self.root.destroy()

'''
root = Tk()
root.title('test')
root.geometry('400x600')
score_tab = scoringDisplay(master=root,quest_index=0,result=[{'result':'','matches':'True'},{'result':'','matches':'True'},{'result':'','matches':'True'},{'result':'','matches':'True'}],username='taro')
Button(master=root,command=score_tab.show,text='show').pack()
Button(master=root,command=score_tab.hide,text='hide').pack()

root.mainloop()
'''