class Solution(object):
    def findErrorNums(self, nums):
        seen = set()

        for n in nums:
            if n in seen:
                duplicate = n
            seen.add(n)

        for i in range(1, len(nums) + 1):
            if i not in seen:
                missing = i

        return [duplicate, missing]
