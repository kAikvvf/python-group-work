import csv

field_names = ['title','quest_statement','estimated_required_time','sample_case','correct_answer']

def getCSVFile():
    with open('data/questDict.csv','r',encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file,field_names)
        quest_list = [i for i in reader]
        return(quest_list)

def getNumOfQuest():
    return(len(getCSVFile())-1)

def getTitle(quest_index):
    return(str(getCSVFile()[quest_index+1]['title']))

def getQuestStatement(quest_index):
    return(str(getCSVFile()[quest_index+1]['quest_statement']))

def getEstimatedRequredTime(quest_index):
    return(int(getCSVFile()[quest_index+1]['estimated_required_time']))

def getSampleCase(quest_index):
    sample_case_list = getCSVFile()[quest_index+1]['sample_case'].split('<sample_separator>')
    for i in range(len(sample_case_list)):
        sample_case_list[i] = sample_case_list[i].split('<case_separator>')
    return(sample_case_list)

def getCorrectAnswer(quest_index):
    correct_answer_raw_string = getCSVFile()[quest_index+1]['correct_answer']
    correct_answer_raw_string = correct_answer_raw_string.replace('\\n','\n')
    correct_answer_list = correct_answer_raw_string.split('<answer_separator>')
    return(correct_answer_list)

'''
print(getTitle(0))
print(getQuestStatement(0))
print(getEstimatedRequredTime(0))
print(getSampleCase(0))
print(getCorrectAnswer(0))
'''