x=int(input("Enter 1st number"))
y=int(input("Enter 2st number"))
z=int(input("Enter 3st number"))
if x>y:
    if x>z:
        l=x
    else:
        l=z
else:
    if y>z:
        l=y
    else:
        l=z
print("largest number",l)