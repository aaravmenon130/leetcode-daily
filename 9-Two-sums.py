#https://leetcode.com/problems/two-sum/submissions/1840983924/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict(int)
        n = len(nums)

        for i in range(n):
            tar_diff = target - nums[i]
            if (target - nums[i] in d) and (i != d[tar_diff]):
                return [i, d[tar_diff]]
            else:
                d[nums[i]] = i
