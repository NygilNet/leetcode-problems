/*

link to problem: https://leetcode.com/problems/container-with-most-water/description/

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

*/

function maxArea(height: number[]): number {
    let max: number = 0;
    const n = height.length;
    let left = 0, right = n - 1;

    while (left < right) {
        const leftEndpoint = height[left];
        const rightEndpoint = height[right];
        const area = Math.min(leftEndpoint, rightEndpoint) * (right - left);
        max = Math.max(area, max);
        rightEndpoint > leftEndpoint ? left++ : right--;
    }

    return max;
}