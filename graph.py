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


    def find_path(self, node1, node2, path=[]):
        path = path + [node1]
        if node1 == node2:
            return path
        if node1 not in self._graph:
            return None
        for node in self._graph[node1]:
            if node not in path:
                new_path = self.find_path(node, node2, path)
                if new_path:
                    return new_path
        return None


    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))
