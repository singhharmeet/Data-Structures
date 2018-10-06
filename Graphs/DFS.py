from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def insert(self,u,v):
        self.graph[u].append(v)
        print(self.graph[u])
        
    # function for traversal of graph from given starting node
    def traverse(self,v,visited):
        visited[v] = True
        print(v)
        
        for i in self.graph[v]:
            if visited[i] == False:
                self.traverse(i, visited)
                
    def DFS(self, v):
        visited = [False]*(len(self.graph))
        self.traverse(v, visited)
        
g = Graph()
g.insert(0,1)
g.insert(0,2)
g.insert(1,2)
g.insert(2,0)
g.insert(2,3)
g.insert(3,3)

g.DFS(0)



