from tkinter import *
from tkinter import messagebox
import importlib
import math
import sys
import csv

root = Tk()
root.title('Quest Maker')
root.geometry('800x600')

class editor:
    def __init__(self,master):
        self.root = master
        #Tkinter の設定
        self.editor_frame = Canvas(master=self.root)
        self.type_area = Text(master=self.editor_frame,background="#4A4A4A",foreground="#9EFFFF",font=("Source Han Code JP",11,"bold"))
        self.editor_frame.place(relheight=1.0,relwidth=0.5,relx=0.5,rely=0.0)
        button_area = Frame(master=self.editor_frame)
        self.sample_debug_button = Button(master=button_area,text="サンプル実行")
        self.write_button = Button(master=button_area,text='書き込み')
        self.sample_debug_button.grid(column=0,row=0,padx=5,pady=5)
        self.write_button.grid(column=1,row=0,padx=5,pady=5)
        button_area.pack(side=BOTTOM)
        self.type_area.pack(fill='both',expand=1,padx=3)

        #インデントをそろえる
        def arrangeIndent(event):
            index_now = self.type_area.index('insert')
            index_inline_now = self.type_area.index('insert lineend')

            row_now = math.floor(float(index_now))
            content_in_line = self.type_area.get(f'{row_now}.0',f'{row_now}.end')
            
            self.type_area.insert('insert',"\n")
            if content_in_line != "":
                #インデントのスペースを数える
                index = 0
                while index < len(content_in_line):
                    if content_in_line[index] != " ":
                        break
                    index +=1
                #インデントを次の行に入れる
                indent = index // 4

                if index_inline_now == index_now:
                    if content_in_line[len(content_in_line)-1] == ":":
                        indent += 1

                    if indent > 0 & index % 4 ==0:
                        for i in range(indent):
                            self.type_area.insert('insert',"    ")     
            return "break"

        #インデントを Tab で入れる
        def tabKey(event):
            self.type_area.insert('insert',"    ")
            return 'break'
        
        def shiftTabKey(event):
            if self.type_area.get('insert -4c','insert') == "    ":
                self.type_area.delete('insert -4c','insert')
            return 'break'
        #print
        #__実行部分__
        self.type_area.configure(insertbackground="#FFFFFF",insertwidth=3)
        self.type_area.bind('<Return>',arrangeIndent)
        self.type_area.bind('<Tab>',tabKey)
        self.type_area.bind('<Shift-Tab>',shiftTabKey)
        self.debug_result = []

    def debug(self,case_index,sample_case):
        prog = self.type_area.get('1.0','end').split('\n')

        num_of_input = 0
        for i in range(len(prog)):
            if "input(" in prog[i]:
                inputed_data = sample_case[case_index][num_of_input]
                prog[i] = prog[i].replace("input(",f"inputMode({inputed_data},")
                num_of_input += 1
            prog[i] = "    " + prog[i]+'\n'
        prog = ["def inputMode(inputed_data,*message):\n    if not message == ():\n        print(message[0])\n    return(inputed_data)\ndef generateResult():\n"]+prog

        with open(f"scripts/run_temp/runProg{case_index}.py",'w',encoding="utf-8") as runFile:
            runFile.write("".join(prog))
        runFile.close()
        
        #実行ファイルをインポートして実行
        sys.stdout = open("debugTerminal.txt",'w',encoding='utf-8')
        self.error = ''
        try:
            runProg = importlib.import_module(f"run_temp.runProg{case_index}")
            importlib.reload(runProg)
            runProg.generateResult()       
        except ModuleNotFoundError as error:
            self.error = f"ModuleNotFoundError : {error}"
        except IndexError as error:
            self.error = f"IndexError : {error}"
        except SyntaxError as error:
            self.error = f"SyntaxError : {error}"
        except IndentationError as error:
            self.error = f"IndentationError : {error}"
        except TypeError as error:
            self.error = f"TypeError : {error}"
        except UnicodeError as error:
            self.error = f"UnicodeError : {error}"
        except ZeroDivisionError as error:
            self.error = f"ZeroDivisionError : {error}"
        except FileNotFoundError as error:
            self.error = f"FileNotFoundError : {error}"
        except SyntaxWarning as warning:
            self.error = f"SyntaxWarning : {warning}"        
        except ImportWarning as warning:
            self.error = f"ImportWarning : {warning}"
        except UnicodeWarning as warning:
            self.error = f"UnicodeWarning : {warning}"
        except EncodingWarning as warning:
            self.error = f"EndcodingWarning : {warning}"
        except Exception as error:
            self.error = f"unexpectedError:{error}"
        finally:
            if not self.error == '':
                print(self.error)
            sys.stdout.close()
            sys.stdout = sys.__stdout__    
        with open("debugTerminal.txt",'r',encoding='utf-8') as read_data:
                self.debugResult = read_data.read()
                #print(self.debugResult)
        
        self.debug_result.append(self.debugResult)

