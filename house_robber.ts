/*

link to leetcode: https://leetcode.com/problems/house-robber/description/?envType=daily-question&envId=2024-01-21

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

have two sum variables, one for every even house and one for every odd house

iterate through the array if index is even add to even total else add to odd total

return the max value between the two totals


maximum value is not ordered in way where we add the total of alternating houses

iterate through the array, creating a hashmap where the key is nums[i] and the value is an array of the indices in the array

have a counter of the the values in the array


*/

function rob(nums: number[]) {

    const map = {}, usedIndices = new Set();

    for (let i = 0; i < nums.length; i++) {
        const val = nums[i];
        map[val] ||= [];
        map[val].push(i);
    }

    let stack = Object.keys(map).sort((a, b) => +a - +b), max = 0;

    while (stack.length) {

        const subStack = map[stack.pop()!];

        while (subStack.length) {
            let index = +subStack.pop();
            if (!usedIndices.has(index)) {
                max += nums[index];
                usedIndices.add(index);
                usedIndices.add(index - 1);
                usedIndices.add(index + 1);
            } 
        }

    }

    return max;

}