num = int(input("Enter a number"))
a=1
if num < 0:
    print("enter a positie number" )
else:
    sum =  0
    while(num > 0):
        sum +=num
        num -= 1
    print("the sum is ",sum)
