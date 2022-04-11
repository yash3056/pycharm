def isEmpty(s):
    if s==[]:
        return True
    else:
        return False

def push(s,x):
    s.append(x)
    Top=len(s) - 1

def pop(s):
    if isEmpty(s):
        return "Underflow"
    else:
        x=s.pop()
        if len(s)==0:
            Top=None
        else:
            Top=len(s) - 1
            return x

def show(s):
    if isEmpty(s):
        print("Stack is Empty")
    else:
        Top=len(s)
        for i in range(Top-1,-1,-1):
            print(s[i])

#----------main----------
stk=[]
Top=None
a="y"
while a=="y":
    print("1. Push")
    print("2. Pop")
    print("3. Show")
    print("4. Exit")
    choice=int(input("Enter your choice :"))
    if choice==1:
        x=int(input("Enter the number :"))
        push(stk,x)
    elif choice==2:
        x=pop(stk)
        if x=="Underflow":
            print("Stack is Empty")
        else:
            print("Popped element is :",x)
    elif choice==3:
        print("-----Stack-----",)
        show(stk)
    elif choice==4:
        break
    else:
        print("Wrong input")