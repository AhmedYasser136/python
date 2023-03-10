word = input("enter word ")
res = max(word, key=lambda x: word.count(x))
print("the most is ", res)