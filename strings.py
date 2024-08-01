a ='a'
print(ord(a))
#output is ASCII value = 97
print(chr(97))
#output will be a
s = 'terminator'
for i in range(len(s)):
    print(s[i],end="")
#output will print terminator
s = 'terminator'
for i in range(len(s)):
    print("a",end="")
#output will be "a" of the length terminator

s = "terminator"
print(s[1:3]) #start from s[1] till s[3] but do not include s[3]
print(s[3:])#start from s[3] onwards including s[3]
print(s[:3])#Do not include s[3] print values before s[3]
print(s[3:-2])#start with s[3] and end at s[-2] which is second from reverse but do not include s[-2]
print(s[-3:4]) # no output
print(s[::2])#start with s[0] skip one place and move to s[2] then s[4]
print(s[1::2])#start with s[1] and skip one place and move to s[3] then s[5]
print(s[-2])#print second digit from reverse
#er
#minator
#ter
#minat

#triao
#emntr
#o

s = "terminator"
print("e" in s) # True
print("y" in s) # False
print("y" not in s) # True

#it does not support delete, append and insert

s = "terminator"
print(s+"s") # output is terminators

s = "terminator"
print(min(s)) # output will be a

s = "terminatorA"
print(min(s)) # output will be A because as per ASCII A is lower place than a

s = "terminator"
print(max(s)) # output will be t

s = "terminator"
print(s.index("t")) # output is 0 as it only shows the first place of t

s = "terminator"
print(list(s))
#it will change string to list ['t', 'e', 'r', 'm', 'i', 'n', 'a', 't', 'o', 'r']

s = "terminator"
print(s.count("t")) # output is 2. it counts the number of time t is present


