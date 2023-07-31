class Graph():
    def __init__(self,nodes=None):
        self.graph = {}
        if nodes is None:
            pass
        else:
            for node in nodes:
                self.add_edge(*node)
    
    def add_edge(self, start, end):
        if start not in self.graph.keys():
            self.graph[start] = [end]
        elif end not in self.graph[start]:
            self.graph[start].append(end)

        if end not in self.graph.keys():
            self.graph[end] = []

    def del_edge(self, start, end):
        if start not in self.graph.keys() or end not in self.graph[start]:
            print("invalid delete")
            return
        elif len(self.graph[start]) == 1:
            del self.graph[start]
        else:
            self.graph[start].remove(end)

    def dfs(self, start):
        dfs_seq = [start]
        stack = [start]
        
        while stack:
            curr = stack[0]
            dfs_seq.append(stack[0])
            stack.remove(stack[0])
            this_layer = []
            for next in self.graph[curr]:
                if next not in dfs_seq and next not in stack and next not in this_layer:
                    this_layer.append(next)
            stack = this_layer + stack
            
        print("->".join(list(map(str, dfs_seq))))

    def bfs(self, start):
        bfs_seq = []
        queue = [start]

        while queue:
            curr = queue[0]
            bfs_seq.append(queue[0])
            queue.remove(queue[0])
            for next in self.graph[curr]:
                if next not in bfs_seq and next not in queue:
                    queue.append(next)
            
        print("->".join(list(map(str, bfs_seq))))


    def tranverse(self):
        for k, v in self.graph.items():
            print(str(k) + ": "+ str(v) )
        

# test cases
#g = Graph([(0, 1), (2, 0)])
#g.add_edge(4, 3)
#g.add_edge(4, 2)
#g.add_edge(1, 0)
#g.add_edge(0, 2)
#g.add_edge(1, 3)
#g.add_edge(3, 1)
#g.add_edge(1, 4)
#g.tranverse()
# output:{'0': ['1', '2'],
#         '1': ['0', '3', '4'],
#         '2': ['0'],
#         '3': ['1'],
#         '4': ['2', '3']}
#g.dfs(0)
# output: 0->1->3->4->2
#g.bfs(0)
# output: 0->1->2->3->4 
#g.del_edge(4,2)
#g.tranverse()
