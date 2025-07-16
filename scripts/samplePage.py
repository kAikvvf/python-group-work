from tkinter import *
from scripts import questDataHandler

class singleDisplay:
    def __init__(self,master,quest_index,sample_index,result:int):
        single_height = 130
        self.root = Canvas(master=master,height=single_height)
        self.quest_index = quest_index
        matches = result['matches']

        sample_case = questDataHandler.getSampleCase(self.quest_index)[sample_index]

        label_height = 20
        sample_label = Label(master=self.root,text="サンプルケース",borderwidth=1,relief="solid")
        sample_label.place(height=label_height,relwidth=1/3,relx=0.0)
        correct_answer_label = Label(master=self.root,text="正解",borderwidth=1,relief="solid")
        correct_answer_label.place(height=label_height,relwidth=1/3,relx=1/3)
        result_label = Label(master=self.root,text="実行結果",borderwidth=1,relief="solid")
        result_label.place(height=label_height,relwidth=1/3,relx=2/3)

        sample_area_frame = Frame(self.root)
        correct_answer_frame = Frame(self.root)
        debug_result_frame = Frame(self.root)

        sample_area = Text(master=sample_area_frame)
        correct_answer = Text(master=correct_answer_frame)
        debug_result = Text(master=debug_result_frame)

        sample_area_scrollbar = Scrollbar(master=sample_area_frame,command=sample_area.yview,orient="vertical",cursor='arrow')
        correct_answer_scrollbar = Scrollbar(master=correct_answer_frame,command=sample_area.yview,orient="vertical",cursor='arrow')
        debug_result_scrollbar = Scrollbar(master=debug_result_frame,command=sample_area.yview,orient="vertical",cursor='arrow')
        
        sample_area.configure(yscrollcommand=sample_area_scrollbar.set)
        correct_answer.configure(yscrollcommand=correct_answer_scrollbar.set)
        debug_result.configure(yscrollcommand=debug_result_scrollbar.set)

        sample_area_scrollbar.configure(command=sample_area.yview)
        correct_answer_scrollbar.configure(command=correct_answer.yview)
        debug_result_scrollbar.configure(command=debug_result.yview)

        sample_area_scrollbar.pack(side="right",fill="y",expand=1)
        correct_answer_scrollbar.pack(side="right",fill="y",expand=1)
        debug_result_scrollbar.pack(side="right",fill="y",expand=1)
        
        sample_area.pack(side="left",fill="both",expand=True)
        correct_answer.pack(side="left",fill="both",expand=True)
        debug_result.pack(side="left",fill="both",expand=True)

        sample_area_frame.place(relwidth=1/3,relx=0.0,y=label_height,height=single_height-label_height)
        correct_answer_frame.place(relwidth=1/3,relx=1/3,y=label_height,height=single_height-label_height)
        debug_result_frame.place(relwidth=1/3,relx=2/3,y=label_height,height=single_height-label_height)

        #入力

        sample_area.insert("1.0",questDataHandler.getSampleCase(quest_index)[sample_index])
        correct_answer.insert("1.0",questDataHandler.getCorrectAnswer(quest_index)[sample_index])
        debug_result.insert("1.0",result['result'])

        #追加入力できなくする
        sample_area.config(state="disabled")
        correct_answer.config(state="disabled")
        debug_result.config(state="disabled")

        self.root.pack(fill="x",expand=1,padx=10,pady=5)

        if matches == True:
            sample_area.config(background="#ABC6FF")
            correct_answer.config(background="#ABC6FF")
            debug_result.config(background="#ABC6FF")
            sample_label.config(background="#529AFF")
            correct_answer_label.config(background="#529AFF")
            result_label.config(background="#529AFF")

        elif matches == False:
            sample_area.config(background="#FFABAB")
            correct_answer.config(background="#FFABAB")
            debug_result.config(background="#FFABAB")
            sample_label.config(background="#FF5252")
            correct_answer_label.config(background="#FF5252")
            result_label.config(background="#FF5252")

class sampleDisplay:
    def __init__(self,master,quest_index,result):
        self.canvas = Canvas(master=master)
        self.canvas.pack(fill="both",expand=1)
        self.frame = Frame(master=self.canvas)
        self.result = [result[i]['result'] for i in range(len(result))]

        canvas_scrollbar = Scrollbar(master=self.canvas,command=self.canvas.yview,orient="vertical",cursor='arrow')

        self.quest_index = quest_index
        num_of_cases = int(len(questDataHandler.getSampleCase(quest_index)))
        self.canvas.configure(scrollregion=(0,0,0,140*num_of_cases+10))

        self.canvas.configure(yscrollcommand=canvas_scrollbar.set)

        canvas_scrollbar.configure(command=self.canvas.yview)
        canvas_scrollbar.pack(anchor="e",fill="y",expand=1)

        
        def getWindowWidth(e):
            window_width = int(self.canvas.winfo_width())-20
            self.canvas.itemconfig(view_window,width=window_width)
            self.canvas.config(height=window_width-30)
        
        self.canvas.bind("<Configure>",getWindowWidth)

        view_window = self.canvas.create_window(0,0,window=self.frame,anchor="nw",width=int(self.canvas.winfo_width()-20))

        #print('result : ',result)
        if num_of_cases >= 1:
            singleDisplay(master=self.frame,quest_index=self.quest_index,sample_index=0,result=result[0])

        if num_of_cases >= 2:
            singleDisplay(master=self.frame,quest_index=self.quest_index,sample_index=1,result=result[1])
        
        if num_of_cases >= 3:
            singleDisplay(master=self.frame,quest_index=self.quest_index,sample_index=2,result=result[2])
        
        if num_of_cases >= 4:
            singleDisplay(master=self.frame,quest_index=self.quest_index,sample_index=3,result=result[3])

        if num_of_cases >= 5:
            singleDisplay(master=self.frame,quest_index=self.quest_index,sample_index=4,result=result[4])
        
        if num_of_cases >= 6:
            singleDisplay(master=self.frame,quest_index=self.quest_index,sample_index=5,result=result[5])

    def show(self):
        self.canvas.pack(fill="both",expand=1)
    def hide(self):
        self.canvas.forget()