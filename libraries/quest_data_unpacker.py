import csv

class unpackQuestData:
    def __init__(self):
        with open("quest-data.csv",encoding="utf8",newline='') as d:
            DATA_FILE = csv.reader(d)
            QUEST_DATA = []
            for row in DATA_FILE:
                QUEST_DATA.append(row)
    
        # 型を直す
        for row_index in range(len(QUEST_DATA)):
            row_data = QUEST_DATA[row_index]
            row_data[0] = str(row_data[0])
            row_data[1] = int(row_data[1])
            row_data[2] = int(row_data[2])
            for i in range(row_data[2]):
                data = row_data[i+3].split("|")
                data[0] = int(data[0])
                row_data[i+3] = data
            QUEST_DATA[row_index] = row_data
        self.QUEST_DATA = QUEST_DATA
    
    def getWholeData(self):
        return(self.QUEST_DATA)
    
    def getQuestData_byQuestNum(self,quest_num):
        return(self.QUEST_DATA[quest_num-1])

    def getQuestStatement_byQuestNum(self,quest_num):
        return(self.QUEST_DATA[quest_num-1][0])
    
    def getQuestTimeLimit_byQuestNum(self,quest_num):
        return(self.QUEST_DATA[quest_num-1][1])
    
    def getQuestSampleQuantity_byQuestNum(self,quest_num):
        return(self.QUEST_DATA[quest_num-1][2])