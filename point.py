# Class naming:
#   1. Capital in beginning
#   2. Camel Case
class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # name the methods starting with verbs
    # when calling this it looks like point1.falls_in_rectangle() - more readable
    def falls_in_rectangle(self, lower_left, upper_right):
        if lower_left[0] < self.x < upper_right[0] \
        and lower_left[1] < self.y < upper_right[1]:
            return True
        else:
            return False

    def distance_from_point(self, x2, y2):
        if self.x == x2:
            return abs(y2-self.y)
        elif self.y == y2:
            return abs(x2-self.x)
        else:
            x_dist_sqrd = (self.x - x2)**2
            y_dist_sqrd = (self.y - y2)**2
            return (x_dist_sqrd + y_dist_sqrd)**0.5