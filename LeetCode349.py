#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


class Solution(object):
    """求两个数组的交集, 思路：内置方法求集合的交集
    时间复杂度： O(n+m)
    空间复杂度：O(n+m)
    """
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set1 & set2)


if __name__=='__main__':
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    demo = Solution()
    print(demo.intersection(nums1, nums2))
