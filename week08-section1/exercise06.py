class Circle:
    def __init__(self, x,y,radius,color):
        self.radius = radius
        self.color = color
        self.x = x
        self.y = y

    def __str__(self):
        return f'Circle({self.x},{self.y},{self.radius},{self.color})'

    def __lt__(self,other):
        return self.radius < other.radius
circle1 = Circle(100,100,50,'red')
print(circle1)
print(str(circle1))
circle2 = Circle(100,100,250,'blue')
print(circle1 < circle2)