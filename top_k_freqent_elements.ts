/*

link to leetcode: https://leetcode.com/problems/top-k-frequent-elements/

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]


input: number array, k (number of elements)
output: number array (k most common elements)

CAN NOT:

    iterate through the array while iterating through the array (O n ^2)
    - can be solved w/o sorted (O n log n)



METHOD 1: Mapping elemnts

    create a map

    for each new element add element: 1 to the map

    return the top k elements from the map

METHOD 2: running array 

    define a k length array

    for elements in the array, shift the values of the array

*/

function topKFrequent(nums: number[], k: number): number[] {
    const map: Map<number,number> = new Map();
    for (const element of nums) {
        map.set(element, map.get(element) + 1 || 1);
    }
    const sortedByFrequency = [...map.entries()].sort((a, b) => b[1] - a[1]);
    let res = [];
    for (const element of sortedByFrequency) {
        if (res.length === k) {
            break;
        }
        res.push(element[0]);
    }
    return res;
};