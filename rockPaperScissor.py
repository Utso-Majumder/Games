from random import *
from string import *

moves = ["ROCK","PAPER","SCISSORS"]
val = [1,2,3]

def rpsFunc(pTurn):
    v = choice(moves)
    pTurn = pTurn.upper()
    if pTurn != "ROCK" and pTurn != "SCISSORS" and pTurn != "PAPER":
        print("***Invalid Input!! Please retry***")
        return
    print("Computer chooses : ", end="")
    print(v)
    d = dict(zip(moves,val))
    if v==pTurn:
        print("Both play same move. Tied.")
        return

    if v=="ROCK" and pTurn=="SCISSORS":
        print("Computer wins !")
    elif pTurn=="ROCK" and v=="SCISSORS":
        print("Player wins !")
    else:
        if d.get(v) > d.get(pTurn):
            print("Computer wins !")
        elif d.get(v) < d.get(pTurn):
            print("Player wins !")

pT = input("Your turn, player. Choose from Rock, Paper, Scissors: ")
n=2
for i in range(n):
    rpsFunc(pT)
    r = input("Continue? (Y/N):")
    r = r.upper()
    if r=="Y":
        n+=1
        pT = input("Your turn, player. Choose from Rock, Paper, Scissors: ")
    else:
        break