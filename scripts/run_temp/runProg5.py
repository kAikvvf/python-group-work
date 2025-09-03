class generateResult:
    def __init__(self):
        self.sample_data = ['45', '8', '一般']
        self.sample_index = 0
        age= int(self.inputMode("年齢を入力してください"))
        birth = int(self.inputMode("誕生月を教えてください"))
        if age >= 18:
            usertype = str(self.inputMode("あなたは、学生ですか？一般ですか？"))
            if usertype == "学生":
                if birth == 7:
                    print("チケット料金は、１０００円です。")
                else:
                    print("チケット料金は、１２００円です。")
            if usertype == "一般":
                if birth == 7:
                    print("チケット料金は、１６００円です。")
                else:
                    print("チケット料金は、１８００円です。")
        
        else:
            if birth == 7:
                print("チケット料金は、８００円です。")
            else:
                print("チケット料金は、１０００円です。")
        
    def inputMode(self,*message):
        if not message == ():
            print(message[0])
        self.sample_index += 1
        return(self.sample_data[self.sample_index-1])