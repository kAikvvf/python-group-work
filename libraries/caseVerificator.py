import csv
def getCaseInput(task_index,input_index,messege):
    cases_list = []
    with open("sample.csv","r") as cases:
        for row in csv.reader(cases):
            cases_list.append(list(map(int,row)))
    print(messege)
    return(cases_list[task_index][input_index])