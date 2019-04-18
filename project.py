#
# CS 224 Spring 2019
# Project
#
#
# Date: March 24, 2019
#
from graph import Graph
from projectgraphics import *

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

def set_window(path):
    p = Plot(path)
    win = p.get_window()
    p.setuppath(win)
    win.getMouse()          # click anywhere in the window to close
    win.close()

def main():
    campus_graph = Graph(get_graph())
    schedule = read_schedule()
    paths = [(p[0], p[1]) for p in [path.split() for path in schedule]]
    for p in paths:
        print campus_graph.find_path(p[0], p[1])

    # still have to plug in the number from the students file
    path1 = [2, 26, 5]
    set_window(path1)
    path2 = {14, 19, 16}
    set_window(path2)

if __name__ == '__main__':
    main()
