import os; os.system('clear')
print("-"*30, f'| {__file__.split("/")[-1]} |', "-"*30, '\n')

class Graph:
    def __init__(self, gTotalNode):
        self.gTotalNode = gTotalNode
        self.vertices = {}

    def addEdge(self, u, v):
        if u not in self.vertices:
            self.vertices[u] = []
        self.vertices[u].append(v)

def recusive_func(graph, node, visited):
    if node in visited:
        return 
    visited.add(node)
    print(f'Current Node -> {node}')
    if node in graph.vertices:
        for edges in graph.vertices[node]:
            recusive_func(graph, edges, visited)


def DFS(graph):
    visited = set()
    return recusive_func(graph, 0, visited)

# Create a graph given in the above diagram 
myGraph = Graph(6) 
myGraph.addEdge(0, 1) 
myGraph.addEdge(1, 2) 
myGraph.addEdge(1, 3) 
myGraph.addEdge(2, 4) 
myGraph.addEdge(3, 4) 
myGraph.addEdge(3, 5) 

print(myGraph.vertices)
DFS(myGraph)
