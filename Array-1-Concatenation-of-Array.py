#https://leetcode.com/problems/concatenation-of-array/description/?envType=problem-list-v2&envId=dsa-linear-shoal-array-i
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums.copy()
        for i in nums:
            ans.append(i)
        return ans
