/*

link to problem: https://leetcode.com/problems/find-peak-element/description/

A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
 

Constraints:

1 <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
nums[i] != nums[i + 1] for all valid i.

CAN NOT:
must run in log n ->    can not iterate through the array (O n)
                        can not sort the array (O n log n)

CAN:
must run in log n ->    binary search (O log n)
                        key into array (O 1)
                        recursive call?

i. define recursive binary search
    ii. params left, right
    iii. calculate mid
    iv. determine if nums[mid] is a peak
    v. if true


*/

function findPeakElement(nums: number[]): number {
    let left = 0, right = nums.length - 1;

    while (left < right) {
        const mid = left + Math.floor((right - left) / 2);

        if (nums[mid] < nums[mid + 1]) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }

    return left;
}

// const visited: boolean[] = new Array(nums.length).fill(false);
// let peak: number = -1;

// function _recursiveBinarySearch(left: number, right: number): void {
//     if ((left > right) || peak !== -1) {
//         return;
//     }
//     const mid = left + Math.floor((right - left) / 2);

//     if (visited[mid]) {
//         return;
//     }
//     visited[mid] = true;

//     const leftNeighbor = nums[mid - 1] === undefined ? Number.MIN_SAFE_INTEGER : nums[mid - 1];
//     const rightNeighbor = nums[mid + 1] === undefined ? Number.MIN_SAFE_INTEGER : nums[mid + 1];

//     if (nums[mid] > leftNeighbor && nums[mid] > rightNeighbor) {
//         peak = mid;
//         return;
//     }

//     _recursiveBinarySearch(left, mid);
//     _recursiveBinarySearch(mid, right)
// }

// _recursiveBinarySearch(0, nums.length - 1);
// return peak;