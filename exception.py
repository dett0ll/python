########################ValueError#####################################
#try:
#  x = int (input('Enter the value of x'))
#  print(f'x is {x}')

#except ValueError:
#  print(' x shold be an integer')


################################Nameerror##################################

#try: 
#    x = int(input('enter x'))
    
#except ValueError:
 #   print('x should be an integer')

#print(f'x is {x}')

#else:
 #   print(f'x is {x}')

# if we normally enter the value of x as 2, we get the output x is 2
#but if enter the value of x as cat, we do not get the value but the name error
#NameError: name 'x' is not defined
#it is because the error is in the int(input('enter x')) itself and its values is not
#passed to LHS i.e, x and hence the error.
#using else above will solve the name error. instead of name error , we will get value error
#else will only print if try block was a success. but in this case, try block was a fail and hence
# it will throw exeption

#basically in the above code, if we do not want to get name error we are using else. else will only execute if try is true

################using break and while#############################
# now, in th above code what happens is that if the user enters incorrect value it will give value error an stop code execution
#but we want use to answer correclty and code should not stop until user answers correctly

#while True:
#    try:
#        x = int(input('enter value of x'))
#    except ValueError:
#        print('x should be an integer')
#    else:
 #       break

#print(f'x is {x}')


##########we can use above wth the function################################## 
#def main():
  #  x = get_int()
  #  print(f'x is {x}')

#def get_int():
  #  while True:
   #     try:
   #         x = int(input('Enter a number'))
   #     except ValueError:
   #         print('x should be an integer')
   #     else:
   #         break
        #we can use return x instead of break. It will not only return value of x but also break out of loop
   # return x

#main()

# instead of usig print statement in the except we can simply use pass. It will repeat qestion untill correct answer is given
# now we cane use prompt also.
def main():
    x = get_int("Enter value of x")
    print(f'x is {x}')

def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
        except ValueError:
            pass
        else:
            break
        #we can use return x instead of break. It will not only return value of x but also break out of loop
    return x

main()
