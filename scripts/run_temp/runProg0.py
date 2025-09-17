class generateResult:
    def __init__(self):
        self.sample_data = ['小太郎']
        self.sample_index = 0
        print('名前を入力してください')
        print('こんにちは、小太郎さん')
        
        
    def inputMode(self,*message):
        if not message == ():
            print(message[0])
        self.sample_index += 1
        return(self.sample_data[self.sample_index-1])