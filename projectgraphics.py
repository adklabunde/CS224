# Class to handle the graphics
from graphics import *

class Plot():

    # Outputs a graphic window of the campus map image
    def get_window(self):
        win = GraphWin("route calculator", 800, 500)
        map_image = Image(Point(385, 110), 'map.gif')
        map_image.draw(win)
        return win

    # finds the corresponding x,y coords for each node number
    def find_coords(self, end=0):
        # list containing the window coordinates for each building
        node_coords = ((1, (110, 220)), (2, (90, 60)), (3, (215, 215)), (4, (205, 30)), (5, (150, 250)), (6, (545, 30)),
                       (7, (595, 35)), (8, (550, 75)),
                       (9, (215, 259)), (10, (560, 125)), (11, (490, 280)), (12, (495, 360)), (13, (525, 435)),
                       (14, (340, 325)), (15, (235, 342)), (16, (445, 260)),
                       (17, (450, 420)), (18, (10, 220)), (19, (385, 280)), (20, (620, 320)), (21, (320, 435)),
                       (22, (340, 240)), (23, (470, 213)), (24, (260, 135)),
                       (25, (475, 138)), (26, (150, 140)), (27, (395, 138)), (28, (390, 450)), (29, (435, 340)))
        if end == 0:
            for n in node_coords:
                if self.startnode == n[0]:
                    return n[1]
        else:
            for n in node_coords:
                if self.endnode == n[0]:
                    return n[1]

    # creates a rectangle
    def plot_point(self, coords):
        r = Rectangle(Point(coords[0], coords[1]), Point(coords[0] + 10, coords[1] + 10))
        r.setFill("white")
        return r

    # draws a rectangle in the window
    def draw_rec(self, rec, win):
        rec.draw(win)

    def __init__(self, p1, p2):
        self.startnode = p1
        self.endnode = p2
