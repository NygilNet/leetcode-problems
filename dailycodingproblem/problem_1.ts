/*

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

Input: list of numbers, target int
Output: boolean, can two numbers from list add up to target

METHOD 1: Map

i. initialize a map to store values

ii. iterate through the array
    
    iii. check if map has target - current value

        iv. if true, return true

        v. else, set target - current in map to true

vi. if we escape the loop w/o returning true, return false

*/

function twoSum(list: number[], k: number): boolean {
    const values: Set<number> = new Set();

    for (const currentNum of list) {
        if (values.has(currentNum)) {
            return true;
        }
        const target = k - currentNum;
        values.add(target);
    }

    return false;
}

console.log(twoSum([10, 15, 3, 7], 17)); // returns true