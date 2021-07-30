msg="Welcome!"
f = open('myfile.bin','wb')
f.write(msg.encode())
f.write(b' To Python Learning')
f.close()