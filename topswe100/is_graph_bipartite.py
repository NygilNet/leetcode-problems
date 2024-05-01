"""

link to problem: https://leetcode.com/problems/is-graph-bipartite/description/

There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

There are no self-edges (graph[u] does not contain u).
There are no parallel edges (graph[u] does not contain duplicate values).
If v is in graph[u], then u is in graph[v] (the graph is undirected).
The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

Return true if and only if it is bipartite.



"""

from collections import deque

class BipartitePair:
    def __init__(self, vertex, distance):
        self.vertex = vertex
        self.distance = distance

def isBipartiteHelper(adj_list):
    queue = deque()
    visited = {}

    for source in adj_list.keys():
        if source in visited:
            continue

        bipartite_pair = BipartitePair(source, 0)
        queue.append(bipartite_pair)

        while queue:
            root = queue.popleft()

            if root.vertex in visited and root.direction != visited[root.vertex]:
                return False

            visited[root.vertex] = root.direction

            for neighbors in adj_list[root.vertex]:
                if neighbors not in visited:
                   nbp = BipartitePair(neighbors, root.direction + 1)
                   queue.append(nbp)

    return True 

def isBipartite(graph: List[List[int]]) -> bool:
    adj_list = {}

    for i in range(len(graph)):
        adj_list[i] = set(graph[i])

    return isBipartiteHelper(adj_list)
