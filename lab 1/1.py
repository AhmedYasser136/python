word = input("Enter word: ")


def reverse(str):
    str = str[::-1]
    return str


print("The original string  is : ", word)
print("The reversed string  is : ", reverse(word))
