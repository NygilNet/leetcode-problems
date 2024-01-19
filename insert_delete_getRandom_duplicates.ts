/*

link to leetcode: https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/description/

RandomizedCollection is a data structure that contains a collection of numbers, possibly duplicates (i.e., a multicollection). It should support inserting and removing specific elements and also reporting a random element.

Implement the RandomizedCollection class:

RandomizedCollection() Initializes the empty RandomizedCollection object.
bool insert(int val) Inserts an item val into the multicollection, even if the item is already present. Returns true if the item is not present, false otherwise.
bool remove(int val) Removes an item val from the multicollection if present. Returns true if the item is present, false otherwise. Note that if val has multiple occurrences in the multicollection, we only remove one of them.
int getRandom() Returns a random element from the current multicollection of elements. The probability of each element being returned is linearly related to the number of the same values the multicollection contains.
You must implement the functions of the class such that each function works on average O(1) time complexity.

Note: The test cases are generated such that getRandom will only be called if there is at least one item in the RandomizedCollection.


*/

class RandomizedCollection {
    private collection: number[] = [];
    private indices = {};

    constructor() {
        this.collection = [];
        this.indices = {};
    }

    insert(val: number): boolean {
        this.collection.push(val);
        this.indices[val] ||= new Set();
        this.indices[val].add(this.collection.length - 1);
        return this.indices[val].size === 1;
    }

    remove(val: number): boolean {
        if (this.indices[val].size === 0) return false;

        const valIndex = this.indices[val].pop();
        const lastVal = this.collection.at(-1);

        [this.collection[valIndex], this.collection[this.collection.length -1]] = [this.collection[this.collection.length - 1], this.collection[val]];
        this.indices[lastVal].push(valIndex);

        this.collection.pop();

        return true;
    }

    getRandom(): number {
        const randomInt = Math.floor(Math.random() * this.collection.length);
        return this.collection[randomInt];
    }
}