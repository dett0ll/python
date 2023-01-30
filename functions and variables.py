########################input###############################
#print("hello world")
#name = input("enter your name")
#print (name)
#num = int(input("enter any number"))
#print(num1)

#####################format string##########################
#formatstring
#name = input("enter name")
#print(f"Hello, {name}")

#######################escape characters###################
#escape characters
#print("hello, \"world\"")

######################strng methods########################
#string methods (methods are built in function)
# remove whitepsaces. 
#name = name.strip()
#name = name.Capitalize()
# capitalize first letter of each word
#name = name.title()
#name = name.strip().title()
#name = input (what is your name”).strip().capitalize()
#name.split(“ ”)
#split removes from left and right but not in the middle

######################int and float###########################
#print(round(x+y)) -  if we don’t need output as float but as integer
#print(round(x+y), 2) -  if the float value is big and we need to round off to two decimal places
#round(number[, ndigits]) — the one in square brackets is optional

#if we want to use commas for the big numbers
#a = 99999999999
#b = 999999999999
#c = a+b
#print(f"{c:,}")
#1,099,999,999,998

#if we want float upto two decimal points
#a = float(2.5335353)
#b = float(2.456666)
#c = a+b
#print(f"{c:.2f}")
#4.99

#####################function###########################
#def hello(to):
#    print("hello", to)

#name = input("enter name")
#hello(name)
#if we have a default parameter
#def hello(to="abc"):
#main() is the part of program which will run first. However we need to take care of scope. If we use return instead of print we will not get the answer because it will not print that

def main():
    name = input("what is your name")
    hello(name)

def hello(to):
    print("hello",to )

main() 

