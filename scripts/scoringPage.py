from tkinter import *
from scripts import questDataHandler
import csv
import datetime

class scoringDisplay:
    def __init__(self,master,quest_index,result,username):
        self.master = master
        self.root = Frame(master=master)
        self.quest_index = quest_index+1
        self.result = [result[i]['matches'] for i in range(len(result))]
        print(self.result)
        self.username = username
        self.time_required = '-'

        buton_area = Frame(self.root)
        self.return_home_button = Button(master=buton_area,text='問題選択に戻る')
        self.next_quest_button = Button(master=buton_area,text='次の問題')

        Label(master=self.root,text='採点結果',font=11).pack()
        required_time_label = Label(master=self.root,text=f'所要時間：{self.time_required}')
        required_time_label.pack()
        with open(f'data/.{username}.csv','r',encoding='utf-8') as user_data_file:
            user_data_reader = csv.DictReader(user_data_file,['quest_index','status','score','start_time','end_time','number_of_confirm','prog_status'])
            user_data = []
            for i in user_data_reader:
                user_data.append(i)

            if not user_data[self.quest_index]['start_time'] == 'null' and not user_data[self.quest_index]['end_time'] == 'null':
                start_time_lst = [int(index) for index in user_data[self.quest_index]['start_time'].split('.')]
                end_time_lst = [int(index) for index in user_data[self.quest_index]['end_time'].split('.')]
                start_time = datetime.datetime(year=start_time_lst[0],month=start_time_lst[1],day=start_time_lst[2],hour=start_time_lst[3],minute=start_time_lst[4],second=start_time_lst[5])
                end_time = datetime.datetime(year=end_time_lst[0],month=end_time_lst[1],day=end_time_lst[2],hour=end_time_lst[3],minute=end_time_lst[4],second=end_time_lst[5])
                
                self.time_required = end_time - start_time
                required_time_label.config(text=f'所要時間：{self.time_required}')
            self.number_of_config = user_data[self.quest_index]['number_of_confirm']

        score_list_frame = Frame(master=self.root)
        score_list_frame.pack()

        self.pass_or_not = True
        for i in range(len(result)):
            single_score_frame = Canvas(master=score_list_frame,highlightbackground='black',highlightthickness=1)
            if self.result[i] == True:
                Label(master=single_score_frame,text=f'ケース {i+1}　　正解',fg="blue",font=12).pack(padx=5,pady=2)
            elif self.result[i] == False:
                Label(master=single_score_frame,text=f'ケース {i+1}　　不正解',fg="red",font=12).pack(padx=5,pady=2)
                self.pass_or_not = False
            elif self.result[i] == 'none':
                Label(master=single_score_frame,text=f'ケース {i+1}　　未回答',fg="red",font=12).pack(padx=5,pady=2)
                self.pass_or_not = False

            single_score_frame.pack()
        

        if self.pass_or_not == True:
            score_basis = self.time_required.total_seconds() / questDataHandler.getEstimatedRequredTime(quest_index)
            score = int(20/score_basis)-int(user_data[self.quest_index]['number_of_confirm'])

            if score >= 25:
                score = 25
            score_label = Label(master=score_list_frame,text=f'最終スコア：{score}',font=20).pack(pady=20)

            passed_label = Label(master=self.root,text='☆☆☆ 合格 ☆☆☆',highlightthickness=2,highlightbackground='black',fg="#000000",bg="#FF00EE",font=('arial',17,'bold')).pack(fill='x',pady=5)
            with open(f'data/.{self.username}.csv','w',encoding='utf-8') as write_target:
                user_data[self.quest_index]['score'] = score
                user_data[self.quest_index]['status'] = True
                user_data[self.quest_index]['number_of_confirm'] = self.num_of_config
                writer = csv.DictWriter(write_target,['quest_index','status','score','start_time','end_time','number_of_confirm','prog_status'])
                writer.writerows(user_data)
            buton_area.pack()
            self.return_home_button.grid(column=0,row=0,padx=5)
            self.next_quest_button.grid(column=1,row=0,padx=5)

        self.root.pack(fill='both',expand=True)

    def show(self):
        self.root.pack(fill='both',expand=True)
    def hide(self):
        self.root.forget()
    
    def config(self,new_result):
        self.root.destroy()
        self.__init__(self.master,self.quest_index-1,new_result,self.username)

'''
root = Tk()
root.title('test')
root.geometry('400x600')
score_tab = scoringDisplay(master=root,quest_index=0,result=[{'result':'','matches':'True'},{'result':'','matches':'True'},{'result':'','matches':'True'},{'result':'','matches':'True'}],username='taro')
Button(master=root,command=score_tab.show,text='show').pack()
Button(master=root,command=score_tab.hide,text='hide').pack()

root.mainloop()
'''