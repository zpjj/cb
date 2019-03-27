#!/user/bin/env python
# _*_ coding: utf-8 _*_
a=[1,2,3]
max = a[0]
sum = 0
for i in range(0, len(a) - 1):
        sum += a[i + 1]
        if sum < 0:
            sum = 0
        elif sum > max:
            max = sum
print (max)

