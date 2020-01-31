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

# Basic Configuration properties of the window
w = turtle.Screen()
w.title("SuperSnake  @karlgarmor")
w.bgcolor("black")
w.setup(width=500, height=500)
w.exitonclick()
w.tracer(0)

# Create the Snake
s_head = turtle.Turtle()
s_head.speed(50)
s_head.shape("circle")
s_head.penup()


