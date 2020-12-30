import random
from hangman_parts import parts
from time import sleep

words = ['python', 'programm', 'dictionary', 'lists', 'functions', 'game']
picker = random.choice(words)
print("The word has", len(picker), 'letters')
right = ['_'] * len(picker)
wrong = []


def update():
	for i in right:
		print(i, end = ' ')
	print()
print("The game start in minute!")

def wait():
	for i in range(5):
		print('.', end='')
	print()
wait()
update()
parts(len(wrong))

while True:
	print("======================")
	guess = input("Guess a letter: ")
	print("Let me check")
	wait()
	if guess in picker:
		index = 0
		for i in picker:
			if i == guess:
				right[index] = guess
			index += 1
		update()
	else:
		if guess not in wrong:
			wrong.append(guess)
			parts(len(wrong))
		else:
			print("You already guessed that!")
		print(wrong)
	if len(wrong) > 4:
		print("Looser! xP")
		print("I picked ", picker)
		break
	elif '_' not in right:
		print("HURAY! You win!")
		break