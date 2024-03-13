/*

link to problem: https://leetcode.com/problems/sqrtx/description/

Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it do


using the same binary search method from the last two problems

i. left = 1, right = x

ii. while (left < right)

    iii. mid = left + Math.floor((right - left) / 2)

    iv. if mid * mid is less than x

        v. left = mid + 1
    vii. else 
        viii. right = mid

ix. return left

*/

function mySqrt(x: number): number {
    let left = 1, right = x; 
    while (left <= right) {
        const mid = Math.floor((right + left) / 2);
        const square = mid * mid;
        if (square === x) {
          return mid;
        }
        square < x ? left = mid + 1 : right = mid - 1;
    }
    return right;
};