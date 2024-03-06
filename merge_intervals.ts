/*

link to leetcode: https://leetcode.com/problems/merge-intervals/description/

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

*/

/*

Input: array of arrays (start number, end number)
Output: array of intervals

stack method

while intervals.length
    i. pop off top interval
    ii. if endi is greater than or equal to our current interval start, we will update current interval
    iii. if endi is less than our current interval start, we will push current interval into result array
return result 

 */
function merge(intervals: number[][]): number[][] {
    intervals.sort((a, b) => a[0] - b[0]);
    const result: number[][] = [];
    let currentInterval: number[] = intervals[0];

    for (let i = 1; i < intervals.length; i++) {
        let curr = intervals[i];
        const [currentStart, currentEnd] = currentInterval;
        const [start, end] = curr;

        if (start <= currentEnd) {
            currentInterval = [Math.min(start, currentStart), Math.max(end, currentEnd)];
        } else {
            result.push(currentInterval);
            currentInterval = curr;
        }
    }
  
    result.push(currentInterval);
    return result;
};

// while (intervals.length) {
//     let top = intervals.pop();
//     const [currentStart, currentEnd] = currentInterval;
//     const [start, end] = top;

//     if (top[1] >= currentInterval[0]) {
//         currentInterval = [Math.min(start, currentStart), Math.max(end, currentEnd)];
//     } else {
//         result.push(currentInterval);
//         currentInterval = top;
//     }
// }