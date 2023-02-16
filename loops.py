#i=3
#while(i!=0):
#    print("hello")
#    i -= 1

#while True: #default infinite loop. We will ask question to break from this loop
    #n =int(input("enter a number"))
   # #if n < 0:
     ##   continue
    ##else:
    # #   break
   # # or we can directly use break

    #if n > 0 :
      #  break

#for _ in range(n):
   # print("hello")
########################################################################################
#def main():
 #   number = get_num()
  #  hello(number)


#def get_num():
 #   while True:
  #      n = int(input("Enter number"))
   #     if n > 0:
    #        break
    #return n  # we need to return n either inside the function or in the while loop but we have to return it

#def hello(number):
 #   for _ in range(number):
  #      print("hello")

#main()

############################################################################################
#students = ['max', 'charles', 'george']
#for student in students:
 #   print(student)
#for student in range(len(students)):
 #   print(students[student])
 # #########################################################################################

#drivers = {
 # "max":"redbull",
  #"charles":"ferrari",
  #"lewis":"mercedes"
 #}

#for driver in drivers:
#  print (driver, drivers[driver], sep=":")

f1 = [
  {"driver":"max", "team":"redbull", "tm":"checo"},
  {"driver":"charles", "team":"ferrari", "tm":"sainz"},
  {"driver":"lewis", "team":"mercedes", "tm":"geroge"}
]

for drivers in f1:
  print(drivers["driver"], drivers["team"], drivers["tm"], sep=":")
