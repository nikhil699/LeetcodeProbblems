class Solution(object):
    def minNumberOfFrogs(self, croakOfFrogs):

        """
        :type croakOfFrogs: str
        :rtype: int
        """
        
        trackFrogs = {
            'c' : 0,
            'r' : 0,
            'o' : 0,
            'a' : 0,
            'k' : 0
        }

        previousStepsFrogs = {
            'r' : 'c',
            'o' : 'r',
            'a' : 'o',
            'k' : 'a'
        }

        activeFrog = 0
        maxFrog = 0

        for item in croakOfFrogs:
            if item == 'c':
                trackFrogs[item] += 1
                activeFrog += 1
                maxFrog = max(maxFrog, activeFrog)
            
            else:
                prev = previousStepsFrogs[item]

                if trackFrogs[prev] == 0:
                    return -1

                trackFrogs[prev] -= 1
                
                if item == 'k':
                    activeFrog -= 1
                else:
                    trackFrogs[item] += 1


        if activeFrog != 0:
            return -1
        else:
            return maxFrog

        


sol = Solution()
croakOfFrogs = "crcoakroak"
print(sol.minNumberOfFrogs(croakOfFrogs))