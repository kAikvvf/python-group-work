from tkinter import *
from tkinter import messagebox
from scripts.kotone import Question
import time

'''
ログイン後に実行する部分
関数 main() 内に書き込む
'''
def main(USERNAME): #引数にユーザー名を入力
    root = Tk()
    root.title(f"Python Techful  -{USERNAME}-")
    root.geometry('800x600')
    Question(root,1)

    def onClosingWindow():
        if messagebox.askokcancel(title='終了',message='本当に終了しますか？') == True:
            root.destroy()
    root.protocol("WM_DELETE_WINDOW", onClosingWindow)
    root.mainloop()
'''---------------------'''