'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example:

    print(tow_sum([2, 7, 11, 15], 9))  # [0, 1]
    print(tow_sum([3, 2, 4], 6))  # [1, 2]
    print(tow_sum([3, 3], 6))  # [0, 1]
    print(tow_sum([3, 2, 3], 6))  # [0, 2]
    print(tow_sum([3, 2, 4], 5))  # [0, 1]
    print(tow_sum([3, 2, 4], 7))  # [1, 2]
'''

def tow_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None


print(tow_sum([2, 7, 11, 15], 9))  # [0, 1]
print(tow_sum([3, 2, 4], 6))  # [1, 2]
print(tow_sum([3, 3], 6))  # [0, 1]
print(tow_sum([3, 2, 3], 6))  # [0, 2]
print(tow_sum([3, 2, 4], 5))  # [0, 1]
