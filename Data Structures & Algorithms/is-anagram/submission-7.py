class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # same length, same unique letters
        if len(s) != len(t): return False

        countS, countT = {}, {}
        for i in range(len(s)): #iterate through indexes of either
            countS[s[i]] = 1 + countS.get(s[i], 0) #create dict of each letter's count
            # countS['A'] 1 + countS.ge
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT