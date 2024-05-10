"""

link to leetcode: https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/description/

You are given a positive integer n representing the number of nodes of a Directed Acyclic Graph (DAG). The nodes are numbered from 0 to n - 1 (inclusive).

You are also given a 2D integer array edges, where edges[i] = [fromi, toi] denotes that there is a unidirectional edge from fromi to toi in the graph.

Return a list answer, where answer[i] is the list of ancestors of the ith node, sorted in ascending order.

A node u is an ancestor of another node v if u can reach v via a set of edges.

Input: n, number of nodes, edgeList, array of tuples showing edges
Output: list of each nodes ancestors

"""
from collections import defaultdict
def getAncestors(n: int, edges: list[list[int]]) -> list[list[int]]:
    res = []
    for i in range(n):
        res.append([])

    adj_list = defaultdict(list)

    for start, end in edges:
        adj_list[start].append(end)

    def _findDescendants(node: int, descendants=[]) -> list[int]:
        