"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle
import random

screen = turtle.Screen()
screen.bgcolor("fuchsia")
screen.colormode(255)

t = turtle.Turtle()
t.color("turquoise")
t.shape("turtle")

def circle():
  t.circle(90)

def randomcolor():
  return random.randint(0,255)

def changecolor():
  t.color(randomcolor(),randomcolor(),randomcolor())

def changebg():
  screen.bgcolor(randomcolor(),randomcolor(),randomcolor())

def fd():
  t.forward(10)

def bd():
  t.backward(10)

def right():
  t.right(10)

def left():
  t.left(10)

screen.listen()
screen.onkey(circle, 'c')

screen.onkey(changebg, 'b')
screen.onkey(changecolor, 'v')

screen.onkey(fd, 'Up')
screen.onkey(bd, 'Down')
screen.onkey(right, 'Right')
screen.onkey(left, 'Left')

input()
