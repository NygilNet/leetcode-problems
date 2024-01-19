/*

link to leetcode: https://leetcode.com/problems/seat-reservation-manager/description/

Implement the SeatManager class:

SeatManager(int n) Initializes a SeatManager object that will manage n seats numbered from 1 to n. All seats are initially available.
int reserve() Fetches the smallest-numbered unreserved seat, reserves it, and returns its number.
void unreserve(int seatNumber) Unreserves the seat with the given seatNumber.

*/

class SeatManager {
    seats: boolean[] = [];

    constructor(n: number) {
        this.seats = new Array(n + 1).fill(true);
    }

    reserve(): number {
        for (let i = 1; i < this.seats.length; i++) {
            if (this.seats[i]) {
                this.seats[i] != this.seats[i];
                return i;
            } 
        }
        return -1;
    }

    unreserve(seatNumber: number): void {
        this.seats[seatNumber] = true;
    }
}