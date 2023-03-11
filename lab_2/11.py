test_list = ['ahmed','yasser','hazem']
cheak = 'a'
res = [idx for idx in test_list if idx.lower().startswith(cheak.lower())]
print(str(res))