/*

link to problem: https://leetcode.com/problems/k-closest-points-to-origin/description/

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).


Input: k, the number of points we want to return; points, the points that exist in the grid
Output: number array, x y coordinates of points closest to origin

closest points -> shortest path -> bfs


i. set up string set of all points in the grid and result array
ii. define bfs function
    iii. while queue has items
        iv. if result array length is equal to k, return result 
        v. if the coordinate we find is in the set, push points into result
        vi. run bfs on all neighbors (left/right, up/down, diagonally)
vii. return bfs function on point 0, 0
viii. return result array
*/

function kClosest(points: number[][], k: number): number[][] {

    points.sort((a, b) => {
        const [aX, aY] = a, [bX, bY] = b;
        const xDistance = Math.sqrt((aX)**2 + (aY)**2);
        const yDistance = Math.sqrt((bX)**2 + (bY)**2);
        return xDistance - yDistance;
    });
    return points.slice(0, k);
}
// const closest: number[][] = [], visited: Set<string> = new Set();
// const DIRECTIONS = [[1, 1], [1, -1], [-1, 1], [-1, -1]];

// function _bfs(): void {
//     const queue = [[0, 0]];
//     while (queue.length) {
//         let snapshot = queue.length;
//         for (let i = 0; i < snapshot; i++) {
//             if (closest.length === k) {
//                 return;
//             }
//             const [x, y] = queue.shift()!;
//             for (const [targetX, targetY] of points) {
//                  if ()
//              }
//             for (const [dx, dy] of DIRECTIONS) {
//                 const newX = x + dx, newY = y + dy;
//                 if (!visited.has(`${newX},${newY}`)) {
//                     visited.add(`${newX},${newY}`);
//                     queue.push([newX, newY]);
//                 }
//             }
//         }
//     }
// }

// _bfs();
// return closest;