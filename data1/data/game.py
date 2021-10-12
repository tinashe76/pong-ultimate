# Pong Ultimate v1.0.2
# By @tinashe76
# Special thanks to @TokyoEdTech

# PATCH NOTES
# Fixed a minor bug that caused the ball to pass through the paddle

import turtle #The turtle module allows us to do some basic graphics
import winsound
import os
import random

winsound.PlaySound("soundtrack.wav", winsound.SND_ASYNC) # file is missing. (add any song of your choice to the current folder and name it soundtrack.wav) 
quote1 = "FOR THE LOW-END GAMERS"
quote2 = "CREATED IN ONE NIGHT"
quote3 = "By ELECTRONIC ARTS"
quote4 = "AVAILABLE IN 4K"
quote5 = "HOPE YOU HAVE ENOUGH BUG SPRAY"
quote6 = "FOR WHEN YOUR PC CANT RUN FORZA"
quote6 = "LOW END HARDWARE DETECTED"

quotes = [quote1, quote2, quote3, quote4, quote5, quote6]

print("\n\n")
print("-" * 120)
print("\t\t		-----------  ------------                ------------- ")
print("\t\t	     /   ____    / /  ______   /;  / \    / \   /    ___    /")
print("\t\t	    /   /    /  / /  /00000/  /;  /   \  /   / /   /   /   /")
print("\t\t	   /   ________/ /  /+    /  /;  /     \/   / /   /   /___/")
print("\t\t  	  /   /00000000 /  /+    /  /;  /   \      / /   /    ___  ULTIMATE EDITION ver 1.0.2      ")
print("\t\t  	 /   /;        /  /_____/  /;  /   /;\    / /    ----/   /       ")
print("\t\t 	/___/;        /___________/;  /___/;  \__/ /________    /           ")
print("\t\t 	0000          000000000000    0000    000  00000000/___/   ")
print("\t\t                                                           0000   ")
print("-" * 120)
print(f"\t\t\t\t\t {random.choice(quotes)}")
print("\n\n\n")
click = input("\n\n\n\n\n\n\t\t\t\t\t>>> Press Enter To Continue <<<")
os.system("color b && cls")

print("\t\t\t\t\t [OKAY LET'S DO THIS]")
print("\n")
print(">> PC REQUIREMENTS\n")
print("\t >> CPU:   3.5Ghz")
print("\t >> RAM:   256MB")
print("\t >> GPU: 32MB @ 250MHz (1280 x 720 display)")
print("\n\n\n NOTE: Using Low-end hardware may cause the game to glitch or statter")
click = input("\n\n\n\n\n\n\t\t\t\t\t>>> CONFIRM SETTINGS <<<")
os.system("color 6 && cls")
player_one = str(input("PLAYER ONE: "))
print("")
player_two = str(input("PLAYER TWO: "))

print("\nCHOOSE DIFFICULTY\n")
print("1. Casual     |    2. Intermediate     |    3. PONG!    |     4. PONG ULTIMATE!")
check = ""
timer = 0

while check != "okay":
	try:
		difficulty = int(input("> "))

		if 0 < difficulty < 5 :
			check += "okay"

	except ValueError:
		print("TYPE THE CORRESPONDING NUMBER!!!")

click = input("\n\n\n\n\n\n\t\t\t\t\t>>> START IMMEDIATELY <<<")

