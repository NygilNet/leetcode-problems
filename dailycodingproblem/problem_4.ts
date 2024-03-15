/*

Good morning! Here's your coding interview problem for today.

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.

Input: array of numbers
Output: number (smallest non-zero positive integer that is missing from the array)

HAS TO:
    linear time   O(n)
    constant space   O(1)

CAN NOT DO:
    - sort the array (O (n log n) time)
    - use a map, array, etc (O(n) space)
    - iterate through the array while iterating

*/

function lowestMissingInteger(input: number[]): number {
    const track: number[] = new Array(Math.max(...input ) + 1).fill(0);
    const len = track.length;
    
    for (const num of input) {
        const index = Math.max(0, num);
        track[index]++;
    }
    
    for (let i = 1; i < len; i++) {
        if (!track[i]) return i; 
    }
    
    return len;
}

// const len = input.length;
// for (let i = 0; i < len; i++) {
//     while (input[i] > 0 && input[i] <= len && input[i] !== input[input[i] - 1]) {
//         [input[i], input[input[i] - 1]] = [input[input[i] - 1], input[i]];
//     }
// }

// let result = len + 1;

// for (let i = 1; i <= len; i++) {
//     if (i !== input[i - 1]) {
//         result = i;
//         break;
//     }
// }

// return result;


// const len: number = input.length;

// for (let i = 0; i < len; i++) {
//     const num = Math.abs(input[i]);
//     if (num <= len) {
//         input[num - 1] = -Math.abs(input[num - 1]);
//     }
// }

// for (let i = 0; i < len; i++) {
//     if (input[i] > 0) {
//         return i + 1;
//     }
// }

// return len + 1;


// if (input.length === 0) return 1;

// const track: Set<number> = new Set(input);

// for (let i = 1; i <= input.length; i++) {
//     if (!track.has(i)) {
//         return i;
//     }
// }

// return -1;

