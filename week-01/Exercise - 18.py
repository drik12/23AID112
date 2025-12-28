secret_number = 7
guess = None
while guess != secret_number:
    guess = int(input("Guess the secret number (between 1 and 10): "))
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Congratulations! You've guessed the secret number.")