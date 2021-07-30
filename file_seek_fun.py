def File_Seek_Fun():
    f=open("notes2.txt",'r')
    f.seek(7)
    f_data=f.read(1)
    pos=f.tell()
    print("contemt of f_data is = ", f_data)
    print("the current position = ",pos)
    f.close()
File_Seek_Fun()