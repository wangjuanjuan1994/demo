class shape:
        
    def __init__(self,x,y):
        self.x = x

        self.y = y

        def area(self):

            pass

class Circle(shape):
    
    def __init__(self,r):

        shape.__init__(self,r,0)
    def area(self):

        return 3.14*self.x*self.x
class Rectangle(shape):

    def __init__(self,w,h):
        
        shape.__init__(self,w,h)

    def area(self):

        return self.x*self.y

class Ellipse(shape):

    def __init__(self,a,b):

        shape.__init__(self,a,b)

    def area(self):

        return 3.14*self.x*self.y

class Square(shape):

    def __init__(self,s):

        shape.__init__(self,s,0)

    def area(self):

        return self.x*self.x

def compute_area(shapes):
    s = 0
    for i in range(0,7):
        s += shapes[i].area()
    
    return s
     

def main():
    
    shapes = [Ellipse(10,20),Square(15),Circle(5),Rectangle(20,15),Circle(5),Square(15),Ellipse(10,20)]

    total_area = compute_area(shapes)

    print(total_area)


main()
    
