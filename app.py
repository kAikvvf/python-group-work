from tkinter import *
from tkinter import messagebox
from scripts.kotone import Question

#ログインするために初期設定
login_root = Tk()
login_root.title("ログイン")
#--------------------#


'''
ログイン後に実行する部分
関数 main() 内に書き込む
'''
def main(USERNAME):
    login_root.destroy()
    print(USERNAME)
    root = Tk()
    root.title("Python Techful")
    root.geometry('800x600')
    Question(root,1)
    root.mainloop()

'''---------------------'''


#------ログインの処理------
with open("data/.user-list.txt","r") as user_data:
    user_data = user_data.read().split(".")
    for i in range(len(user_data)):
        user_data[i] = user_data[i].split(",")
    USERNAME_INPUT = Entry(master=login_root,width=30)
    PASSWORD_INPUT = Entry(master=login_root,width=30)
    confirm_button = Button(master=login_root,text="ログイン")
    new_user_button = Button(master=login_root,text="新規")

def start():
    Label(master=login_root,text="ユーザー名とパスワードを入力してください").grid(column=0,row=0,columnspan=2,padx=3)
    Label(master=login_root,text="ユーザー名",padx=3).grid(row=1,column=0)
    USERNAME_INPUT.grid(row=1,column=1,padx=5,pady=3)
    Label(master=login_root,text="パスワード",padx=3).grid(row=2,column=0)
    PASSWORD_INPUT.grid(row=2,column=1,padx=5,pady=3)
    confirm_button.grid(row=3,column=1,padx=5,pady=5)
    new_user_button.grid(row=3,column=0,padx=5,pady=5)
    login_root.mainloop()

#ユーザーを照合
def verificateUser():
    username = USERNAME_INPUT.get()
    password = PASSWORD_INPUT.get()
    if [username,password] in user_data:
        successLogin(username)
    else:
        failLogin()
confirm_button.config(command=verificateUser)

#新規ユーザを作成
def newUser():
    login_root.destroy()
    new_user_win = Tk()
    new_user_win.title("ユーザーを新規作成")

    def confirmNewUser():
        new_username = new_username_input.get()
        new_password = new_password_input.get()

        username_list = []
        for i in range(len(user_data)):
            current_username = user_data[i][0]
            username_list.append(current_username)
        password_list = []
        for i in range(len(user_data)):
            current_password = user_data[i][1]
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
                new_user_win.destroy()
                start()
                
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
new_user_button.config(command=newUser)

#ログイン成功時の処理
def successLogin(username):
    main(username)
    login_root.destroy()

#ログイン失敗時の処理
def failLogin(self):
    messagebox.showerror("ログインエラー","ログインできません。\nユーザーまたはパスワードが間違えています。\n未登録の場合は ユーザー を新規作成して下さ。")
#--------------------#

#実行
start()