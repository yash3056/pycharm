stk=[]
choice='y'
while (choice in "yY"):
    print("Option Menu")
    print("1. Push (insert) an element in stack")
    print("2. Pop (delete) an element from stack")
    print("3. Traverse (display) stack data")
    opt=int(input("enter your choice(1 to 3):"))
    if (opt==1):
        d=input("enter data to be inserted in stack")
        stk.append(d)
    elif(opt==2):
        if(stk==[]):
            print("stack is empty")
        else:
            p=stk.pop()
            print("popped",p,"from stack")
    elif(opt==3):
        l=len(stk)
        for i in range(l-1,-1,-1):
            print(stk[i])
    else:
        print("invalid option")
    choice=input("do you want to continue y/n ")