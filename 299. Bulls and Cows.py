# approach : i iterate both the string and check the index and character if i found any character then i count those character for bull count and for cow count i store the frequency of each character of the scret and guess and take the miminum of the frequesncy of each character and take of count of those kind of character and return at the end
# Time & Space Complexity:
# Time: O(n), where n = length of the secret
# Space: O(1), since at most 10 digits ('0'-'9')

from collections import Counter

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls = 0
        secret_count = Counter()
        guess_count = Counter()

        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                secret_count[s] += 1
                guess_count[g] += 1

        cows = 0
        for digit in secret_count:
            cows += min(secret_count[digit], guess_count[digit])

        return "{}A{}B".format(bulls, cows)

secret = "1807"
guess = "7810"

sol = Solution()
print(sol.getHint(secret,guess))