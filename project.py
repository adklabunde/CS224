#
# CS 224 Spring 2019
# Project
#
# Date: April 19, 2019
#
from graph import Graph
from projectgraphics import *
import heapq

# Get student number and day of the week
# Read the schedule from the txt file pertaining to the day provided
def read_schedule():
    student_num = "student" + raw_input("Student Number: ")
    student_day = raw_input("Day: ").lower() + ".txt"
    fn = open("students/" + student_num + '/' + student_day, 'r')
    schedule_lines = fn.read().splitlines()
    return schedule_lines

# Read in the graph paths
# Return a tuple with (start, finish, weight)
def get_graph():
    fn = open('campus_graph.txt', 'r')
    graph_lines = fn.read().splitlines()
    path_tuples = [(line[0], line[1], int(line[2])) for line in [path.split() for path in graph_lines]]
    return path_tuples

# Outputs a graphic window of the campus map image
def get_window():
    win = GraphWin("route calculator", 800, 500)
    map_image = Image(Point(385, 110), 'map.gif')
    map_image.draw(win)
    return win

# sets up graphics
def set_window(path):
    win = get_window()
    p = Plot(path)
    p.setuppath(win)
    win.getMouse()          # click anywhere in the window to close
    win.close()

# Get the shortest path from the chain of v.previous
# Append to return list
# Will be in opposite order
def get_shortest_path(v, path):
    if v.previous:
        path.append(v.previous.get_id())
        get_shortest_path(v.previous, path)
    return

# Build the shortest path from start to target
# Path is save in each vertex
def build_shortest_path(graph, start, target):
    # Need to reset the previous and distance values on vertices
    graph.reset_verts()

    # Set the distance for the start node to zero
    start.set_distance(0)

    # Put tuple pair into the priority queue
    unvisited_queue = [(v.get_distance(),v) for v in graph]
    heapq.heapify(unvisited_queue)

    while len(unvisited_queue):
        # Pops a vertex with the smallest distance
        uv = heapq.heappop(unvisited_queue)
        current = uv[1]
        current.set_visited()

        #for next in v.adjacent:
        for next in current.adjacent:
            # if visited, skip
            if next.visited:
                continue
            new_dist = current.get_distance() + current.get_weight(next)

            if new_dist < next.get_distance():
                next.set_distance(new_dist)
                next.set_previous(current)

        # Rebuild heap
        # 1. Pop every item
        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
        # 2. Put all vertices not visited into the queue
        unvisited_queue = [(v.get_distance(),v) for v in graph if not v.visited]
        heapq.heapify(unvisited_queue)


def main():
    path_list = []
    campus_graph = Graph(get_graph())
    student_schedule = read_schedule()
    student_path = [(p[0], p[1]) for p in [path.split() for path in student_schedule]]

    for path in student_path:
        start = campus_graph.get_vertex(path[0])
        finish = campus_graph.get_vertex(path[1])
        user_route = [finish.get_id()]

        # Run Dijkstra's shortest path algorithm
        build_shortest_path(campus_graph, start, finish)
        get_shortest_path(finish, user_route)

        # Reverse the order of the path
        user_route = list(reversed(user_route))

        # Save all points on path as ints
        user_route = map(int, user_route)

        path_list.append(user_route)

    for path in path_list:
        #print path
        set_window(path)

if __name__ == '__main__':
    main()
