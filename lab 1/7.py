word = str(input("inter word : "))
vowels = "aeiou"
for i in vowels:
    print(i, word.lower().count(i))
