"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.

Example 1:
nums1 = [1, 3]
nums2 = [2]
The median is 2.0

Example 2:
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
"""
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        p, q = 0, 0
        ans = []
        while p < len(nums1) and q < len(nums2):
            if nums1[p] < nums2[q]:
                ans.append(nums1[p])
                p += 1
            else:
                ans.append(nums2[q])
                q += 1
        ans.extend(nums2[q:])
        ans.extend(nums1[p:])

        mid = len(ans) // 2
        if len(ans)%2:
            return ans[mid] * 1.
        else:
            return (ans[mid - 1] + ans[mid]) / 2

if __name__ == '__main__':
    nums1, nums2 = [1, 2], [3, 4]
    s = Solution().findMedianSortedArrays(nums1, nums2)
    print(s)
