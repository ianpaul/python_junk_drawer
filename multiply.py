# I wrote this to help my kids learn their times tables.

import random

#generate a random number
def random_number(): 
	multi = random.randint(1,10)
	return multi

# create a math problem using two random numbers and ask the user to solve it.
def get_answer():
	turn = 0
	correct = 0
	while turn < 10:
		number1 = random_number()
		number2 = random_number()
		question = int(input("What is " + str(number1) + "x" + str(number2) + "?"))
		if question == number1*number2:
			print ("Great work you got it!")
			turn += 1 
			correct += 1
		elif question != number1*number2:
			print("Sorry, that wasn't it. The answer was " + str(number1*number2) + ". Try another one!")
			turn += 1
	print("\nThat was fun! You got " + str(correct) + " out of 10! Let's play again soon!")

get_answer()







