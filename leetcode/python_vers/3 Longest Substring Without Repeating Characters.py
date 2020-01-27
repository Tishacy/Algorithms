"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

Sliding Window
Back to our problem. We use HashSet to store the characters in current window [i, j)(j = i initially). Then we slide the index j to the right. If it is not in the HashSet, we slide j further. Doing so until s[j] is already in the HashSet. At this point, we found the maximum size of substrings without duplicate characters start with index i. If we do this for all i, we get our answer.

Complexity Analysis
- Time complexity : O(2n) = O(n). In the worst case each character will be visited twice by i and j.
- Space complexity : O(min(m, n)). Same as the previous approach. We need O(k) space for the sliding window, where k is the size of the Set. The size of the Set is upper bounded by the size of the string n and the size of the charset/alphabet m.
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlen = 0
        for i, c in enumerate(s):
            substr = ""
            # sliding window
            for j, b in enumerate(s[i:]):
                if b not in substr:
                    substr += b
                else:
                    maxlen = len(substr) if len(substr) > maxlen else maxlen
                    break
                maxlen = len(substr) if len(substr) > maxlen else maxlen
        return maxlen

if __name__=="__main__":
    str = "pwwkew"
    s = Solution().lengthOfLongestSubstring(str)
    print(s)
