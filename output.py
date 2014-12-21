import csv
from datetime import datetime

project = datetime.now


with open('file.csv','rb') as csvfile:
    filereader = csv.reader(csvfile, delimiter=',')
    line1 = filereader.next() #Skip the first row
    print(line1)
    csvfile.close()

with open('file.csv', 'wb') as csvfile:
    filewriter = csv.writer(csvfile)
    filewriter.writerows(str(project)) 
    print("Wrote successfully")
    
#problem with code, fix line 15, the program overrides the first line and does not
#write the program successfully