/*
 * @lc app=leetcode.cn id=438 lang=cpp
 *
 * [438] 找到字符串中所有字母异位词
 */

// @lc code=start
class Solution {
    bool helper(vector<int> &svec, vector<int> &pvec){
        for(int i = 0; i < 26; ++i){
            if(svec[i] != pvec[i]){
                return false;
            }
        }
        return true;
    }
public:
    vector<int> findAnagrams(string s, string p) {
        int left, right = 0;
        vector<int> ans, svec(26, 0), pvec(26, 0);
        for(auto &c: p){
            ++pvec[c -'a'];

        }
        while ((right < s.size()))
        {
            if(right - left + 1 > p.size()){
                --svec[s[left] - 'a'];
                ++left;
            }
            ++svec[s[right] - 'a'];
            if(right - left + 1 == p.size() && helper(svec, pvec)){
                ans.push_back(left);
            }
            ++right;
        }
        return ans;
       
        
    }
};
// @lc code=end

