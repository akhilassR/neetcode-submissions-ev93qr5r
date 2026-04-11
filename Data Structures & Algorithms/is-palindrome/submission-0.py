class Solution:
    def isPalindrome(self, s: str) -> bool:
        #remove space - irrelevant
        s = s.replace(" ", "").lower()
        filtered_s = [c for c in s if c.isalnum()]
        for i in range(len(filtered_s)):
            if filtered_s[i] != filtered_s[len(filtered_s)-i-1]:
                return False
        return True
        
