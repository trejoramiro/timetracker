#timetracker.py

#start, pause, exit, save, update, close, terminate

import csv

import time
import calendar 

from datetime import datetime

projectList = []
#Enter your project's name
projectName = raw_input("Enter Project Name: ")

#Place project into projectList
projectList.append(projectName)

start = datetime.now()
print("Active Project Name: {}".format(projectList[0]))
print("Start Time: {}:{}:{}".format(start.hour,start.minute,start.second))
print("Date: {}:{}:{}".format(start.month,start.day,start.year))

while(projectName != "QUIT"):
    
    if(projectName == "STATUS"):
    
        sum_hour = abs(start.hour - datetime.now().hour)
        sum_minute = abs(start.minute - datetime.now().minute)
        sum_second = abs(start.second - datetime.now().second)

        print("Status: {} hours {} minutes {} seconds".format(sum_hour,sum_minute,sum_second))
                  
     if(projectName == "PAUSE"):
        
        pause_period = datetime.now()
        

     else:
        continue
                                  
                     
#####Notes to Self#####
## the program must be able to save each entered time
## in case the computer shuts down