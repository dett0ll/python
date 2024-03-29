#Collection of different datatypes which can be ordered and can be modified
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
print(vegetables)
print(len(vegetables))
print(vegetables[0])
print(vegetables[4])
print(vegetables[-5])
print(vegetables[-1])

#slicing
print(vegetables[0:5]) #it will start from 0 and it will print all elements before the index 5
print(vegetables[0:4])
print(vegetables[0:]) #if we want to print all items starting from index 0
print(vegetables[1:4]) # it does not include the first and last item
print(vegetables[1:])
print(vegetables[::1]) #steps. it will start from index 0 and will take 0 step
print(vegetables[::2]) # 1 step. It will start from 0 index and skip one element. It will choose alternate

#output
#['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
#5
#Tomato
#Carrot
#Tomato
#Carrot
#['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
#['Tomato', 'Potato', 'Cabbage', 'Onion']
#['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
#['Potato', 'Cabbage', 'Onion']
#['Potato', 'Cabbage', 'Onion', 'Carrot']
#['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
#['Tomato', 'Cabbage', 'Carrot']

Vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']

print('Tomato' in Vegetables) #case sensitive
Vegetables.append ('Peas') # appends item to the last of the list
print(Vegetables)

Vegetables.insert(3,'Raddish') # it will insert before the index 3
print(Vegetables)

Vegetables.remove('Raddish') #specify the item we need to remove
print(Vegetables)

Vegetables.pop() # it will remove the last item if index not specified
print(Vegetables)

Vegetables.pop(0) 
print(Vegetables)

# the difference between remove ans pop is that in remove we need to mention the item name while in pop we need to mention index

del Vegetables[0] #delete item with 0 index
print(Vegetables)

del Vegetables
print(Vegetables) # it shows undefined because the list vegtables is deleted
#output
#True
#['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot', 'Peas']
#['Tomato', 'Potato', 'Cabbage', 'Raddish', 'Onion', 'Carrot', 'Peas']
#['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot', 'Peas']
#['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
#['Potato', 'Cabbage', 'Onion', 'Carrot']
#['Cabbage', 'Onion', 'Carrot']
#Traceback (most recent call last):
#  File "<string>", line 25, in <module>
#NameError: name 'Vegetables' is not defined

vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
vegetables.clear() # it will clear the list
print(vegetables)

vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
veg = vegetables.copy() #copy the list
print(veg)
#output
#[]
#['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']

veg1 = ['tomato', 'potato']
veg2 = ['radish', 'peas']
veg = veg1 + veg2 #joins two lists
print(veg)
n1 = [0,1,2]
n2 = [3,4,5]
n1.extend(n2) #append list in a list
print(n1)

a = [1,2,3,4,5,6,1,1,3,4,5]
print(a.count(1)) #how many time 1 appears in the list
print(a.index(2)) #it return the index where 2 appears for the first time
a.reverse() #reverse the items in list
print(a)
a.sort() #sorts the list in ascending order
print(a)
a.sort(reverse=True) #sorts list in descending order
print(a)

#output
#['tomato', 'potato', 'radish', 'peas']
#[0, 1, 2, 3, 4, 5]
#3
#1
#[5, 4, 3, 1, 1, 6, 5, 4, 3, 2, 1]
#[1, 1, 1, 2, 3, 3, 4, 4, 5, 5, 6]
#[6, 5, 5, 4, 4, 3, 3, 2, 1, 1, 1]
