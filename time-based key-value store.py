# Problem Statement
# Implement a custom Set (or more like a dictionary) that stores data like:
# (key, timestamp, value)
# And supports:
# get(key, timestamp) → return value of largest timestamp ≤ given timestamp for that key

# Examples

# put("a", 5, "apple")
# put("a", 10, "banana")
# put("a", 20, "carrot")

# get("a", 5)   => "apple"
# get("a", 7)   => "apple"  # Closest ≤ 7 is 5
# get("a", 10)  => "banana"
# get("a", 15)  => "banana"
# get("a", 3)   => None

# Time Complexity : for put its o(n) and for get the time complexity is 0(log n)
# Space Complexity : 0(K * T) where k is the number of unique keys stored, and T is the maximum number
# of (timestamp,value) pairs per key

import bisect
from collections import defaultdict


class timestamp:
    def __init__(self):
        self.store = defaultdict(list)
    

    def put(self,key,timestamp,value):
        pair = (timestamp, value)
        bisect.insort(self.store[key], pair)

    def get(self,key,timestamp):
        if key not in self.store:
            return None

        items = self.store[key] # (5, apple), (10, "banana"), (15, "carrot") 
        timestamps = [k for k,_ in items] # 5,10,30

        idx = bisect.bisect_right(timestamps,timestamp)

        if idx == 0:
            return None
        else:
            return items[idx-1][1]

tm = timestamp()
tm.put("a", 5, "apple")
tm.put("a", 10, "banana")
tm.put("a", 20, "carrot")

print(tm.get("a", 3))   # ➜ None
print(tm.get("a", 5))   # ➜ apple
print(tm.get("a", 7))   # ➜ apple
print(tm.get("a", 10))  # ➜ banana
print(tm.get("a", 15))  # ➜ banana
print(tm.get("a", 20))  # ➜ carrot
print(tm.get("a", 25))  # ➜ carrot

    
    
