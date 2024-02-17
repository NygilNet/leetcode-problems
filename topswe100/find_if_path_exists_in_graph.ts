/*

link to problem: https://leetcode.com/problems/find-if-path-exists-in-graph/description/

There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.

Input: n (number of nodes), edges (array of tuples where nodes connect), source (where we start), destination (where we are trying to get)
Output: boolean (can we get to the destination from the source)

create an adjacency list from the edges array
    since we know nodes will be 0 to n - 1, we can use an array and key into the val of the node we are at
        i. create an array of length n
        ii. fill the array with empty arrays
        iii. iterate through the edges array, and push vi at the ui index of our adjacency list

find if it's possible to get to our destination
    dfs with our adjacency list
        i. for each possible path of our source
            ii. start an empty sta


*/

function validPath(n: number, edges: number[][], source: number, destination: number): boolean {
    if (source === destination) return true;
    const adjacencyList: number[][] = Array.from({ length: n }, () => new Array());
    for (const [start, end] of edges) {
        adjacencyList[start].push(end);
        adjacencyList[end].push(start);
    }

    let found = false;

    function _dfs(node: number | null, visited: boolean[]) {
        if (node === null || found) return;
        if (node === destination) {
            found = true;
            return;
        }
        visited[node] = true;
        for (const vertex of adjacencyList[node]) {
            if (!visited[vertex]) _dfs(vertex, visited);
            
        }
    }

    for (const startingPoint of adjacencyList[source]) {
        if (startingPoint === destination) return true;
        let v = Array.from({ length: n }, (el, i) => i === source ? true : false);
        _dfs(startingPoint, v);
        if (found) return true;
    }

    return false;
}