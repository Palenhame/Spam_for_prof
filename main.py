from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    for count, item in enumerate(nums):
        if target - item in nums and count != nums.index(target - item):
            return [count, nums.index(target - item)]


print(twoSum([3,3], 6))
