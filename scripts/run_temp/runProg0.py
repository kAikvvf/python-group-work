class generateResult:
    def __init__(self):
        self.sample_data = ['1.60', '45.2']
        self.sample_index = 0
        class Person:
            def __init__(self, height, weight):
                self.height = height
                self.weight = weight
        
        
            def bmi_num(self):
                num = self.weight/self.height**2
                return num
        
            def bmi_level(self):
                num = self.bmi_num()
                if num < 18.5:
                    level = "低体重"
                elif num < 25:
                    level = "普通体重"
                elif num < 35:
                    level = "肥満"
                else:
                    level = "高度肥満"
        
                print("あなたのbmiは、", self.bmi_num(), "で、" + level + "です。")
        
                return level
        
        height = float(self.inputMode("身長（m）を入力してください"))
        weight = float(self.inputMode("体重（㎏）を入力してください"))
        
        fa = Person(height,weight)
        fa.bmi_level()
        
    def inputMode(self,*message):
        if not message == ():
            print(message[0])
        self.sample_index += 1
        return(self.sample_data[self.sample_index-1])