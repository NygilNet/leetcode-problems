/*

link to problem: https://leetcode.com/problems/reverse-string/description/

Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

You can't convert to to an array, reverse the array and return that because this is an in-place 

Constant memory means we can't store variables in a data structure 


We can iterate over half the array and swap the indices of the array

*/

function reverseString(s: string[]): void {

    const fullLength = s.length, halfLength = Math.floor(fullLength / 2);

    for (let left = 0, right = fullLength - 1; left < halfLength; left++, right--) {
        [s[left], s[right]] = [s[right], s[left]];
    }

}