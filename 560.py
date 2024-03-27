class Solution:
    def subarraySum(self, nums, k):
        mp = {0: 1}
        count, pre = 0, 0
        for x in nums:
            pre += x
            if pre - k in mp:
                count += mp[pre - k]
            mp[pre] = mp.get(pre, 0) + 1
        return count
# Path: 561.py
nums =[3,4,7,2,-3,1,4,2]

