import random

def generate_number():
    return random.randint(1, 20)

def game_rutine(secret_number):
    number_of_attempts = 0
    while True:
        guess = input("Your guess: ")
        if guess == 's':
            print(f"The secret number is: {secret_number}")
        elif guess == 'x':
            print("Game over!")
            return 'x'
        elif guess == 'n':
            print("restarting the game")
            return 'n'
        try:
            guess = int(guess)
            number_of_attempts += 1
            if guess == secret_number:
                print(f"Correct! Number of guesses: {number_of_attempts}.")
                return 'x'
            elif guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        except ValueError:
            print("use number or 's' for cheating or 'x' to exit, or 'n' restart the game.")

def main():
    while True:
        secret_number = generate_number()
        result = game_rutine(secret_number)
        if result == 'x':
            break
        elif result == 'n':
            continue

main()
