"""
[연습] 엘리베이터 남은 정원  (정답 파일: leetcode/easy/0003-elevator-remaining-capacity.py)

이 파일은 '직접 풀어보는 연습용'입니다.
아래 함수 몸통(return 부분)을 스스로 채워보고 실행해서 OK 가 뜨는지 확인하세요.

[문제]
정원이 limit(kg)인 엘리베이터에 앞에서부터 한 명씩 태운다.
태웠을 때 무게 합이 limit 을 '초과(strictly greater)'하면 그 사람부터 안 태우고 멈춘다.
(합이 limit 과 '같으면' 태울 수 있다.)
최종적으로 탄 사람 수를 반환하라.

예시:
- [50, 60, 70], 120 -> 2
- [40, 40, 40], 120 -> 3
- [200],        120 -> 0
"""

from typing import List


class Solution:
    def remainingCapacity(self, weights: List[int], limit: int) -> int:
        total = 0 # 현재까지 채운 무게 합
        count = 0 # 사람 수
        for w in weights:
            if total + w > limit:
                break # total 몸무게가 제한 limit 을 넘으면 정지
            total += w
            count += 1
        return count


# ---- 채점기 (건드리지 마세요) ----
if __name__ == "__main__":
    s = Solution()
    assert s.remainingCapacity([50, 60, 70], 120) == 2
    assert s.remainingCapacity([40, 40, 40], 120) == 3
    assert s.remainingCapacity([200], 120) == 0
    assert s.remainingCapacity([], 100) == 0
    assert s.remainingCapacity([60, 60], 120) == 2
    print("OK")
