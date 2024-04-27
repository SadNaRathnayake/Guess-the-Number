import random

while True:
    try:
        start = int(input("Enter the start: "))
        end = int(input("Enter the end: "))

        # Check if both start and end are integers
        if isinstance(start, int) and isinstance(end, int):
            if start >= end:
                print("End must be greater than start.")
            else:
                break
        else:
            print("Both start and end must be integers.")
    except ValueError:
        print("Both start and end must be integers.")

ran_number = random.randint(start, end)

while True:
    try:
        user_integer = int(input("Enter your guess: "))
        if user_integer < ran_number:
            print("Too low")
        elif user_integer > ran_number:
            print("Too high")
        else:
            print("You're correct!")
            break
    except ValueError:
        print("Please enter a valid integer.")
