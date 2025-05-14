from libraries.codeDebugger import codeDebugger
import tkinter as tk

class prompt:
    def __init__(self,
                 root_Tk,
                 width = 100,
                 row = 50,
                 input_pack_padx = 10,
                 input_pack_pady = 10,
                 input_font_size = 5,
                 result = 0
                 ):
        
        self.input_pad = tk.Text(root_Tk,width=width,height=row,font=("",input_font_size))
        self.input_pad.pack(padx=input_pack_padx,pady=input_pack_pady)
        debug_button = tk.Button(root_Tk,text="Confirm",command=self.debug)
        debug_button.pack()
        self.result = result

    def debug(self):
        prog = self.input_pad.get("1.0","end").splitlines("\n")
        for i in range(len(prog)):
            prog[i] = "    " + prog[i]
        prog = ["def run():\n"]+prog
        debugger = codeDebugger
        self.result = debugger.debug(prog)
    
    def get_result(self):
        return(self.result)