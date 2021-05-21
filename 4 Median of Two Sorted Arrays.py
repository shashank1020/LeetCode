# https://leetcode.com/problems/median-of-two-sorted-arrays/


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums2.extend(nums1)
        nums2.sort()
        mid = len(nums2)//2
        return (nums2[mid]+nums2[~mid])/2


'''
Runtime: 84 ms, faster than 92.71% of Python3 online submissions for Median of Two Sorted Arrays.
Memory Usage: 14.6 MB, less than 20.86% of Python3 online submissions for Median of Two Sorted Arrays.
'''