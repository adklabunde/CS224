# Class to handle the graphics
from graphics import *

class Plot():

    # finds the corresponding x,y coords for each node number
    def find_coords(self, curnode):
        # list containing the window coordinates for each building
        node_coords = ((1, (110, 220)), (2, (90, 60)), (3, (215, 215)), (4, (205, 30)), (5, (150, 250)), (6, (545, 30)),
                       (7, (595, 35)), (8, (550, 75)), (9, (215, 259)), (10, (560, 125)), (11, (490, 280)),
                       (12, (495, 360)), (13, (525, 435)), (14, (340, 325)), (15, (235, 342)), (16, (445, 260)),
                       (17, (450, 420)), (18, (10, 220)), (19, (385, 280)), (20, (620, 320)), (21, (320, 435)),
                       (22, (340, 240)), (23, (470, 213)), (24, (260, 135)), (25, (475, 138)), (26, (150, 140)),
                       (27, (395, 138)), (28, (390, 450)), (29, (435, 340)), (30, (275, 190)), (31, (280, 285)),
                       (32, (390, 200)), (33, (280, 380)), (34, (390, 380)), (35, (530, 285)), (36, (510, 130)))
        for n in node_coords:
            if curnode == n[0]:
                return n[1]

    # creates a rectangle
    def draw_rec(self, coords, win):
        r = Rectangle(Point(coords[0], coords[1]), Point(coords[0] + 10, coords[1] + 10))
        r.setFill("white")
        r.draw(win)
        return r

    def draw_line(self, p1, p2, win):
        line = Line(Point(p1[0], p1[1]), Point(p2[0], p2[1]))
        line.setWidth(3)
        line.setFill("red")
        line.draw(win)

    # sets up
    def setuppath(self, win):
        count = 0
        for n in self.path:
            p1 = self.find_coords(n)
            if p1 != None:
                self.draw_rec(p1, win)
                if count != 0:
                    self.draw_line(p1, p2, win)
                p2 = p1
                count = count + 1

    def __init__(self, path):
        self.path = path
