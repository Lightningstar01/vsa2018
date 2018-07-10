# Name: Elizabeth Sims and Mia shines
# Date: 7/10/18

import random
""" 
proj 03: Guessing Game

Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, 
or exactly right. Keep the game going until the user types exit.
Keep track of how many guesses the user has taken, and when the game ends, print this out.

"""
# #setup and variables
# random_number = random.randint(1, 9)
# guess_number = 0
# print "I'm thinking of a number between 1 and 9. Can you guess my number?"
# max_guesses = int(raw_input("How many guesses do you want? "))
#
# #while loop
# while True:
#     if guess_number == max_guesses:
#         print "You are out of guesses! The number was " + str(random_number) + "!"
#         break
#     else:
#         user_input = raw_input("Enter a number, or 'exit' to end the game: ")
#     try:
#         int(user_input)
#         if int(user_input) < 1 or int(user_input) > 9:
#             print "That is not a number between 1 and 9!"
#         elif int(user_input) > random_number:
#             print "Your number is too high!"
#             guess_number = guess_number + 1
#         elif int(user_input) < random_number:
#             print "Your number is too low!"
#             guess_number = guess_number + 1
#         elif int(user_input) == random_number:
#             guess_number = guess_number + 1
#             print "Congratulations, you guessed my number!", "You used", guess_number, "guesses."
#             break
#     except ValueError:
#         if str(user_input) == "exit" or "Exit":
#             print "Game ended."
#             break
#         else:
#             print "That is not a valid answer!"

#define variables
second_loop = True

while True:
    random_number = random.randint(1, 9)
    guess_number = 0
    print "I'm thinking of a number between 1 and 9. Can you guess my number?"
    max_guesses = int(raw_input("How many guesses do you want? "))
    while second_loop == True:
        if guess_number == max_guesses:
            print "You are out of guesses! The number was " + str(random_number) + "!"
            break
        else:
            user_input = raw_input("Enter a number, or 'exit' to end the game: ")
        try:
            int(user_input)
            if int(user_input) < 1 or int(user_input) > 9:
                print "That is not a number between 1 and 9!"
            elif int(user_input) > random_number:
                print "Your number is too high!"
                guess_number = guess_number + 1
            elif int(user_input) < random_number:
                print "Your number is too low!"
                guess_number = guess_number + 1
            elif int(user_input) == random_number:
                guess_number = guess_number + 1
                print "Congratulations, you guessed my number!", "You used", guess_number, "guesses."
                break
        except ValueError:
            if str(user_input) == "exit" or "Exit":
                print "Game ended."
                break
            else:
                print "That is not a valid answer!"