#左の表示のフレーム
display_frame = Frame(master=root)
display_frame.place(relheight=1.0,relwidth=0.5)

class singleDisplay:

    def __init__(self,master,sample,result):
        single_height = 130
        self.root = Canvas(master=master,height=single_height)

        label_height = 20
        Label(master=self.root,text="サンプルケース",borderwidth=1,relief="solid").place(height=label_height,relwidth=0.5,relx=0.0)
        Label(master=self.root,text="実行結果",borderwidth=1,relief="solid").place(height=label_height,relwidth=0.5,relx=0.5)
        sample_area = Text(master=self.root)
        debug_result = Text(master=self.root)

        sample_area_scrollbar = Scrollbar(master=sample_area,command=sample_area.yview,orient="vertical",cursor='arrow')
        debug_result_scrollbar = Scrollbar(master=debug_result,command=sample_area.yview,orient="vertical",cursor='arrow')
        
        sample_area.configure(yscrollcommand=sample_area_scrollbar.set)
        debug_result.configure(yscrollcommand=debug_result_scrollbar.set)

        sample_area_scrollbar.configure(command=sample_area.yview)
        debug_result_scrollbar.configure(command=debug_result.yview)

        sample_area_scrollbar.pack(anchor="e",fill="y",expand=1)

        debug_result_scrollbar.pack(anchor="e",fill="y",expand=1)
        
        sample_area.place(relwidth=0.5,relx=0.0,y=label_height,height=single_height-label_height)
        debug_result.place(relwidth=0.5,relx=0.5,y=label_height,height=single_height-label_height)

        #入力
        sample_area.insert("1.0",'\n'.join(sample))
        for i in range(len(result)):
            debug_result.insert(f'{i+1}.0',result[i])

        #追加入力できなくする
        sample_area.config(state="disabled")
        debug_result.config(state="disabled")

        self.root.pack(fill="x",expand=1,padx=10,pady=5)

class sampleDisplay:
    def __init__(self,master,sampleCases:list,result:list):
        self.canvas = Canvas(master=master)
        self.canvas.pack(fill="both",expand=1)
        self.frame = Frame(master=self.canvas)
        self.master = master
        self.result = result

        canvas_scrollbar = Scrollbar(master=self.canvas,command=self.canvas.yview,orient="vertical",cursor='arrow')
        self.sample_cases = sampleCases
        num_of_cases = len(self.sample_cases)
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

        self.display_samples = []
        for i in range(num_of_cases):
            self.display_samples.append(singleDisplay(master=self.frame,sample=self.sample_cases[i],result=self.result[i]))

    def reload(self):
        self.hide()
        self.__init__(self.master,self.sample_cases,self.result)
    def hide(self):
        for i in range(len(self.display_samples)):
            self.display_samples[i].root.destroy()
        self.canvas.destroy()

class makeQuest:
    def __init__(self,master):
        self.root = Frame(master=master)
        Label(master=self.root,text='問題のタイトル').pack()
        self.title_entry = Entry(master=self.root)
        self.title_entry.pack()

        Label(master=self.root,text='予想所要時間 [分]').pack()
        self.estimated_required_time_entry = Entry(master=self.root)
        self.estimated_required_time_entry.pack()

        Label(master=self.root,text='問題文').pack()
        self.question_entry = Text(master=self.root,height=10)
        self.question_entry.pack()

        Label(master=self.root,text='サンプル数').pack()
        self.num_of_sample_cases_entry = Entry(master=self.root)
        self.num_of_sample_cases_entry.pack()

        confirm_num_of_sample_case = Button(master=self.root,text='サンプル数を反映',command=self.refer_num_of_cases)
        confirm_num_of_sample_case.pack()

        self.root.pack(fill='both',expand=True)
        self.sample_case = []
        self.sample_case_frame = []
    
    def refer_num_of_cases(self):
        self.num_of_cases = self.num_of_sample_cases_entry.get()
        for i in range(len(self.sample_case)):
            self.sample_case_frame[i].destroy()
        for i in range(int(self.num_of_cases)):
            single_case_entry_frame = Frame(master=self.root)
            Label(master=single_case_entry_frame,text=f"サンプルケース {i+1}").grid(column=0,row=0)
            sample_case_entry = Entry(master=single_case_entry_frame)
            sample_case_entry.grid(column=1,row=0)
            single_case_entry_frame.pack()
            self.sample_case.append(sample_case_entry)
            self.sample_case_frame.append(single_case_entry_frame)

    def getSampleCases(self):
        return(self.sample_case)

    def show(self):
        self.root.pack(fill='both',expand=True)
    
    def hide(self):
        self.root.forget()

