#file operations

myfile = open("data.txt")
content = myfile.read()
myfile.close()


#better way to write the same code:

with open("data.txt") as myfile:
    content = myfile.read()

print(content)


#write to the file:

with open("data.txt", "a+") as myfile:
    myfile.write("\nmango")
    myfile.seek(0)
    content = myfile.read()

print(content)


