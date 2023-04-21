# two conditions
a = 3
if a>0:
    print('a is positive number')
else:
    print('a is not positive number')
#multiple conditions
#we need to give condition to elif also. Only else executes with default condition
a = 0
if a>0:
    print('a is positive number')
elif a<0:
    print('a is not positive number')
else:
    print('a is zero')
    
#nested conditions
a = 4
if a>0:
    if (a%2==0):
        print('a is positiven number and even')
    else:
        print('a is positive number')
elif a<0:
    print('a is negative number')
else:
    print('a is equal to zero')
