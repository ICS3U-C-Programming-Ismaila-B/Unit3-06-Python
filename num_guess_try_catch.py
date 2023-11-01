import random

# Generate a random number between 0 and 9
correct_number = random.randint(0, 9)
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    try:
        # Ask the user to guess the number
        user_guess = int(input("Guess the number between 0 and 9: "))

        if user_guess == correct_number:
            print("Congratulations! You guessed correctly.")
            break
        else:
            print("Sorry, that's not the correct number.")
            attempts += 1
    except ValueError:
        print("Your input is not an integer. Try again.")

if attempts == max_attempts:
    print(
        "Sorry, you're out of tries. The secret number was {}.".format(correct_number)
    )

if attempts < max_attempts:
    print("End of the game. Thanks for playing!")
