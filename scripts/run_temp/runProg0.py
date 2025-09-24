class generateResult:
    def __init__(self):
        self.sample_data = ['']
        self.sample_index = 0
        print('Hello World')
        
        
        
    def inputMode(self,*message):
        if not message == ():
            print(message[0])
        self.sample_index += 1
        return(self.sample_data[self.sample_index-1])