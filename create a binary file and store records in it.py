size=20
with open("names.dat","wb") as f:
    ans='y'
    while ans.lower()=='y':
        name=input("ENTER NAME: ")
        l=len(name)
        name = name + (size-l)*""
        name=name.encode()
        f.write(name)
        ans=input("ADD MORE? (y/n)")