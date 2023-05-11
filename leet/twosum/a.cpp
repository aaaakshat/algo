#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
		ios_base::sync_with_stdio(0);
		cin.tie(0); cout.tie(0);

		unordered_map<int, int> comp;
		vector<int> ans;
		int it = 0;
		for (int el: nums) {
			int diff = target - nums[it];
			if (comp.count(diff) >0) {
				ans.push_back(it);
				ans.push_back(comp[diff]);
				return ans;
			}
			comp.insert(make_pair(el, it));
			it++;
		}
		return ans;
    }
};