if difficulty == 1:
	window = turtle.Screen() # GUI Window
	window.title("Pong Ultimate")
	window.bgcolor("orange")
	window.setup(width=1280, height=680)
	window.tracer(10) # speeds up game (I noticed using a lower value causes lags)


	# SCORES
	score_a = 0
	score_b = 0

	# Paddle A
	paddle_a = turtle.Turtle() # It's a turtle object
	paddle_a.speed(2) # Sets speed to maximum possible value
	paddle_a.shape("square") # Square is simple to resize
	paddle_a.color("black")
	paddle_a.shapesize(stretch_wid=8, stretch_len=1) # Default size of square 'turtle' is 20px [so when we stretch we simply multiply by the specified value]
	paddle_a.penup() # 'Turtles' draw a line as they move, and this removes that line
	paddle_a.goto(-600, 0) # Centre of the screen (left)

	# Paddle B
	paddle_b = turtle.Turtle() # It's a turtle object
	paddle_b.speed(2) # Sets speed to maximum possible value
	paddle_b.shape("square") # Square is simple to resize
	paddle_b.color("black")
	paddle_b.shapesize(stretch_wid=8, stretch_len=1) # Default size of square 'turtle' is 20px [so when we stretch we simply multiply by the specified value]
	paddle_b.penup() # 'Turtles' draw a line as they move, and this removes that line
	paddle_b.goto(600, 0) # Centre of the screen (right)

	# Ball 
	ball = turtle.Turtle() # It's a turtle object
	ball.speed(1.3) # Sets speed to maximum possible value
	ball.shape("circle") # Square is simple to resize
	ball.color("black")
	ball.shapesize(stretch_wid=2)
	ball.penup() # 'Turtles' draw a line as they move, and this removes that line
	ball.goto(0, 0) # Centre of the screen (right)
	ball.dx = 1.3 # x movement
	ball.dy = 1.3 # y movement

	# Score_Board
	score = turtle.Turtle()
	score.speed(0)
	score.color("black")
	score.penup()
	score.hideturtle()
	score.goto(0, 260)
	score.write(f"{player_one}: 0	{player_two}: 0", align="center", font=("Courier", 24, "normal"))
	# ---------------- Behaviour------------------------------

	# Movement for Paddle A
	def paddle_a_up():
		y = paddle_a.ycor() # .ycor() returns the y co-ordinate
		y += 30 # Add 20px to y coordinate
		paddle_a.sety(y) # Set y to new y

		if y > 240:
			paddle_a.sety(240) # Prevents Paddle from moving beyond window border

	def paddle_a_down():
		y = paddle_a.ycor() # .ycor() returns the y co-ordinate
		y -= 30 # Add 20px to y coordinate
		paddle_a.sety(y) # Set y to new y

		if y < -240:
			paddle_a.sety(-240)

	# Movement for Paddle B
	def paddle_b_up():
		y = paddle_b.ycor() # .ycor() returns the y co-ordinate
		y += 30 # Add 20px to y coordinate
		paddle_b.sety(y) # Set y to new y

		if y > 240:
			paddle_b.sety(240) # Prevents Paddle from moving beyond window border

	def paddle_b_down():
		y = paddle_b.ycor() # .ycor() returns the y co-ordinate
		y -= 30 # sub 20px to y coordinate
		paddle_b.sety(y) # Set y to new y

		if y < -240:
			paddle_b.sety(-240) # Prevents Paddle from moving beyond window border

	# Keyboard Binding
	window.listen() # Listen for keyboard input
	window.onkeypress(paddle_a_up, "w") # When user presses "w", the function paddle_a_up will be called
	window.onkeypress(paddle_a_down, "s") # reverse
	window.onkeypress(paddle_b_up, "Up")
	window.onkeypress(paddle_b_down, "Down")


	# Main game loop

	while score_a != 50 and score_b != 50:
		window.update() # Everytime time the loop runs, it updates the screen

		# Moving the ball
		ball.setx(ball.xcor() + ball.dx)
		ball.sety(ball.ycor() + ball.dy)

		# Border Checking (What happens when the ball reaches the border)
		if ball.ycor() > 320:
			ball.sety(320)
			ball.dy *= -1 # Reverses direction of ball i.e if ball is at 2y it will return to -2y

		if ball.ycor() < -320:
			ball.sety(-320)
			ball.dy *= -1

		if ball.xcor() > 650: # Return Ball to center 
			ball.goto(0, 0)
			ball.dx *= -1
			score_a += 1
			score.clear()
			score.write(f"{player_one}: {score_a}	{player_two}: {score_b}", align="center", font=("Courier", 24, "normal"))

		if ball.xcor() < -650: # Return Ball to center 
			ball.goto(0, 0)
			ball.dx *= -1
			score_b += 1
			score.clear()
			score.write(f"{player_one}: {score_a}	{player_two}: {score_b}", align="center", font=("Courier", 24, "normal"))

		# Paddle and Ball Collisions (Physics)
		if  (ball.xcor() > 550 and ball.xcor() < 570) and (ball.ycor() < paddle_b.ycor() + 80 and ball.ycor() > paddle_b.ycor() -80):
			ball.setx(550)
			ball.dx *= -1

		if  (ball.xcor() < -550 and ball.xcor() < -570) and (ball.ycor() < paddle_a.ycor() + 80 and ball.ycor() > paddle_a.ycor() -80):
			ball.setx(-550)
			ball.dx *= -1

	if score_a < score_b:
		window = turtle.Screen() # GUI Window
		window.title("Pong Ultimate")
		window.bgcolor("black")
		window.setup(width=1280, height=680)
		window.tracer(10) # speeds up game (I noticed using a lower value causes lags)

		score = turtle.Turtle()
		score.speed(0)
		score.color("white")
		score.penup()
		score.hideturtle()
		score.goto(0, 260)
		score.write(f"{player_two} WINS", align="center", font=("Courier", 24, "normal"))

	if score_a > score_b:
		window = turtle.Screen() # GUI Window
		window.title("Pong Ultimate")
		window.bgcolor("black")
		window.setup(width=1280, height=680)
		window.tracer(10) # speeds up game (I noticed using a lower value causes lags)

		score = turtle.Turtle()
		score.speed(0)
		score.color("white")
		score.penup()
		score.hideturtle()
		score.goto(0, 260)
		score.write(f"{player_one} WINS", align="center", font=("Courier", 24, "normal"))


