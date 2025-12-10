class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def printPoint(self):
        print(f"Point has coordinates: {self.x}, {self.y}")

    
    def isEqual(self, otherPoint):
        if self.x == otherPoint.x and self.y == otherPoint.y:
            return True
        else:
            return False
        
    
    def distance(self, otherPoint):
        return ((self.x - otherPoint.x)**2 + (self.y - otherPoint.y)**2) ** 0.5
    
p1 = Point(0, 0)
p2 = Point(3, 4)
print("Distance:", p1.distance(p2)) 



class Vector(Point):
    def __init__(self, x, y):
        super().__init__(x, y)

    def __str__(self):
        return f"Vector has a point with x= {self.x} and y= {self.y}"

    def __add__(self, otherPoint):
        return Vector(self.x + otherPoint.x, self.y + otherPoint.y)
    
v1 = Vector(5, 1)
v2 = Vector(2, 3)


print("Vector 1:", v1)                
print("Vector 2:", v2)                  
print(v1 + v2) 