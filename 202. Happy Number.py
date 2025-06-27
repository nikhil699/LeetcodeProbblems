# Space Complexity:
# O(1) — constant, because max possible distinct numbers is small (bounded).
# Final Time Complexity:
# O(log n) per iteration, and only up to ~243 unique numbers.
# Jab hum kehte hain 243 numbers, wo ek estimated upper bound hai from math research:
# Actually, maximum 243 unique numbers possible hote hain before repeating (cycle banne se pehle)
# Ye bound proof kiya gaya hai

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()


        while n != 1:
            if n in seen:
                return False
            seen.add(n)

            n = sum(int(digit) ** 2 for digit in str(n))

        return True

n = 19

sol = Solution()

print(sol.isHappy(n))