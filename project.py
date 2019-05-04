#
# CS 224 Spring 2019
# Project
#
# Date: April 19, 2019
#
from graph import Graph
from projectgraphics import *
import heapq

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
    count = 0
    path_count = []
    dest_list = []
    colors = ['red', 'orange', 'blue', 'purple', 'green', 'yellow']
    win = get_window()
    for route in path:
        p = Plot(route)
        path_count.append(count)
        d = p.setuppath(win, colors[count], count)
        dest_list.append(d)
        count = count + 1
    if count != 0:
        p.add_key(win, path_count, dest_list)
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

# creates the start up window
def start_menu():
    win = GraphWin("start", 800, 500)
    win.setBackground('dark red')
    stripe = Rectangle(Point(0, 100), Point(800, 250))
    stripe.setFill('black')
    stripe.draw(win)
    t = Text(Point(400, 175), "START")
    t.setSize(20)
    t.setStyle('bold')
    t.setTextColor('white')
    t.draw(win)

    # get the student number and day from the user
    ui = Text(Point(400, 300), 'Please enter your student number: ')
    ui.draw(win)
    e = Entry(Point(580, 300), 10)
    e.draw(win)
    win.getMouse()
    st_num = e.getText()
    e.setFill('green')
    ui2 = Text(Point(400, 370), 'Enter the day: ')
    ui2.draw(win)
    e2 = Entry(Point(580, 370), 10)
    e2.draw(win)
    win.getMouse()
    day = e2.getText().lower()
    e2.setFill('green')

    # read in data from corresponding student number and day entered in text files
    lines = []
    try:
        student_num = "student" + st_num
        user_day = day.lower() + ".txt"
        fn = open("students/" + student_num + '/' + user_day, 'r')
        lines = fn.read().splitlines()
    except IOError:
        e.setFill('red')
        e2.setFill('red')
        e.setText('Invalid input')
        e2.setText('Invalid input')
    win.getMouse()
    win.close()
    return lines


def main():
    path_list = []
    campus_graph = Graph(get_graph())
    student_schedule = start_menu()
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

    daylist = []
    for path in path_list:
        daylist.append(path)
    set_window(daylist)

if __name__ == '__main__':
    main()
