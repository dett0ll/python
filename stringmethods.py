s = "terminator"
a = "jOhnCena"
c = "john12"
d = "A@ple"
e = "123"
print(s.capitalize()) # Terminator
print(a.capitalize()) #Johncena
print(s.endswith("or")) #True
print(s.endswith("yo")) #False
print(s.find("e")) #it prints e which is s[1]
print(s.find("t")) #it prints t which is s[0]
print(s.find("t",2)) #it prints t which is s[7] because it starts from [s[1]
print(s.isalnum()) # True because only alphabet
print(c.isalnum()) #True because alphabet and number
print(d.isalnum()) #False because @ is not alphabet or number
print(c.isalpha()) # False because 12 is num
print(e.isdigit()) #True because e has only digits
f ="TERMINATOR"
print(f.islower()) #false
print(s.islower()) #True
g = "terminator is back"
print(g.isspace()) #False
h = " "
print(h.isspace()) #True
print(f.isupper()) #True
print(s.join("ar")) #aterminatorr
print(','.join(['a','b','c'])) #a,b,c
i="COCACOLA"
print(i.lower())#cocacola
print(g.replace("terminator", "t3")) #t3 is back
j ="are are are"
print(j.replace("are","is",2)) #is is are
print(j.split()) #['are'.'are','are']
print(i.startswith('COCA')) #True
print(a.swapcase()) #JoHNcENA
print(i.title()) #Cocacola
print(s.upper()) #TERMINATOR
