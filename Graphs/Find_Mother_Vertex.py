from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
    
    def insert(self,u,v):
        self.graph[u].append(v)
    
    def traverse(self, v, visited):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                self.traverse(i, visited)
                
    def findMotherVertex(self):
        mv = []
        visited = [False]*(self.V)
        
        v = 0
        for i in range(self.V):
            if visited[i] == False:
                self.traverse(i, visited)
                v = i
                
        visited = [False]*(self.V)
        self.traverse(v, visited)
        if all(i == True for i in visited):
            mv.append(v)
            
        if len(mv)>0:
            return mv
        else:
            return -1
            
            
g = Graph(7)
g.insert(0,1)
g.insert(0,2)
g.insert(1,3)
g.insert(4,1)
g.insert(6,4)
g.insert(5,6)
g.insert(5,2)
g.insert(6,0)
 
print(g.findMotherVertex())

g = Graph(4)
g.insert(2,1)
g.insert(2,0)
g.insert(1,2)
g.insert(0,2)
g.insert(0,3)
g.insert(3,3)

print(g.findMotherVertex())
