def count_dig():
    f=open("notes.txt","r")
    text=f.read()
    dig=0
    for i in text:
        if(i.isnumeric()):
            dig+=1
    print("no. of digits =",dig)
count_dig()