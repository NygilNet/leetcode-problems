/*

link to problem: https://leetcode.com/problems/kth-largest-element-in-an-array/description/

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

WITH sorting

i. create a set from the array
ii. turn set back into array and sort it
iii. return kth element

WITHOUT sorting

i. make an array, length k
ii. iterate over  

*/



function findKthLargest(nums: number[], k: number): number {
    const target = nums.length - k;

    function _quickSelect(l: number, r: number): number {
        let pivot: number = nums[r];
        let p: number = l;
        for (let i = l; i < r; i++) {
            if (nums[i] <= pivot) {
                [nums[p], nums[i]] = [nums[i], nums[p]];
                p++;
            }
        }
        [nums[p], nums[r]] = [nums[r], nums[p]];

        if (p > target) {
            return _quickSelect(l, p - 1);
        }

        if (p < target) {
            return _quickSelect(p + 1, r);
        }

        if (p === target) {
            return nums[p];
        }
    }

    return _quickSelect(0, nums.length - 1);
};

// FIRST SOLUTION: TOO SLOW
// const ranking: number[] = new Array(k).fill(Number.MIN_SAFE_INTEGER);

// function _updateRankings(n: number): void {
//     let toPlace: number = n;
//     for (let i = k - 1; i >= 0; i--) {
//         if (ranking[i] === Number.MIN_SAFE_INTEGER) {
//             ranking[i] = toPlace;
//             break;
//         }
//         if (ranking[i] < toPlace) {
//             [toPlace, ranking[i]] = [ranking[i], toPlace];
//         }
//     }
// }

// for (const num of nums) {
//     _updateRankings(num);
// }

// return ranking[0];