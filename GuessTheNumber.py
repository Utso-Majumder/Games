from random import *

n = int(input("Enter a maximum range : "))
m = int(input("Enter a minimum range : "))
v = randint(m,n)
h = int(input("Guess the number : "))
if h==v:
    print("You've guessed correctly!")
else:
    print("You've guessed wrongly!")