

from turtle import *        # importing everything from turtle library 

speed(0)                    # adding speed 

bgcolor("black")            # setting black color for background

# Creating Orange Planet
color("orange")             # orange color turtle tip
begin_fill()                # beginning to fill color inside the circle
circle(90)                  # drawing circle with radius 90
end_fill()                  # ending to fill the color inside the circle 

# Moves Forward
penup()                     # penup removes the trail 
forward(160)                # moving forward to create more circles
pendown()                   # it starts adding trail now.

# Now we do same for creating another circle with grey color 
# Creating Grey Planet
color("grey")
begin_fill()
circle(50)
end_fill()

# Moves Forward
penup()
forward(150)
pendown()

# Creating Red Planet
color("red")
begin_fill()
circle(70)
end_fill()

# Moves Forward
penup()
forward(140)
pendown()

# Creating Green Planet
color("green")
begin_fill()
circle(60)
end_fill()



done()