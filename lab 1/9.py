start = int(input("inter start : "))
end = int(input("inter end : "))
for num in range(start, end + 1):
    if num % 2 == 0:
        print(num, end=" ")
