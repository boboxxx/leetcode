from collections import Counter

class Solution:
    def findAnagrams(self, s, p):
        # 创建一个结果列表
        res = []
        # 创建一个计数器，用于计算字符串p中的字符数量
        pCounter = Counter(p)
        # 创建一个计数器，用于计算字符串s中前len(p)-1个字符的数量
        sCounter = Counter(s[:len(p)-1])
        # 遍历字符串s中从第len(p)-1个字符到第len(s)个字符
        for i in range(len(p)-1,len(s)):
            # 将字符串s中第i个字符的数量加1
            sCounter[s[i]] += 1
            # 如果字符串s中前len(p)个字符的数量与字符串p中字符的数量相等
            if sCounter == pCounter:
                # 将i-len(p)+1添加到结果列表中
                res.append(i-len(p)+1)
            # 将字符串s中第i-len(p)+1个字符的数量减1
            sCounter[s[i-len(p)+1]] -= 1
            # 如果字符串s中第i-len(p)+1个字符的数量为0
            if sCounter[s[i-len(p)+1]] == 0:
                # 删除字符串s中第i-len(p)+1个字符的数量
                del sCounter[s[i-len(p)+1]]
        # 返回结果列表
        return res
    
s = "cbaebabacd"
p = "abc"
solution = Solution()
print(solution.findAnagrams(s, p))

