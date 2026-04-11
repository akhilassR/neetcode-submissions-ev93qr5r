class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L, R = 1, max(piles)
        res = R

        #use binary search to look for speed 

        while L <= R:
            k = (R+L)//2
            time = 0
            for p in piles:
                time = time + math.ceil(float(p)/k)
            if time <=h:
                res = k
                R = k - 1
            else:
                L = k + 1
        return res