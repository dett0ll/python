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

veg = {'peas', 'beans', 'raddish', 'tomato', 1}
num = {1,2,3,4, 'beans'}
vegnum = veg.union(num) #this method returns a new set
print(vegnum)

veg.update(num) #insert set(num) to another set(veg)
print(veg)

a = {1,2,3,4}
b = {3,4,5}
print(a.intersection(b)) #items that are common in both sets

c= {1,2,3,4,5,6,7,8}
d={5,6,7}
print(d.issubset(c))
print(c.issuperset(d))
print(c.difference(d))
print(d.symmetric_difference(c))
print(d.isdisjoint(c)) #it will give false because they havse some common elements

#output
#{1, 2, 'raddish', 3, 4, 'tomato', 'beans', 'peas'}
#{1, 2, 'raddish', 3, 4, 'tomato', 'beans', 'peas'}
#{3, 4}
#True
#True
#{1, 2, 3, 4, 8}
#{1, 2, 3, 4, 8}
#False
#
