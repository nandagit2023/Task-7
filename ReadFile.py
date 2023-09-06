
#created a text file and wrote a line in it
file = open("sample.txt", "w")
content = ["Hello Guvi! I have created a file and this is the content inside it"]
file.writelines(content)
file.close()

#function to read the created file and print the content of file in console
def read_content():
    f = open("/Users/nandakumargk/PycharmProjects/pythonProject/sample.txt" , "r")
    print(f.read())
    f.close()


print(read_content())
