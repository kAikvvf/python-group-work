class generateResult:
    def __init__(self):
        self.sample_data = ['5', '4', '3', '6', '3', '3', '1']
        self.sample_index = 0
        while True:
            x = int(self.inputMode('1~10 までの整数を入力'))
            if x == 1:
                print('clear')
                break
        
    def inputMode(self,*message):
        if not message == ():
            print(message[0])
        self.sample_index += 1
        return(self.sample_data[self.sample_index-1])