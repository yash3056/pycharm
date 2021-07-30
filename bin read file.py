def bin_read_file():
    import pickle
    f=open("list.dat",'rb')
    list1=pickle.load(f)
    print("content of binary file is: \n")
    print(list1)
    f.close()
bin_read_file()