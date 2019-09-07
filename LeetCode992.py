#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


class Solution(object):
    """按奇偶排序数组 II"""
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        """方法一,不开辟新的内存，思路：双指针, 遍历数组, 遇到偶数位则停下来，寻找奇数位是偶数的进行交换
        时间复杂度： O(n)
        空间复杂度：O(1)
        """
        j = 1  # 记录奇数位
        L = len(A)
        for i in range(0, L, 2):  # 遍历偶数位
            if A[i]&1:  # 如果偶数位为奇数则停下来
                while A[j]&1:  # 如果奇数位是奇数则继续往后后面的奇数位找,直到找到奇数位是偶数, 进行交换
                    j += 2
                A[i], A[j] = A[j], A[i]
        return A

    def sortArrayByParityII_2(self, A: List[int]) -> List[int]:
        """方法二,开辟新的内存，思路：2次遍历,找到所有的奇数和偶数,依次放到新数组上即可
        时间复杂度： O(n)
        空间复杂度：O(n)
        """
        N = len(A)
        ans = [None] * N
        t = 0
        for i, x in enumerate(A):  # 第一次遍历，放偶数
            if not x&1:
                ans[t] = x
                t += 2

        t = 1
        for i, x in enumerate(A):  # 第二次遍历，放奇数
            if x&1:
                ans[t] = x
                t += 2

        # We could have also used slice assignment:
        # ans[::2] = (x for x in A if not x%2
        # ans[1::2] = (x for x in A if x%21)
        return ans


if __name__=='__main__':
    A= [4,2,5,7]
    demo = Solution()
    print(demo.sortArrayByParityII(A))
    print(demo.sortArrayByParityII_2(A))


