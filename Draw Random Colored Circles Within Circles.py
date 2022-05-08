'''
Purpose: Draw randomly colored circles within circles. The circle radius 
and pensize will increase. The background will change color.
Programmer: Jae Bird
Date: 5/4/22
'''
# Import modules
import turtle
import random
#-------------------------------------------------------
def main():
  write_heading_text()
  perform_house_keeping()
  draw_colorful_circles()
  write_footing_text()
  animate_background_colors()
#------------------------------------------------------
def write_heading_text():
  turtle.speed(0)
  heading_x = -450
  heading_y = 250
  turtle.penup()
  turtle.goto(heading_x,heading_y)
  turtle.pencolor('black')
  turtle.bgcolor('pink')
  turtle.write('Drawing Colorful Circles in Circles',
               font=('ariel',44,'bold'))
  turtle.goto(heading_x - 4,heading_y + 4)
  turtle.pencolor('white')
  turtle.write('Drawing Colorful Circles in Circles',
               font=('ariel',44,'bold'))
#------------------------------------------------------------
def perform_house_keeping():
  turtle.shape('turtle')
  pensize = 2
  turtle.pensize(pensize)
  turtle.speed(0)
  circles = 0
  turtle.colormode(255)
#-------------------------------------------------------
def draw_colorful_circles():
  pensize = 1
  radius = 4
  # Use for statement to loop 
  for circles in range (26):
    turtle.pensize(pensize)
    # Generate random number for red color
    red = random.randint(0,255)
    # Generate random number for green color
    green = random.randint(0,255) 
    # Generate random number for blue color
    blue = random.randint(0,255)
    # Pass the 3 colors to create a mixed color
    turtle.pencolor(red,green,blue) 
    # Raise the pen up so no drawing will happen
    turtle.penup()
    # Tell turtle to fo to position x = 0, y=-circle*20
    turtle.goto(0,-circles*radius) # -circles * 20
    # Lower the pen down to draw again
    turtle.pendown()
    #Draw a large circle of radius*circle radius
    turtle.circle(radius*circles)
    # Increment the radius and pensize to make it larger
    radius += 0.2
    pensize += 1
#----------------------------------------------------------
def write_footing_text():
  footing_x = -350
  footing_y = -320
  turtle.penup()
  turtle.goto(footing_x,footing_y)
  
  turtle.pencolor('black')
  turtle.pendown()
  turtle.write('Python Programmer: Jae Bird',
               font = 'times 40 italic')
  turtle.penup()
  turtle.goto(footing_x - 2,footing_y + 2)
  turtle.pendown()
  turtle.pencolor('white')
  turtle.write('Python Programmer: Jae Bird',
               font = 'times 40 italic')
  turtle.hideturtle()
#----------------------------------------------------------
def animate_background_colors():
  # Use while True which will loop forever unless you close it
  while True:
    red = random.randint(0,255)
    print ('Red color value is:',red)
    green = random.randint(0,255)
    print ('Green color value is:',green)
    blue = random.randint(0,255)
    print('Blue color value is:',blue)
    # Pass the 3 colors to create a mixed color
    turtle.bgcolor(red,green,blue)
    print('----------------------------------------')
    turtle.speed(10)
    turtle.delay(2000)
#--------------------------------------------------------
main()
turtle.done()