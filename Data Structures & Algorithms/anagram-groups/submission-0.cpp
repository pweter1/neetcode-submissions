class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> m;
        for (const auto& s : strs) {
            vector<int> cnts(26, 0);
            for (char c : s) {
                cnts[c - 'a']++;
            }
            string key = "";
            for (int i = 0; i < 26; i++) {
                key += to_string(cnts[i]) + "#";
            }
            m[key].push_back(s);
        }
        vector<vector<string>> ans;
        for (auto& [k, v] : m) {
            ans.push_back(v);
        }
        return ans;
    }
};
