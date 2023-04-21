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
