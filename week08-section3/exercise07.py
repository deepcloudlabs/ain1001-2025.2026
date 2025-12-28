class Circle:
    def __init__(self, x,y,radius,color):
        self.radius = radius
        self.color = color
        self.x = x
        self.y = y

    def __str__(self):
        return f'Circle(x: {self.x},y: {self.y},radius: {self.radius},color: {self.color})'

    def __lt__(self, other):
        return self.radius < other.radius

c1 = Circle(1,2,30,'red')
c2 = Circle(10,-20,200,'blue')
print(c1 < c2)
print(str(c1))
