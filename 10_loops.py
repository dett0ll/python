#while
#it will kepp on printing until the condition becomes false
count = 0
while count < 5:
    print(count)
    count = count + 1
    
#Break: We use break when we like to get out of or stop the loop
count = 0
while count < 5:
    print(count)
    count = count + 1
    if (count==3):
        break
        
#Continue: With the continue statement we can skip the current iteration, and continue with the next
#it will skip 3
count = 0
while count < 5:
    if count == 3:
        continue
    print(count)
    count = count + 1
    

#for
num = [1,2,3,4,5]
for n in num:
    print(n)

name = 'John'
for s in name:
    print(s)
    
redbull = {'name':'max',
            'age':'22',
            'championship':'2'}
for key in redbull:
    print(key)
    
#range(start,end,step)
a =list(range(11))
print(a) # it will print from 0 to 11

b =list(range(2,11))
print(b) #it will satrt from 2 and end at 10

c = list(range(2, 11, 2))
print(c) #it will start fromm 2 and end at 10 but 2, 4, 6, 8, 10
