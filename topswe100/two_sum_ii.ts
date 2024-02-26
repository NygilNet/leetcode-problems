/*

link to problem: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

Input: array of number, target number
Output: "tuple" of indexes

solution can only use constant space, so we can't use an object

multiple points of the problem mention array is sorted, so this must be an important piece of information


iterate through the array
for each number we perform a binary search for the the number that will add up to the target
if two values are found, return the array

*/

function twoSum(numbers: number[], target: number): number[] {
    let left: number, right: number, mid: number, newTarget: number;
    const n = numbers.length;

    for (let i = 0; i < n; i++) {
        newTarget = target - numbers[i];
        left = i + 1;
        right = n - 1;
        while (left <= right) {
            mid = left + Math.floor((right - left) / 2);
            let current = numbers[mid];
            if (current === newTarget) return [i + 1, mid + 1];
            current > newTarget ? right = mid - 1 : left = mid + 1;
        }
    }

    return [-1, -1];
}

/*

According to ChatGPT:
    time complexity: O(n log n)
    space complexity: O(1)



*/