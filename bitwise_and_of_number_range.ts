/*

link to problem: https://leetcode.com/problems/bitwise-and-of-numbers-range/description/?envType=daily-question&envId=2024-02-21

Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.


Example 1:

Input: left = 5, right = 7
Output: 4
Example 2:

Input: left = 0, right = 0
Output: 0
Example 3:

Input: left = 1, right = 2147483647
Output: 0
 

Constraints:

0 <= left <= right <= 231 - 1


Input: two numbers (range)
Output: single number

According the MDN, bitwise AND (&) returns a number whose binary representation has a 1 in each bit position for which the corresponding bits of both operands are 1

first example 
5 -> 101
7 -> 111

so 5 & 7 -> 101 -> 5, not the return we are looking for

5 -> 101
6 -> 110
7 -> 111

so 5 & 6 -> 100 -> 4 & 7 -> 100 -> 4, which is the return we are looking for

take left as the initial running number 

for left + 1 to right:
    update running bitwise with calculate running bitwise AND i
    if at any point our running number is 0, it will not change, so we return 0

return what running number we have

left = 1, right = 2
runningNum = 1

*/
// function rangeBitwiseAnd(left: number, right: number): number {
//     let runningNum = left;
//     for (let i = left + 1; i <= right; i++) {
//         runningNum = runningNum & i;
//         if (runningNum === 0) return runningNum;
//     }
//     return runningNum;
// }

function rangeBitwiseAnd(left: number, right: number): number {
    let shift = 0;
    while (left < right) {
        left >>= 1;
        right >>= 1;
        shift++;
    }
    return left << shift;
}
