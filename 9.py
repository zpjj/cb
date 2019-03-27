arr=[-1,1,2,-2,3]
if not arr:  # 数组为空，则返回空
   print ("None")
maxsum = int(arr[0])  # 定义为第一个为最大
presum = 0  # 存放之前的累加和
for i in arr:  # 遍历数组中的元素
    if presum < 0:
        presum = int(i)  # 如果之前的累加和小于0，则从当前值进行累加
    else:
        presum += int(i)
        # 如果是大于等于0，则将当前的数加到当前最大子数组中
    if presum > maxsum:
        maxsum = presum
print (maxsum)