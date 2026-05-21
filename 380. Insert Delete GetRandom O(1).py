# list + hashmap
import random

class RandomizedSet(object):

    def __init__(self):
        self.bucketOfItems = []
        self.countIndex = {}

    def insert(self, val):

        """
        :type val: int
        :rtype: bool
        """

        if val not in self.countIndex:
            self.countIndex[val] = len(self.bucketOfItems)
            self.bucketOfItems.append(val)
            return True
        else:
            return False
        

    def remove(self, val):

        """
        :type val: int
        :rtype: bool
        """

        if val not in self.countIndex:
            return False
        
        currIndex = self.countIndex[val]
        lastElement = self.bucketOfItems[-1]
        self.bucketOfItems[currIndex] = lastElement
        self.countIndex[lastElement] = currIndex
        self.bucketOfItems.pop()
        del self.countIndex[val]

        return True
        

    def getRandom(self):

        """
        :rtype: int
        """

        randomIndex = random.randint(0,len(self.bucketOfItems) - 1)
        return self.bucketOfItems[randomIndex]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

