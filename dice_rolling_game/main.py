import random


def main():
    Roll_Dice()


def Roll_Dice():
    # How many time rolling counter
    counter = 0
    Dice_Counter = int(input("How many times you want to roll a Dice: "))
    if Dice_Counter == 1:
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        print(f"({x},{y})")
        counter += 1
        print(f"You have rolled the dice {counter} times")
        
    elif Dice_Counter > 1:
        while Dice_Counter != counter:

            x = random.randint(1, 6)
            y = random.randint(1, 6)
            print(f"({x},{y})")
            counter += 1
        print(f"You have rolled the dice {counter} times")


main()
print("Thanks for playing")