use_editor = editor(root)

left_frame = Frame(master=root)
left_frame.place(relwidth=0.5,relheight=1.0)
tab_frame = Frame(master=left_frame)

make_quest_tab = makeQuest(tab_frame)

sample_debug_tab = Frame(master=tab_frame)

def showMakeQuestTab():
    sample_debug_tab.forget()
    make_quest_tab.show()

def showSampleDebugTab():
    sample_debug_tab.pack(fill='both',expand=True)
    make_quest_tab.hide()

showMakeQuestTab()

quest_tab_button = Button(master=left_frame,command=showMakeQuestTab,text='問題作成')
debug_tab_button = Button(master=left_frame,command=showSampleDebugTab,text='実行結果')
quest_tab_button.pack()
debug_tab_button.pack()
tab_frame.pack(fill='both',expand=True)
sample_display = sampleDisplay(sample_debug_tab,[['1']],[['1']])

def sampleDebug():
    showSampleDebugTab()
    use_editor.debug_result = []
    sample_case_data = []
    for i in range(len(make_quest_tab.getSampleCases())):
        sample_case_inputted = make_quest_tab.sample_case[i].get().split('|')
        sample_case_data.append(sample_case_inputted)

    for i in range(len(sample_case_data)):
        use_editor.debug(i,sample_case_data)
    sample_display.sample_cases = sample_case_data
    sample_display.result = use_editor.debug_result

    sample_display.reload()
    return([sample_case_data,use_editor.debug_result])

use_editor.sample_debug_button.config(command=sampleDebug)

def clear():
    make_quest_tab.num_of_sample_cases_entry.delete(0,'end')
    make_quest_tab.num_of_sample_cases_entry.insert(0,'0')
    make_quest_tab.refer_num_of_cases()

    make_quest_tab.title_entry.delete(0,'end')
    make_quest_tab.estimated_required_time_entry.delete(0,'end')
    make_quest_tab.question_entry.delete(1.0,'end')
    use_editor.type_area.delete(1.0,'end')

    showMakeQuestTab()

def confirmQuest():
    title = make_quest_tab.title_entry.get()
    quest_statement = make_quest_tab.question_entry.get('1.0','end')
    estimated_required_time = make_quest_tab.estimated_required_time_entry.get()
    sample_case = sampleDebug()[0]
    debug_result = sampleDebug()[1]

    sample_check_statement = ''
    for i in range(len(sample_case)):
        sample_check_statement = sample_check_statement + f'サンプルケース {i} : {str(sample_case[i])}' + f"\n-----正答-----\n{debug_result[i]}--------\n"
    if messagebox.askokcancel(title='内容確認',message=f'問題の内容を確認しれください。\n\nタイトル：{title}\n所要時間：{estimated_required_time}\n問題文：{quest_statement}\n{sample_check_statement}') == True:
        field_names = ['title','quest_statement','estimated_required_time','sample_case','correct_answer']

        quest_data = []
        with open('data/questDict.csv','r',encoding='utf-8') as data_dict_file_to_read:
            reader = csv.DictReader(data_dict_file_to_read,fieldnames=field_names)
            for i in reader:
                quest_data.append(i)
        
        data = {'title':str(title),'quest_statement':str(quest_statement).replace('\n','\\n'),'estimated_required_time':str(estimated_required_time),'sample_case':str(sample_case),'correct_answer':str(debug_result)}
        with open('data/questDict.csv','a',encoding='utf-8') as data_dict_file_to_write:
            writer = csv.DictWriter(data_dict_file_to_write,fieldnames=field_names)
            writer.writeheader
            writer.writerow(data)
        clear()
        

use_editor.write_button.config(command=confirmQuest)
root.mainloop()