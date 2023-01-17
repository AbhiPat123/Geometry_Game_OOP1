print("Running main.py ...")

# MODULE IMPORTS
import turtle
from random import randint


# CLASS DEFINITONS
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.point1.x < self.x < rectangle.point2.x \
                and rectangle.point1.y < self.y < rectangle.point2.y:
            return True
        else:
            return False

    def distance_from_point(self, point):
        if self.x == point.x:
            return abs(point.y - self.y)
        elif self.y == point.y:
            return abs(point.x - self.x)
        else:
            x_dist_sqrd = (self.x - point.x) ** 2
            y_dist_sqrd = (self.y - point.y) ** 2
            return (x_dist_sqrd + y_dist_sqrd) ** 0.5


class Rectangle:

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return (self.point2.x - self.point1.x) * \
            (self.point2.y - self.point1.y)


class RectangleGraphics(Rectangle):

    def draw(self, canvas):
        print("Drawing rectangle ...")
        canvas.hideturtle()
        canvas.penup()
        canvas.goto(self.point1.x, self.point1.y)
        canvas.pendown()

        # get rectangle height and width
        rect_width = abs(self.point1.x - self.point2.x)
        rect_height = abs(self.point1.y - self.point2.y)

        # do steps to draw a rectangle
        canvas.forward(rect_width)
        canvas.left(90)
        canvas.forward(rect_height)
        canvas.left(90)
        canvas.forward(rect_width)
        canvas.left(90)
        canvas.forward(rect_height)
        canvas.left(90)

        print("... rectangle drawn!")


rectangle_graphics = RectangleGraphics(Point(randint(0, 100), randint(0, 100)), \
                                       Point(randint(150, 250), randint(150, 250)))
myturtle = turtle.Turtle()
rectangle_graphics.draw(myturtle)
turtle.done()

# # RUNNING GAME CODE
# while True:
#     # Guess coordinates
#     rectangle = Rectangle(Point(randint(0, 400), randint(0, 400)), \
#                           Point(randint(10, 400), randint(10, 400)))
#     print("Rectangle Coordinates:", rectangle.point1.x, rectangle.point1.y, "and", \
#           rectangle.point2.x, rectangle.point2.y)
#
#     user_point = Point(float(input("Guess X: ")), float(input("Guess Y: ")))
#
#     print("Is your point in rectangle? -", user_point.falls_in_rectangle(rectangle))
#
#     # Guess area
#     user_area = float(input("Guess Rectangle Area: "))
#
#     guess_diff = round(abs(rectangle.area() - user_area))
#     print("Your area value guess is", int(user_area), "off by", guess_diff)
#     if guess_diff == 0:
#         print("Great, on the point!")
#
#     user_game_input = input("Run once more?: (y/n)")
#     if user_game_input == 'n':
#         break

# myturtle = turtle.Turtle()
# go_to_point = (100,50)
# myturtle.hideturtle()
# myturtle.penup()
# myturtle.goto(go_to_point[0], go_to_point[1])
# myturtle.pendown()
#
# # do steps to draw a rectangle
# myturtle.forward(100)
# myturtle.left(90)
# myturtle.forward(50)
# myturtle.left(90)
# myturtle.forward(100)
# myturtle.left(90)
# myturtle.forward(50)
# myturtle.left(90)
#
# turtle.done()


# from point import Point
# from rectangle import Rectangle
#
# def draw_rectangle(trtl, lower_left, upper_right):
#     # get rectangle height and width
#     rect_width = abs(upper_right.x - lower_left.x)
#     rect_height = abs(upper_right.y - lower_left.y)
#
#     # hide the turtle cursor and go to lower left point (with penup)
#     trtl.hideturtle()
#     trtl.penup()
#     trtl.goto(lower_left.x, lower_left.y)
#     trtl.pendown()
#
#     # do steps to draw a rectangle
#     trtl.forward(rect_width)
#     trtl.left(90)
#     trtl.forward(rect_height)
#     trtl.left(90)
#     trtl.forward(rect_width)
#     trtl.left(90)
#     trtl.forward(rect_height)
#     trtl.left(90)
#
#     turtle.done()
#
# myturtle = turtle.Turtle()
# draw_rectangle(myturtle, lower_left, upper_right)
