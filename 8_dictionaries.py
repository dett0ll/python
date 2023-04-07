#A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.
veg = {'v1':'tomato', 'v2':'potato', 'v3':'onion', 'v4':'garlic'}
print (veg)
print(len(veg))
print(veg['v1'])
print(veg['v4'])
veg['v5'] = 'Raddish'  #adding value to dict
print(veg)

veg['v1'] = 'lime' # change the value of key v1
print(veg)
print('v1' in veg) # True because v1 key is present
veg.pop('v1') #it will remove key1 and its value
print(veg)
veg.popitem() # it removes last key value pair
print(veg)
del veg['v2'] # deletes the key 2 and its value
print(veg)
#changing dictionary to list
print(veg.items())
del veg # it will delete the dictionary
veg = {'v1':'tomato', 'v2':'potato', 'v3':'onion', 'v4':'garlic'}
#if we want to make copy of veg dictionary so that original remain same
veg_cpy = veg.copy()
print(veg_cpy)

#getting dict keys as list
print(veg.keys())

#in order to get the values of dictionary as list
print(veg.values())

##output
#{'v1': 'tomato', 'v2': 'potato', 'v3': 'onion', 'v4': 'garlic'}
#4
#tomato
#garlic
#{'v1': 'tomato', 'v2': 'potato', 'v3': 'onion', 'v4': 'garlic', 'v5': 'Raddish'}
#{'v1': 'lime', 'v2': 'potato', 'v3': 'onion', 'v4': 'garlic', 'v5': 'Raddish'}
#True
#{'v2': 'potato', 'v3': 'onion', 'v4': 'garlic', 'v5': 'Raddish'}
#{'v2': 'potato', 'v3': 'onion', 'v4': 'garlic'}
#{'v3': 'onion', 'v4': 'garlic'}
#dict_items([('v3', 'onion'), ('v4', 'garlic')])
#{'v1': 'tomato', 'v2': 'potato', 'v3': 'onion', 'v4': 'garlic'}
#dict_keys(['v1', 'v2', 'v3', 'v4'])
#dict_values(['tomato', 'potato', 'onion', 'garlic'])
