class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        searched = set()
        for i in nums:
            if i in searched:
                return True
            searched.add(i)

        return False
