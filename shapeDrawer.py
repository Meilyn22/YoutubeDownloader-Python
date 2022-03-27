#Import turtle

import turtle

#Polygon class contains the name of the shape, sides, size and color.
#It also does the calculation according to geometry on how to draw shapes.
class Polygon:
    def __init__(self, sides, name, size=100):
        self.sides = sides
        self.name = name
        self.size = size
        self.interior_angles = (self.sides-2)*180
        self.angle = self.interior_angles/self.sides

#Inherits from the Polygon class and adds the methods. Draw and About.
#It adds information about the shape. Add colors to the shape.
class About(Polygon):
    def __init__(self, sides, name, color, about={}):
        Polygon.__init__(self, sides, name)
        self.about = about
        self.color = color
#Draws the shapes, writes the text and adds colors to them.
    def draw(self):
        turtle.color(self.color)
        turtle.write(self.about_shape()[self.name])
        for i in range(self.sides):
            turtle.forward(100)
            turtle.right(180-self.angle)
        turtle.done()
       
#Gives information about the shape.
    def about_shape(self):
        self.about = {
        "Square": """
        The square has 4 equal sides.
        """,
        "Pentagon": """
        The Pentagon has 5 sides.
        """,
        "Hexagon": """
        The Hexagon has 6 sides.
        """
        }

        return self.about

#Instances of our class
square = About(4, "Square", "blue")
pentagon = About(5, "Pentagon", "red")
hexagon = About(6, "Hexagon", "green")

# Run our methods.
#square.draw()
#pentagon.draw()
hexagon.draw()
