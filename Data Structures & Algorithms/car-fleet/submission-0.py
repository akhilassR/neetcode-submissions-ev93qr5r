class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p, s in zip(position, speed)]
        
        stack = []
        for p, s in sorted(pair)[::-1]:
            stack.append((target - p) / s) #append time of arrival of the right most vehicle
            if len(stack) >= 2 and stack[-1] <= stack[-2]: #if fleet has more than 1, and the eta of added veh is shorter than og veh,
                stack.pop() #pop next veh as it is considered a fleet with the front veh
        
        return len(stack)