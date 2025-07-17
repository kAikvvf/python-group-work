from tkinter import *
from tkinter import messagebox
from scripts.kotone import Question
from scripts.revenge import Main
import time

'''
ログイン後に実行する部分
関数 main() 内に書き込む
'''
def main(USERNAME): #引数にユーザー名を入力
    root = Tk()
    root.title(f"Python Techful  -{USERNAME}-")
    root.geometry('800x600')

    quest_select_page = Frame(root)
    answer_page = Frame(root)

    quest_list = Main(quest_select_page,USERNAME,answer_page)
    quest_select_page.pack(fill='both',expand=True)

    def onClosingWindow():
        if messagebox.askokcancel(title='終了',message='本当に終了しますか？') == True:
            root.destroy()
    root.protocol("WM_DELETE_WINDOW", onClosingWindow)
    root.mainloop()
'''---------------------'''