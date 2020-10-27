num = int(input("Enter a Number: "))
for i in range(2,num):
    if num%i==0:
       print (num,"it is not a prime number")
       break;
else:
    print(num,"it is a prime number")