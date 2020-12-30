from turtle import *
from random import randint, random
from time import sleep

start = 0
sliderH, sliderW = 80,20

totalX, totalY = 600, 550
ballX, ballY = 0.0, 0.0
collision = 0

dX = random() + 1
dY = random() + 1

screen = Screen()
screen.setup(totalX + 70, totalY + 70)
screen.screensize(totalX, totalY)
screen.title('Ping Pong Game')
print('Screeen size: ', screen.screensize())
screen.bgcolor('brown')

t0 = Turtle()
t0.hideturtle()
t0.color('white')
t0.speed(10)
t0.penup()
t0.goto(0, totalY // 2 + 10)
t0.write('PRESS "m" to start, "e" - to start again.', True, align='left')
t0.penup()
t0.goto(-totalX // 2, -totalY // 2)
t0.pendown()
t0.goto(-totalX // 2, totalY // 2)
t0.goto(totalX // 2, totalY // 2)
t0.goto(totalX // 2, -totalY // 2)
t0.goto(-totalX // 2, -totalY // 2)
t0.penup()

t1 = Turtle()
t1.hideturtle()
screen.register_shape('line', ((-sliderW // 3, -sliderH // 3), (-sliderW // 3, sliderH // 3), (sliderW // 3, sliderH // 3), (sliderW // 3, -sliderH // 3)))
t1.shape('line')
t1.speed(5)
t1.color('yellow')
t1.setheading(90)
t1.penup()
t1.goto(-totalX // 2 + 10, 0)
t1.showturtle()

def go_up():
	t1.fd(15)

def go_down():
	t1.bk(15)

def start_game():
	global start
	start = 1

def stop_game():
	global start
	start = 0

screen.onkey(go_up, 'w')
screen.onkey(go_down, 's')
screen.onkey(start_game, 'm')
screen.onkey(stop_game, 'e')

t2 = Turtle()
t2.shape('circle'); t2.speed(5)
t2.color('pink')
t2.penup(); t2.goto(ballX, ballY); t2.setheading(70)

t3 = Turtle()
t3.shape('triangle'); t3.speed(25)
t3.color('blue')
t3.penup(); t3.goto(ballX, ballY); t3.setheading(50)

def move_t2():
	global sliderH, sliderW
	global totalX, totalY
	global ballX, ballY
	global dX, dY
	global collision
	global start

	t2.goto(ballX, ballY)

	sliderX, sliderY = t1.pos()

	if ballY >= (sliderY - sliderH // 2) and ballY <= (sliderY + sliderH // 2) and ballX <= -totalX // 2 + sliderW + 10:
		if collision == 0:
			dX = -dX
			collision = 1
	if ballY <= (sliderY - sliderH // 2) or ballY >= (sliderY + sliderH // 2):
		if ballX <= -totalX // 2 + sliderW + 10 - 5:
			start = 0

	if ballX >= -totalX // 2 + sliderW + 10:
		collision = 0
	if ballX > totalX // 2 - 10:
		dX = -dX
	if ballY > totalY // 2 - 10:
		dY = -dY
	if ballY < -totalY // 2 + 10:
		dY =-dY

	if start == 1:
		ballX += dX
		ballY += dY
	else:
		ballX = 0
		ballY = 0

	screen.ontimer(move_t2, 1)

def move_t3():
	global sliderH, sliderW
	global totalX, totalY
	global ballX, ballY
	global dX, dY
	global collision
	global start

	t3.goto(ballY, ballX)

	sliderX, sliderY = t1.pos()

	if ballY >= (sliderY - sliderH // 2) and ballY <= (sliderY + sliderH // 2) and ballX <= -totalX // 2 + sliderW + 10:
		if collision == 0:
			dX = -dX
			collision = 1
	if ballY <= (sliderY - sliderH // 2) or ballY >= (sliderY + sliderH // 2):
		if ballX <= -totalX // 2 + sliderW + 10 - 5:
			start = 0

	if ballX >= -totalX // 2 + sliderW + 10:
		collision = 0
	if ballX > totalX // 2 - 10:
		dX = -dX
	if ballY > totalY // 2 - 10:
		dY = -dY
	if ballY < -totalY // 2 + 10:
		dY =-dY

	if start == 1:
		ballX += dX
		ballY += dY
	else:
		ballX = 0
		ballY = 0

	screen.ontimer(move_t3, 1)

move_t2()
move_t3()
screen.listen()
screen.mainloop()