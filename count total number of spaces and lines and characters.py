def count_txt():
    f = open('notes.txt','r')
    text = f.read()
    space=char=line=0
    for i in text:
        if (i ==" "):
            space += 1
        elif (i =="\n"):
            line += 1
        else:
            char += 1
    print("space =", space,"lines =", line,"char =", char )
count_txt()
