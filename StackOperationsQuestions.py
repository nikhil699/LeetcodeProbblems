# 1. Basic Stack Operations
# Implement Stack using Arrays/Linked List
# Implement Queue using Arrays/Linked List
# Implement Stack using 2 Queues
# Implement Queue using 2 Stacks
# 2. Validations / Expression Problems
# Valid Parentheses ✅ (tumne kiya)
# Min Add to Make Parentheses Valid
# Balanced Parentheses with *,) (advanced)
# Evaluate Reverse Polish Notation ✅
# Infix to Postfix Conversion
# Basic Calculator I/II (expression evaluation with stack)
# 3. Next Greater / Smaller Element Variations
# Next Greater Element I ✅
# Next Greater Element II (circular array)
# Next Smaller Element (similar idea)
# Daily Temperatures ✅
# Stock Span Problem ✅
# 4. Monotonic Stack Hard Level
# Trapping Rain Water
# Largest Rectangle in Histogram
# Maximal Rectangle (extension of histogram)
# 5. Design Problems (OOP + Stack/Queue)
# Min Stack ✅
# Max Stack
# Implement Circular Queue
# Online Stock Span (LeetCode 901)
# Design Browser History (queue-like behavior)
# 6. Queue Specific
# Sliding Window Maximum (monotonic deque)
# Rotten Oranges (multi-source BFS → queue)
# Implement LRU Cache (Queue + HashMap)
# 7. Advanced / Mix Concepts
# Asteroid Collision (stack)
# Remove K Digits (monotonic stack)
# Next Greater Element in Linked List
# Decode String (e.g. "3[a2[c]]" → "accaccacc")







class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        return self.items.append(x)
       

    def pop(self):
        return self.items.pop()
       

    def peek(self):
        # return top element without removing
        return self.items[-1]
         

    def isEmpty(self):
        # return True if empty else False
        if len(self.items) == 0:
            return True
        else:
            return False
          


# Example usage [ our stack looks like this = [30,20,10] ]
s = Stack()
s.push(10)
s.push(20)
s.push(30)

print(s.peek())   # expected 30
print(s.pop())    # expected 30
print(s.peek()) 
print(s.pop()) 
print(s.pop())  # expected 20
print(s.isEmpty())  # expected False





# Questions 2 ----  Balanced Parentheses
# Given a string containing only the characters:
# (, ), {, }, [, ]
# Check whether the string has balanced parentheses.
# A string is balanced if:
# Every opening bracket has a corresponding closing bracket.
# Brackets are closed in the correct order.




class Solution:
    def balancedParentheses(self,s):
        symbols = { ')':'(','}':'{',']':'[' }
        stack = []

        for char in s:
            if char in symbols.values():
                stack.append(char)
            elif char in symbols:
                if not stack or stack[-1] != symbols[char]:
                    return False
                
                stack.pop()
        
        return len(stack) == 0
           


Input01 =  "({[]})"
Input02 =  "([)]"
Input03 = "((("
sol = Solution()

print(sol.balancedParentheses(Input01))
print(sol.balancedParentheses(Input02))
print(sol.balancedParentheses(Input03))





# Problem Statement: Next Greater Element
# Given an array arr[] of integers, find the Next Greater Element (NGE) for every element.
# The Next Greater Element for an element x is the first greater element on the right side of x in the array.
# If no greater element exists, put -1


class Solution:
    def nextGreaterElement(self, s):
        result = [-1] * len(s)
        stack = []

        for element in range(len(s)):
            # while stack not empty and current element is greater
            # than element at index in stack → update result
            while stack and s[element] > s[stack[-1]]:
                idx = stack.pop()
                result[idx] = s[element] 
            
            stack.append(element)
        
        return result



arr01 = [4, 5, 2, 25]
arr02 = [13, 7, 6, 12]

sol = Solution()
print(sol.nextGreaterElement(arr01))
print(sol.nextGreaterElement(arr02))







# Design a stack that supports the following operations in O(1) time:
# push(x) → Insert an element.
# pop() → Remove the top element.
# top() → Get the top element.
# getMin() → Retrieve the minimum element in the stack.



class Solution:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self,element):
        if not self.minStack or element <= self.minStack[-1]:
            self.minStack.append(element)
        self.stack.append(element)
        
        pass
    
    def pop(self):
        idx = self.stack.pop()
        if self.minStack and self.minStack[-1] == idx:
            self.minStack.pop()
        pass
    
    def getMin(self):
        return self.minStack[-1] if self.stack else None


sol = Solution()

sol.push(5)
sol.push(3)
sol.push(7)
print(sol.getMin()) #→ 3
sol.pop()   #→ removes 7
print(sol.getMin()) #→ 3
sol.pop()   #→ removes 3
print(sol.getMin()) #→ 5







# Problem Statement: Evaluate Reverse Polish Notation (RPN)
# You are given an array of strings tokens representing a mathematical expression in Reverse Polish Notation.
# Valid operators: +, -, *, /
# Each operand may be an integer.
# Division should truncate toward zero.
# The expression is always valid.
# 👉 Your task: Evaluate the expression and return the integer result.




def evalRPN(tokens):
    stack = []
    match = ["+","*","-","/"]

    for token in tokens:
        # 1. If token is number → push to stack
        if token not in match:
            stack.append(int(token))
        # 2. If token is operator → pop two elements, apply operation, push result back
        else:
            b = stack.pop()
            a = stack.pop()

            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            else:
                stack.append(int(a / b))
    
    return stack[-1]  # final result


# Tests
print(evalRPN(["2","1","+","3","*"]))         # 9
print(evalRPN(["4","13","5","/","+"]))       # 6
print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))  # 22







# Problem Statement: Stock Span Problem
# You are given an array prices[] where prices[i] is the price of a stock on day i.
# 👉 For each day, calculate the Stock Span = number of consecutive days (including today) the price of the stock 
# was less than or equal to today's price.



# Input:  prices = [100, 80, 60, 70, 60, 75, 85]
# Output: [1, 1, 1, 2, 1, 4, 6]

# Explanation:
# - Day 1 (100): no previous greater → span = 1  
# - Day 2 (80): no previous greater → span = 1  
# - Day 3 (60): no previous greater → span = 1  
# - Day 4 (70): previous 60 ≤ 70 → span = 2  
# - Day 5 (60): no previous greater → span = 1  
# - Day 6 (75): previous 60,70 ≤ 75 → span = 4  
# - Day 7 (85): previous 75,60,70,80 ≤ 85 → span = 6

class Solution:
    def calculateSpanStock(self,prices):

        stack = []
        span = 1
        maxSpan = 0

        for price in range(len(prices)):
            while stack and prices[stack[-1]] < prices[price]:
                span += 1
                stack.pop()
            stack.append(price)
            
        
        return span






sol = Solution()
prices = [100, 80, 60, 70, 60, 75, 85]
print(sol.calculateSpanStock(prices))