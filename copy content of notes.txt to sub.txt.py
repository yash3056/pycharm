def copy_file():
    f1=open("notes.txt",'r')
    f2=open("sub.txt",'w+')
    data=f1.read()
    f2.write(data)
    print("FILE IS COPIED")
    f1.close()
    f2.close()
copy_file()