/*

link to leetcode: https://leetcode.com/problems/all-paths-from-source-to-target/description/

Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).


dfs to traverse entire graph

problem is asking for a list of a possible ways of doing something
    backtracking

*/

function allPathsSourceTarget(graph: number[][]): number[][] {
    const paths: number[][] = [], target = graph.length - 1;

    function _backtracking(node: number, path: number[]): void {
        path.push(node);
        if (node === target) {
            paths.push(path);
            return;
        }

        for (const neighbor of graph[node]) {
            _backtracking(neighbor, [...path]);
        }
    }

    _backtracking(0, []);
    return paths;
}