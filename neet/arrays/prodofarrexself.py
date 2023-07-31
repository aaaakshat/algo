#!/usr/bin/env python3

"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        n = len(nums)
        pre[0]=1
        post[n-1]=1
        for i in range(1, n)):
            pre[i] = pre[i-1] * nums[i-1]
            post[n-i-1] = post[n-i] * nums[n-i]

"""

def run(nums):
	n = len(nums)
	pre = [1] * n
	post = [1] * n

	for i in range(1, n):
		pre[i] = pre[i-1] * nums[i-1]
		post[n-i-1] = post[n-i] * nums[n-i]

	ans = []
	for i in range(0, n):
		ans.append(pre[i] * post[i])


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1] * n
        for i in range(1, n):
            pre[i] = pre[i-1] * nums[i-1]
        # mutiply by suffix
        post = 1
        for i in range(n):
            pre[n-i] *= post
            post *= nums[n-i]
        return pre


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = 1
        post = 1
        ans = [1] * n
        for i in range(n):
            ans[i] *= pre
            pre *= nums[i]
            ans[n-i-1] *= post
            post *= nums[n-i-1]
        return ans


