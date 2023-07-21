class Graph():
    def __init__(self,nodes):
        pass
    
    def add_edge(self, start, end):
        pass


g = Graph(8)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(3, 0)
g.add_edge(4, 5)
g.add_edge(5, 6)
g.add_edge(6, 4)
g.add_edge(6, 7)



def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start)

    for next in graph[start]:
        if next not in visited:
            dfs(graph, next, visited)

graph = {'0': ['1', '2'],
         '1': ['0', '3', '4'],
         '2': ['0'],
         '3': ['1'],
         '4': ['2', '3']}

dfs(graph, '0')