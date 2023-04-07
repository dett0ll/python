#In Python set is used to store unique items, and it is possible to find the union, intersection, difference, 
#symmetric difference, subset, super set and disjoint set among sets.
veg = {'peas', 'beans', 'raddish', 'tomato'}
print(veg)
print(len(veg))
print('peas' in veg) #True
veg.add('carrot') # add 1 item to set
print(veg)
veg2 = ('onion', 'greens')
veg.update(veg2) #if we want to add other set 
print(veg)
veg.remove('greens') 
print(veg)
veg.pop() #removes random item from set
print(veg)
veg.clear() # to clear the set

veg = {'peas', 'beans', 'raddish', 'tomato'}
del veg #to delete a set
#converting list to set
veg = ['peas', 'beans', 'raddish', 'tomato']
veg = set(veg)
print(veg)

#output
#{'beans', 'raddish', 'peas', 'tomato'}
#4
#True
#{'raddish', 'peas', 'carrot', 'beans', 'tomato'}
#{'raddish', 'peas', 'greens', 'carrot', 'beans', 'tomato', 'onion'}
#{'raddish', 'peas', 'carrot', 'beans', 'tomato', 'onion'}
#{'peas', 'carrot', 'beans', 'tomato', 'onion'}
#{'beans', 'raddish', 'peas', 'tomato'}
