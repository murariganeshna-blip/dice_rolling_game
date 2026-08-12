import random

count = [0]

while True:
    dice=input("Roll the dice? (y/n):")
    if dice.lower()=="y":
        num=int(input("How many dice ?:"))
        rolls=[]
        for i in range(num):
            rolls.append(random.randint(1,6))
        count[0]+= 1
        print(rolls)
        print(f"Num of rolls: {count[0]}")

    elif dice.lower()=="n":
        print("Thanks for playing !")
        break
    else:
        print("Invalid choice!")





