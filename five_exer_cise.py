

from turtle import *

# Setting up the turtle speed and background color
speed(10)
bgcolor("#645452")  # Light background color

# Draw the first circle with a fill
color("#FF5733")  # Orange color
begin_fill()
circle(90)  # Making circle with radius 90
end_fill()

# Move forward with a different color
color("#FF5733")  # Orange color
forward(200)
begin_fill()
circle(90)  # Second circle
end_fill()

# Draw a smaller shape with a different color
color("#33FF57")  # Green color
backward(100)
right(90)
forward(50)

# Diagonal line with color
color("#33FF57")  # Green color
right(45)
begin_fill()
forward(200)


# Additional lines to form shapes
color("#33FF57")  # Green color
left(135)

forward(280)


# Add another diagonal section
color("#33FF57")  # Green color
left(135)
forward(198)


# Draw a mirrored line
color("#33FF57")  # Green color
left(135)
forward(200)
end_fill()

# Draw the rectangle
color("#4682B4")  # Steel blue color
right(90)
forward(100)
left(90)
begin_fill()
forward(100)
left(90)
forward(200)
left(90)
forward(100)
left(90)
forward(100)
end_fill()

# Finish
done()
