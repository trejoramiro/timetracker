#timetracker.py
#start, pause, exit, status, close

#from sql import *
#from sql.aggregate import *
#from sql.conditionals import *
#import mysql.connector

from datetime import datetime
from datetime import date
import csv

#Enter your project's name
print("Timetracker On.")
projectTitle = raw_input("Enter Project Name to Track: ")
projectType = raw_input("Enter Type of Project: ")

#before going inside the while loop, make sure user has input a project name.
#the program will then combine the data that duplicates at a later date using R or python

#*************************
#projectTitle
#projectType
noteSection = " "
totalMinutes = 0.0
projectDate = date.today()
initTime = datetime.now()
#***************************

print("**Init Project: {}**".format(projectTitle))
#print("Start Time: {}:{}:{}".format(start.hour,start.minute,start.second))
#print("Date: {}:{}:{}".format(start.month,start.day,start.year))

userInput = " "
userInput = raw_input(">> ")

while(userInput != "EXIT"):

    
    if(userInput == "STATUS"):
    
        sumHour = abs(initTime.hour - datetime.now().hour)
        sumMinute = abs(initTime.minute - datetime.now().minute)
        sumSecond = abs(initTime.second - datetime.now().second)

        print("Status: {} hours {} minutes {} seconds".format(sumHour,sumMinute,sumSecond))
        
        #after paused, status starts all over, should not be like this!
                  
    if(userInput == "PAUSE"):
        
        pauseTime = datetime.now()
        print("Project has been paused.")
        
        input = raw_input("Press any key to continue timetracking: ")
        
        sumHour = abs(initTime.hour - pauseTime.hour)
        sumMinute = abs(initTime.minute - pauseTime.minute)
        sumSecond = abs(initTime.second - pauseTime.second)
        
        totalMinutes = (sumHour*60) + sumMinute + (sumSecond/60)
        initTime = datetime.now()
        print("Project {} Continued".format(projectTitle))
        
    if(userInput == "CLOSE"):
        
        print("Project Closed.")
        #create a function to include a project input and return a value to projectName
        
    if(userInput == "NOTE"):
        noteSection = raw_input("Start note: ")
        print("**Note Completed**")
        
    else:
        print("INVALID INPUT")
        print("VALID INPUTS: STATUS, PAUSE, CLOSE, NOTE, and EXIT.")
    
    userInput = raw_input(">> ")

#calculate the time in minutes
timeCalculated = (initTime.hour*60) + initTime.minute + (initTime.second/60)
totalMinutes+= timeCalculated

#format date
stringDate = str(projectDate.month) + "/" + str(projectDate.day) + "/" + str(projectDate.year)

#creat list 
x = [projectTitle,projectType,stringDate,totalMinutes,noteSection]

#write to CSV file
with open ('january.csv', 'ab') as f:
    wtr = csv.writer(f)
    wtr.writerow(x)
# writes the data on one row!! not good

#print exit message
print("Project {} Saved and Closed.".format(projectTitle))   
print("Timetracker Closed.")        

#Timetracker does not recognize AM and PM, must fix for next verison. 