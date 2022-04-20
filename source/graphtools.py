from source.vectortools import VectorTools
from source.priorityqueue import PriorityQueue, Entry

# default velocity for ship in kph
VELOCITY = 25.0

def generate_vertices(nodes):
    # returns dictionary where KEY is position of vertex and VALUE is list of adjacent vertices
    vertices = {}
    for key, node in nodes.items():
        vertices[key] = list(node.neighbors.values())
    return vertices

def generate_edges(nodes):
    # returns dictionary where KEY is tuple of (origin, destination) nodes and VALUE is time to cross edge
    edges = {}
    for node in nodes.values():
        for direction, position in node.neighbors.items():
            neighbor = nodes[position]
            key = (node.position, neighbor.position)
            distance = VectorTools.distance(node.position, neighbor.position)
            current = VectorTools.sum_current(node.current, neighbor.current)
            height = VectorTools.sum_height(node.height, neighbor.height)
            delta = VectorTools.delta(current, direction, height)
            velocity = VELOCITY + delta
            time = distance / velocity
            edges[key] = time
    return edges

class Path:
    def __init__(self, position):
        self.position = position
        self.cost = float('inf')
        self.prev = None

    def setCost(self, cost):
        self.cost = cost
    
    def setPrev(self, prev):
        self.prev = prev

    def getPos(self):
        return self.position

    def getCost(self):
        return self.cost
    
    def getPrev(self):
        return self.prev

    def startHere(self):
        self.cost = 0

    @staticmethod
    def generate_path(PATHS, point):
        # accepts dictionary of PATHS and generates list of segments from point to start
        path = []
        current = PATHS[point]
        cost = current.getCost()
        while current.getPrev():
            path.append((current.getPos(),current.getPrev()))
            current = PATHS[current.getPrev()]
        return path


class Graph:
    def __init__(self, nodes):
        self.vertices = generate_vertices(nodes)
        self.edges = generate_edges(nodes)

    def show_vertices(self):
        for key, val in self.vertices.items():
            print(f'NODE {key} has NEIGHBORS\n\t {val}')

    def show_edges(self):
        for key, neighbors in self.vertices.items():
            print(f'ORIGIN: {key}')
            for neighbor in neighbors:
                print(f'\tto {neighbor} has value {self.edges[(key, neighbor)]}')
    
    def dijkstra(self, start):
        # returns dictionary PATHS where KEY is coordinate point and VALUE is PATH object with COST and PREV point
        PATHS = {}
        VERTICES = self.vertices.keys()
        VISITED = []
        # initiate paths table
        for vertex in VERTICES:
            PATHS[vertex] = Path(vertex)
        # initialize start node
        PATHS[start].startHere()
        # initialize priority queue
        Q = PriorityQueue()
        Q.insert(Entry(start, PATHS[start].getCost()))
        prev = start
        while not Q.isEmpty():
            current = Q.pop_min().getName()
            if current not in VISITED:
                for neighbor in self.vertices[current]:
                    cost = self.edges[(current, neighbor)] + PATHS[current].getCost()
                    if(cost < PATHS[neighbor].getCost()):
                        PATHS[neighbor].setCost(cost)
                        PATHS[neighbor].setPrev(current)
                        Q.insert(Entry(neighbor, PATHS[neighbor].getCost()))
                VISITED.append(current)
        for k, v in PATHS.items():
            print(k, vars(v))
        return PATHS