with open(r"D:\ITI\py\lab_2\file.txt", "r") as myfile:
    mydata = myfile.read()
revdata = mydata[::-1]
print(revdata)



# # replace with the directory path you want to list files from
# # replace with the directory path you want to list files from for filename in os.listdir(directory):

# import os
# # directory = 'lab_2'

# # for filename in os.listdir(directory):
# #     if os.path.isfile(os.path.join(directory, filename)):
# #         if filename == "file.txt":
# #             with open( "file.txt", "r") as myfile:

# #                 mydata=myfile.read()
# #                 revdata=mydata[::-1]
# #                 print(revdata)

# file_path = 'file.txt'
# full_path = os.path.abspath(file_path)
# print(full_path)

# X = r"D:\ITI\py\lab_2\file.txt"

# # with open("amit.txt", "r") as myfile:


# with open(X, "r") as myfile:
#     mydata = myfile.read()

# revdata = mydata[::-1]

# print(revdata)
