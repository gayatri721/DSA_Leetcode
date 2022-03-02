class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         num3=nums1[:len(nums1)]+nums[len(nums2)-1:]
#         num3.sort()
#         n=len(num3)
#         if len(num3 % 2 != 0):
#             return float(num3[int(n/2)]) 
#         return float((num3[int((n-1)/2)] +num3[int(n/2)])/2.0)
          nums1 = nums1 + nums2
          nums = sorted(nums1)
          n = len(nums)
          m = n//2
          if(n%2 != 0):
            return nums[m]
          return (nums[m] + nums[m - 1])/2