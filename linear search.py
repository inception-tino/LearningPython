l = [11, 2, 33, 11, 24, 55, 11, 77]

searchKey = int(input("Enter the search key = "))
flag = 0
noOfElements = len(l)

for i in range(noOfElements):
    if l[i] == searchKey:
        flag = 1
        print("We found the key at index =", i)
        break

if flag == 0:
    print("The search key = {} not found".format(searchKey))

