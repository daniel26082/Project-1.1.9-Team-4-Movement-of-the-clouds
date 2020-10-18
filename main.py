# imports turtle 
import turtle
# set the screen
screen = turtle.Screen()
screen.bgcolor('light blue')
screen.tracer(0)
# imports cloud
cloud = turtle.Turtle()
cloud.color('white')
cloud.speed(0)
cloud.hideturtle()
# define the function that draw the cloud
def draw_cloud():
  # fill color with white
  cloud.fillcolor('white')
  cloud.begin_fill()
  cloud.setheading(345)
  for i in range(2):
    cloud.circle(30,210)
    cloud.right(90)
    cloud.circle(30,150)
    cloud.right(90)
  cloud.end_fill()
  cloud.setheading(0)
# define the function that draw two clouds
def draw_two_clouds():
  # draw the first cloud
  draw_cloud()
  # set the position of second cloud
  cloud.penup()
  cloud.forward(250)
  cloud.right(90)
  cloud.forward(50)
  cloud.left(90)
  cloud.pendown()
  # draw the second cloud
  draw_cloud()
  # return
  cloud.penup()
  cloud.backward(250)
  cloud.left(90)
  cloud.forward(50)
  cloud.right(90)
  cloud.pendown()
cloud.penup()
cloud.goto(-250,100)
cloud.pendown()
# infinite loop
while (True):
  # move forward
  for i in range(250):
    cloud.clear()
    draw_two_clouds()
    screen.update()
    # speed of the cloud
    cloud.forward(1)
  # move backward
  for i in range(250):
    cloud.clear()
    draw_two_clouds()
    screen.update()
    # speed of the cloud
    cloud.backward(1)