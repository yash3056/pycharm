import csv
with open('student.csv','r' ) as file:
    reader = csv.reader(file,delimiter=',')
    count_rec=0
    count_s=0
    for row in reader:
        if row[1][0].lower()=='t':
            print(row[0],',',row[1],',',row[2])
            count_s+=1
        count_rec+=1
    print("Number of „T‟ names are",count_s,"/",count_rec)
