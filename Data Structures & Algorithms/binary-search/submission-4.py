class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums)
        while L < R :
            mid = int((R+L)/2)
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                R = mid
            else:
                L = mid + 1
        return -1