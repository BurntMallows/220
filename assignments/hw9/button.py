"""
Name: <Queen Hamilton, II>
<button>.py

Problem: This program creates a button

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""


from graphics import Text


class Button:
    """ This class creates a button object """
    def __init__(self, shape, label):
        self.shape = shape
        center_p = self.shape.getCenter()
        self.text = Text(center_p, label)

    def get_label(self):
        """Returns the chracters of a text object as a string data type"""
        return self.text.getText()

    def draw(self, win):
        """Draws the button object onto a graphical window"""
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        """Un-draws the button object from a graphical window"""
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        """Returns a Boolean value depicting whether or not the button object was clicked"""
        point_x = point.getX()
        point_y = point.getY()
        shape_p1 = self.shape.getP1()
        shape_p1_x = shape_p1.getX()
        shape_p1_y = shape_p1.getY()
        shape_p2 = self.shape.getP2()
        shape_p2_x = shape_p2.getX()
        shape_p2_y = shape_p2.getY()
        return shape_p1_x <= point_x <= shape_p2_x and shape_p1_y <= point_y <= shape_p2_y

    def color_button(self, color):
        """Completely shades the interior of the button object to whatever you select
        All buttons are originally white"""
        self.shape.setFill(color)

    def set_label(self, label):
        """Sets the graphical text equal to what you choose"""
        self.text.setText(label)
