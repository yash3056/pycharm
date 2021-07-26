def file_handle():
    f = open("notes3.text", "w")
    f.write("this is my first program on file handling")
    print("file created")
    f.close()
    f.open("notes3.text", "r")
    f.read()
    f.close()
file_handle()