# Time complexity : 0(n) where n is the number of asteroid given in the asteroids array
# Space complexity : 0(n) where n is the number of asteroid stored in the asteroids array

class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """

        stack = []

        for a in asteroids:
            while stack and stack[-1] > 0 and a < 0:
                if stack[-1] < -a: # right asteroid explodes, continue checking
                    stack.pop() 
                
                elif stack[-1] == -a:
                    stack.pop()
                    break
                
                else:  # left asteroid explodes
                    break
            
            else:
                stack.append(a)
        
        return stack


sol = Solution()

asteroids = [5,10,-5]
asteroids01 = [8,-8,5,-10,15]
print(sol.asteroidCollision(asteroids01))