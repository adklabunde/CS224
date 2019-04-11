from collections import defaultdict

class Graph(object):

    def __init__(self, connections):
        self._graph = defaultdict(set)
        self._directed = False
        self.add_connections(connections)


    def add_connections(self, connections):
        for node1, node2 in connections:
            self.add(node1, node2)


    def add(self, node1, node2):
        self._graph[node1].add(node2)
        if not self._directed:
            self._graph[node2].add(node1)


    def find_path(self, start, finish, path=[]):
        path = path + [start]
        if start == finish:
            return path
        if start not in self._graph:
            return None
        for node in self._graph[start]:
            if node not in path:
                new_path = self.find_path(node, finish, path)
                if new_path:
                    return new_path
        return None


    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))
