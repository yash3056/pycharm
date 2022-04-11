stack = []


def push(stack, ele):
    stack.append(ele)
    print(stack)


def pop(stack):
    print(stack.pop())


def peek(stack):
    print(stack[-1])


def display(stack):
    a = stack[::-1]
    print(a)

stk = []
while True:
    print("1 push")
    print("2. pop")
    print("3. peek")
    print("4.display")
    print("5 exit")
    ch = int(input("entre choice"))

    if ch == 1:
        ele = int(input("ele"))
        push(stk, ele)
    if ch == 2:
        pop(stk)

    if ch == 3:
        peek(stk)
    if ch == 4:
        display(stk)


    elif ch == 5:
        break