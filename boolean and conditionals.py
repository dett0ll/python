def main():
    x = int (input('Enter a number: '))
    if is_even(x):  #if this condition is true
        print ("Even")
    else:
        print ("Odd)")

main()
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
