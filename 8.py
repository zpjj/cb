# _*_ encoding:utf-8 _*_
class Solution:
      def find_sub(self, array):
        """
        sum_p记录当前子组和，当子数组和<0,则重置为0，重新开始计和
        sum_max记录目前出现过最大的子数组和
        """
        if not array:
            return
        sum_p = 0
        sum_max = array[0]
        for number in array:
            sum_p += number
            if sum_p > sum_max:
                sum_max = sum_p
            if sum_p < 0:
                sum_p = 0
        return sum_max
    # 单元测试用例
if __name__ == '__main__':
    arrays = [[1,2,3,6,2],[-2,-4,-1,-3],[-1,3,6,22],[21,2,-3,-4],[]]
    s = Solution()
    print(s.find_sub([]))
    for array in arrays:
        print(s.find_sub(array))
