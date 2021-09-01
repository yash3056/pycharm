def string(s):
    d={"UPPER_CASE":0,"LOWER_CASE":0}
    for i in s:
        if i.isupper():
            d["UPPER_CASE"]+=1
        elif i.islower():
            d["LOWER_CASE"]+=1
        else:
            pass
    print("NO. OF UPPERCASE CHARACTERS:",d["UPPER_CASE"])
    print("NO. OF LOWER CASE CHARACTERS: ",d["LOWER_CASE"])
string("pythonprogramming")