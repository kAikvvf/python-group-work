import datetime
import csv

class userDataHandler:
    def __init__(self,username):
        self.username = username
        self.field_name = ['quest_index','status','score','start_time','end_time','number_of_confirm','prog_statement']

        self.user_data = []
        with open(f'data/.{username}.csv','r',encoding='utf-8') as user_read_file:
            reader = csv.DictReader(user_read_file,self.field_name)
            for i in reader:
                self.user_data.append(i)
    
    def getQuestStatus(self,quest_index):
        return(self.user_data[quest_index+1]['status'])
    
    def getScore(self,quest_index):
        return(self.user_data[quest_index+1]['score'])

    def getNumOfConfirm(self,quest_index):
        return(int(self.user_data[quest_index+1]['number_of_confirm']))

    def getStatus(self,quest_index):
        return(self.user_data[quest_index+1]['status'])
    
    def getStartTime(self,quest_index):
        if not self.user_data[quest_index+1]['start_time'] == 'null':
            time_now = self.user_data[quest_index+1]['start_time'].split('</>')
            time_now = datetime.datetime(int(time_now[0]),int(time_now[1]),int(time_now[2]),int(time_now[3]),int(time_now[4]),int(time_now[5]))
            return(time_now)
        else:
            return('null')

    def getEndTime(self,quest_index):
        if not self.user_data[quest_index+1]['end_time'] == 'null':
            time_now = self.user_data[quest_index+1]['end_time'].split('</>')
            time_now = datetime.datetime(int(time_now[0]),int(time_now[1]),int(time_now[2]),int(time_now[3]),int(time_now[4]),int(time_now[5]))
            return(time_now)
        else:
            return('null')
    
    def getProgStatement(self,quest_index):
        return(self.user_data[quest_index+1]['prog_statement'])

    def setStartTime(self,quest_index):
        time_now = datetime.datetime.now()
        year_now = time_now.year
        month_now = time_now.month
        day_now = time_now.day
        hour_now = time_now.hour
        minute_now = time_now.minute
        second_now = time_now.second
        self.user_data[quest_index+1]['start_time'] = f'{year_now}</>{month_now}</>{day_now}</>{hour_now}</>{minute_now}</>{second_now}'
        self.rewrite()
    
    def setEndTime(self,quest_index):
        time_now = datetime.datetime.now()
        year_now = time_now.year
        month_now = time_now.month
        day_now = time_now.day
        hour_now = time_now.hour
        minute_now = time_now.minute
        second_now = time_now.second
        time_now = f'{year_now}</>{month_now}</>{day_now}</>{hour_now}</>{minute_now}</>{second_now}'
        self.user_data[quest_index+1]['end_time'] = time_now
        self.rewrite()
    
    def addNumOfConfirm(self,quest_index):
        num_of_confirm_now = int(self.getNumOfConfirm(quest_index))+1
        self.user_data[quest_index+1]['number_of_confirm'] = num_of_confirm_now
        self.rewrite()
    
    def setStatus(self,quest_index,status:bool):
        self.user_data[quest_index+1]['status'] = status
        self.rewrite()
    
    def setProgStatement(self,quest_index:int,prog_statement:bool):
        self.user_data[quest_index+1]['prog_statement'] = prog_statement.replace('\n','\\n')
        self.rewrite()
    
    def setScore(self,quest_index,score):
        self.user_data[quest_index+1]['score'] = score
        self.rewrite()

    def rewrite(self):
        with open(f'data/.{self.username}.csv','w',encoding='utf-8') as write_file:
            writer = csv.DictWriter(write_file,self.field_name)
            writer.writerows(self.user_data)
        self.__init__(self.username)