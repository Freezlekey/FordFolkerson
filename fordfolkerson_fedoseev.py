graph = [
    [0, 30, 40, 20, 0],
    [0, 0, 50, 0, 40],
    [0, 0, 0, 20, 30],
    [0, 0, 0, 0, 30],
    [0, 0, 0, 0, 0]
]

source = 0
sink = 4

class FordFulkerson:
    def init(self, graph):
        self.graph = graph
        self.ROW = len(graph)

    def ford_fulkerson(self, source, sink):
        parent = [-1] * (self.ROW)
        max_flow = 0

        while self.bfs(source, sink, parent): 
            path_flow = float('inf') 
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s]) 
                s = parent[s]

            max_flow += path_flow

            v = sink
            while v != source:
                u = parent[v] 
                self.graph[u][v] -= path_flow 
                self.graph[v][u] += path_flow 
                v = u

        return max_flow

    def bfs(self, source, sink, parent):
        visited = [False] * (self.ROW)
        queue = [source]
        visited[source] = True
        while queue: 
            u = queue.pop(0)
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] is False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return True if visited[sink] else False

ford_fulkerson = FordFulkerson(graph)

max_flow = ford_fulkerson.ford_fulkerson(source, sink)
print("Max flow:", max_flow)