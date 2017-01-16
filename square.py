from rectangle import Rectangle
class Square(Rectangle) :
    def __init__(self,length):
        super(Square,self).__init__(length,length)
    def set_hight(self,new_height):
        super(Square,self).set_height(new_height)
        super(Square,self).set_length(new_height)


'''
self.turtle.clear
self.turtle.penup()
self.turtle.goto(0,0)
self.turtle.pendown()
self.turtle.goto(self.length,0)
self.turtle.goto(self.length,self.height)
self.turtle.goto(0,self.height)
self.turtle.goto(0,0)
self.turtle.penup()
self.has_been_drawn=True
'''
