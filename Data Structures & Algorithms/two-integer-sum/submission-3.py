class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # given a target value, find indices in list that sums to target

        indices = {}

        for i, n in enumerate(nums):
            indices[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]