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
        self.type_area = Text(master=self.editor_frame,font=("Source Han Code JP",11,"bold"),wrap='none',background="#232323",foreground="#FFFFFF",insertwidth=3,insertbackground='white')
        self.editor_frame.place(relheight=1.0,relwidth=0.5,relx=0.5,rely=0.0)
        button_area = Frame(master=self.editor_frame)
        self.sample_debug_button = Button(master=button_area,text="サンプル実行")
        self.sample_debug_button.grid(column=0,row=0,padx=5,pady=5)
        self.scoring_button = Button(master=button_area,text="採点")
        self.scoring_button.grid(column=1,row=0,padx=5,pady=5)
        button_area.pack(side=BOTTOM)
        self.type_area.pack(fill='both',expand=1,padx=3)


        def addColor(*args,**kwargs):
            buitlin_lst = ['id', 'abs', 'all', 'any', 'bin', 'chr', 'hex', 'int', 'len', 'map', 'max', 'min', 'oct', 'ord', 'pow', 'set', 'str', 'sum', 'zip','bool', 'dict', 'eval', 'exec', 'exit', 'hash', 'help', 'iter', 'list', 'next', 'open', 'repr', 'type', 'vars', 'input', 'print', 'range', 'round', 'slice', 'super', 'ascii', 'bytes', 'filter', 'format', 'object', 'sorted', 'aiter', 'anext', 'callable', 'compile', 'complex', 'getattr', 'globals', 'hasattr', 'locals', 'property', 'setattr', 'bytearray', 'classmethod', 'frozenset','isinstance', 'issubclass', 'breakpoint', 'staticmethod', 'memoryview']
            bracket_lst = ['[',']','(',')','{','}']
            number_lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            operator_lst = ['+','-','/','*','%']
            iterable_lst = ['for','in','while','True','False','if','else','try','except','finally','break']
            variable_lst = []
            variable_used = ''
            prog = self.type_area.get('1.0','end').split('\n')

            #変数を認識して格納
            for prog_row in range(len(prog)):
                if '=' in prog[prog_row]:
                    row_line = prog[prog_row].split(' ')
                    while '' in row_line:
                        row_line.remove('')
                    for i in range(len(row_line)):
                        try:
                            row_line[i] = float(row_line[i])
                        except:
                            pass
                        try:
                            row_line[i] = int(row_line[i])
                        except:
                            pass
                        if row_line[i] == 'True':
                            row_line[i] = True
                        if row_line[i] == 'False':
                            row_line[i] = False
                    
                    var_string = variable_used+'\n'+''.join([str(i) for i in row_line])
                    try:
                        exec(var_string)
                    except:
                        pass
                    else:
                        if not ('\u0027' in row_line[0] or '\u0022' in row_line[0] or '(' in row_line[0] or ')' in row_line[0] or '{' in row_line[0] or '}' in row_line[0] or '[' in row_line[0] or ']' in row_line[0] ):
                            variable_lst.append(row_line[0])
                            variable_used = var_string

                if 'for' in prog[prog_row]:
                    row_line = prog[prog_row].split(' ')
                    while '' in row_line:
                        row_line.remove('')

                    if row_line[0] == 'for':
                        if len(row_line) > 2:
                            var_string = variable_used+'\n'+f"{row_line[1]}='var'"
                            try:
                                exec(var_string)
                            except:
                                pass
                            else:
                                variable_lst.append(row_line[1])
                                variable_used = var_string
                        
            tag_refer = []
            for i in operator_lst:
                tag_refer.append({'len':len(i),'string':i,'tag':'operator'})
            for i in number_lst:
                tag_refer.append({'len':len(i),'string':i,'tag':'number'})
            for i in buitlin_lst:
                tag_refer.append({'len':len(i),'string':i,'tag':'builtin'})
            for i in bracket_lst:
                tag_refer.append({'len':len(i),'string':i,'tag':'bracket'})
            for i in variable_lst:
                tag_refer.append({'len':len(i),'string':i,'tag':'variable'})
            for i in iterable_lst:
                tag_refer.append({'len':len(i),'string':i,'tag':'iterable'})

            for i in range(len(tag_refer)):
                for j in range(len(tag_refer) - i -1):
                    if tag_refer[j]['len'] < tag_refer[j+1]['len']:
                        tag_refer[j], tag_refer[j+1] = tag_refer[j+1], tag_refer[j]

            row_with_tag = []
            prog_to_find = prog

            for row in range(len(prog_to_find)):
                for tag in tag_refer:
                    while tag['string'] in prog_to_find[row]:
                        index = prog_to_find[row].index(tag['string'])
                        row_with_tag.append({'tag':tag['tag'],'string':tag['string'],'start':f'{row+1}.{index}','end':f'{row+1}.{index+tag['len']}'})
                        prog_to_find[row] = prog_to_find[row].replace(tag['string'],''.join(['`' for i in range(tag['len'])]),1)

            for attaching_tag in row_with_tag:
                self.type_area.tag_add(attaching_tag['tag'],attaching_tag['start'],attaching_tag['end'])
            
            for row in range(len(prog)):
                for indent in range(len(prog)):
                    if prog[row][indent*4:(indent+1)*4] == '    ':
                        self.type_area.tag_add('indent',f'{row+1}.{indent*4+3}',f'{row+1}.{indent*4+4}')
                single_quotation = []
                double_quotation = []
                for index in range(len(prog[row])):
                    if self.type_area.get(f'{row+1}.{index}') == '\u0027':
                        single_quotation.append(f'{row+1}.{index}')
                    elif self.type_area.get(f'{row+1}.{index}') == '\u0022':
                        double_quotation.append(f'{row+1}.{index}')
                
                if len(double_quotation) % 2 == 0:
                    for index in range(len(double_quotation)//2):
                        for tag in self.type_area.tag_names('1.0')[1:]:
                            self.type_area.tag_remove(tag,double_quotation[index*2],f'{double_quotation[index*2+1]} +1char')
                        self.type_area.tag_add('string',double_quotation[index*2],f'{double_quotation[index*2+1]} +1char')
                else:
                    prev_str = len(double_quotation) // 2
                    for tag in self.type_area.tag_names('1.0')[1:]:
                        self.type_area.tag_remove(tag,f'{double_quotation[len(double_quotation)-1]}',f'{row+1}.end')
                    for index in range(prev_str):
                        self.type_area.tag_add('string',double_quotation[index*2],f'{double_quotation[index*2+1]} +1char')
                    self.type_area.tag_add('unclosed_s',double_quotation[len(double_quotation)-1],f'{row+1}.end')

                for single_index in range(len(single_quotation)):
                    if len(self.type_area.tag_names(single_quotation[single_index])) == 0:
                        if len(single_quotation) % 2 == 0:
                            for index in range(len(single_quotation)//2):
                                for tag in self.type_area.tag_names('1.0')[1:]:
                                    self.type_area.tag_remove(tag,single_quotation[index*2],f'{single_quotation[index*2+1]} +1char')
                                self.type_area.tag_add('string',single_quotation[index*2],f'{single_quotation[index*2+1]} +1char')
                        else:
                            prev_str = len(single_quotation) // 2
                            for tag in self.type_area.tag_names('1.0')[1:]:
                                self.type_area.tag_remove(tag,f'{single_quotation[len(single_quotation)-1]}',f'{row+1}.end')
                            for index in range(prev_str):
                                self.type_area.tag_add('string',single_quotation[index*2],f'{single_quotation[index*2+1]} +1char')
                            self.type_area.tag_add('unclosed_s',single_quotation[len(single_quotation)-1],f'{row+1}.end')
            
            bracket_index = []
            prog = self.type_area.get('1.0','end').split('\n')
            for row in range(len(prog)):
                for index in range(len(prog[row])):
                    for n in [['(',')'],['{','}'],['[',']']]:
                        if n[0] == prog[row][index]:
                            if not f'{row+1}.{index}' in bracket_index:
                                num_double_quotation_before = 0
                                num_double_quotation_after = 0
                                string_before = prog[row][:index]
                                string_after = prog[row][index+1:]
                                for m in string_before:
                                    if m == '\u0022':
                                        num_double_quotation_before +=1
                                        string_before.replace('\u0022','`',1)
                                    print(string_before)
                                for m in string_after:
                                    if m == '\u0022':
                                        num_double_quotation_after +=1
                                        string_after.replace('\u0022','`',1)
                                    print(string_after)
                                num_single_quotation_before = 0
                                num_single_quotation_after = 0
                                string_before = prog[row][:index].split('\u0022')[len(prog[row][:index].split('\u0022'))-1]
                                string_after = prog[row][index+1:].split('\u0022')[0]
                                for m in string_before:
                                    if m == '\u0022':
                                        num_single_quotation_before +=1
                                        string_before.replace('\u0022','`',1)
                                    print(string_before)
                                for m in string_after:
                                    if m == '\u0022':
                                        num_single_quotation_after +=1
                                        string_after.replace('\u0022','`',1)
                                    print(string_after)

                                if not((num_double_quotation_after % 2 == 0 and num_double_quotation_before % 2 == 0) or (num_single_quotation_after % 2 == 0 and num_single_quotation_before % 2 == 0)) or (num_double_quotation_after == 0 and num_double_quotation_before == 0) or (num_single_quotation_after == 0 and num_single_quotation_before == 0) and not 'string' in self.type_area.tag_names(f'{row+1}.{index}') and 'unclosed_s' in self.type_area.tag_names(f'{row+1}.{index}'):
                                    bracket_index.append(f'{row+1}.{index}')
                        elif n[1] == prog[row][index]:
                            try:
                                bracket_index.remove(bracket_index[len(bracket_index)-1])
                            except:
                                pass
            if len(bracket_index) >= 1:
                self.type_area.tag_add('unclosed_b',f'{bracket_index[len(bracket_index)-1]} +1char','end')

        def keyInput(event):
            if event.state != 4 and len(event.keysym) == 1:
                if len(str(event.keycode)) == 5:
                    self.type_area.insert(self.type_area.index('insert'),chr(event.keycode))
                    for i in self.type_area.tag_names():
                        self.type_area.tag_remove(i,'1.0','end')
                    addColor()
                else:
                    self.type_area.insert(self.type_area.index('insert'),event.char)
                    for i in self.type_area.tag_names():
                        self.type_area.tag_remove(i,'1.0','end')
                    addColor()
                return('break')
            elif event.keysym in ['quotedbl','apostrophe','parenleft','parenright','braceright','bracketleft','bracketright']:
                self.type_area.insert(self.type_area.index('insert'),event.char)
                for i in self.type_area.tag_names():
                    self.type_area.tag_remove(i,'1.0','end')
                addColor()
                return('break')
            elif event.keysym == 'BackSpace':
                addColor()
            else:
                addColor()

        #インデントを Tab で入れる
        def tabKey(event):
            self.type_area.insert('insert',"    ")
            addColor()
            return 'break'
        
        def shiftTabKey(event):
            if self.type_area.get('insert -4c','insert') == "    ":
                self.type_area.delete('insert -4c','insert')
            addColor()
            return 'break'

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
            addColor()  
            return "break"
        #__実行部分__
        self.type_area.bind('<Return>',arrangeIndent)
        self.type_area.bind('<Tab>',tabKey)
        self.type_area.bind('<Shift-Tab>',shiftTabKey)
        self.type_area.bind('<KeyPress>',keyInput)
        self.type_area.tag_config('iterable',foreground="#E18ADD")
        self.type_area.tag_config('builtin',foreground="#F3DE92")
        self.type_area.tag_config('number',foreground="#9AFFC7")
        self.type_area.tag_config('bracket',foreground="#FFE089")
        self.type_area.tag_config('operator',foreground="#FFFFFF")
        self.type_area.tag_config('variable',foreground="#97C6FF")
        self.type_area.tag_config('indent',background="#707070")
        self.type_area.tag_config('string',foreground="#FFC272")
        self.type_area.tag_config('unclosed_b',background="#5D5D5D")
        self.type_area.tag_config('unclosed_s',background="#564218",foreground='white')
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