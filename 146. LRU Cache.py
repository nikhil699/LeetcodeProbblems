class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache(object):
    def __init__(self, capacity):

        """
        :type capacity: int
        """

        self.cache = {}
        self.capacity = capacity

        self.head = Node(0,0)
        self.tail = Node(0,0)

        self.head.next = self.tail
        self.tail.prev = self.head
    

    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
    
    # Add node just before tail (most recently used)
    def add(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node


    def get(self, key):

        """
        :type key: int
        :rtype: int
        """

        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.remove(node)
        self.add(node)

        return node.value


    def put(self, key, value):

        """
        :type key: int
        :type value: int
        :rtype: None
        """

        if key in self.cache:
            self.remove(self.cache.get(key))
        
        node = Node(key, value)
        self.cache[key] = node

        self.add(node)

        if len(self.cache) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]
        

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


obj = LRUCache(2)

obj.put(1, 1)
obj.put(2, 2)
print(obj.get(1))     # Output: 1

obj.put(3, 3)         # Evicts key 2
print(obj.get(2))     # Output: -1

obj.put(4, 4)         # Evicts key 1
print(obj.get(1))     # Output: -1
print(obj.get(3))     # Output: 3
print(obj.get(4))     # Output: 4
