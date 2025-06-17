import csv

def entireData():
    with open("data/questData.csv","r",encoding="utf-8") as questData:
        reader = csv.reader(questData)
        questDataList = []
        for row in reader:
            questDataList.append(list(row))
        questData.close()

    for i in range(len(questDataList)):
        questDataList[i][0] = questDataList[i][0].replace("\\n","\n")
        for j in range(int(questDataList[i][2])):
            questDataList[i][3+j] = questDataList[i][3+j].split("|")
            questDataList[i][3+j][1] = questDataList[i][3+j][1].split(".")
            questDataList[i][3+j][2] = questDataList[i][3+j][2].replace("\\n","\n")

    return(questDataList)

def questStatement(quest_index):
    return(entireData()[quest_index][0])

def estimatedRequiredTime(quest_index):
    return(entireData()[quest_index][1])
    
def numberOfCases(quest_index):
    return(entireData()[quest_index][2])
    
def entireSampleCases(quest_index):
    return(entireData()[quest_index][3:])
    
def sampleCase(quest_index:int,case_index:int):
    return(entireData()[quest_index][3+case_index])