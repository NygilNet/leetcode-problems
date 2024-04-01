/*

This problem was asked by Snapchat.

Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.


Input: array of tuples (start time of class, end time of class)
Output: integer (minimum number of classrooms needed to host all classes)


METHOD 1: Two Pointer

- find the intersect with the most classes and return number of classes needed at that time

- initialize roomsNeeded variable @ 1
- sort the array from earliest time to latest time [O n log n]
- initialize left pointer @ 0
- iterate through the array of intervals (right pointer) [O n]
    - access the end time of earliest class (left pointer) and the start time of latest class (right pointer)
    - if end time of earliest class is greater than start time of latest class
        - calculate rooms needed: (right - left) + 1
        - update roomsNeeded to max between its current value and calculation
    - while end time of earliest class is less than start time of latest class
        - update left pointer to left + 1
- return roomsNeeded

*/

function calculateRoomsNeeded(intervals: [number, number][]): number {
    let roomsNeeded: number = 1, left: number = 0;
    const len = intervals.length;
    intervals.sort((a, b) => a[0] - b[0]);

    for (let right = 1; right < len; right++) {
        let endTimeEarlyClass = intervals[left][1];
        const startTimeLateClass = intervals[right][0];

        if (endTimeEarlyClass >= startTimeLateClass) {
            const simultaneousClasses = (right - left) + 1;
            roomsNeeded = Math.max(roomsNeeded, simultaneousClasses);
        } else {
            while (left < right && endTimeEarlyClass < startTimeLateClass) {
                left++;
                endTimeEarlyClass = intervals[left][1];
            }
        }
    }
    
    return roomsNeeded;
}