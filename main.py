from typing import List, Optional


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        for i in range(n + 1):
            if i ** 4 == n:
                return True
            pass
        return False


tests = Solution()
print(tests.isPowerOfFour(1))
# print(tests.isValid("([)]"))
