def armstrong_check(n):
    orig = n
    sum=0
    while n>0:
        sum = sum+(n%10)*(n%10)*(n%10)
        n=n//10
    if orig==sum:
        print("YES IT IS ARMSTRONG NO.")
    else:
        print("NOT ARMSTRONG NO.")

n=int(input("ENTER NO. TO CHECK:"))
armstrong_check(n)