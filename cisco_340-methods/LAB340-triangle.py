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
        return math.hypot(abs(self.__x - x), abs(self.__y - y))
    
    def distance_from_point(self, point):
        return self.distance_from_xy(point.getx(), point.gety())


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        if not isinstance(vertice1, Point) or \
            not isinstance(vertice2, Point) or \
            not  isinstance(vertice3, Point):
            print("Wrong points data")
            raise ValueError
        self.__triangle = [vertice1, vertice2, vertice3]

    def perimeter(self):
        AB = self.__triangle[0].distance_from_point(self.__triangle[1])
        BC = self.__triangle[1].distance_from_point(self.__triangle[2])
        CA = self.__triangle[2].distance_from_point(self.__triangle[0])
        return AB + BC + CA


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
    