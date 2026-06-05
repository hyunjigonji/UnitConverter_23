# UnitConverter_23 — RED Session Transcript

**Export date:** 2026-06-05  
**Source:** Cursor Agent 세션 L (첫 Logic Track RED)  
**프로젝트:** UnitConverter_23 — 단위 변환 CLI, ECB, Dual-Track TDD  
**Phase:** RED · **Layer:** entity · **Track:** Logic

---

## Session L — D-LEN-01 RED (Length · entity)

### Turn L0 — `/red-test-plan`

**User:** `/red-test-plan`  
Phase: red | Layer: entity | Track: Logic  
이번 RED 묶음: D-LEN-01 (FR-01-1, FR-01-4, AC-01)  
C2C 추적표 · Track B 설계표 · 테스트 플랜 · ECB·Mock 점검 작성.  
`tests/`·`src/` 파일은 만들지 말 것.

**Cursor:**

| 산출물 | 내용 |
|--------|------|
| C2C Rule 1 | FR-01-1 · FR-01-4 · AC-01 PRD 원문 인용 |
| C2C Rule 2 | To-Do T-01: assert 범위 A(8단위) vs B(cm 단일) → **B 권장** |
| C2C Rule 3 | D-LEN-01 Given/When/Then — `Quantity("meter", 1.0)` → `cm:100` |
| Track B 표 | `Converter.convert()` · Expected RED: `ModuleNotFoundError` |
| 테스트 플랜 | `tests/entity/test_d_len_01.py` · `test_d_len_01_meter_to_centimeter` |
| RED 묶음 | D-LEN-01 ~ D-LEN-03 (본 턴: D-LEN-01만) |
| ECB·Mock | Logic Mock 금지 · entity E001~E005 출력 금지 |
| 승인 | **승인 가능** — `/red-skeleton` 준비 완료 |

**제약 준수:** `src/`·`tests/` 파일 **미생성**

---

### Turn L1 — `/red-skeleton`

**User:** `/red-skeleton`  
Phase: red | Layer: entity | Track: Logic  
Test ID: D-LEN-01  
파일: `tests/entity/test_d_len_01.py`  
픽스처: `tests/conftest.py` (`sample_meter_input` — `"meter:1"`)  
규칙: AAA 주석 · `pytest.fail` 한 줄 · assert/skip/xfail/통과더미 금지 · `src/` 수정 금지

**Cursor:**

| 파일 | 내용 |
|------|------|
| `tests/conftest.py` | `@pytest.fixture sample_meter_input → "meter:1"` |
| `tests/entity/test_d_len_01.py` | `test_d_len_01_meter_to_centimeter` — 의도적 `pytest.fail` |

**pytest 실행:**

```bash
python -m pytest tests/entity/test_d_len_01.py::test_d_len_01_meter_to_centimeter -v
```

**결과:** `1 failed in 0.11s`

```
Failed: RED: D-LEN-01 — meter→centimeter 변환 미구현, 의도적 실패
```

**제약 준수:** `src/` **무변경** · assert 본문 없음 · skip/xfail 없음

---

### Turn L2 — Export 요청

**User:** `02_Prompt_Red.md` · `02_Report_Red.md` 생성

**Cursor:** 본 Transcript · RED 보고서 작성

---

## 세션 타임라인 (누적)

```
Session A~K  Governance · Spec · Command · Docs     → 01_Report · 01_Prompt
Session L    첫 Logic Track RED — D-LEN-01          → 02_Report · 02_Prompt ← 본 Export
STEP 3+      /green — src/entity 최소 구현
```

---

## 파일 트리 (Export 시점)

```
UnitConverter_23/
├── .cursor/
│   ├── commands/          spec · red · green · refactor
│   ├── rules/             unitconverter-*.mdc (6)
│   └── skills/unit-converter-tdd/
├── docs/
│   ├── PRD.md
│   └── ARCHITECTURE.md
├── reports/
│   ├── 01_Report_Spec.md
│   └── 02_Report_Red.md          ← 신규
├── prompts/
│   ├── 01_Prompt_Spec.md
│   └── 02_Prompt_Red.md          ← 신규
├── tests/                        ← 신규
│   ├── conftest.py
│   └── entity/
│       └── test_d_len_01.py
├── AGENTS.md
├── UnitConverter.py
└── README.md
```

**미구현:** `src/` · D-LEN-02~03 · GREEN · REFACTOR

---

## Command 워크플로 (본 세션)

```
/red-test-plan  →  /red-skeleton  →  (다음) /green
```

| Command | 본 세션 수행 | 산출 |
|---------|-------------|------|
| `/red-test-plan` | ✅ | C2C · 설계표 · 플랜 (파일 없음) |
| `/red-skeleton` | ✅ | `tests/` 2파일 · pytest FAIL |
| `/green` | ⏳ | — |
| `/refactor` | ⏳ | — |

---

## Open Items (Transcript 종료 시)

| # | 항목 | 상태 |
|---|------|------|
| O1 | 같은 카테고리만 출력? | PRD AC-02 · 사용자 확인 권장 |
| O2 | Temperature 전략 | ARCHITECTURE · 확인 권장 |
| O3 | pyeong 계수 | 미확정 |
| O4 | Length first vs 전체 | **D-LEN-01 RED 착수** (Length first 진행 중) |
| O5 | U-* 카탈로그 | STEP 3 |
| O8 | src/ + 첫 RED | **D-LEN-01 RED 완료** · GREEN 대기 |
| O9 | T-01 assert 범위 | **B(cm 단일)** 확정 — `/red-test-plan` |

---

## TDD RED 템플릿 (확정)

```python
def test_d_len_01_meter_to_centimeter(sample_meter_input):
    # Given: meter:1 입력
    # When: convert(sample_meter_input) 호출
    # Then: cm:100 포함
    pytest.fail(
        "RED: D-LEN-01 — meter→centimeter 변환 미구현, 의도적 실패"
    )
```

---

## 종료 메모

- STEP 3 첫 RED: **D-LEN-01** (entity · Logic) — `pytest.fail` 의도적 FAIL 확인.
- C2C: FR-01-1 · FR-01-4 · AC-01(부분) 추적.
- 다음: `/green` — `src/unitconverter/entity/` 최소 구현 후 assert 본문 교체.
