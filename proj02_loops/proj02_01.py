# Name: Elizabeth
# Date: 7/10/18

# proj02: sum

# Write a program that prompts the user to enter numbers, one per line,
# ending with a line containing 0, and keep a running sum of the numbers.
# Only print out the sum after all the numbers are entered
# (at least in your final version). Each time you read in a number,
# you can immediately use it for your sum,
# and then be done with the number just entered.

#Example:
# Enter a number to sum, or 0 to indicate you are finished: 4
# Enter a number to sum, or 0 to indicate you are finished: 5
# Enter a number to sum, or 0 to indicate you are finished: 2
# Enter a number to sum, or 0 to indicate you are finished: 10
# Enter a number to sum, or 0 to indicate you are finished: 0
#The sum of your numbers is: 21

#define variable
current_sum = 0

#loop
while True:
    current_number = int(raw_input("Enter a number to sum, or 0 to indicate that you are finished: "))
    current_sum = current_sum + current_number
    if current_number == 0:
        print "The sum of your numbers is:", current_sum
        break


