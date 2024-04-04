/*

link to leetcode: https://leetcode.com/problems/distant-barcodes/

In a warehouse, there is a row of barcodes, where the ith barcode is barcodes[i].

Rearrange the barcodes so that no two adjacent barcodes are equal. You may return any answer, and it is guaranteed an answer exists.

 

Example 1:

Input: barcodes = [1,1,1,2,2,2]
Output: [2,1,2,1,2,1]
Example 2:

Input: barcodes = [1,1,1,1,2,2,3,3]
Output: [1,3,1,3,1,2,1,2]
 

Constraints:

1 <= barcodes.length <= 10000
1 <= barcodes[i] <= 100


dictionary to keep track of frequencies
put tuple of (freq, val) in a heap
prioritize taking the hightest freq val
    if val matches previous, then prioritize second highest freq

*/

function rearrangeBarcodes(barcodes: number[]): number[] {
    
};