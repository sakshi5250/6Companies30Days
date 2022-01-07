class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def AreaOfRectangle(self):
        width = abs(self.x1-self.x2)
        height = abs(self.y1-self.y2)
        return width*height

    def AreaOfSharedRectangle(R1, R2):
        Shared_width = max(R1.x1, R2.x1)-min(R1.x2, R2.x2)
        Shared_height = max(R1.y1, R2.y1)-min(R1.y2, R2.y2)
        return Shared_width*Shared_height

    def CheckOverlapOrNot(R1, R2):
        if(R1.x1 > R2.x1 or R1.x2 > R2.x2):
            print("no overlap")
        elif(R1.y1 > R2.y1 or R1.y2 > R2.y2):
            print("no overlap")
        else:
            print("overlap")


R1 = Rectangle(0, 1, 1, 0)
R2 = Rectangle(1, 1, 2, 0)
print("Area of First Rectangle:", R1.AreaOfRectangle())
print("Area of Second Rectangle:", R2.AreaOfRectangle())
print("Area of Shared Rectangle:", Rectangle.AreaOfSharedRectangle(R1, R2))
print("Total Area Of Reactangle: ", R1.AreaOfRectangle() +
      R2.AreaOfRectangle()-Rectangle.AreaOfSharedRectangle(R1, R2))
Rectangle.CheckOverlapOrNot(R1, R2)
