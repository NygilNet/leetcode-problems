/*

link to leetcode: https://leetcode.com/problems/insert-delete-getrandom-o1/description/?envType=daily-question&envId=2024-01-16

Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.

*/

class RandomizedSet {
    // private list: Set<number>;

    // constructor() {
    //     this.list = new Set<number>();
    // }

    // insert(val: number): boolean {
    //     if (this.list.has(val)) return false;
    //     this.list.add(val);
    //     return true;
    // }

    // remove(val: number): boolean {
    //     if (!this.list.has(val)) return false;
    //     this.list.delete(val);
    //     return true;
    // }

    // getRandom(): number {
    //     const randomInt = Math.floor(Math.random() * this.list.size);
    //     let i = 0;
    //     for (const value of this.list.values()) {
    //         if (i === randomInt) {
    //             return value;
    //         }
    //         i++;
    //     }
    //     return -1;
    // }

    private set: number[] = [];
    private indices = {};

    constructor() {
        this.set = [];
        this.indices = {};
    }

    insert(val: number): boolean {
        if (val in this.indices) return false;
        this.indices[val] = this.set.length;
        this.set.push(val);
        return true;
    }

    remove(val: number): boolean {

        if (!(val in this.indices)) return false;

        const valIndex = this.indices[val];
        const lastVal = this.set.at(-1);

        [this.set[valIndex], this.set[this.set.length -1]] = [this.set[this.set.length - 1], this.set[val]];
        this.indices[lastVal] = valIndex;

        this.set.pop();
        delete this.indices[val];

        return true;

    }

    getRandom(): number {
        const randomInt = Math.floor(Math.random() * this.set.length);
        return this.set[randomInt];
    }
}

/*

According to ChatGPT:

    Average time complexity of each method: O(1)
    Average space complexity of each method: O(1)

My original version of the getRandom method:

    getRandom(): number {
        const randomInt = Math.floor(Math.random() * this.list.size);
        let values = [...this.list.values()];
        return values[randomInt];
    }

    Interesting that iterating values was a little faster than generating an array.
    
Looking through solutions on leetcode alterative method includes using a combination of an array and an object

Refresher on es5 syntax

    no constructor keyword

    using function variable nature and .prototype to define and set methods

*/