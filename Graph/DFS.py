'''
white -> gray -> black
'''
class Vertex:
    def __init__(self, n):
        self.name = n
        self.neighbors = list()
        self.distance = 9999
        self.color = 'white'
        self.pred = None    # predecessor(parent)
        self.finish = None    # finish time for DFS

    def add_neighbor(self, v):    # v: name
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort()

class Graph:
    vertices = {}
    time = 0

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        
        else:
            return False

    def add_edge(self, u, v):     # u, v: name
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.add_neighbor(v)
                if key == v:
                    value.add_neighbor(u)
            return True
        else:
            return False

    def dfs(self, vertex):
        global time
        time = 0
        self.dfsVisit(vertex)

    def dfsVisit(self, u):
        global time
        u.color = 'gray'
        u.distance = time    # discovery time
        time += 1
        for v in u.neighbors:
            if self.vertices[v].color == 'white':
                self.vertices[v].pred = u
                self.dfsVisit(self.vertices[v])
        
        u.color = 'black'
        u.finish = time    # finish time
        time += 1

    def print_graph_dfs(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbors) + "  " + str(self.vertices[key].distance) + ' ' + str(self.vertices[key].finish))
    
def create_graph():
    g = Graph()
    a = Vertex('A')
    g.add_vertex(a)
    g.add_vertex(Vertex('B'))
    for i in range(ord('A'), ord('K')):
	    g.add_vertex(Vertex(chr(i)))

    edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
    for edge in edges:
	    g.add_edge(edge[:1], edge[1:])
    
    return g, a


g, a = create_graph()
g.dfs(a)
g.print_graph_dfs()