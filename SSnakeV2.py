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
import os

w_wait = 0.1
score_count = 0

# Basic Configuration properties of the window
w = turtle.Screen()
w.title("SuperSnake  @karlgarmor")
w.bgcolor("black")
w.bgpic("fondo.gif")
w.setup(width=500, height=500)
#w.exitonclick()
w.tracer(0)
w.addshape("~/SuperSnakeGame/head.gif")
w.addshape("~/SuperSnakeGame/body.gif")


# Create the Snake

s_head = turtle.Turtle()
s_head.speed(50)
s_head.shape("~/SuperSnakeGame/head.gif")
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

# Text to Score
score_text = turtle.Turtle()
score_text.speed(0)
score_text.color("white")
score_text.penup()
score_text.hideturtle()
score_text.goto(0,195)
score_text.write("Score: 0", align = "center", font = ("courrier", 18, "normal"))

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
        s_head.settiltangle(90)
        y = s_head.ycor()
        s_head.sety(y + 15)

    if s_head.direction == "down":
        s_head.settiltangle(-90)
        y = s_head.ycor()
        s_head.sety(y - 15)

    if s_head.direction == "left":
        s_head.settiltangle(-180)
        x = s_head.xcor()
        s_head.setx(x - 15)

    if s_head.direction == "right":
        s_head.settiltangle(0)
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
        
        #Reset score
        score_count = 0 
        score_text.clear()
        score_text.write("Score: {}".format(score_count), align = "center", font = ("courrier", 18,  "normal"))  
        
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
        n_head.shape("~/SuperSnakeGame/body.gif")
        n_head.color("lightgreen")
        n_head.penup()
        new_seg.append(n_head)

        #increment score
        score_count += 1
        score_text.clear()
        score_text.write("Score: {}".format(score_count), align = "center", font = ("courrier", 18,  "normal"))
        

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

    #collitions with the snake body
    #for seg in new_seg:
        #if seg.distance(s_head) < 20:
            #time.sleep(1)
            #s_head.goto(0,0)
            #s_head.direction = "stop"

            #hidde segments of body
            #for seg in new_seg:
                #seg.goto(1000,1000)

            #new_seg.clear()
 
    time.sleep(w_wait)
