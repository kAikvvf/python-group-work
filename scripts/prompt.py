from tkinter import *
import importlib
import math
import sys
from scripts import questDataHandler

class editor:
    def __init__(self,master,question_index): #プログラム番号で呼び出し。インデックスではない。
        self.root = master
        self.prog_index = question_index

        #Tkinter の設定
        self.editor_frame = Canvas(master=self.root)
        self.type_area = Text(master=self.editor_frame,font=("Source Han Code JP",11,"bold"),wrap='none')
        self.editor_frame.place(relheight=1.0,relwidth=0.5,relx=0.5,rely=0.0)
        button_area = Frame(master=self.editor_frame)
        self.sample_debug_button = Button(master=button_area,text="サンプル実行")
        self.sample_debug_button.grid(column=0,row=0,padx=5,pady=5)
        self.scoring_button = Button(master=button_area,text="採点")
        self.scoring_button.grid(column=1,row=0,padx=5,pady=5)
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

        #__実行部分__
        self.type_area.bind('<Return>',arrangeIndent)
        self.type_area.bind('<Tab>',tabKey)
        self.type_area.bind('<Shift-Tab>',shiftTabKey)

    def sampleDebug(self):
        self.entire_result = []
        for i in range(len(questDataHandler.getSampleCase(self.prog_index))):
            self.debug(i)

    def debug(self,case_index):
        sample_case = questDataHandler.getSampleCase(self.prog_index)[case_index]
        self.prog = self.type_area.get('1.0','end')
        prog = self.prog.split('\n')

        for i in range(len(prog)):
            if "input(" in prog[i]:
                prog[i] = prog[i].replace("input(","self.inputMode(")
            if "while" in prog[i]:
                while_term = prog[i].replace('while','')
                while_sentence = prog[i]
                prog[i] = f"for while_index in range(1000):\n            if not {while_term}\n                break\n            else:"
                while_indent = 0
                while while_sentence[while_indent*4:(while_indent+1)*4] == '    ':
                    while_indent += 1
                for j in range(i+1,len(prog)):
                    indent = ''.join(['    ' for indent_str in range(while_indent+1)])
                    if prog[j][0:while_indent+4] == indent:
                        prog[j] = indent + prog[j]
            prog[i] = "        " + prog[i]+'\n'
        prog = [f"class generateResult:\n    def __init__(self):\n        self.sample_data = {sample_case}\n        self.sample_index = 0\n"]+prog+["    def inputMode(self,*message):\n        if not message == ():\n            print(message[0])\n        self.sample_index += 1\n        return(self.sample_data[self.sample_index-1])"]

        with open(f"scripts/run_temp/runProg{case_index}.py",'w',encoding="utf-8") as runFile:
            runFile.write("".join(prog))
        runFile.close()

        #実行ファイルをインポートして実行
        sys.stdout = open("scripts/debugTerminal.txt",'w',encoding='utf-8')
        self.error = ''
        try:
            runProg = importlib.import_module(f"scripts.run_temp.runProg{case_index}")
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
        with open("scripts/debugTerminal.txt",'r',encoding='utf-8') as read_data:
                self.debugResult = read_data.read()

        correct_answer = questDataHandler.getCorrectAnswer(self.prog_index)[case_index]
        if self.debugResult == correct_answer:
            self.matches = True
        else:
            self.matches = False
        
        self.entire_result.append({'result':self.debugResult,'matches':self.matches})


    def show(self):
        self.editor_frame.place(relheight=1.0,relwidth=0.5,relx=0.5,rely=0.0)

    def hide(self):
        self.editor_frame.place_forget()