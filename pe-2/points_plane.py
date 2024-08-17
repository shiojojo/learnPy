import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def distance_from_xy(self, x, y):
        distance = ((self.x - x) ** 2 + (self.y - y) ** 2) ** 0.5
        return distance

    def distance_from_point(self, point):
        distance = ((self.x - point.getx()) ** 2 + (self.y - point.gety()) ** 2) ** 0.5
        return distance


point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))
