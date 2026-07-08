import random

while True :
    Choice = input(" Roll the dice ? (y/n):").lower()
    if Choice == "y":
      dice1 = random.randint(1,6)
      dice2 = random.randint(1,6)
    # print("you rolled a , dice and the number is : ")
      print(f"({dice1} , {dice2})")
    elif Choice == "n" :
     print("Thanks for playing!")
    break 
else:
    print("invalid input" )