if difficulty == 2:
	window = turtle.Screen() # GUI Window
	window.title("Pong Ultimate")
	window.bgcolor("orange")
	window.setup(width=1280, height=680)
	window.tracer(10) # speeds up game (I noticed using a lower value causes lags)


	# SCORES
	score_a = 0
	score_b = 0

	# Paddle A
	paddle_a = turtle.Turtle() # It's a turtle object
	paddle_a.speed(3) # Sets speed to maximum possible value
	paddle_a.shape("square") # Square is simple to resize
	paddle_a.color("black")
	paddle_a.shapesize(stretch_wid=5, stretch_len=1) # Default size of square 'turtle' is 20px [so when we stretch we simply multiply by the specified value]
	paddle_a.penup() # 'Turtles' draw a line as they move, and this removes that line
	paddle_a.goto(-600, 0) # Centre of the screen (left)

	# Paddle B
	paddle_b = turtle.Turtle() # It's a turtle object
	paddle_b.speed(3) # Sets speed to maximum possible value
	paddle_b.shape("square") # Square is simple to resize
	paddle_b.color("black")
	paddle_b.shapesize(stretch_wid=5, stretch_len=1) # Default size of square 'turtle' is 20px [so when we stretch we simply multiply by the specified value]
	paddle_b.penup() # 'Turtles' draw a line as they move, and this removes that line
	paddle_b.goto(600, 0) # Centre of the screen (right)

	# Ball 
	ball = turtle.Turtle() # It's a turtle object
	ball.speed(1.7) # Sets speed to maximum possible value
	ball.shape("circle") # Square is simple to resize
	ball.color("black")
	ball.shapesize(stretch_wid=2)
	ball.penup() # 'Turtles' draw a line as they move, and this removes that line
	ball.goto(0, 0) # Centre of the screen (right)
	ball.dx = 1.7 # x movement
	ball.dy = 1.7 # y movement

	# Score_Board
	score = turtle.Turtle()
	score.speed(0)
	score.color("black")
	score.penup()
	score.hideturtle()
	score.goto(0, 260)
	score.write(f"{player_one}: 0   |   {timer}    |{player_two}: 0", align="center", font=("Courier", 24, "normal"))
	# ---------------- Behaviour------------------------------

	# Movement for Paddle A
	def paddle_a_up():
		y = paddle_a.ycor() # .ycor() returns the y co-ordinate
		y += 40 # Add 20px to y coordinate
		paddle_a.sety(y) # Set y to new y

		if y > 240:
			paddle_a.sety(240) # Prevents Paddle from moving beyond window border

	def paddle_a_down():
		y = paddle_a.ycor() # .ycor() returns the y co-ordinate
		y -= 40 # Add 20px to y coordinate
		paddle_a.sety(y) # Set y to new y

		if y < -240:
			paddle_a.sety(-240) # Prevents Paddle from moving beyond window border

	# Movement for Paddle B
	def paddle_b_up():
		y = paddle_b.ycor() # .ycor() returns the y co-ordinate
		y += 40 # Add 20px to y coordinate
		paddle_b.sety(y) # Set y to new y

		if y > 240:
			paddle_b.sety(240) # Prevents Paddle from moving beyond window border

	def paddle_b_down():
		y = paddle_b.ycor() # .ycor() returns the y co-ordinate
		y -= 40 # Add 20px to y coordinate
		paddle_b.sety(y) # Set y to new y

		if y < -240:
			paddle_b.sety(-240) # Prevents Paddle from moving beyond window border

	# Keyboard Binding
	window.listen() # Listen for keyboard input
	window.onkeypress(paddle_a_up, "w") # When user presses "w", the function paddle_a_up will be called
	window.onkeypress(paddle_a_down, "s") # reverse
	window.onkeypress(paddle_b_up, "Up")
	window.onkeypress(paddle_b_down, "Down")


	# Main game loop

	while timer != 10:
		window.update() # Everytime time the loop runs, it updates the screen

		# Moving the ball
		ball.setx(ball.xcor() + ball.dx)
		ball.sety(ball.ycor() + ball.dy)

		# Border Checking (What happens when the ball reaches the border)
		if ball.ycor() > 320:
			ball.sety(320)
			ball.dy *= -1 # Reverses direction of ball i.e if ball is at 2y it will return to -2y

		if ball.ycor() < -320:
			ball.sety(-320)
			ball.dy *= -1

		if ball.xcor() > 700: # Return Ball to center 
			ball.goto(0, 0)
			ball.dx *= -1
			score_a += 1
			timer += 0.5
			score.clear()
			score.write(f"{player_one}: {score_a}   |   {timer}    |{player_two}: {score_b}", align="center", font=("Courier", 24, "normal"))

		if ball.xcor() < -700: # Return Ball to center 
			ball.goto(0, 0)
			ball.dx *= -1
			score_b += 1
			timer += 0.5
			score.clear()
			score.write(f"{player_one}: {score_a}   |   {timer}    |{player_two}: {score_b}", align="center", font=("Courier", 24, "normal"))

		# Paddle and Ball Collisions (Physics)
		if  (ball.xcor() > 550 and ball.xcor() < 570) and (ball.ycor() < paddle_b.ycor() + 80 and ball.ycor() > paddle_b.ycor() -80):
			ball.setx(550)
			ball.dx *= -1

		if  (ball.xcor() < -550 and ball.xcor() < -570) and (ball.ycor() < paddle_a.ycor() + 80 and ball.ycor() > paddle_a.ycor() -80):
			ball.setx(-550)
			ball.dx *= -1

	if score_a < score_b:
		window = turtle.Screen() # GUI Window
		window.title("Pong Ultimate")
		window.bgcolor("black")
		window.setup(width=1280, height=680)
		window.tracer(10) # speeds up game (I noticed using a lower value causes lags)

		score = turtle.Turtle()
		score.speed(0)
		score.color("white")
		score.penup()
		score.hideturtle()
		score.goto(0, 260)
		score.write(f"{player_two} WINS", align="center", font=("Courier", 24, "normal"))

	if score_a > score_b:
		window = turtle.Screen() # GUI Window
		window.title("Pong Ultimate")
		window.bgcolor("black")
		window.setup(width=1280, height=680)
		window.tracer(10) # speeds up game (I noticed using a lower value causes lags)

		score = turtle.Turtle()
		score.speed(0)
		score.color("white")
		score.penup()
		score.hideturtle()
		score.goto(0, 260)
		score.write(f"{player_one} WINS", align="center", font=("Courier", 24, "normal"))

