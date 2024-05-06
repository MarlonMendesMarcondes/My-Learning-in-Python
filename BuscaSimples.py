nums = [-5, -3, 0, 1, 3, 8, 12]
target = 3
def binary_search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return print(i)
    return print(-1)
    
binary_search(nums,target)