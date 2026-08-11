import random
while True:
    dice=input("Roll the dice ? (y/n):")
    if dice.lower()=="y":
        dice1=random.randint(1,6)
        dice2=random.randint(1,6)
        print(f"{dice1},{dice2}")
    elif dice.lower()=="n":
        print("Thanks for playing !")
        break
    else:
       print("Invalid choice!")

