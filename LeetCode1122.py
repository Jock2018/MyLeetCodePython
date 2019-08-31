#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


class Solution:
    """数组的相对排序"""
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        """计数排序：核心思想是利用了数组的随机索引特性,数组随机索引时间复杂度为O(1)
        时间复杂度：O(n+m)
        空间复杂度：(1001)"""
        ls = [0] * 1001  # 用于存储arr1中每个数出现的次数
        ans = list()  # 答案
        # 第一步：计数，把arr1的值变为索引,值出现的次数变为对应索引的值,比如3在arr1中出现了4次,那么ls[3]=4
        for n in arr1:  # 第一轮遍历，存储arr值出现的次数
            ls[n] += 1
        # 第二步：遍历arr2，开始存储答案
        for n in arr2:  # 第二轮遍历arr1，把出现在arr2的值，依次添加到ans中
            while ls[n]:  # arr1中出现几次，就往ans添加几次
                ans.append(n)
                ls[n] -= 1  # 添加一次就减1，直到为0
        N = len(ls)
        # 第三步：处理不在arr2，但在arr1的数
        for i in range(N):  # 第三轮遍历ls，把ls中值不为0的索引添加到ans中，值为几就添加几次
            while ls[i]:
                ans.append(i)
                ls[i] -= 1
        return ans


if __name__=='__main__':
    arr1 = [2,3,1,3,2,4,6,7,9,2,19]
    arr2 = [2,1,4,3,9,6]
    demo = Solution()
    print(demo.relativeSortArray(arr1, arr2))



