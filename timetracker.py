#timetracker.py

#start, pause, exit, save, update, close

import csv

import time
import calendar 

from datetime import datetime

projectList = []
#Enter your project's name
print("Timetracker On.")
projectName = raw_input("Enter Project Name: ")

#Place project into projectList
projectList.append(projectName)

#before going inside the while loop, make sure user has input a project name.

#the program will then combine the data that duplicates at a later date using R or python

start = datetime.now()
print("Active Project Name: {}".format(projectList[0]))
print("Start Time: {}:{}:{}".format(start.hour,start.minute,start.second))
print("Date: {}:{}:{}".format(start.month,start.day,start.year))

while(projectName != "EXIT"):
    
    projectName = raw_input(">> ")
    
    if(projectName == "STATUS"):
    
        sum_hour = abs(start.hour - datetime.now().hour)
        sum_minute = abs(start.minute - datetime.now().minute)
        sum_second = abs(start.second - datetime.now().second)

        print("Status: {} hours {} minutes {} seconds".format(sum_hour,sum_minute,sum_second))\
        continue
                  
    if(projectName == "PAUSE"):
        
        pause_period = datetime.now()
        print("Project has been paused.")
        
        input = raw_input("Press any key to continue timetracking.")
        print("Project {} Continued".format(projectList[0]))
        continue
    
    #if(projectName == "EXIT"):
            
        #print("Project Saved and Closed.")      
        #break 
        
    if(projectName == "CLOSE"):
        
        print("Project Closed.")
        #create a function to include a project input and return a value to projectName
        
    else:
        print("INVALID INPUT")

print("Project Saved and Closed.")   
print("Timetracker Closed.")                                
                     
#####Notes to Self#####
## the program must be able to save each entered time
## in case the computer shuts down

#also need to make sure how to write data onto a cvs file, should
#i put the data in a list before placing it inside