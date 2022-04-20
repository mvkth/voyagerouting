class Node:
    def __init__(self, position, neighbors, current, height):
        self.position = position
        self.neighbors = neighbors # KEY is direction, VALUE is position of neighbor
        self.current = current
        self.height = height

    def get_position(self):
        return (self.position)

    def get_current(self):
        return self.current

    def get_height(self):
        return self.height

    def get_neighbors(self):
        return self.neighbors

    def set_current(self, current):
        self.current = current

    def set_height(self, height):
        self.height = height

    def print_node(self):
        print(self.position)
        print(f'\tneighbors: {self.neighbors}')
        print(f'\tcurrent: {self.current}')
        print(f'\theight: {self.height}')

class NodeMap:
    @staticmethod
    def generate_nodes(points, neighbors, weather):
        if not neighbors:
            print('No connected points')
            return
        nodes = {}
        points = sum(points,[]) # flatten points since it is a 2d array
        neighbors = neighbors
        weather = weather
        for p in points:
            if p:
                if neighbors[p]:
                    n = neighbors[p]
                    c = None
                    h = None
                    if(weather[p]):
                        if(weather[p]['current']):
                            c = weather[p]['current']
                        if(weather[p]['height']):
                            h = weather[p]['height']
                    nodes[p] = Node(p, n, c, h)
        return nodes

    @staticmethod
    def show_nodes(nodes):
        for node in nodes.values():
            node.print_node()