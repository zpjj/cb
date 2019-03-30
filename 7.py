#!/user/bin/env python
# _*_ coding: utf-8 _*_
"""
  author:zhangPeiJing  date:On March 30
"""
class Solution:
    #Find the sum of the largest subarrays
 def find_Sum(self,arr):
     # Returns null if the array is empty
    if not arr:
        return
    maxSum=int(arr[0])
    preSum=0
    for i in arr:
        # If the previous sum is less than 0, it is accumulated from the current value
        if preSum<0:
            preSum=int(i)
        else:
            preSum+=int(i)
        #Find the maximum
        if preSum>maxSum:
            maxSum=preSum
    return maxSum
     #Unit test cases
if __name__ == '__main__':
    arrays = [[1, 2, 3, 6, 2], [-2, -4, -1, -3], [-1, 3, 6, 22], [21, 2, -3, -4], []]
    s = Solution()
    for array in arrays:
        print(s.find_Sum(array))