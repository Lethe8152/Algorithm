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
├── easy/
│   └── 0001-two-sum.py
├── medium/
└── hard/
```

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
