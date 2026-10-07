class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = {}
        max_len = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)
            curr_window_size = r - l + 1
            valid = (curr_window_size - max(count.values())) <= k
            if not valid:
                count[s[l]] -= 1
                l += 1
            corrected_window_size = r - l + 1    
            max_len = max(max_len, corrected_window_size)
        return max_len
                