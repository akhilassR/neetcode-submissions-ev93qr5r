class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
    
        countT = {}
        countS = {}

        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1 #retrieve current count of s[i], and increment by 1 
            countT[t[i]] = countT.get(t[i], 0) + 1
        return countS == countT #check whether frequencies of each key in dicts are same