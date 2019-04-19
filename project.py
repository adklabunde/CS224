#
# CS 224 Spring 2019
# Project
#
#
# Date: April 19, 2019
#
from graph import Graph
from projectgraphics import *

# Get student number and day of the week
def read_schedule():
    student_num = "student" + raw_input("Student Number: ")
    user_day = raw_input("Day: ").lower() + ".txt"
    fn = open("students/" + student_num + '/' + user_day, 'r')
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
    student_path = [(p[0], p[1]) for p in [path.split() for path in schedule]]
    for path in student_path:
        user_route = campus_graph.find_path(path[0], path[1])
        user_route = map(int, user_route)
        print user_route
        set_window(user_route)

    #path1 = [2, 26, 5]
    #print path1
    #set_window(path1)
    #path2 = [14, 19, 16]
    #set_window(path2)

if __name__ == '__main__':
    main()
