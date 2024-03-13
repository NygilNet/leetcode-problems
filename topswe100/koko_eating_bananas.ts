/*

link to problem: https://leetcode.com/problems/koko-eating-bananas/description/

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.


Input: number array (piles of bananas), number of hours before guards get back
Output: number (smallest number of bananas koko can eat an hour before the guards get back)


piles length is guaranteed to be equal to or less than h

    koko must finish each pile in h / piles.length (call this time)

if piles[i] is less than k, koko will eat all the bananas in an hour

    so this problem is like the pramp grant money problem

sort the piles array so koko quickly eats all the small piles as fast as possible

some guess on what k is

    after sorting, assuming k is at least piles[0]

*/

function minEatingSpeed(piles: number[], h: number): number {
    let left = 1, right = Math.max(...piles);
    while (left <= right) {
        const k = Math.floor((right + left) / 2);
        const hours = piles.reduce((acc, curr) => acc + (curr / k), 0);
        if (hours === h) {
            return k;
        }
        hours > h ? left = k + 1 : right = k - 1;
    }
    return right;
}