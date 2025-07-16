from tkinter import *
from tkinter import messagebox
import csv
from scripts import questDataHandler
from scripts import main

class loginPad:
    def __init__(self):
        self.root = Tk()
        self.root.title("ログイン")
        
        with open("data/.user-list.txt","r") as user_data:
            self.user_data = user_data.read().split(".")
            for i in range(len(self.user_data)):
                self.user_data[i] = self.user_data[i].split(",")
        Label(master=self.root,text="ユーザー名とパスワードを入力してください").grid(column=0,row=0,columnspan=2,padx=3)
        Label(master=self.root,text="ユーザー名",padx=3).grid(row=1,column=0)
        self.USERNAME_INPUT = Entry(master=self.root,width=30)
        self.USERNAME_INPUT.grid(row=1,column=1,padx=5,pady=3)
        Label(master=self.root,text="パスワード",padx=3).grid(row=2,column=0)
        self.PASSWORD_INPUT = Entry(master=self.root,width=30)
        self.PASSWORD_INPUT.grid(row=2,column=1,padx=5,pady=3)
        Button(master=self.root,text="ログイン",command=self.verificateUser).grid(row=3,column=1,padx=5,pady=5)
        Button(master=self.root,text="新規",command=self.newUser).grid(row=3,column=0,padx=5,pady=5)

        self.root.mainloop()
    #ユーザーを照合
    def verificateUser(self):
        username = self.USERNAME_INPUT.get()
        password = self.PASSWORD_INPUT.get()
        if [username,password] in self.user_data:
            self.successLogin(username)
        else:
            self.failLogin()

    #新規ユーザを作成
    def newUser(self):
        self.root.destroy()
        new_user_win = Tk()
        new_user_win.title("ユーザーを新規作成")

        def confirmNewUser():
            new_username = new_username_input.get()
            new_password = new_password_input.get()

            username_list = []
            for i in range(len(self.user_data)):
                current_username = self.user_data[i][0]
                username_list.append(current_username)
            password_list = []
            for i in range(len(self.user_data)):
                current_password = self.user_data[i][1]
                password_list.append(current_password)

            if len(new_password) <8:
                messagebox.showwarning("エラー","パスワードは8桁以上にしてください。")
    
            elif new_username in username_list:
                messagebox.showwarning("エラー","入力したユーザー名は既に使われています。")
            elif new_password in password_list:
                messagebox.showwarning("エラー","入力したパスワードは既に使われています。")
            else:
                if messagebox.askokcancel("確認",f"ユーザー名とパスワードがあっているか確認してください。\nユーザー名：{new_username}\nパスワード：{new_password}") == True:
                    with open("data/.user-list.txt","a") as append_directory:
                        append_directory.write(f".{new_username},{new_password}")
                    with open(f'data/.{new_username}.csv','w',encoding='utf-8') as new_user_data_file:
                        writer = csv.DictWriter(new_user_data_file,['quest_index','status','score','start_time','end_time','number_of_confirm','prog_statement'])
                        writer.writeheader()
                        empty_data = []
                        for i in range(len(questDataHandler.getCSVFile())):
                            empty_data.append({'quest_index':i,'status':False,'score':0,'start_time':'null','end_time':'null','number_of_confirm':0,'prog_statement':''})
                        writer.writerows(empty_data)
                    new_user_win.destroy()
                    self.__init__()
        Label(master=new_user_win,text="ユーザーを新規作成").grid(row=0,column=0,columnspan=2)
        Label(master=new_user_win,text="ユーザー名").grid(row=1,column=0)
        Label(master=new_user_win,text="パスワード").grid(row=2,column=0)
        new_username_input = Entry(master=new_user_win,width=30)
        new_username_input.grid(row=1,column=1)
        new_password_input = Entry(master=new_user_win,width=30)
        new_password_input.grid(row=2,column=1)
        Button(master=new_user_win,text="確認",command=confirmNewUser).grid(row=3,column=1)
        Label(master=new_user_win,text="*注意*\nパスワードは全て半角英数とする。また、パスワードは８桁以上。").grid(row=4,column=0,columnspan=2)
        new_user_win.mainloop()

    #ログイン成功時の処理
    def successLogin(self,username):
        self.root.destroy()
        main.main(username)
        self.__init__()

    #ログイン失敗時の処理
    def failLogin(self):
        print("Failed To Login")
        messagebox.showerror("ログインエラー","ログインできません。\nユーザーまたはパスワードが間違えています。\n未登録の場合は ユーザー を新規作成して下さ。")