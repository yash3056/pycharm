n=int(input('enter n'))
f=1
x=0
for i in range(1,n+1):
    f=f*i
    a=1/f
    x=x+a
    print(float(x))