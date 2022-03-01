class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other_point):
        return ((other_point.x - self.x) ** 2 + (other_point.y - self.y) ** 2) ** 0.5

class Triangle:
    def __init__(self,p1,p2,p3):
        self.point1 = p1
        self.point2 = p2
        self.point3 = p3
    def perimetr(self):
        a = self.point1.distance(self.point2)
        b = self.point2.distance(self.point3)
        c = self.point3.distance(self.point1)
        return a + b + c
    def area(self):
        a = self.point1.distance(self.point2)
        b = self.point2.distance(self.point3)
        c = self.point3.distance(self.point1)
        p = (a + b + c) / 2
        s = (p - a) * (p - b) * (p - c) ** 0.5
        return s


triangle1 = Triangle(Point(1, 9), Point(12,-4), Point(-10, -8))
triangle2 = Triangle(Point(50, 6), Point(2357,-90), Point(-320, -8976))

print("Периметр первого треугольника = ",triangle1.perimetr())
print("Плащадь первого треугольника = ",triangle1.area())
print("Периметр второго треугольника = ",triangle2.perimetr())
print("Плащадь второго треугольника = ",triangle2.area())


