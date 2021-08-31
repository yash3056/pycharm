def bubblesort(l):
    n=len(l)
    print("ORIGINAL LIST: ",l)
    for i in range(n-1):
        for j in range(n-i-1):
            if l[j]>l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    print("LIST AFTER SORTING IS: ",l)
list=[42,67,55,11,98,34,83,72]
bubblesort(list)