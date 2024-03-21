class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        vector<char> ans;
        int res = 0;
        for (int i = 0; i < s.size(); ++i) {
            while (find(ans.begin(), ans.end(), s[i]) != ans.end()) {
                ans.erase(ans.begin());
            }
            ans.push_back(s[i]);
            res = max(res, (int)ans.size());
        }
        return res;
    }
};
