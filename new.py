import random

while True:
    dice=input("Roll the dice ? (y/n):")
    if dice.lower()=="y":
        num=int(input("How many dice to be rolled?:"))
        rolls=[]
        for i in range(num):
            rolls.append(random.randint(1,6))
        print(rolls)
    elif dice.lower()=="n":
        print("Thanks for playing !")
        break
    else:
       print("Invalid choice!")

