# Polygon excercise from Week 0

# Name:


from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()				

# This is where you put code to move bob

def polygon(turtle, side_len, sides):
	angle = 360/sides
	for i in range (sides):
		fd(turtle, side_len)
		lt(turtle, angle)	

def circle (turtle, radius):
	circumfernce = 2*radius*3.145
	sides = 20
	side_len = circumfernce/ sides
	polygon(turtle, side_len, sides)


def square (t, bob):
	for i in range(4):
		bob.fd(t)
		bob.lt()

def arc (turtle, radius, theta=360):
	arc = theta/360.0
	circumfernce = 2*radius*3.145
	sides = 40
	side_len = circumfernce/ sides
	piece_of_pie = int(arc * sides)
	polygon2(turtle, side_len, sides, piece_of_pie)

def polygon2(turtle, side_len, sides, piece_of_pie):
	angle = 360/sides
	for i in range (piece_of_pie):
		fd(turtle, side_len)
		lt(turtle, angle)	

#arc(bob, 50, 200)
square(100, bob);

wait_for_user()					
