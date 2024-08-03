class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums=nums1+nums2
        nums=sorted(nums)
        total=len(nums)
        if (total%2)==1:
            return float(nums[total//2])
        else:
            mid1=nums[total//2]
            mid2=nums[total//2-1]
            return float(mid1+mid2)/2