def File_Handle():
    f=open("notes2.txt",'w')
    f.write("this is test 2")
    print("FILE created")
    f.close()
File_Handle()