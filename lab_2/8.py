with open(r"D:\ITI\py\lab_2\file.txt" , 'r') as firstfile, open(r"D:\ITI\py\lab_2\file3.txt" , 'w') as secondfile:
    for line in firstfile:
        secondfile.write(line)

# a > add
# w > remove and add
