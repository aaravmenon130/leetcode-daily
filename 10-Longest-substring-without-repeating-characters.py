#https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        n = len(s)
        se = set()
        maxx = 0

        while i <= j and j < n:
            if s[j] in se:
                while s[j] in se:
                    se.remove(s[i])
                    i += 1
                
            else:
                se.add(s[j])
                j += 1

            maxx = max(maxx, j-i)
        return maxx
