#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
class Solution:
    def helper(self, svec, pvec):
        for i in range(26):
            if svec[i] != pvec[i]:
                return False
        return True

    def findAnagrams(self, s: str, p: str) -> List[int]:
        left, right = 0, 0
        ans = []
        svec = [0] * 26
        pvec = [0] * 26

        for c in p:
            pvec[c - 'a'] += 1

        while (right < len(s)):
            if right - left + 1 > len(p):
                svec[s[left] - 'a'] -= 1
                left += 1
            svec[s[right] - 'a'] += 1
            if right - left + 1 == len(p) and self.helper(svec, pvec):
                ans.append(left)
            right += 1
        return ans

# @lc code=end

 s