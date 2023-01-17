# Class naming:
#   1. Capital in beginning
#   2. Camel Case
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # name the methods starting with verbs
    # when calling this it looks like point1.falls_in_rectangle() - more readable
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