#!/usr/bin/env python3
# Created by: Lia Duggan
# Created on: Nov. 8th, 2022
# This program generates a random number
# and has the user guess a number
# until they guess the correct number


def main():

    # Generating the random number
    import random

    random_number = random.randint(0, 9)
    print(random_number)

    while True:
        # Having the user guess a number
        user_guess_as_string = input("Guess a number between 0 and 9: ")

        try:
            user_guess = int(user_guess_as_string)
        # If the user inputs an invalid number
        except ValueError:
            print(user_guess_as_string, "is not an number from 0 - 9")

        else:
            if user_guess < 0 or user_guess > 9:
                print("please input a number between 0 and 9")
            elif user_guess == random_number:
                print("You guessed correctly!")
                break
            else:
                print("incorrect, try again")

    print("Thanks for playing!")


if __name__ == "__main__":
    main()
