import random

number = random.randint(1, 20)
number_of_try = 0

while True:
    try_num = int(input("Your guess: "))
    number_of_try += 1
    
    if try_num == number:
        print(f"Correct! number of guesses: {number_of_try}.")
        break
    elif try_num < number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
