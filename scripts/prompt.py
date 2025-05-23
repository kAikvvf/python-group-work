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

        def addIndent(func):
            def indentWrapper(*args,**kwargs):
                func(*args,**kwargs)
                if self.indent > 0 & self.index % 4 ==0:
                    self.input_pad.insert('insert',"\n")
                    for i in range(self.indent):
                        self.input_pad.insert('insert',"    ")
            return indentWrapper

        @addIndent
        def checkIndent(event):
            index_now = self.input_pad.index('insert')
            row_now = math.floor(float(index_now))
            content_in_line = self.input_pad.get(f'{row_now}.0',f'{row_now}.end')
            index = 0

            #インデントのスペースを数える
            while True:
                if content_in_line[index] != " ":
                    break
                index +=1
            #インデントを次の行に入れる
            indent = index // 4

            self.index = index
            self.indent = indent

        self.input_pad.bind('<Return>',checkIndent)


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