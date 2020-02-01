#!/usr/bin/python3
"""
Basic Module - main
this module contain all instructions and code to create
a classic game Skane - SuperSnake

Autor: Carlos Andres Garcia Morales
Date: 30/01/20
E-mail: agzsoftsi@gmail.com
Twitter: @karlgarmor

"""

import turtle
""" The turtle module provides turtle graphics primitives """
import time
""" The time module provides manage of the time """
import random

w_wait = 0.1

# Basic Configuration properties of the window
w = turtle.Screen()
w.title("SuperSnake  @karlgarmor")
w.bgcolor("black")
w.setup(width=500, height=500)
#w.exitonclick()
w.tracer(0)

# Create the Snake
s_head = turtle.Turtle()
s_head.speed(50)
s_head.shape("square")
s_head.color("green")
s_head.penup()
s_head.goto(0,0)
s_head.direction = "stop"

# Create the food
s_food = turtle.Turtle()
s_food.speed(50)
s_food.shape("circle")
s_food.color("red")
s_food.penup()
s_food.goto(100,100)
s_food.direction = "stop"

# new Segment

new_seg = []

# Actions
def keyup():
    s_head.direction = "up"

def keydown():
    s_head.direction = "down"

def keyleft():
    s_head.direction = "left"

def keyright():
    s_head.direction = "right"

def movement():
    if s_head.direction == "up":
        y = s_head.ycor()
        s_head.sety(y + 15)

    if s_head.direction == "down":
        y = s_head.ycor()
        s_head.sety(y - 15)

    if s_head.direction == "left":
        x = s_head.xcor()
        s_head.setx(x - 15)

    if s_head.direction == "right":
        x = s_head.xcor()
        s_head.setx(x + 15)

# Configure keyboard
w.listen()
w.onkeypress(keyup, "Up")
w.onkeypress(keydown, "Down")
w.onkeypress(keyleft, "Left")
w.onkeypress(keyright, "Right")

while True:
    w.update()

    #Collitions
    if s_head.xcor() > 238 or s_head.xcor() < -240 or s_head.ycor() > 240 or s_head.ycor() < -238:
        time.sleep(1)
        s_head.goto(0,0)
        s_head.direction = "stop" 
  
        #hidde segments
        for seg in new_seg:
            seg.goto(1000,1000)
            seg.hideturtle()

	#clear segment
        new_seg.clear()

    if s_head.distance(s_food) < 20:
        x = random.randint(-240,240)
        y = random.randint(-240,240)
        s_food.goto(x,y)

        # new segment of the Snake
        n_head = turtle.Turtle()
        n_head.speed(50)
        n_head.shape("square")
        n_head.color("green")
        n_head.penup()
        new_seg.append(n_head)

     #move n_head
    count_seg = len(new_seg)
    for index in range(count_seg -1, 0, -1):
        x = new_seg[index - 1].xcor()
        y = new_seg[index - 1].ycor()
        new_seg[index].goto(x,y)

    if count_seg > 0:
        x = s_head.xcor()
        y = s_head.ycor()
        new_seg[0].goto(x,y)


        
    movement()
    time.sleep(w_wait)
