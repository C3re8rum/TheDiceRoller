import random
rolls = 0

while True:
    Total = 0
    DieType = int(input("How many sides do you want your die to have(6 for d6 20 for d20 etc)?"))
    Dice = int(input("How many dies do you want to roll?"))
    print(f"{Dice}D{DieType}")
    
    x = 0

    while x != Dice:
        x = x + 1

        ActualDie = random.randint(1,DieType)

        Total = Total + ActualDie

    print(Total)

    continues = str(input("Do you want to continue?(Yes/No)"))

    if continues == "No":
        break
