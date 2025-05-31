from libraries.quest_data_unpacker import unpackQuestData

class questExtracter:
    def __init__(self,quest_num):
        self.quest_index = quest_num-1
        self.quest_num = quest_num
        self.unpacker = unpackQuestData()
        self.data = self.unpacker.getWholeData()

    def getQuestStatement(self):
        return(self.data[self.quest_index][0])
    
    def getQuestRequiredTime(self):
        return(self.data[self.quest_index][1])
    
    def getSampleQuantities(self):
        return(self.data[self.quest_index][2])
    
    def getSampleCases(self):
        return(self.data[self.quest_index][3:])