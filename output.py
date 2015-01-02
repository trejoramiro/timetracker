import csv


with open('discoveries.csv','rb') as f:
    reader = csv.reader(f, delimiter=',')
    rownum = 0
    years = 0
    for row in reader: #reader functions as a multiarray string containing list ojbects
########################################################        
        #if rownum == 0:
            #header = row #row contains a list of strings 
        #for col in row:
            #print(col)
            #how much data bits are used for each integer type in python?
            #row[0] row[1] row[2] are each column in entirety
            #break
########################################################
        if rownum == 0:
            print(row[1])
            rownum = rownum + 1
        else:
            string_num = row[1]
            years = years + int(string_num)
            rownum = rownum + 1
            
    f.close()


csv_data = []

#open the cvs file and save the data into a list
f = open('discoveries.csv','rb')
#reader = csv.reader(f,delimiter=',')
#print(reader.next())
#print(reader)
csv_data = list(csv.reader(f, delimiter=','))
f.close()

#combining two csv files may be a small issue bec we need to eliminate its fieldnames

f2 = open('discoveries.csv','rb')
csv_data2 = list(csv.reader(f2, delimiter=','))
f2.close()

csv_data2.pop(0)

print(len(csv_data))
print(len(csv_data2))

mergedData = csv_data + csv_data2

print(len(mergedData))

print("The average year is: {}".format(years/(rownum-1)))

    #line1 = filereader.next() #Skip the first row
    #print(line1)
    #line2 = filereader.next()
    #print(line2)

#with open('file.csv', 'wb') as csvfile:
#    filewriter = csv.writer(csvfile)
#    filewriter.writerows(str(project)) 
#    print("Wrote successfully")
    
#problem with code, fix line 15, the program overrides the first line and does not
#write the program successfully