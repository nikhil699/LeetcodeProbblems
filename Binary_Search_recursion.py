# def binarySearch(target):

    
    
    # def search(start, end):
    #     if start > end:
    #         return -1
        
    #     mid = ( start + end ) // 2

    #     if nums[mid] == target:
    #         return mid
        
    #     if target < nums[mid]:
    #         return search(start, mid - 1)
        
    #     else:
    #         return search(mid + 1, end)

    # return search(0, len(nums) - 1)
# once its create entry in stack and when its recursively back its print
# def printNumber(target):
#     if target == 1:
#         print(target)
#         return


#     printNumber(target - 1)
#     print(target)

def factorial(target):
    # Base condition
    if target <= 1:
        return 1
    
    target * factorial(target - 1)
    print(target)
    

  
        






# nums = [1,2,5,8,9,23,67]
target = 5
print(factorial(target))