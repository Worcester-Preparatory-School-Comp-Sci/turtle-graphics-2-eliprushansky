#ELI PRUSHANSKY 151019
import turtle
screen=turtle.Screen()

#This turtle covers the whole canvas as the blue sky
def sky():
    sky=turtle.Screen()
    sky.bgcolor("sky blue")

sky()

#This turtle covers the bottom section of the canvas with green grass
def grass():
    grass=turtle.Turtle()
    grass.ht()
    grass.begin_fill()
    grass.up()
    grass.goto(500,-300)
    for x in range(2):
        grass.left(90)
        grass.forward(200)
        grass.left(90)
        grass.forward(1000)
    grass.fillcolor("green")
    grass.end_fill()

grass()

#This turtle creates a pyramid to sit in the middle of the landscape
def pyramid():
    pyramid=turtle.Turtle()
    pyramid.ht()
    pyramid.begin_fill()
    pyramid.up()
    pyramid.right(60)
    pyramid.forward(150)
    for x in range(2):
        pyramid.right(120)
        pyramid.forward(150)
    pyramid.fillcolor("beige")
    pyramid.end_fill()

pyramid()

#This turtle created the first part of a three part cloud
def cloud():
    cloud=turtle.Turtle()
    cloud.ht()
    cloud.begin_fill()
    cloud.up()
    cloud.goto(-100,100)
    cloud.circle(40)
    cloud.fillcolor("white")
    cloud.end_fill()

cloud()

#This turtle created the second part of a three part cloud
def cloud2():
    cloud2=turtle.Turtle()
    cloud2.ht()
    cloud2.begin_fill()
    cloud2.up()
    cloud2.goto(-160,100)
    cloud2.circle(40)
    cloud2.fillcolor("white")
    cloud2.end_fill()

cloud2()

#This turtle created the third part of a three part cloud
def cloud3():
    cloud3=turtle.Turtle()
    cloud3.ht()
    cloud3.begin_fill()
    cloud3.up()
    cloud3.goto(-190,130)
    cloud3.circle(40)
    cloud3.fillcolor("white")
    cloud3.end_fill()


cloud3()
