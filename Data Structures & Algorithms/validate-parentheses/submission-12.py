class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        key = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []

        for i in s:
            if i in key:
                if not stack or stack.pop() != key[i]:
                    return False
            else:
                stack.append(i)

        return len(stack) == 0