/*

link to problem: https://leetcode.com/problems/clone-graph/description/

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.


Input: node of a graph
Output: copy of the graph

*/

class GraphNode {
     val: number
     neighbors: GraphNode[]
     constructor(val?: number, neighbors?: GraphNode[]) {
         this.val = (val===undefined ? 0 : val)
         this.neighbors = (neighbors===undefined ? [] : neighbors)
     }
}

const memo = new Map<GraphNode, GraphNode>();
function cloneGraph(node: GraphNode | null): GraphNode | null {
    if (!node) {
        return null;
    }
    if (memo.has(node)) {
        return memo.get(node)!;
    }

    const { val, neighbors } = node;
    const clone = new GraphNode(val);

    memo.set(node, clone);
    clone.neighbors = neighbors.map((neighbor) => cloneGraph(neighbor)!);

    return clone;
}

// function cloneGraph(node: GraphNode | null, memo: GraphNode[] = [new GraphNode()]): GraphNode | null {
//     if (!node) {
//         return null;
//     }
//     if (memo[node.val]) {
//         return memo[node.val];
//     }

//     const { val, neighbors } = node;
//     const clone = new GraphNode(val);

//     for (const neighbor of neighbors) {
//         if (!memo[neighbor.val]) {
//             const neighborClone = cloneGraph(neighbor, memo);
//             if (neighborClone) {
//                 memo[neighbor.val] = neighborClone;
//             }
//         }
//         clone.neighbors.push(memo[neighbor.val]);
//     }
//     memo[clone.val] = clone;

//     return clone;
// }