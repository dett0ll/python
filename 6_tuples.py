#Collection of different data types which is ordered and cannot be changed
veg = ('peas', 'beans', 'raddish', 'tomato')
print(veg)
print(len(veg))
print(veg[0])
print(veg[3])
print(veg[-1])
print(veg[-4])

#slicing
print(veg[0:4])
print(veg[1:3])
print(veg[0:])
print(veg[1:])
print(veg[-4:])
print(veg[-3:-1])

#changing tuples to list
veg = list(veg)
print(veg)

veg = ('peas', 'beans', 'raddish', 'tomato')
print('peas' in veg) #case sensitive - True
num = (1,2,3,4)
vegnum = veg+num #joining tuples
print(vegnum)
del num #deleting tuples
del veg

#output
#('peas', 'beans', 'raddish', 'tomato')
#4
#peas
#tomato
#tomato
#peas
#('peas', 'beans', 'raddish', 'tomato')
#('beans', 'raddish')
#('peas', 'beans', 'raddish', 'tomato')
#('beans', 'raddish', 'tomato')
#('peas', 'beans', 'raddish', 'tomato')
#('beans', 'raddish')
#['peas', 'beans', 'raddish', 'tomato']
#True
#('peas', 'beans', 'raddish', 'tomato', 1, 2, 3, 4)
