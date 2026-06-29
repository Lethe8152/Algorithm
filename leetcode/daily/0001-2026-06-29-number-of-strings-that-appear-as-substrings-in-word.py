"""
[Daily #0001] 2026-06-29
Number of Strings That Appear as Substrings in Word
https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/
(LeetCode 원본 번호: 1967)

난이도: Easy
유형: String, Array

[문제]
문자열 배열 patterns 와 문자열 word 가 주어진다.
patterns 의 원소 중 word 의 '부분 문자열(substring, 연속된 문자열)'로
등장하는 것의 개수를 반환한다. (중복 원소도 각각 센다.)

[예시]
- patterns = ["a","abc","bc","d"], word = "abc"        -> 3  ("a","abc","bc")
- patterns = ["a","b","c"],        word = "aaaaabbbbb" -> 2  ("a","b")
- patterns = ["a","a","a"],        word = "ab"         -> 3  (각각 모두 등장)

[제약]
- 1 <= patterns.length <= 100
- 1 <= patterns[i].length <= 100
- 1 <= word.length <= 100
- patterns[i], word 는 모두 소문자 영어

[접근법]
- 각 pattern 에 대해 `pattern in word` 로 부분 문자열 여부를 확인하고 개수를 센다.
- 파이썬의 `in` 연산자가 substring 검사를 그대로 해준다.

[복잡도]
- n = len(patterns), m = max(len(pattern)), L = len(word)
- 시간: O(n * L * m)  (각 검사가 최악 O(L*m))
- 공간: O(1)
"""

from typing import List


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count = 0
        for pattern in patterns:
            if pattern in word:
                count += 1
        return count


if __name__ == "__main__":
    s = Solution()
    assert s.numOfStrings(["a", "abc", "bc", "d"], "abc") == 3
    assert s.numOfStrings(["a", "b", "c"], "aaaaabbbbb") == 2
    assert s.numOfStrings(["a", "a", "a"], "ab") == 3
    print("OK")
