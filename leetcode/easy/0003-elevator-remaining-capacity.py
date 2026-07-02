"""
[자작 문제 #0001] 엘리베이터 남은 정원
(LeetCode 문제가 아닌, 학습용으로 직접 만든 문제입니다.)

난이도: Easy
유형: Array, Simulation

[문제]
정원이 limit(kg)인 엘리베이터가 있다. 1층에서 사람들이 순서대로 타는데,
각 사람의 몸무게가 배열 weights 에 들어 있다.
앞에서부터 한 명씩 태우되, 태웠을 때 무게 합이 limit 을 '초과'하면
그 사람부터는 태우지 않고 멈춘다.
엘리베이터에 최종적으로 탄 사람 수를 반환하라.

[예시]
- weights = [50, 60, 70], limit = 120  -> 2   (50+60=110 OK, +70=180 초과 → 멈춤)
- weights = [40, 40, 40], limit = 120  -> 3   (전부 태워도 120, 초과 아님)
- weights = [200],        limit = 120  -> 0   (첫 사람부터 초과)
- weights = [],           limit = 100  -> 0   (아무도 없음)

[제약]
- 0 <= len(weights) <= 1000
- 1 <= weights[i] <= 1000
- 1 <= limit <= 100000
- '초과'는 strictly greater. 즉 무게 합이 limit 과 '같으면' 태울 수 있다.

[접근법]
- 현재까지 태운 무게 합 total 을 0에서 시작한다.
- 앞에서부터 한 명씩 더해보고, limit 을 넘으면 즉시 멈춘다(break).
- 넘지 않으면 인원수 count 를 1 늘린다.

[복잡도]
- 시간: O(n)  (최악의 경우 전원 확인)
- 공간: O(1)
"""

from typing import List


class Solution:
    def remainingCapacity(self, weights: List[int], limit: int) -> int: #self는 뭘까?
        total = 0
        count = 0
        for w in weights:
            if total + w > limit:   # 태우면 정원 초과 → 여기서 멈춤
                break
            total += w
            count += 1
        return count


if __name__ == "__main__":
    s = Solution()
    assert s.remainingCapacity([50, 60, 70], 120) == 2
    assert s.remainingCapacity([40, 40, 40], 120) == 3
    assert s.remainingCapacity([200], 120) == 0
    assert s.remainingCapacity([], 100) == 0
    # 경계값: 합이 정확히 limit 과 같으면 태울 수 있어야 한다
    assert s.remainingCapacity([60, 60], 120) == 2
    print("OK")
