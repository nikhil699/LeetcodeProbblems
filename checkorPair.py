# Given an array A[] and a number x, check for pair in A[] with sum as x.

# Example1:
# Input: arr[] = {0, -1, 2, -3, 1}
#        sum = -2
# Output: -3, 1
# Valid pair exists.


https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/description/
https://leetcode.com/problems/minimum-average-difference/
https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/description/
https://leetcode.com/problems/search-suggestions-system/description/
https://leetcode.com/problems/peak-index-in-a-mountain-array/
https://leetcode.com/problems/rotting-oranges/description/
https://leetcode.com/problems/spiral-matrix/
https://leetcode.com/problems/search-suggestions-system/
https://leetcode.com/problems/minimum-window-substring/
https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/description/
https://leetcode.com/problems/sum-of-two-integers/description/
https://leetcode.com/problems/subarrays-with-k-different-integers/
https://leetcode.com/problems/frequency-of-the-most-frequent-element/description/
https://leetcode.com/problems/equal-sum-arrays-with-minimum-number-of-operations/description/
https://leetcode.com/problems/3sum/description/
https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/
https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/
https://leetcode.com/problems/replace-the-substring-for-balanced-string/
https://leetcode.com/problems/max-consecutive-ones-iii/
https://leetcode.com/problems/subarrays-with-k-different-integers/
https://leetcode.com/problems/fruit-into-baskets/
https://leetcode.com/problems/get-equal-substrings-within-budget/
https://leetcode.com/problems/longest-repeating-character-replacement/
https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
https://leetcode.com/problems/minimum-size-subarray-sum/
https://leetcode.com/problems/sliding-window-maximum/
https://leetcode.com/problems/network-delay-time/?envType=problem-list-v2&envId=x1wy4de7
https://leetcode.com/problems/next-greater-element-iii/description/
https://leetcode.com/problems/minimum-number-of-refueling-stops/
https://leetcode.com/problems/counting-bits/description/
https://leetcode.com/problems/lfu-cache/description/
https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/description/
https://leetcode.com/problems/word-ladder-ii/description/
https://leetcode.com/problems/word-ladder/description/
https://leetcode.com/problems/get-equal-substrings-within-budget/description/
https://leetcode.com/problems/merge-intervals/description/
https://leetcode.com/problems/merge-k-sorted-lists/description/
https://leetcode.com/problems/lru-cache/description/
https://leetcode.com/problems/minimum-cost-for-tickets/description/?envType=problem-list-v2&envId=x1k8lxi5
https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
https://leetcode.com/problems/edit-distance/description/
https://leetcode.com/problems/word-search-ii/description/
https://leetcode.com/problems/the-skyline-problem/description/
https://leetcode.com/problems/divide-two-integers/description/?envType=problem-list-v2&envId=bit-manipulation
https://leetcode.com/problems/climbing-stairs/description/
https://leetcode.com/problems/pacific-atlantic-water-flow/description/
https://leetcode.com/problems/shortest-path-in-binary-matrix/description/
https://leetcode.com/problems/unique-paths/description/
https://leetcode.com/problems/find-eventual-safe-states/description/
https://leetcode.com/problems/valid-sudoku/description/
https://leetcode.com/problems/shortest-path-to-get-all-keys/description/
https://leetcode.com/problems/word-search-ii/description/
https://leetcode.com/problems/h-index-ii/description/
https://leetcode.com/problems/satisfiability-of-equality-equations/description/?envType=problem-list-v2&envId=x1wy4de7
https://leetcode.com/problems/map-of-highest-peak/description/
https://leetcode.com/problems/number-of-provinces/description/?envType=problem-list-v2&envId=x1wy4de7
https://leetcode.com/problems/surrounded-regions/description/?envType=problem-list-v2&envId=x1wy4de7
https://leetcode.com/problems/find-common-characters/description/?envType=problem-list-v2&envId=504wrexe
https://leetcode.com/problems/copy-list-with-random-pointer/description/?envType=problem-list-v2&envId=504wrexe
https://leetcode.com/problems/uncommon-words-from-two-sentences/description/?envType=problem-list-v2&envId=504wrexe
https://leetcode.com/problems/kth-missing-positive-number/description/?envType=problem-list-v2&envId=504wrexe
https://leetcode.com/problems/subarray-sum-equals-k/description/
https://leetcode.com/problems/add-two-numbers/description/
https://leetcode.com/problems/container-with-most-water/description/
https://leetcode.com/problems/search-in-rotated-sorted-array/description/
https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/description/
https://leetcode.com/problems/jump-game-ii/description/



class Solution(object):
    def CheckForpair(self, arr, target_sum):
        """
        :type arr: list
        :type target_sum: int
        """
        frequency = set()

        for num in arr:
            result = target_sum - num  
            
            if result in frequency:
                return (result, num)  
            
            frequency.add(num)  
        
        return "No valid pair exists"



sol = Solution()
arr = [0, -1, 2, -3, 1]
sum = -2

print(sol.CheckForpair(arr,sum))


      



