"""
1. Two Sum
https://leetcode.com/problems/two-sum/

난이도: Easy
유형: Array, Hash Table

[접근법]
- 지금까지 본 숫자를 {값: 인덱스} 해시맵에 저장한다.
- 각 숫자 num에 대해 target - num 이 맵에 있으면 정답.

[복잡도]
- 시간: O(n)
- 공간: O(n)
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            need = target - num
            if need in seen:
                return [seen[need], i]
            seen[num] = i
        return []


if __name__ == "__main__":
    assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert Solution().twoSum([3, 2, 4], 6) == [1, 2]
    print("OK")
