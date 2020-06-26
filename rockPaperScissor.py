from random import *
from string import *

moves = ["ROCK","PAPER","SCISSORS"]
val = [1,2,3]

def rpsFunc(pTurn,s1,s2):
    v = choice(moves)
    pTurn = pTurn.upper()
    if pTurn != "ROCK" and pTurn != "SCISSORS" and pTurn != "PAPER":
        print("***Invalid Input!! Please retry***")
        return s1,s2
    print("Computer chooses : ", end="")
    print(v)
    d = dict(zip(moves,val))
    if v==pTurn:
        print("Both play same move. Tied.")
        return s1,s2

    if v=="ROCK" and pTurn=="SCISSORS":
        print("Computer wins !")
        s2+=1
        return s1,s2
    elif pTurn=="ROCK" and v=="SCISSORS":
        print("Player wins !")
        s1+=1
        return s1,s2
    else:
        if d.get(v) > d.get(pTurn):
            print("Computer wins !")
            s2+=1
            return s1,s2
        elif d.get(v) < d.get(pTurn):
            print("Player wins !")
            s1+=1
            return s1,s2

pT = input("Your turn, player. Choose from Rock, Paper, Scissors: ")
sComp=0
sPlayer=0
n=1
while n>0:
    sPlayer, sComp = rpsFunc(pT, sPlayer, sComp)
    print("Computer "+str(sComp)+" : "+str(sPlayer)+" Player ")
    r = input("Continue? (Y/N):")
    r = r.upper()
    if r=="Y":
        n+=1
        pT = input("Your turn, player. Choose from Rock, Paper, Scissors: ")
    else:
        break
