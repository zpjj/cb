#!/user/bin/env python
# _*_ coding: utf-8 _*_
class Solution:
 def find_sub(self,arr):
    if not arr:   #数组为空，则返回空
        return
    maxsum=int(arr[0])#定义为第一个为最大
    presum=0   #存放之前的累加和
    for i in arr:#遍历数组中的元素
        if presum<0:
            presum=int(i) #如果之前的累加和小于0，则从当前值进行累加
        else:
            presum+=int(i)
            #如果是大于等于0，则将当前的数加到当前最大子数组中
        if presum>maxsum:
            maxsum=presum
    return maxsum
     #单元测试用例
if __name__ == '__main__':
    arrays = [[1, 2, 3, 6, 2], [-2, -4, -1, -3], [-1, 3, 6, 22], [21, 2, -3, -4], []]
    s = Solution()
    for array in arrays:
        print(s.find_sub(array))