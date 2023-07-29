#!/usr/bin/env python3

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        maps = []
        for i in strs:
            d = {}
            for j in i:
                d[j] = d.get(j, 0) + 1
            maps.append(d)

        met = {}
        for i, d in enumerate(maps):
            if i in met: continue
            met[i] = True
            a = [strs[i]]
            for j in range(i+1, len(maps)):
                if d == maps[j]:
                    a.append(strs[j])
                    met[j] = True
            ans.append(a)

        return ans

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sat = defaultdict(list)

        for word in strs:
            sort = "".join(sorted(word))
            sat[sort].append(word)

        return sat.values(