if difficulty == 3:
	window = turtle.Screen() # GUI Window
	window.title("Pong Ultimate")
	window.bgcolor("orange")
	window.setup(width=1280, height=680)
	window.tracer(10) # speeds up game (I noticed using a lower value causes lags)


	# SCORES
	score_a = 0
	score_b = 0

	# Paddle A
	paddle_a = turtle.Turtle() # It's a turtle object
	paddle_a.speed(3) # Sets speed to maximum possible value
	paddle_a.shape("square") # Square is simple to resize
	paddle_a.color("black")
	paddle_a.shapesize(stretch_wid=8, stretch_len=1) # Default size of square 'turtle' is 20px [so when we stretch we simply multiply by the specified value]
	paddle_a.penup() # 'Turtles' draw a line as they move, and this removes that line
	paddle_a.goto(-600, 0) # Centre of the screen (left)

	# Paddle B
	paddle_b = turtle.Turtle() # It's a turtle object
	paddle_b.speed(3) # Sets speed to maximum possible value
	paddle_b.shape("square") # Square is simple to resize
	paddle_b.color("black")
	paddle_b.shapesize(stretch_wid=8, stretch_len=1) # Default size of square 'turtle' is 20px [so when we stretch we simply multiply by the specified value]
	paddle_b.penup() # 'Turtles' draw a line as they move, and this removes that line
	paddle_b.goto(600, 0) # Centre of the screen (right)

	# Ball 
	ball = turtle.Turtle() # It's a turtle object
	ball.speed(4) # Sets speed to maximum possible value
	ball.shape("circle") # Square is simple to resize
	ball.color("black")
	ball.shapesize(stretch_wid=2)
	ball.penup() # 'Turtles' draw a line as they move, and this removes that line
	ball.goto(0, 0) # Centre of the screen (right)
	ball.dx = 4 # x movement
	ball.dy = 4 # y movement

	# Score_Board
	score = turtle.Turtle()
	score.speed(0)
	score.color("black")
	score.penup()
	score.hideturtle()
	score.goto(0, 260)
	score.write(f"{player_one}: 0	{player_two}: 0", align="center", font=("Courier", 24, "normal"))
	# ---------------- Behaviour------------------------------

	# Movement for Paddle A
	def paddle_a_up():
		y = paddle_a.ycor() # .ycor() returns the y co-ordinate
		y += 40 # Add 20px to y coordinate
		paddle_a.sety(y) # Set y to new y

		if y > 240:
			paddle_a.sety(240) # Prevents Paddle from moving beyond window border

	def paddle_a_down():
		y = paddle_a.ycor() # .ycor() returns the y co-ordinate
		y -= 40 # Add 20px to y coordinate
		paddle_a.sety(y) # Set y to new y

		if y < -240:
			paddle_a.sety(-240) # Prevents Paddle from moving beyond window border

	# Movement for Paddle B
	def paddle_b_up():
		y = paddle_b.ycor() # .ycor() returns the y co-ordinate
		y += 40 # Add 20px to y coordinate
		paddle_b.sety(y) # Set y to new y

		if y > 240:
			paddle_b.sety(240) # Prevents Paddle from moving beyond window border

	def paddle_b_down():
		y = paddle_b.ycor() # .ycor() returns the y co-ordinate
		y -= 40 # Add 20px to y coordinate
		paddle_b.sety(y) # Set y to new y

		if y < -240:
			paddle_b.sety(-240) # Prevents Paddle from moving beyond window border

	# Keyboard Binding
	window.listen() # Listen for keyboard input
	window.onkeypress(paddle_a_up, "w") # When user presses "w", the function paddle_a_up will be called
	window.onkeypress(paddle_a_down, "s") # reverse
	window.onkeypress(paddle_b_up, "Up")
	window.onkeypress(paddle_b_down, "Down")


	# Main game loop

	while score_a != 30 and score_b != 30:
		window.update() # Everytime time the loop runs, it updates the screen

		# Moving the ball
		ball.setx(ball.xcor() + ball.dx)
		ball.sety(ball.ycor() + ball.dy)

		# Border Checking (What happens when the ball reaches the border)
		if ball.ycor() > 320:
			ball.sety(320)
			ball.dy *= -1 # Reverses direction of ball i.e if ball is at 2y it will return to -2y

		if ball.ycor() < -320:
			ball.sety(-320)
			ball.dy *= -1

		if ball.xcor() > 700: # Return Ball to center 
			ball.goto(0, 0)
			ball.dx *= -1
			score_a += 1
			score.clear()
			score.write(f"{player_one}: {score_a}	{player_two}: {score_b}", align="center", font=("Courier", 24, "normal"))

		if ball.xcor() < -700: # Return Ball to center 
			ball.goto(0, 0)
			ball.dx *= -1
			score_b += 1
			score.clear()
			score.write(f"{player_one}: {score_a}	{player_two}: {score_b}", align="center", font=("Courier", 24, "normal"))

		# Paddle and Ball Collisions (Physics)
		if  (ball.xcor() > 550 and ball.xcor() < 570) and (ball.ycor() < paddle_b.ycor() + 80 and ball.ycor() > paddle_b.ycor() -80):
			ball.setx(550)
			ball.dx *= -1

		if  (ball.xcor() < -550 and ball.xcor() < -570) and (ball.ycor() < paddle_a.ycor() + 80 and ball.ycor() > paddle_a.ycor() -80):
			ball.setx(-550)
			ball.dx *= -1

	if score_a < score_b:
		window = turtle.Screen() # GUI Window
		window.title("Pong Ultimate")
		window.bgcolor("black")
		window.setup(width=1280, height=680)
		window.tracer(10) # speeds up game (I noticed using a lower value causes lags)

		score = turtle.Turtle()
		score.speed(0)
		score.color("white")
		score.penup()
		score.hideturtle()
		score.goto(0, 260)
		score.write(f"{player_two} WINS", align="center", font=("Courier", 24, "normal"))

	if score_b < score_a:
		window = turtle.Screen() # GUI Window
		window.title("Pong Ultimate")
		window.bgcolor("black")
		window.setup(width=1280, height=680)
		window.tracer(10) # speeds up game (I noticed using a lower value causes lags)

		score = turtle.Turtle()
		score.speed(0)
		score.color("white")
		score.penup()
		score.hideturtle()
		score.goto(0, 260)
		score.write(f"{player_one} WINS", align="center", font=("Courier", 24, "normal"))

