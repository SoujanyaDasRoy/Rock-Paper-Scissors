import random

rps = ["r","p","s"]

comp = random.choice(rps)
name = input("Please Enter your name: ")
user = input("Choose for Rock(r)/Paper(p)/Scissors(s): ")

if user == comp:
    print("Draw")

if user == "r" and comp == "p":
    print("Paper beats Rock, Computer Wins!")
if user == "r" and comp == "s":
    print("Paper beats Rock, You Win!")
if user == "p" and comp == "r":
    print("Paper beats Rock, You Wins!")
if user == "p" and comp == "s":
    print("Paper beats Rock, Computer Wins!")

print(f"Well Played {name}!")