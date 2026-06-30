"""
[Daily #0002] 2026-06-30
Number of Substrings Containing All Three Characters
https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/
(LeetCode 원본 번호: 1358)

난이도: Medium
유형: Hash Table, String, Sliding Window

[문제]
'a', 'b', 'c' 로만 이루어진 문자열 s 가 주어진다.
'a', 'b', 'c' 를 모두 최소 1개씩 포함하는 부분 문자열(substring)의 개수를 반환한다.

[예시]
- s = "abcabc" -> 10
- s = "aaacb"  -> 3
- s = "abc"    -> 1

[제약]
- 3 <= s.length <= 5 * 10^4
- s 는 'a', 'b', 'c' 로만 구성된다

[접근법]
- 오른쪽 끝 인덱스 i 를 하나씩 늘려가며, 각 글자가 마지막으로 등장한 위치(last_seen)를 갱신한다.
- i 를 오른쪽 끝으로 하는 substring 이 'a','b','c' 를 모두 포함하려면,
  왼쪽 끝은 세 글자의 '가장 최근 등장 위치들 중 최소값' j 이하여야 한다.
  (왼쪽 끝이 j 보다 커지면 셋 중 하나가 빠지기 때문)
- 따라서 왼쪽 끝으로 가능한 인덱스는 0..j 이며, i 를 끝으로 하는 유효 substring 은 j + 1 개다.
- 모든 i 에 대해 j + 1 을 누적하면 답이 된다.

[복잡도]
- n = len(s)
- 시간: O(n)  (각 글자 1회 방문)
- 공간: O(1)  (last_seen 은 항상 글자 3개)
"""


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last_seen = {'a': -1, 'b': -1, 'c': -1}  
        count = 0

        for i, ch in enumerate(s): #목록에 자동으로 번호(인덱스)를 매겨주는 함수
                                    #JS의 for (let i=0; ...; i++)처럼 직접 카운터를 만들고 i++로 늘리는 작업을 파이썬에서는 enumerate가 자동으로 처리해줌
                                    #for i, ch in enumerate(s): → i는 위치, ch는 글자
          
            last_seen[ch] = i   # 현재 글자의 마지막 등장 위치 갱신
            j = min(last_seen['a'], last_seen['b'], last_seen['c']) #괄호 안 값들 중 가장 작은 값을 반환 ex) min(3, 7, 1) → 1
            count += j + 1       # j+1개의 부분문자열이 조건 만족

        return count


if __name__ == "__main__":
    s = Solution()
    assert s.numberOfSubstrings("abcabc") == 10
    assert s.numberOfSubstrings("aaacb") == 3
    assert s.numberOfSubstrings("abc") == 1
    print("OK")
