#!/usr/bin/env python3

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        e = {}
        for i in s:
            d[i] = d.get(i, 0) + 1
        for i in t:
            e[i] = e.get(i, 0) + 1
        return d == e

