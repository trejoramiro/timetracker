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