from collections import Counter
class Solution(object):
    def findOriginalArray(self, changed):
        """
        :type changed: List[int]
        :rtype: List[int]
        """
        if len(changed) % 2 != 0:
            return []
        
        result = []
        freq = Counter(changed)
        changed.sort()

        for item in changed:
            if freq[item] == 0:
                continue
            
            if item == 0:
                if freq[item] < 2:
                    return []
                freq[item] -= 2
                result.append(item)
            
            else:
                if freq[2 * item] == 0:
                    return []
                
                freq[item] -= 1
                freq[2 * item] -= 1
                result.append(item)


        
        return result

        

changed = [1,3,4,2,6,8]

sol = Solution()
print(sol.findOriginalArray(changed))