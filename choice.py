from random import randint

for i in range(10):
    print(randint(1, 10), end=',')

##################################################
from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(my_list))
# the above code will choose any random number from the list
from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(sample(my_list, 5))

#sample has two values sequence and elemnets to choose. Now sequence here is the list and it chooses any 5 random values
