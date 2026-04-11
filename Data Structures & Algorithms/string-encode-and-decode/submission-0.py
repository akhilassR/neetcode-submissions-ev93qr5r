class Solution:

    def encode(self, strs: List[str]) -> str:
        res = "" #becomes a string
        for s in strs:
            res = res + str(len(s)) + '#' + s #append each string (length+#+word)
        return res

    def decode(self, s: str) -> List[str]:
        res = [] #back into a list of strings
        i = 0

        while i<len(s):
            j = i
            while s[j] != '#': #
                j += 1
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            i = j + 1 + length#start of next string
        return res