import sys
sys.path.append(r"C:\Documents\GitHub\Data-Structure-and-Algorithms")
from Graph.DFS import Vertex, Graph

def create_graph():
    g = Graph()
    for i in range(ord('A'), ord('K')):
	    g.add_vertex(Vertex(chr(i)))

    edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
    for edge in edges:
	    g.add_edge(edge[:1], edge[1:])
    
    return g, g.vertices['A']

def topo_sort():
    g, a = create_graph()
    g.dfs(a)
    tasks = {}
    tasks_order = []
    for key in list(g.vertices.keys()):
        tasks[g.vertices[key].finish] = key
    
    for i in sorted(tasks):
        tasks_order.insert(0, tasks[i])
    
    return tasks_order

print(topo_sort())