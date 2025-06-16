from tkinter import *
import importlib
import math
import data.questDataExtracter as dataExtracter

class editor:
    def __init__(self,master,question_index): #プログラム番号で呼び出し。インデックスではない。
        self.root = master
        self.prog_index = question_index
        self.result = {'result':'null','matches':'null'} #結果を格納

        #Tkinter の設定
        self.editor_frame = Canvas(master=self.root)
        self.type_area = Text(master=self.editor_frame,background="#4A4A4A",foreground="#9EFFFF",font=("Source Han Code JP",11,"bold"))
        self.editor_frame.place(relheight=1.0,relwidth=0.5,relx=0.5,rely=0.0)
        button_area = Frame(master=self.editor_frame)
        sample_debug_button = Button(master=button_area,text="サンプル実行",command=self.sampleDebug)
        sample_debug_button.grid(column=0,row=0)
        scoring_button = Button(master=button_area,text="採点",command=self.scoreing)
        scoring_button.grid(column=1,row=0)
        button_area.pack(side=BOTTOM)
        self.type_area.pack(fill='both',expand=1)

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

        #__実行部分__
        self.type_area.configure(insertbackground="#FFFFFF",insertwidth=3)
        self.type_area.bind('<Return>',arrangeIndent)
        self.type_area.bind('<Tab>',tabKey)
        self.type_area.bind('<Shift-Tab>',shiftTabKey)

    def sampleDebug(self):
        for i in range(int(dataExtracter.numberOfCases(quest_index=self.prog_index))):
            print(f"sample {i}\n")
            self.debug(i)
            print(self.result)

    def scoreing(self):
        print("scoring",self.debug(0))

    def debug(self,case_index):
        sample_case = dataExtracter.sampleCase(quest_index=self.prog_index,case_index=case_index)
        prog = self.type_area.get("1.0","end").splitlines("\n")
        num_of_input = 0
        for i in range(len(prog)):
            if "input(" in prog[i]:
                inputed_data = sample_case[1][num_of_input]
                prog[i] = prog[i].replace("input(",f"inputMode({inputed_data},")
                num_of_input += 1
            prog[i] = "        " + prog[i]
        prog = ["def inputMode(inputed_data,message):\n    print(message,inputed_data)\n    return(inputed_data)\ndef generateResult():\n    import sys\n    sys.stdout = open('scripts/debugTerminal.txt','w',encoding='utf-8')\n    try:\n"]+prog+["    except Exception as e:\n        print(e)\n    finally:\n        sys.stdout.close()\n        sys.stdout = sys.__stdout__\n        with open('scripts/debugTerminal.txt','r',encoding='utf-8') as terminal_file:\n            return(terminal_file.read())"]

        with open(f"scripts/run_temp/runProg{case_index}.py",'w',encoding="utf-8") as runFile:
            runFile.write("".join(prog))
        runFile.close()
        
        #実行ファイルをインポートして実行
        runProg = importlib.import_module(f"scripts.run_temp.runProg{case_index}")
        importlib.reload(runProg)
        self.debugResult = runProg.generateResult()

        correct_answer = dataExtracter.sampleCase(quest_index=self.prog_index,case_index=case_index)[2]
        if self.debugResult == correct_answer:
            self.matches = True
        else:
            self.matches = False
        self.result['result'] = self.debugResult
        self.result['matches'] = self.matches


    def show(self):
        self.editor_frame.place(relheight=1.0,relwidth=0.5,relx=0.5,rely=0.0)

    def hide(self):
        self.editor_frame.place_forget()

root = Tk()
root.title("prompt-test")
root.geometry("800x500")
editor1 = editor(root,1)

quest_statement = Label(master=root,text=dataExtracter.questStatement(quest_index=1))
quest_statement.pack(side="left")

root.mainloop()