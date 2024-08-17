import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        distance = ((self.__x - x) ** 2 + (self.__y - y) ** 2) ** 0.5
        return distance

    def distance_from_point(self, point):
        distance = ((self.__x - point.getx()) ** 2 + (self.__y - point.gety()) ** 2) ** 0.5
        return distance


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__vertices = [vertice1, vertice2, vertice3]

    def perimeter(self):
        total = 0
        for i in range(len(self.__vertices)):
            total += self.__vertices[i].distance_from_point(self.__vertices[i - 1])
        return total


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
