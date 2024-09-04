from os import strerror
f = open("file.txt.txt","rt")
#print(f.read())#reads all the file content
#print(f.read(1)) # reads only the first alphabet
'''a = f.read(1)
while a != '':
    print (a,end='')
    a= f.read(1)'''
#the above code reads the alphabet one by one

#if we want to count the number of alpabets
'''a = f.read(1)
c = 0
while a != '':
    print(a, end='')
    c +=1
    a = f.read(1)
print (f"\n{c}") # this will print counter value in next line'''

#now in the above we read lines char by char. What if we want to read all the file

#print(f.read()) #this will read all the file
#now we want to count alphabets

'''a =  f.read()
count = 0
for c in a:
    count +=1
print(a) 
print (count)'''

#now we want to read content as lines
#print(f.readline(1)) #reads a single alphabet
#print(f.readline()) #reads one line

#now we will read line one by one
'''a = f.readline()
lc = 0
ac = 0
while a != '':
    lc += 1
    for char in a:
        ac += 1
    a = f.readline()
    print(a)    
print(f"\n{lc}")
print(f"\n{ac}")'''

#print(f.readlines()) # it will show newlines as well like below
#'Beautiful is better than ugly.\n', 'Explicit is better than implicit.\n',
 #'Simple is better than complex.\n', 'Complex is better than complicated.']
print(f.readlines(50))


