mylist = [21, 25, 21, 23, 22, 20]
print(mylist)

mylist.append(31)
print(mylist)

newlist = [29, 33, 30]
mylist.extend(newlist)
print(mylist)

del mylist[0]
print(mylist)

mylist.pop(-1)
print(mylist)

index = mylist.index(31)
print(f"元素31在列表中的位置是: {index}")
