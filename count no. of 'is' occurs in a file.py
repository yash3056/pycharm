def count_is():
    f=open("notes.txt","r")
    s=f.read()
    l=s.split()
    count=0
    for i in l:
        if i=="is":
            count+=1
    print("NO. OF TIMES WORD 'IS' OCCURS: ",count)
    f.close()
count_is()