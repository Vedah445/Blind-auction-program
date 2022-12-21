import os
import logo as l

print("Welcome to blind aution program \n", l.logo)
volunteers = {}

def getInput():
    name = input("enter name ")
    bid = int(input("enter bid "))
    volunteers[name] = bid
    over = input("is it over? ")
    os.system('cls')
    if over == "no":
        getInput()
      
def getWinner():
    mx = 0
    key = None
    for keys in volunteers:
        if mx < volunteers[keys]:
            mx = volunteers[keys]
            key = keys
    print("winner is ", key, " with a bid of " ,  mx)
    
getInput()
getWinner()