from turtle import Screen
import turtle as t
import random

# import heroes
# print(heroes.gen())
turtle = t.Turtle()
t.colormode(255)
turtle.shape("classic")
turtle.speed("fastest")


# # Random Walk
def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colors = (r, g, b)
    return random_colors



# def draw_spirograph(size_of_gap):
#     integer = int(360 / size_of_gap)
#     for _ in range(integer):
#         turtle.color(random_colors())
#         turtle.circle(100)
#         turtle.setheading(turtle.heading() + size_of_gap)
#
#
# draw_spirograph(5)

# directions = [0, 90, 180, 270]
# turtle.pensize(10)
#
# for _ in range(200):
#     turtle.color(random_colors())
#     turtle.forward(30)
#     turtle.setheading(random.choice(directions))

# # Make all shapes
# def draw_shapes(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         turtle.forward(100)
#         turtle.right(angle)
#
#
# for shapes in range(3, 11):
#     turtle.color(random.choice(colors))
#     draw_shapes(shapes)

# # Make dashed lines
# for _ in range(15):
#     turtle.forward(10)
#     turtle.penup()
#     turtle.forward(10)
#     turtle.pendown()

# # Make a square
# for _ in range(4):
#     turtle.forward(100)
#     turtle.left(90)
#
screen = Screen()
screen.exitonclick()
