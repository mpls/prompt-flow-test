# prompt-flow-test — 영혼 문서

## 이 프로젝트는 무엇인가

프롬프트 플로우 테스트용 Python 유틸리티 라이브러리.
에이전트가 이슈를 자동 처리하는 플로우를 검증하기 위한 테스트 리포지토리.

## 문서 구조

```
prompt-flow-test/
├── CLAUDE.md      # 영혼 문서 — 프로젝트 규칙과 컨텍스트
├── PROGRESS.md    # 진행 상황
├── PLAN.md        # 다음 작업
├── src/           # 소스 코드
├── tests/         # 테스트 코드
└── pyproject.toml # 프로젝트 설정
```

## 에이전트 세션 규칙

- **읽기 순서**: CLAUDE.md → PROGRESS.md → PLAN.md
- 새 세션에서 "어디까지 했나" 묻지 말 것 — 위 파일을 읽으면 알 수 있음
- PROGRESS.md는 작업 완료 시 갱신
- PLAN.md는 다음 작업을 항상 최신 상태로 유지

## 기술 스택

- Python 3.12+
- pytest

## Git 규칙

- commit 메시지: https://cbea.ms/git-commit/ + 한국어
- Feature 완료 단위로 commit
