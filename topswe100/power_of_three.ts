/*

link to problem: https://leetcode.com/problems/power-of-three/description/

Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.


*/

function isPowerOfThree(n: number): boolean {
    if (n < 1) return false;
     
    let left = 0, right = Math.floor(n / 3);

    while (left <= right) {

        let mid = left + Math.floor((right - left) / 2);
        let powerOfThree = 3 ** mid;

        if (powerOfThree === n) return true;

        if (powerOfThree > n) {
            right = mid - 1;
        } else {
            left = mid + 1;
        } 

    }

    return false;
}