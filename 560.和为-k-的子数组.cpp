/*
 * @lc app=leetcode.cn id=560 lang=cpp
 *
 * [560] 和为 K 的子数组
 */
#include <iostream>
using namespace std;
#include <vector> 

// @lc code=start
class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int, int> mp;
        mp[0] = 1;
        int count = 0, pre = 0;
        for (auto& x:nums) {
            pre += x;
            if (mp.find(pre - k) != mp.end()) {
                count += mp[pre - k];
            }
            mp[pre]++;
        }
        return count;
    }
};

int main(){
    Solution s;
    vector<int> nums = {3,4,7,2,-3,1,4,2};
    int k = 2;
    cout << s.subarraySum(nums, k) << endl;
    return 0;
}