/*

link to problem: https://github.com/appacademy/graduated-job_seeker-program/blob/master/pairboarding-problems/w3d3-a.md

Given an array of integers, find the largest product yielded from three of the integers.

Examples:

maxOfThree([10, 3, 5, 6, 20]) // Output: 1200. Multiply 10, 6, 20

maxOfThree([-10, -3, -5, -6, -20]) // Output: -90

maxOfThree([1, -4, 3, -6, 7, 0]) // Output: 168
Hints:

Remind your partner that you cannot simply take the max three numbers, as two negative numbers make a positive number
We do not want our algorithm to check for negative numbers or take absolute values


*/
// function maxOfThree(array) {

//     let max = -Infinity;
//     let first = 0, length = array.length;
    
//     while (first < length) {
//         let second = first + 1;
//         while (second < length) {
//             let third = second + 1;
//             while (third < length) {
//                 max = Math.max(max, array[first] * array[second] * array[third]);
//                 third++;
//             }
//             second++;
//         }
//         first++;
//     }
    
//     return max;
    
// }

function maxOfThree(array) {
    let sorted = [...array].sort((a, b) => a - b);
    return Math.max(sorted.at(-1) * sorted.at(0) * sorted.at(1), sorted.at(-1) * sorted.at(-2) * sorted.at(-3));
}

console.log(maxOfThree([10, 3, 5, 6, 20])) // Output: 1200. Multiply 10, 6, 20

console.log(maxOfThree([-10, -3, -5, -6, -20])) // Output: -90

console.log(maxOfThree([1, -4, 3, -6, 7, 0])) // Output: 168


/*

According to ChatGPT:
    Time complexity of first solution: O(n^3)
    Time complexity of second solution: O(n log n)

Things to look out for:

    identifying major elements, drilling down to what the question is asking


*/

    