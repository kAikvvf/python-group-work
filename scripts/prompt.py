from libraries.codeDebugger import codeDebugger
import tkinter as tk
import math

class prompt:
    def __init__(self,
                 root_Tk,
                 input_font_size = 5,
                 ):
        self.Prompt = tk.Canvas(master=root_Tk) #プロンプト全体のエリア
        Button_Pad = tk.Canvas(master=self.Prompt) #ボタンを表示するエリア

        #コマンドを入力するプロンプトのウィジェット
        self.input_pad = tk.Text(self.Prompt,
                                 font=("Bahnschrift SemiCondensed",input_font_size),
                                 foreground="#FFFFFF",
                                 background="#2D2D2D")
        
        #サンプル実行ボタン
        test_debug_button = tk.Button(Button_Pad,
                                      text="サンプル実行",
                                      command=self.test_debug,
                                      font=("BIZ UDゴシック",10,"bold"),
                                      background="#69B7FC",
                                      relief="groove")

        #採点ボタン
        confirm_answer_button = tk.Button(Button_Pad,
                                          text="採点",
                                          command=self.confirm_answer,
                                          font=("BIZ UDゴシック",10,"bold"),
                                          background="#FF6FBC",
                                          relief="groove")

        #各コンポーネントを配置
        test_debug_button.pack(anchor=tk.SE,side=tk.LEFT,padx=5,pady=3,ipadx=3,ipady=3)
        confirm_answer_button.pack(anchor=tk.SE,side=tk.LEFT,padx=5,pady=3,ipadx=3,ipady=3)
        Button_Pad.pack(anchor=tk.SE,side=tk.BOTTOM)
        self.input_pad.pack(fill=tk.BOTH,expand=1)

        #----------編集時に書きやすくするコマンド----------#
        self.indent = 0
        self.index = 0

        #__改行時にインデントをそろえる__
        def arrangeIndent(event):
            index_now = self.input_pad.index('insert')
            index_inline_now = self.input_pad.index('insert lineend')
            print(index_now,index_inline_now)
            row_now = math.floor(float(index_now))
            content_in_line = self.input_pad.get(f'{row_now}.0',f'{row_now}.end')
            
            self.input_pad.insert('insert',"\n")
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
                            self.input_pad.insert('insert',"    ")     
            return "break"

        #インデントを Tab で入れる
        def tabKey(event):
            self.input_pad.insert('insert',"    ")
            return 'break'
        
        def shiftTabKey(event):
            if self.input_pad.get('insert -4c','insert') == "    ":
                self.input_pad.delete('insert -4c','insert')
            return 'break'

        #__実行部分__
        self.input_pad.configure(insertbackground="#FFFFFF",insertwidth=3)
        self.input_pad.bind('<Return>',arrangeIndent)
        self.input_pad.bind('<Tab>',tabKey)
        self.input_pad.bind('<Shift-Tab>',shiftTabKey)

        #--------------------#
    
    #サンプル実行
    def test_debug(self):
        print("sample")
        print(self.debug())
    
    #採点する
    def confirm_answer(self):
        print("confirm")
        print(self.debug())

    #デバッグする
    def debug(self):
        prog = self.input_pad.get("1.0","end").splitlines("\n")
        num_of_input = 0
        task_num = 0
        for i in range(len(prog)):
            if "input(" in prog[i]:
                prog[i] = prog[i].replace("input(",f"getCaseInput({task_num},{num_of_input},")
                num_of_input += 1
            prog[i] = "    " + prog[i]
        prog = ["from libraries.caseVerificator import getCaseInput\ndef run():\n"]+prog
        debugger = codeDebugger
        result = debugger.debug(prog=prog)
        return(result)
        
    #デバッグの結果を取得
    def get_result(self):
        return(self.debug())

    #プロンプトを表示
    def show(self):
        self.Prompt.place(relheight=1.0,relwidth=0.5,relx=0.5,rely=0.0)

    #プロンプトを非表示
    def hide(self):
        self.Prompt.place_forget()
    
    #サンプルケースを設定
    def setInputSampleCase(self,cases):
        self.input_cases = cases