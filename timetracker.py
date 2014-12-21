#timetracker.py

#start, pause, exit, save, update, close, terminate

import csv

import time
import calendar 

from datetime import datetime


#Enter your project's name
project = raw_input("Enter Project Name: ")

#Start project object instance
start = datetime.now()
print("Your Project Name is {}".format(project))
print("Start time: {}:{}:{}".format(start.hour,start.minute,start.second))
print("On: {}:{}:{}".format(start.month,start.day,start.year))


#math variables 

continues = raw_input("Enter to continue ")
end = datetime.now()

sum_hour = abs(start.hour - datetime.now().hour)
sum_minute = abs(start.minute - datetime.now().minute)
sum_second = abs(start.second - datetime.now().second)

print("Status: {} hours {} minutes {} seconds".format(sum_hour,sum_minute,sum_second))
#Open CSV
                     
#Record the time


                     
                     
                     
                     
#####Notes to Self#####
## the program must be able to save each entered time
## in case the computer shuts down