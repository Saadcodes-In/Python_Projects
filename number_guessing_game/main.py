import random
# Choosing random number between 1 to 100 using random module
number_to_guess = random.randint(1, 100)

user_number_guess = 0
# Guess counter
guesses = 0
while (user_number_guess != number_to_guess):
    try:
        user_number_guess = int(input("Guess a number:"))
        if (user_number_guess > number_to_guess):
            print("Lower number please")
        elif (user_number_guess < number_to_guess):
            print("Higher number please")
        guesses += 1
    except ValueError:
        print("Please enter a valid input")
        continue


print(f"You have guessed the number {number_to_guess} in {guesses} guesses")
