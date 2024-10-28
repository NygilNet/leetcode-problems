"""
link to leetcode: https://leetcode.com/problems/lru-cache/

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
 

Constraints:

1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.



"""

class LRUCache:

    def __init__(self, capacity: int):
        if capacity <= 0:
            raise Exception('LRU cache must be initialized with positive size capacity')
        
        self.capacity = capacity
        self.dictionary = {}
        self.history = []
        self.history_indices = {}

    
    def updateHistory(self, key: int) -> None:
        if key in self.history_indices:
            index_in_history = self.history_indices[key]
            self.history.pop(index_in_history)
        self.history.append(key)
        self.history_indices[key] = len(self.history) - 1


    def get(self, key: int) -> int:
        if key not in self.dictionary:
            return -1
        
        self.updateHistory(key)
        return self.dictionary[key]


    def put(self, key: int, value: int) -> None:
        if key in self.dictionary:
            self.dictionary[key] = value
            self.updateHistory(key)
            return
        
        if len(self.dictionary) >= self.capacity:
            least_used_key = self.history.pop(0)
            del self.dictionary[least_used_key]
            del self.history_indices[least_used_key]

        self.dictionary[key] = value
        self.updateHistory(key)

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)