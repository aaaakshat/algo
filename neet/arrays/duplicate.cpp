#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
		unordered_map<int, int> set;
		for (int i: nums) {
			if (set.count(i) > 0) {
				return true;
			}
			set.insert(make_pair(i, 0));
		}
		return false;
    }
};
