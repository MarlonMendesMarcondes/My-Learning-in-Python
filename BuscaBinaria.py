nums = [-5, -3, 0, 1, 3, 8, 12]
target = 3
def binary_search(nums, target):
    left = 0
    right = len(nums)-1
    while left <= right:
        middle = int((right+left)/2)
        if nums[middle] == target:
            return print(middle)
        elif target > nums[middle]:
            left = middle+1
        else :
            right = middle -1
    return -1
binary_search(nums,target)