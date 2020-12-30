from tkinter import *
from tkinter import messagebox
from random import randint
ActivePlayer = 1
p1 = []
p2 = []
window = Tk()
window.title("Game")
button1 = Button(window, text = "")
button1.grid(row = 0, column = 0, sticky = "snew", ipadx = 40, ipady = 40)
button1.config(command = lambda: ButtonClick(1))
button2 = Button(window, text = "")
button2.grid(row = 0, column = 1, sticky = "snew", ipadx = 40, ipady = 40)
button2.config(command = lambda: ButtonClick(2))
button3 = Button(window, text = "")
button3.grid(row = 0, column = 2, sticky = "snew", ipadx = 40, ipady = 40)
button3.config(command = lambda: ButtonClick(3))
button4 = Button(window, text = "")
button4.grid(row = 1, column = 0, sticky = "snew", ipadx = 40, ipady = 40)
button4.config(command = lambda: ButtonClick(4))
button5 = Button(window, text = "")
button5.grid(row = 1, column = 1, sticky = "snew", ipadx = 40, ipady = 40)
button5.config(command = lambda: ButtonClick(5))
button6 = Button(window, text = "")
button6.grid(row = 1, column = 2, sticky = "snew", ipadx = 40, ipady = 40)
button6.config(command = lambda: ButtonClick(6))
button7 = Button(window, text = "")
button7.grid(row = 2, column = 0, sticky = "snew", ipadx = 40, ipady = 40)
button7.config(command = lambda: ButtonClick(7))
button8 = Button(window, text = "")
button8.grid(row = 2, column = 1, sticky = "snew", ipadx = 40, ipady = 40)
button8.config(command = lambda: ButtonClick(8))
button9 = Button(window, text = "")
button9.grid(row = 2, column = 2, sticky = "snew", ipadx = 40, ipady = 40)
button9.config(command = lambda: ButtonClick(9))
def ButtonClick(id):
	global ActivePlayer
	global p1
	global p2
	print(f"ID:{id}")
	if (ActivePlayer == 1):
		SetLayout(id, "X")
		p1.append(id)
		ActivePlayer = 2
		print(f"P1:{p1}")
	elif (ActivePlayer == 2):
		SetLayout(id, "O")
		p2.append(id)
		ActivePlayer = 1
		print(f"P2:{p2}")
		ChooseWinner()
def SetLayout(id, PlayerSymbol):
	if (id == 1):
		button1.config(text = PlayerSymbol, state = DISABLED)
	elif (id == 2):
		button2.config(text = PlayerSymbol, state = DISABLED)
	elif (id == 3):
		button3.config(text = PlayerSymbol, state = DISABLED)
	elif (id == 4):
		button4.config(text = PlayerSymbol, state = DISABLED)
	elif (id == 5):
		button5.config(text = PlayerSymbol, state = DISABLED)
	elif (id == 6):
		button6.config(text = PlayerSymbol, state = DISABLED)
	elif (id == 7):
		button7.config(text = PlayerSymbol, state = DISABLED)
	elif (id == 8):
		button8.config(text = PlayerSymbol, state = DISABLED)
	elif (id == 9):
		button9.config(text = PlayerSymbol, state = DISABLED)
def ChooseWinner():
	Winner = -1
	''' W I N N E R - 1 '''
	if ((1 in p1) and (2 in p1) and (3 in p1)):
		Winner = 1
	if ((1 in p2) and (2 in p2) and (3 in p2)):
		Winner = 2
	if ((4 in p1) and (5 in p1) and (6 in p1)):
		Winner = 1
	if ((4 in p2) and (5 in p2) and (6 in p2)):
		Winner = 2
	if ((7 in p1) and (8 in p1) and (9 in p1)):
		Winner = 1
	if ((7 in p2) and (8 in p2) and (9 in p2)):
		Winner = 2
		''' W I N N E R - 2 '''
	if ((1 in p1) and (4 in p1) and (7 in p1)):
		Winner = 1
	if ((1 in p2) and (4 in p2) and (7 in p2)):
		Winner = 2
	if ((2 in p1) and (6 in p1) and (8 in p1)):
		Winner = 1
	if ((2 in p2) and (6 in p2) and (8 in p2)):
		Winner = 2
	if ((3 in p1) and (7 in p1) and (9 in p1)):
		Winner = 1
	if ((3 in p2) and (7 in p2) and (9 in p2)):
		Winner = 2
		''' W I N N E R - 3 '''
	if ((1 in p1) and (5 in p1) and (9 in p1)):
		Winner = 1
	if ((1 in p2) and (5 in p2) and (9 in p2)):
		Winner = 2
	if ((3 in p1) and (5 in p1) and (7 in p1)):
		Winner = 1
	if ((3 in p2) and (5 in p2) and (7 in p2)):
		Winner = 2
	if Winner == 1:
		messagebox.showinfo("Winner", "Player 1 is Winner")
	elif Winner == 2:
		messagebox.showinfo("Winner", "Player 2 is Winner")
def AutoPlay():
	global p1
	global p2
	EmplyCells = []
	for i in range(9):
		if ( (i+1 in p1) or (i+1 in p2)):
			EmplyCells.append(i+1)
		RandomIndex = randint(0, len(EmplyCells)-1)
		ButtonClick(EmplyCells[RandomIndex])
window.mainloop()