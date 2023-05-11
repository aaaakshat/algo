#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
		if (s.size() != t.size()) return false;

        /*
        // Solution 1 using hashmaps:
		// letter, count
		unordered_map<char, int> set_s;
		unordered_map<char, int> set_t;

		for (int i=0; i<s.size(); i++) {
            set_s[s[i]]++;
            set_t[t[i]]++;
		}

		return set_s == set_t;
        */

        // Solution 2 with sorting
        sort(s.begin(), s.end());
        sort(t.begin(), t.end());
        return s.compare(t) == 0;
    }
};
