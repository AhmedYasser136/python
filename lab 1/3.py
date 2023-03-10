# create list
list = []

# ask user
num = int(input("int num of element : "))

# find the maximum
for i in range(1, num + 1):
    ele = int(input("enter number : "))
    list.append(ele)

# print max
print("max is : ", max(list))
