from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs:
            string = []
            for i in strs:
                string.append(set(i))

            answer = ''.join(self.rec(string))
            while answer not in strs[0]:
                i = answer[:-1]
                b = answer[-1]
                answer = b + i

            return answer
        return ''

    def rec(self, item: list):
        if len(item) == 2:
            return item[0] & item[1]
        return item[0] & self.rec(item[1:])


tests = Solution()
print(tests.longestCommonPrefix([""]))
