# def fibonacciNumber(k):
#     # Base cases: F(0) = 0, F(1) = 1
#     if k == 0:
#         return 0
#     if k == 1:
#         return 1
#     # Recursive call: F(n) = F(n-1) + F(n-2)
#     return fibonacciNumber(k-1) + fibonacciNumber(k-2)
# k = 5
# print(fibonacciNumber(k))

# def printNumber(p):
#     if p == 0 :
#         return 0
#     if p == 1:
#         return 1
    
#     return printNumber(p-1) + 1

# print(printNumber(10))

def fun(n):
    if n == 0:
        return
    fun(n-1)  # last statement = tail recursion


print(fun(10))
