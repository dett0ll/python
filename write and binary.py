#how to write a file
'''f = open("test.txt", "wt")
a ="test file"
f.write(a)
f.close()'''

data = bytearray(10)
for i in range (len(data)):
    data[i] = 10-i
print(data)
for b in data:
    print(b)
f = open("test.bin","wb")
a = f.write(data)
f.close()
print(a)
r = open("test.bin","rb")
b = r.read()
r.close()
print(b)





