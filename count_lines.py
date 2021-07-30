def Count_Lines():
    f = open("notes2.txt",'r')
    count = 0
    for l in f.readline():
        c =l[0]
        print(c)
        if(c=='D') or (c=='M'):
            count+=1
            print(count)

    print("Total no of Lines = ", count)
Count_Lines()

def countwords():
    f=open("notes2.txt",'r')
    data=f.read()
    word=data.split()
    print(word)
    for i in word:
        if i=="to" or i=="the"
            print(i)