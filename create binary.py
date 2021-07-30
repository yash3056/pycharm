def bin_create():
    import pickle
    list1=[40,50,67,39,42,95,897,647,125]
    f=open("list.dat",'wb')
    pickle.dump(list1,f)
    print("information added to binary file")
    f.close()
bin_create()