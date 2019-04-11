#
# CS 224 Spring 2019
# Project
#
#
# Date: March 24, 2019
#
import math
from graph import Graph
from graphics import *

def read_schedules():
    file = "student1.txt"
    fn = open("students/" + file, 'r')
    lines = fn.read().splitlines()
    return lines


# takes in the start and end points of two x,y coordinates and returns the distance in meters
def calc_distance(startpoint, endpoint):
    x = startpoint[0] - endpoint[0]
    y = startpoint[1] - endpoint[1]
    distance = math.sqrt(x**2 + y**2)
    # convert to kilometers using radius of earth 6371*pi/180 (108)
    distance = distance * 108
    # convert to meters
    distance = distance * 1000
    return distance

# calculates the amount of time it will take to travel a certain distance in meters
# 90 meters = 1 minute
def calc_time(distance):
    totalminutes = distance / 90
    return totalminutes

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
    schedule = read_schedules()
    paths = [(p[0], p[1]) for p in [path.split() for path in schedule]]
    for p in paths:
        print campus_graph.find_path(p[0], p[1])

if __name__ == '__main__':
    main()
