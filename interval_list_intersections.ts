/*

link to leetcode: https://leetcode.com/problems/interval-list-intersections/description/

You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].


*/

function intervalIntersection(firstList: number[][], secondList: number[][]): number[][] {

    const intervals: number[][] = [];
    let firstPointer = 0, secondPointer = 0;

    while (firstPointer < firstList.length && secondPointer < secondList.length) {

        const [ firstStart, firstEnd ] = firstList[firstPointer];
        const [ secondStart, secondEnd ] = secondList[secondPointer];

        const intersectionStart = Math.max(firstStart, secondStart);
        const intersectionEnd = Math.min(firstEnd, secondEnd);

        if (intersectionEnd >= intersectionStart) intervals.push([ intersectionStart, intersectionEnd ]);

        if (firstEnd >= secondEnd) secondPointer++;
        if (firstEnd <= secondEnd) firstPointer++;
        
    }
    
    return intervals;

}