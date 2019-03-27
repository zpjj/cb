#!/user/bin/env python
# _*_ coding: utf-8 _*_
def max_sum(a):
    max = a[0]
    sum = 0
    for i in range(0, len(a) - 1):
        sum += a[i + 1]
        if sum < 0:
            sum = 0
        elif sum > max:
            max = sum
    return max
import unittest
from max import max_sumO
class MaxTestCase(unittest.TestCase):
    def test_first_condition(self):
        max1 = max_sum([-1,2,3,-4])
        self.assertEqual(max1, 5)
    def test_second_condition(self):
        max2 = max_sum([-1,-2,-5,-3,-8])
        self.assertEqual(max2, -1)
if __name__ == "__main__":
    unittest.main()
