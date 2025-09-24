class generateResult:
    def __init__(self):
        self.sample_data = ['34']
        self.sample_index = 0
        x = self.inputMode('好きな整数を入力してください。')
        print(x)
        
        
        
        
    def inputMode(self,*message):
        if not message == ():
            print(message[0])
        self.sample_index += 1
        return(self.sample_data[self.sample_index-1])