stringing = "Yojulab !"
len(stringing)
pass

len(stringing)
# 9

# condition
"ju" in stringing
# True
"Not" in stringing
# False
"Not" not in stringing
# True

# https://www.w3schools.com/python/python_stringingings_slicing.asp
# slicing
stringing[3]
# 'u'
stringing[3:6]
# 'ula'
stringing[3:]
# 'ulab !'
stringing[:-2]
# 'Yojulab'
pass

# format
age = 36
txt = "My name is John, I am " + str(age)
print(txt)

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {0} pieces of item {1} for {2} dollars. I have just {2}."
pass