if difficulty == 4:
	window = turtle.Screen() # GUI Window
	window.title("Pong Ultimate")
	window.bgcolor("orange")
	window.setup(width=1280, height=680)
	window.tracer(10) # speeds up game (I noticed using a lower value causes lags)


	# SCORES
	score_a = 10
	score_b = 10

	# Paddle A
	paddle_a = turtle.Turtle() # It's a turtle object
	paddle_a.speed(6) # Sets speed to maximum possible value
	paddle_a.shape("square") # Square is simple to resize
	paddle_a.color("black")
	paddle_a.shapesize(stretch_wid=5, stretch_len=1) # Default size of square 'turtle' is 20px [so when we stretch we simply multiply by the specified value]
	paddle_a.penup() # 'Turtles' draw a line as they move, and this removes that line
	paddle_a.goto(-600, 0) # Centre of the screen (left)

	# Paddle B
	paddle_b = turtle.Turtle() # It's a turtle object
	paddle_b.speed(6) # Sets speed to maximum possible value
	paddle_b.shape("square") # Square is simple to resize
	paddle_b.color("black")
	paddle_b.shapesize(stretch_wid=5, stretch_len=1) # Default size of square 'turtle' is 20px [so when we stretch we simply multiply by the specified value]
	paddle_b.penup() # 'Turtles' draw a line as they move, and this removes that line
	paddle_b.goto(600, 0) # Centre of the screen (right)

	# Ball 
	ball = turtle.Turtle() # It's a turtle object
	ball.speed(4.3) # Sets speed to maximum possible value
	ball.shape("circle") # Square is simple to resize
	ball.color("black")
	ball.shapesize(stretch_wid=2)
	ball.penup() # 'Turtles' draw a line as they move, and this removes that line
	ball.goto(0, 0) # Centre of the screen (right)
	ball.dx = 4.3 # x movement
	ball.dy = 4.3 # y movement

	# Score_Board
	score = turtle.Turtle()
	score.speed(0)
	score.color("black")
	score.penup()
	score.hideturtle()
	score.goto(0, 260)
	score.write(f"{player_one}: {score_a}	{player_two}: {score_b}", align="center", font=("Courier", 24, "normal"))
	# ---------------- Behaviour------------------------------

	# Movement for Paddle A
	def paddle_a_up():
		y = paddle_a.ycor() # .ycor() returns the y co-ordinate
		y += 60 # Add 20px to y coordinate
		paddle_a.sety(y) # Set y to new y

		if y > 240:
			paddle_a.sety(240) # Prevents Paddle from moving beyond window border

	def paddle_a_down():
		y = paddle_a.ycor() # .ycor() returns the y co-ordinate
		y -= 60 # Add 20px to y coordinate
		paddle_a.sety(y) # Set y to new y

		if y < -240:
			paddle_a.sety(-240) # Prevents Paddle from moving beyond window border

	# Movement for Paddle B
	def paddle_b_up():
		y = paddle_b.ycor() # .ycor() returns the y co-ordinate
		y += 60 # Add 20px to y coordinate
		paddle_b.sety(y) # Set y to newy

		if y > 240:
			paddle_b.sety(240) # Prevents Paddle from moving beyond window border

	def paddle_b_down():
		y = paddle_b.ycor() # .ycor() returns the y co-ordinate
		y -= 60 # Add 20px to y coordinate
		paddle_b.sety(y) # Set y to new y

		if y < -240:
			paddle_b.sety(-240) # Prevents Paddle from moving beyond window border

	# Keyboard Binding
	window.listen() # Listen for keyboard input
	window.onkeypress(paddle_a_up, "w") # When user presses "w", the function paddle_a_up will be called
	window.onkeypress(paddle_a_down, "s") # reverse
	window.onkeypress(paddle_b_up, "Up")
	window.onkeypress(paddle_b_down, "Down")


	# Main game loop

	while score_a != 0 and score_b != 0:
		window.update() # Everytime time the loop runs, it updates the screen

		# Moving the ball
		ball.setx(ball.xcor() + ball.dx)
		ball.sety(ball.ycor() + ball.dy)

		# Border Checking (What happens when the ball reaches the border)
		if ball.ycor() > 320:
			ball.sety(320)
			ball.dy *= -1 # Reverses direction of ball i.e if ball is at 2y it will return to -2y

		if ball.ycor() < -320:
			ball.sety(-320)
			ball.dy *= -1

		if ball.xcor() > 700: # Return Ball to center 
			ball.goto(0, 0)
			ball.dx *= -1
			score_a -= 1
			score.clear()
			score.write(f"{player_one}: {score_a}	{player_two}: {score_b}", align="center", font=("Courier", 24, "normal"))

		if ball.xcor() < -700: # Return Ball to center 
			ball.goto(0, 0)
			ball.dx *= -1
			score_b -= 1
			score.clear()
			score.write(f"{player_one}: {score_a}	{player_two}: {score_b}", align="center", font=("Courier", 24, "normal"))

		# Paddle and Ball Collisions (Physics)
		if  (ball.xcor() > 550 and ball.xcor() < 570) and (ball.ycor() < paddle_b.ycor() + 80 and ball.ycor() > paddle_b.ycor() -80):
			ball.setx(550)
			ball.dx *= -1

		if  (ball.xcor() < -550 and ball.xcor() < -570) and (ball.ycor() < paddle_a.ycor() + 80 and ball.ycor() > paddle_a.ycor() -80):
			ball.setx(-550)
			ball.dx *= -1

	if score_a == 0:
		window = turtle.Screen() # GUI Window
		window.title("Pong Ultimate")
		window.bgcolor("black")
		window.setup(width=1280, height=680)
		window.tracer(10) # speeds up game (I noticed using a lower value causes lags)

		score = turtle.Turtle()
		score.speed(0)
		score.color("white")
		score.penup()
		score.hideturtle()
		score.goto(0, 260)
		score.write(f"{player_two} WINS", align="center", font=("Courier", 24, "normal"))

	if score_b == 0:
		window = turtle.Screen() # GUI Window
		window.title("Pong Ultimate")
		window.bgcolor("black")
		window.setup(width=1280, height=680)
		window.tracer(10) # speeds up game (I noticed using a lower value causes lags)

		score = turtle.Turtle()
		score.speed(0)
		score.color("white")
		score.penup()
		score.hideturtle()
		score.goto(0, 260)
		score.write(f"{player_one} WINS", align="center", font=("Courier", 24, "normal"))
		

else:
	print("LEARN TO READ SUNSHINE")
