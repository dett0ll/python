a = open("test.txt","rt")
s = (a.read(1)).lower()
count = {}
while s :
    for al in s:
        if al in count:
            count[al] += 1
        else:
            count[al] = 1
    s = (a.read(1)).lower()
print(count)
for letters in count.keys():
    c = count[letters]
    if c > 0:
        print(letters, "->", c)
