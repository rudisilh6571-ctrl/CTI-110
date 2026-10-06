# Holly Rudisill
# 10/06//2026
# P4LAB
# Turtles

# set up your turtle
import turtle

screen = turtle.Screen()
screen.setup(800, 600)
screen.title("P4LAB1")
screen.bgcolor("midnightblue") # change this id you want

t = turtle.Turtle()

#set these to your reference
t.color("red")
t.shape("turtle")
t.pencolor("cyan3")
t.fillcolor("cyan4")
t.pensize(7)

"""
# draw with t (your code here)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)


# try as a  for loop
sides = 4 
for sides in range(4):
    t.forward(100)
    t.left(90)
"""
sides = 4
angle = 360 / sides
length = 100

# while loop 
with t.fill():
    while sides > 0:
        t.forward(length)
        t.right(angle)
        #sides = sides - 1
        sides -= 1
        
# put a roof on the house
t.fillcolor("cyan2")
sides = 3
t.begin_fill()
for sides in range(sides):
    t.forward(100)
    t.left(120)
t.end_fill()


# example 2 for loop
t.teleport(-200, 0)
t.fillcolor("cyan4")
sides = 4
t.begin_fill()
for sides in range(sides):
    t.forward(length)
    t.right(angle)
t.end_fill()

# put a roof on the house
t.fillcolor("cyan2")
sides = 3
t.begin_fill()
for sides in range(sides):
    t.forward(100)
    t.left(120)
t.end_fill()


"""
# put a star in the sky
t.penup()
t.goto(200, 180)          # a place in the sky, above and right of the house
t.pendown()

t.fillcolor("gold")
t.pencolor("gold")
t.begin_fill()
for point in range(5):
    t.forward(80)
    t.right(144)           # the only big change: 90 became 144
t.end_fill()
"""

# ---- THE KNOBS: change these numbers, then press F5 again ----
COUNT = 120        # how many times the loop runs
LENGTH = 30       # length of the first line, in steps
TURN = 162         # degrees to turn left after each line
GROW = 2           # steps added to the length after each line
COLORS = ["#023E8A", "#0077B6", "#00B4D8", "#48CAE4"]

t = turtle.Turtle()
t.speed(0)         # 0 = fastest
t.teleport(180, 180)# one pass = one line
# lines drawn = COUNT = 120
length = LENGTH
for i in range(COUNT):
    t.pencolor(COLORS[i % len(COLORS)])    # pick the next color
    t.forward(length)
    t.left(TURN)
    length = length + GROW

t.hideturtle()
# End - keep window open
turtle.done()

