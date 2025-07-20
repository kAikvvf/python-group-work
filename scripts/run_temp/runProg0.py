class generateResult:
    def __init__(self):
        self.sample_data = ['2']
        self.sample_index = 0
        for i in range(10):
            print(i)
        
    def inputMode(self,*message):
        if not message == ():
            print(message[0])
        self.sample_index += 1
        return(self.sample_data[self.sample_index-1])