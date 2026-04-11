class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) -1
        leftMax, rightMax = height[l], height[r]
        res = 0
        
        while l < r:
            if leftMax < rightMax:
                l += 1 # shift index
                leftMax = max(leftMax, height[l]) #update height max
                res = res + (leftMax - height[l]) #water at index
            else: 
                r -= 1
                rightMax = max(rightMax, height[r])
                res = res + rightMax - height[r]
        return res