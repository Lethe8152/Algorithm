# Algorithm

알고리즘 공부 저장소입니다.

## 목적

- 알고리즘 문제 풀이 기록
- 자료구조 및 알고리즘 개념 정리

## 폴더 구조

LeetCode 풀이는 **난이도별**로 정리합니다. 언어는 Python입니다.

```
leetcode/
├── TEMPLATE.py        # 새 풀이 작성용 템플릿
├── daily/             # 데일리 챌린지 (풀이순 번호 + 날짜)
│   └── 0001-2026-06-29-number-of-strings-that-appear-as-substrings-in-word.py
├── easy/
│   └── 0001-two-sum.py
├── medium/
└── hard/
```

> 데일리 챌린지는 LeetCode 원본 번호 대신 **`풀이순 번호(0001) + 푼 날짜`** 로 파일명을 지어
> 언제 푼 문제인지 바로 알아볼 수 있게 합니다.

- 파일명: `<4자리 번호>-<문제-제목-kebab-case>.py` (예: `0001-two-sum.py`)
- 각 파일 상단 docstring에 문제 링크 / 접근법 / 복잡도를 기록합니다.

## 새 문제 푸는 방법

1. `leetcode/TEMPLATE.py`를 복사해 해당 난이도 폴더에 `번호-제목.py`로 저장
2. 풀이 작성 후 `python 파일명.py`로 테스트
3. 아래 표에 한 줄 추가
4. `git add . && git commit -m "Solve N. 제목" && git push`

## 풀이 목록

| # | Title | Difficulty | Solution |
|---|-------|-----------|----------|
| 1 | Two Sum | Easy | [Python](./leetcode/easy/0001-two-sum.py) |
| 2 | Fizz Buzz | Easy | [Python](./leetcode/easy/0002-fizz-buzz.py) |

## 데일리 챌린지 목록

| 풀이# | 날짜 | Title | Difficulty | Solution |
|------|------|-------|-----------|----------|
| 0001 | 2026-06-29 | Number of Strings That Appear as Substrings in Word | Easy | [Python](./leetcode/daily/0001-2026-06-29-number-of-strings-that-appear-as-substrings-in-word.py) |
| 0002 | 2026-06-30 | Number of Substrings Containing All Three Characters | Medium | [Python](./leetcode/daily/0002-2026-06-30-number-of-substrings-containing-all-three-characters.py) |
