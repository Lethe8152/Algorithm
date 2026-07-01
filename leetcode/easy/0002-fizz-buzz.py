"""
412. Fizz Buzz
https://leetcode.com/problems/fizz-buzz/

난이도: Easy
유형: Math, String, Simulation

[문제]
정수 n 이 주어질 때, 1부터 n 까지의 문자열 배열 answer 를 반환한다.
- 3과 5로 모두 나누어지면 "FizzBuzz"
- 3으로만 나누어지면 "Fizz"
- 5로만 나누어지면 "Buzz"
- 그 외에는 그 숫자 자체를 문자열로

[예시]
- n = 3  -> ["1", "2", "Fizz"]
- n = 5  -> ["1", "2", "Fizz", "4", "Buzz"]
- n = 15 -> ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

[접근법]
- 1부터 n 까지 반복하며 나머지(%) 로 배수 여부를 판단한다.
- 3과 5의 공배수(=15의 배수)를 먼저 검사하는 것이 핵심.

[복잡도]
- 시간: O(n)
- 공간: O(n)  (결과 배열)
"""

from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[int]:
        answer = []
        for i in range(1, n + 1):   # range(1, n+1) → 1, 2, ..., n (끝값은 포함 안 됨)
            if i % 15 == 0:         # % 는 나머지 연산자. 나머지가 0이면 나누어떨어짐
                answer.append("FizzBuzz")
            elif i % 3 == 0:
                answer.append("Fizz")
            elif i % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i))   # str(i): 숫자를 문자열로 변환 (JS의 String(i))
        return answer


if __name__ == "__main__":
    s = Solution()
    assert s.fizzBuzz(3) == ["1", "2", "Fizz"]
    assert s.fizzBuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]
    assert s.fizzBuzz(15) == [
        "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz",
        "Buzz", "11", "Fizz", "13", "14", "FizzBuzz",
    ]
    print("OK")
