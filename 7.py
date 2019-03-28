#!/user/bin/env python
# _*_ coding: utf-8 _*_
class Solution:
    #找到最大子数组和
 def find_Sum(self,arr):
    if not arr:         #数组为空，则返回空
        return
    maxSum=int(arr[0])  #定义为第一个为最大
    preSum=0            #存放之前的累加和
    for i in arr:      #遍历数组中的元素
        if preSum<0:   #如果之前的累加和小于0，则从当前值进行累加
            preSum=int(i)
        else:
            preSum+=int(i)
        if preSum>maxSum:
            maxSum=preSum
    return maxSum
     #单元测试用例
if __name__ == '__main__':
    arrays = [[1, 2, 3, 6, 2], [-2, -4, -1, -3], [-1, 3, 6, 22], [21, 2, -3, -4], []]
    s = Solution()
    for array in arrays:
        print(s.find_Sum(array))