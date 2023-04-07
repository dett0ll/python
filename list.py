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
