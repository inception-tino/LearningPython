import os

#os.mkdir("folder1")

#checkpath = os.path.exists("folder1")
#print(checkpath)

#os.rmdir("folder1")

#os.mkdir("foldernew")

#os.mkdir("foldernew/myfolder")

#pathname= r"C:\Users\natur\PycharmProjects\pythonProject\foldernew\myfolder\newfolder1"
#os.mkdir(pathname)

for file_name in os.listdir("."):
    print(file_name)

print("_________________________________________________________________")