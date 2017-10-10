magic_number = 37

guess_is_wrong = True
while guess_is_wrong:
	guess = input("Guess a number between 0 and 100")
	guess = int(guess)
	if guess == magic_number:
		guess_is_wrong = False
		print("You did it!")
	else:
		guess_is_wrong = True
		print("Sorry")
	

range = (1, 2, 3, 4, 5, 6)
x = range
for i in x:
	print ("*****")

