# 초기화 방법
thisdict = {}   # empty initial
thisdict = dict() #empty initial
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

dict_format = "key : {1}, value : {0}"
for key, value in thisdict.items():
    print(dict_format.format(value, key))
    pass
pass 

# add item in dict

# remove item in dict