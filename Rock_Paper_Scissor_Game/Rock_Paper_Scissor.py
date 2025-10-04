'''
0 for Rock
1 for Paper
2 for Scissors'''

import random


def main():
    computer, user = Choices()

    print(Results(computer, user))


def Choices():
    # r is for rock, p is for paper, s is for scisoors
    your_Choice = input("Rock paper scissors (r,p,s): ")
    # Computers choice
    computer = random.choice([0,1,2])
    # Validationg input
    if your_Choice not in ['r', 'p', 's']:
        print("Invalid Choice")
    else:
        # Converting input into number
        dict_Values = {
            'r': 0, 'p': 1, 's': 2,}
        
        # Converitng number into value
        dic_p = {0: 'Rock 🪨', 1: 'Paper 📄',
                 2: 'Scissors ✂️'}

        you = dict_Values[your_Choice]
        computer_choice = dic_p[computer]
        


        choice = print(
            f"\t\tyou chose {dic_p[you]},\n\t\t computer chose {computer_choice}")
        return dict_Values[your_Choice] , computer


def Results(you,computer):
    if (computer == you):
        return "it's a draw!"
    if computer == 0 and you == 1 or computer == 1 and you == 2 or computer == 2 and you ==0:
        return "You Won"
    else:
        return "You L0se"

    
main()
