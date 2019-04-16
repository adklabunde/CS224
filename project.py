#
# CS 224 Spring 2019
# Project
#
#
# Date: March 24, 2019
#
from graph import Graph
from graphics import *

def read_schedule():
    day = "monday.txt"
    student_num = "student" + "1";
    fn = open("students/" + student_num + '/' + day, 'r')
    lines = fn.read().splitlines()
    return lines

# The input file for the graph is in the form of:
# place1 place2 distance
# where distance is in minutes
def get_graph():
    fn = open('campus_graph.txt', 'r')
    lines = fn.read().splitlines()
    tuples = [(l[0], l[1]) for l in [line.split() for line in lines]]
    return tuples

# Outputs a graphic window of the campus map image
def get_window():
    win = GraphWin("gps", 800, 500)
    map_image = Image(Point(385, 110), 'map.gif')
    map_image.draw(win)
    win.mainloop()

def main():
    campus_graph = Graph(get_graph())
    schedule = read_schedule()
    paths = [(p[0], p[1]) for p in [path.split() for path in schedule]]
    for p in paths:
        print campus_graph.find_path(p[0], p[1])

if __name__ == '__main__':
    main()
