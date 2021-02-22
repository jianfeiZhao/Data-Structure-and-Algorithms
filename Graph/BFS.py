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

    def print_graph_bfs(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbors) + "  " + str(self.vertices[key].distance))
    
    def bfs(self, s):
        q = list()
        s.distance = 0
        s.color = 'gray'
        q.append(s.name)
        while len(q) > 0:
            u = q.pop(0)
            for v in self.vertices[u].neighbors:
                if self.vertices[v].color == 'white':
                    self.vertices[v].color = 'gray'
                    self.vertices[v].distance = self.vertices[u].distance + 1
                    self.vertices[v].pred = self.vertices[u]
                    q.append(v)
                
            self.vertices[u].color = 'black'

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
g.bfs(a)
g.print_graph_bfs()