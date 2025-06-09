# Time: O(k) — we try k+1 combinations
# Space: O(1) — constant extra space


# Low-Level Design → Focused on core interview-ready problems like a Quiz Platform, Parking Lot System, Rate Limiter, 
# and Multithreaded Task Scheduler in Java. Emphasized clean OOP, SOLID principles, design patterns, 
# and proper concurrency handling — practiced consistently, not just before interviews.


# • Behavioral Rounds → Gave them equal weight. Prepared well-structured stories 
# for real scenarios — conflict resolution, taking ownership, and learnings from failure. 
# These rounds can absolutely impact the final decision.


# • DSA with Patterns → Prioritized depth over volume. Revisited core patterns like DP, 
# Union-Find, and Sliding Window until I could solve confidently. Categorized problems by technique — not 
# just solving for the sake of it.


# 1st I was asked about OOPS concept.
# 2nd I was asked abstract class, its implementation, etc.
# Then I was asked how Abstract class is different from interface and to implement interface.
# Then, some code snippets were given to me and I was asked for code-pair and do some operations on abstract class and interfaces examples. This was very complex to be honest and java concepts to the core were tested here. Then, I was asked if 2 interfaces can be implemented by abstract.
# Next, I was asked to implement polymorphism.
# Then threading in java was asked and was to create the thread(extending the class, implementing runnable interface, implementing callable).




class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        n = len(cardPoints)
        total = 0

        for i in range(0,k):
            total = total + cardPoints[i]
        
        maximumResult = total

        for i in range(0,k):
            total = total - cardPoints[k - 1 - i]
            total = total + cardPoints[n - 1 - i]
            maximumResult = max(maximumResult,total)
        
        return maximumResult



sol = Solution()
cardPoints = [1,2,3,4,5,6,1]
k = 3

print(sol.maxScore(cardPoints,k))