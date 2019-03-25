#
# CS 224 Spring 2019
# Project
#
#
# Date: March 24, 2019
#

def read_schedule(filename):
    fn = open(filename, 'r')
    lines = fn.readlines()
    return lines

# The input file for the graph is in the form of:
# place1 place2 distance
# where distance is in minutes
def get_graph():
    fn = open('campus_graph.txt', 'r')
    lines = fn.readlines()
    return lines

spots = get_graph()

print spots
