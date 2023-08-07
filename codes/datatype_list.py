# slicing
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
type(thislist)
# <class 'list'>
len(thislist)
# 7
thislist[1:3]
# ['banana', 'cherry']
thislist[:-1]
# ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon']

# change value in list
thislist[1] = 'watermelon'
thislist[1:3] = ['cherry', 'watermelon']
thislist.sort()
thislist.sort(reverse=True)
pass