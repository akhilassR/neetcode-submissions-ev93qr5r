class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [3,4,5,6,1,2], target = 1
        # rotated n times -> n is not made clear to us
        # return target variable's index in nums

        l, r = 0, len(nums) - 1
        # if nums[l] > target, next best search is r

        while l < r:
            m = (l+r)//2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        pivot = l

        l, r = 0, len(nums) -1

        if target >= nums[pivot] and target <= nums[r]:
            l = pivot
        else:
            r = pivot - 1
        
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1