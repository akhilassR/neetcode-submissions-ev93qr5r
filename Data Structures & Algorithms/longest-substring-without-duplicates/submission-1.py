class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet: #if current char is not unique
                charSet.remove(s[l]) #remove the first char which is == r
                l += 1 #update l
            charSet.add(s[r]) #add unique char into set
            res = max(res, r-l + 1) #update longest string by max(res, length of string from r to l)
        return res