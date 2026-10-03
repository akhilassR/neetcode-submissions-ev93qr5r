class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}

        for i, n in enumerate(nums):
            diff = target - n # balance of target - curr
            if diff in prev: # if the balance has been seen, return balance index + current index
                return [prev[diff], i]
            prev[n] = i #otherwise, just store curr 