nums = [0,1,0,3,12,5,6,0,0,0,6]
def move_zeroes(nums):
    lastZero = 0
    sorted(nums)
    for i in range(len(nums)):
        if nums[i] != 0:
            aux = nums[lastZero]
            nums[lastZero] = nums[i]
            nums[i] = aux
            lastZero += 1
    return print(nums)
    
move_zeroes(nums)