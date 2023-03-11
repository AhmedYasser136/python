last = open(r"D:\ITI\py\lab_2\file2.txt").read()

path = "D:\ITI\py\lab_2\file2.txt"

data = open(r"D:\ITI\py\lab_2\file.txt" , 'r').read()

data = data.replace("\n" , '')

print(last)
print (data)