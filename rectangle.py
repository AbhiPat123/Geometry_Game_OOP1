class Rectangle:

    def __init__(self, lower_left, upper_right):
        self.lower_left = lower_left
        self.upper_right = upper_right

    def area(self):
        return (self.upper_right.x - self.lower_left.x) * \
        (self.upper_right.y - self.lower_left.y)