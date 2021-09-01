size=20
num=int(input("ENTER RECORD NO. TO BE SEARCHED: "))
with open("names.dat","rb") as f:
    f.seek(size*(num-1))
    str=f.read(size)
    if(len(str)==0):
        print("INCORRECT POSITION")
    else:
        print(str.decode())