#!/usr/bin/env python3

"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1

        top = sorted(d.items(), key=lambda i: i[1])[:-k]
        return [x[1] for x in top]
        """


def runner(nums, k):
    d = {}
    for i in nums:
        d[i] = d.get(i, 0) + 1

    top = sorted(d.items(), key=lambda i: i[1])
    print(top)
    print(top[:-k])
    return [x[1] for x in top]

print(runner([1,1,1,2,2,3,3,3,3], 2))
