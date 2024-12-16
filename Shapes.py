from math import pi

class Shape:
    pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def getr(self):
        return self.r
    def Area(self):
        return pi * self.r * self.r 
    def Circumference(self):
        return 2 * pi * self.r

class Triangle(Shape):
    def __init__(self, m, n, k):
        self.m = m
        self.n = n
        self.k = k
    def getm(self):
        return self.m
    def getn(self):
        return self.n
    def getk(self):
        return self.k
    def Perimeter(self):
        return self.m + self.n + self.k

class Quadrilateral(Shape):
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def geta(self):
        return self.a
    def getb(self):
        return self.b
    def getc(self):
        return self.c
    def getd(self):
        return self.d            

class Rectangle(Quadrilateral):
    def __init__(self, l, w):
        super().__init__(l, w, l, w)
    def getLength(self):
        return self.a
    def getWidth(self):
        return self.b
    def Perimeter(self):
        return 2 * (self.a + self.b)
    def Area(self):
        return self.a * self.b

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    def getSide(self):
        return self.a
    def Perimeter(self):
        return 4 * self.a
    def Area(self):
        return self.a * self.a

s = Square(5)
print(s.Area())

r = Rectangle(6, 8)
print(r.Perimeter())

q = Quadrilateral(4, 8, 1, 2)
print(q.getc())

c = Circle(10)
print(c.Area()) # 314
print(c.Circumference()) # 62.8

t = Triangle(3, 5, 8)
print(t.Perimeter())