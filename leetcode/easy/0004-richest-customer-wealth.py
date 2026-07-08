"""
1672. Richest Customer Wealth
https://leetcode.com/problems/richest-customer-wealth/

난이도: Easy
유형: Array, Matrix (2차원 배열)

[문제]
손님별 은행 잔액이 2차원 배열 accounts 로 주어진다.
accounts[i] 는 i번째 손님이 각 은행에 넣은 돈 목록이다.
한 손님의 재산 = 그 손님이 가진 돈의 총합.
가장 부유한 손님의 재산(최댓값)을 반환하라.

[예시]
- [[1,2,3],[3,2,1]]         -> 6   (두 손님 다 합 6)
- [[1,5],[7,3],[3,5]]       -> 10  (2번 손님 7+3=10)
- [[2,8,7],[7,1,3],[1,9,5]] -> 17  (1번 손님 2+8+7=17 이 최대)

[제약]
- 1 <= accounts.length <= 50
- 1 <= accounts[i].length <= 50
- 1 <= accounts[i][j] <= 100

[핵심]
- 2차원 배열이므로 '두 겹'으로 생각한다:
    바깥 = 손님 한 명씩(customer = 리스트),  안쪽 = 그 손님의 돈 하나씩(m = 숫자)
- 각 손님의 재산(합)을 구해 그중 최댓값을 추적한다.

[복잡도]
- 시간: O(m * n)  (손님 수 m, 은행 수 n)
- 공간: O(1)
"""

from typing import List


class Solution:
    # ------------------------------------------------------------------
    # 풀이 1) 내장함수 sum() 사용 — 짧고 파이썬다운 방법
    # ------------------------------------------------------------------
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for customer in accounts:        # customer = [1,2,3] 처럼 '한 손님의 리스트'
            wealth = sum(customer)        # sum()이 리스트 안 숫자들을 한 번에 더해줌
            if wealth > max_wealth:       # 더 부자면 갱신
                max_wealth = wealth
        return max_wealth

    # ------------------------------------------------------------------
    # 풀이 2) 중첩 반복문 — sum() 없이 직접 더하기 (동작은 위와 완전히 동일)
    # ------------------------------------------------------------------
    def maximumWealth_nested(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for customer in accounts:        # 바깥 루프: 손님 한 명씩
            wealth = 0                    # ★ 손님마다 0으로 초기화 (안 하면 재산이 섞임!)
            for m in customer:            # 안쪽 루프: 그 손님의 돈 하나씩
                wealth += m               # 직접 합산 (sum(customer)와 같은 일)
            if wealth > max_wealth:
                max_wealth = wealth
        return max_wealth


# ======================================================================
# 내가 처음 틀렸던 코드 & 왜 틀렸는지 (복습용 기록)
# ----------------------------------------------------------------------
# def maximumWealth(self, accounts):
#     total = 0
#     sum = 0
#     for money in accounts:
#         if total < sum:
#             total = sum
#             sum = 0
#             break          # (3)
#         sum += money       # (1) 여기서 TypeError 발생
#     return total
#
# [무엇이 문제였나]
# (1) money 는 숫자가 아니라 '리스트'였다.
#     accounts=[[1,2,3],[3,2,1]] 일 때 money = [1,2,3] (손님 1명 전체).
#     그래서 int + list 를 시도 -> TypeError: unsupported operand type(s) for +=: 'int' and 'list'
#     => 2차원 배열은 '두 겹'으로 돌아야 하는데 반복이 '한 겹'뿐이었던 게 근본 원인.
#
# (2) 각 손님의 재산은 따로 계산해야 하는데 sum 에 계속 누적해서 손님끼리 섞였다.
#     => 손님마다 wealth 를 0으로 초기화하고, 그 손님 합만 구해서 max 와 비교해야 한다.
#
# (3) break 가 첫 손님에서 바로 탈출시켜 나머지 손님을 아예 못 봤다.
#     => 모든 손님을 끝까지 확인해야 최댓값을 찾을 수 있다.
#
# (4) 변수명 sum 은 파이썬 내장함수 sum() 을 가려버린다 -> 이름 피하기.
# ======================================================================


if __name__ == "__main__":
    s = Solution()
    for fn in (s.maximumWealth, s.maximumWealth_nested):   # 두 풀이 모두 같은 테스트로 채점
        assert fn([[1, 2, 3], [3, 2, 1]]) == 6
        assert fn([[1, 5], [7, 3], [3, 5]]) == 10
        assert fn([[2, 8, 7], [7, 1, 3], [1, 9, 5]]) == 17
    print("OK")
