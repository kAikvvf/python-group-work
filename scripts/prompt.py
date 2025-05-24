from libraries.codeDebugger import codeDebugger
import tkinter as tk
import math

class prompt:
    def __init__(self,
                 root_Tk,
                 input_font_size = 5,
                 ):
        self.Prompt = tk.Canvas(master=root_Tk)
        Button_Pad = tk.Canvas(master=self.Prompt)
        self.input_pad = tk.Text(self.Prompt,
                                 font=("",input_font_size),
                                 foreground="#000000",
                                 background="#FFFFFF")
        test_debug_button = tk.Button(Button_Pad,
                                      text="サンプル実行",
                                      command=self.debug,
                                      font=("BIZ UDゴシック",10,"bold"),
                                      background="#69B7FC",
                                      relief="groove")

        confirm_answer_button = tk.Button(Button_Pad,
                                          text="採点",
                                          command=self.confirm_answer,
                                          font=("BIZ UDゴシック",10,"bold"),
                                          background="#FF6FBC",
                                          relief="groove")

        test_debug_button.pack(anchor=tk.SE,side=tk.LEFT,padx=5,pady=3,ipadx=3,ipady=3)
        
        confirm_answer_button.pack(anchor=tk.SE,side=tk.LEFT,padx=5,pady=3,ipadx=3,ipady=3)
        Button_Pad.pack(anchor=tk.SE,side=tk.BOTTOM)
        self.input_pad.pack(fill=tk.BOTH,expand=1)

        #----------編集時に書きやすくする----------#
        self.indent = 0
        self.index = 0

        #__改行時にインデントをそろえる__
        def arrangeIndent(event):
            index_now = self.input_pad.index('insert')
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
                print(index)
                #インデントを次の行に入れる
                indent = index // 4


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

        self.input_pad.bind('<Return>',arrangeIndent)
        self.input_pad.bind('<Tab>',tabKey)
        self.input_pad.bind('<Shift-Tab>',shiftTabKey)

        #--------------------#
    def confirm_answer(self):
        self.debug()
        print(self.get_result())
        print(type(self.get_result()))

    def debug(self):
        prog = self.input_pad.get("1.0","end").splitlines("\n")
        for i in range(len(prog)):
            prog[i] = "    " + prog[i]
        prog = ["def run():\n"]+prog
        debugger = codeDebugger
        self.result = debugger.debug(prog)
        

    def get_result(self):
        return(self.result)

    def show(self):
        self.Prompt.place(relheight=1.0,relwidth=0.5,relx=0.5,rely=0.0)

    def hide(self):
        self.Prompt.place_forget()