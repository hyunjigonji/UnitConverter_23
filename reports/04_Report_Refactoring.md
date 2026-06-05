# UnitConverter_23 — REFACTOR Phase Report

**문서 ID:** 04.UnitConverter_REFACTOR_Report  
**프로젝트:** UnitConverter_23  
**단계:** STEP 4 — REFACTOR (R1 · LENGTH_UNITS 이중 순회 중복 제거)  
**버전:** 0.1  
**일자:** 2026-06-05  
**근거:** Cursor Agent 세션 R · `/refactor-smell` · `/refactor-safe`

---

## 1. Executive Summary

UnitConverter_23에서 GREEN 완료 직후 **동작 불변 REFACTOR** 1건(R1)을 수행했다.  
`/refactor-smell` 스캔 → R1 선택 → `Converter.convert_ordered()` extract → 전체 회귀 **14 passed** 유지.

| 항목 | 상태 |
|------|------|
| **선택 스멜** | R1 — Duplicated Code (`LENGTH_UNITS` 순회·출력 조립 2곳 분산) |
| **Phase** | REFACTOR |
| **Layer** | entity (+ control 1파일 연동) |
| **Track** | Logic (+ UI Golden 회귀 확인) |
| **변경 파일** | 2 (`converter.py`, `convert_use_case.py`) |
| **extract 메서드** | 1 (`convert_ordered`) |
| **pytest** | **14 passed, 0 failed** (REFACTOR 전·후 동일) |
| **Golden (U-OUT-01)** | matched |
| **동작 변경** | 없음 |
| **다음 RED 진입** | ✅ 가능 |

---

## 2. 범위

### 2.1 In Scope (완료)

| 항목 | 산출물 |
|------|--------|
| GREEN 전제 확인 | `python -m pytest tests/ -v` → 14 passed |
| 스멜 스캔 | `/refactor-smell` — P0/P1/P2 표 · 후보 3건 선정 |
| REFACTOR R1 | `convert_ordered()` extract · control `LENGTH_UNITS` import 제거 |
| ECB · SSOT 검사 | import 방향 유지 · `conversion_factors.py` 계수 중복 없음 |
| 회귀 검증 | Logic 13 + UI 1 = **14 passed** |
| Export | `04_Report_Refactoring.md` · `04_Prompt_Refactoring.md` |

### 2.2 Out of Scope (미착수 · 후속)

| 항목 | 비고 |
|------|------|
| R2 `ConvertResult` 도입 | Primitive Obsession — 별도 REFACTOR 또는 RED/GREEN |
| R3 `UnitRegistry` SSOT 통합 | `conversion_factors.py` 흡수 — 별도 REFACTOR |
| R4 control → entity SSOT import 정리 | R1에서 `LENGTH_UNITS` import 제거로 부분 해소 |
| tests `LENGTH_UNITS` 중복 | `test_d_len_10/12` 로컬 set — 후속 REFACTOR |
| `sample_meter_input` Dead Code | `conftest.py` — 후속 REFACTOR |
| D-I01~D-I04 (입력 검증) | entity `InputValidator` RED/GREEN |
| AC-04 (E001~E004) | control/boundary 오류 처리 |
| git commit | 사용자 요청 시만 |

---

## 3. `/refactor-smell` 스캔 결과

### 3.1 전제

```bash
python -m pytest tests/ -v
# 14 passed in 0.14s ✅
```

### 3.2 P0 스멜

| 우선순위 | 스멜 | 위치 | 판정 |
|---------|------|------|------|
| — | **해당 없음** | — | ECB 위반·계수 이중 SSOT·Long Method·boundary 변환 침범 없음 |

### 3.3 P1 스멜 (요약)

| # | 스멜 | 위치 | Budget 적합 |
|---|------|------|-------------|
| **R1** | Duplicated Code — `LENGTH_UNITS` 순회 2곳 | `converter.py`, `convert_use_case.py` | ✅ **선택** |
| — | Output Formatting Duplication | `convert_use_case.py`, `output_formatter.py` | ✅ |
| — | SSOT 위반 (tests 단위 문자열) | `test_d_len_10.py`, `test_d_len_12.py` | ✅ |
| — | Validation 위치 부적절 | `convert_use_case.py:execute` | ❌ (RED 대기) |
| — | Feature Envy (OUTPUT_PRECISION in entity) | `converter.py`, `conversion_factors.py` | ❌ (동작 변경) |

### 3.4 P2 스멜 (요약)

| 스멜 | 위치 |
|------|------|
| Dead Code | `conftest.py:sample_meter_input` |
| 테스트 보일러플레이트 중복 | `test_d_len_01~13.py` |
| Mysterious Name (`raw`) | `convert_use_case.py`, `output_presenter.py` |
| 과잉 추상화 | `convert_gateway.py` (pass-through) |

---

## 4. REFACTOR R1 — 구현표

### 4.1 변경 전 (Before)

**문제:** `LENGTH_UNITS` 순회가 entity(`Converter.convert`)와 control(`ConvertInputUseCase.execute`) 2곳에 분산.

```python
# converter.py — dict 빌드 루프
for unit in LENGTH_UNITS:
    value = base_meters / METERS_PER_UNIT[unit]
    ...

# convert_use_case.py — lines 포맷 루프 (LENGTH_UNITS 재순회)
lines = [f"{name}:{format_value(result[name])}" for name in LENGTH_UNITS]
```

### 4.2 변경 후 (After)

| 파일 | 변경 | 책임 |
|------|------|------|
| `entity/converter.py` | `convert_ordered()` extract | `LENGTH_UNITS` 순회 SSOT (단일 루프) |
| `entity/converter.py` | `convert()` → dict comprehension | 공개 API 시그니처 유지 |
| `control/convert_use_case.py` | `convert_ordered()` 소비 | lines 조립만 (SSOT import 제거) |

**핵심 API (추가):**

```python
Converter().convert_ordered(Quantity("meter", 2.5))
# [("mm", 2500.0), ("cm", 250.0), ("meter", 2.5), ...]
```

**공개 API (유지):**

```python
Converter().convert(Quantity("meter", 2.5)) -> dict[str, float]
# {"mm": 2500.0, "cm": 250.0, "meter": 2.5, ...}
```

### 4.3 Change Budget 준수

| 항목 | Budget | 실제 |
|------|--------|------|
| 파일 | ≤ 3 | **2** |
| 클래스 | ≤ 1 | **0** (메서드만) |
| 함수/메서드 extract | ≤ 3 | **1** (`convert_ordered`) |

---

## 5. 동작 동결 검증

### 5.1 변환 결과 (Logic Track)

| 검증 | Before | After | 판정 |
|------|--------|-------|------|
| `convert()` 반환 타입 | `dict[str, float]` | 동일 | ✅ |
| `OUTPUT_PRECISION` 반올림 | inch/feet/yard/mile | 동일 | ✅ |
| D-LEN-01~13 assert | 13건 PASS | 13건 PASS | ✅ |

### 5.2 출력 (UI Track)

| 검증 | Before | After | 판정 |
|------|--------|-------|------|
| U-OUT-01 Golden | matched | matched | ✅ |
| `LENGTH_UNITS` 순서 | mm → mile | 동일 | ✅ |
| `format_value()` 포맷 | trailing zero 없음 | 동일 | ✅ |

**Golden 출력 (불변):**

```
mm:2500
cm:250
meter:2.5
km:0.0025
inch:98.4252
feet:8.2021
yard:2.734
mile:0.001553
```

---

## 6. pytest 결과

### 6.1 REFACTOR 전 (GREEN Exit)

```bash
python -m pytest tests/ -v
```

| 항목 | 값 |
|------|-----|
| collected | 14 |
| passed | **14** |
| failed | 0 |

### 6.2 REFACTOR 후 (회귀)

```bash
python -m pytest tests/ -v
python -m pytest tests/boundary/test_u_out_01.py -v
```

| 항목 | 값 |
|------|-----|
| collected | 14 |
| passed | **14** |
| failed | 0 |
| Golden diff | **없음** |
| 소요 시간 | ~0.05s |

---

## 7. REFACTOR 완료 체크리스트

### 7.1 TDD REFACTOR 규칙

- [x] GREEN 전제 확인 (14 passed) 후 REFACTOR 시작
- [x] assert 삭제·완화·skip·xfail 없음
- [x] 새 기능·새 테스트 추가 없음
- [x] 공개 `convert()` 시그니처·반환값 불변
- [x] entity E001~E007 emit·raise 없음

### 7.2 ECB 규칙

- [x] entity → control/boundary import 없음
- [x] control → entity만 import (`Converter`, `Quantity`)
- [x] boundary → control만 import (entity 직접 import 없음)
- [x] control에서 `LENGTH_UNITS` SSOT 직접 import **제거** (R4 부분 해소)

### 7.3 SSOT

- [x] Length 변환 계수 — `conversion_factors.py` 단일 정의 (변경 없음)
- [x] `LENGTH_UNITS` 순회 — entity `convert_ordered()` **1곳**
- [ ] `UnitRegistry` 통합 — 후속 REFACTOR (R3)
- [ ] tests `LENGTH_UNITS` 로컬 set — 후속 REFACTOR

### 7.4 REFACTOR Exit Criteria

- [x] REFACTOR 전·후 pytest 14 passed
- [x] U-OUT-01 Golden matched
- [x] 동작·API·출력 불변
- [x] Change Budget 준수 (파일 2, 메서드 1)
- [x] **다음 RED 진입 가능**

---

## 8. 갭 분석 (REFACTOR 직후)

| 항목 | GREEN 후 | REFACTOR 후 |
|------|----------|-------------|
| `LENGTH_UNITS` 순회 | converter + use_case 2곳 | entity `convert_ordered()` 1곳 ✅ |
| control SSOT import | `LENGTH_UNITS` 직접 참조 | 제거 ✅ |
| `ConvertResult` | 미구현 | 미구현 (R2 후속) |
| `UnitRegistry` | 미구현 | 미구현 (R3 후속) |
| 입력 검증 (E001~E004) | 미구현 | 미구현 (D-I RED) |
| tests SSOT 중복 | `test_d_len_10/12` | 미변경 (후속) |

---

## 9. Open Items

| ID | 항목 | 상태 |
|----|------|------|
| O1 | 출력 범위 — 같은 카테고리만? | D-LEN-12 ✅ · U-OUT-01 ✅ |
| O2 | Temperature 비선형 전략 | ARCHITECTURE · 확인 권장 |
| O3 | pyeong ↔ sqm | 미확정 |
| O4 | Length first | D-LEN-01~13 GREEN ✅ · REFACTOR R1 ✅ |
| O5 | U-* 카탈로그 | U-OUT-01 1건 ✅ · 확장 ⏳ |
| O10 | REFACTOR R2~R4 | R1 ✅ · R2/R3/R4 후속 |
| O11 | tests SSOT 중복 | `test_d_len_10/12` — 후속 REFACTOR |

---

## 10. 성공 기준

| ID | 기준 | 판정 |
|----|------|------|
| SC5-1 | REFACTOR 전·후 pytest 14 passed | ✅ |
| SC5-2 | U-OUT-01 Golden matched | ✅ |
| SC5-3 | `convert()` API·반환값 불변 | ✅ |
| SC5-4 | ECB import 방향 위반 0건 | ✅ |
| SC5-5 | assert 완화·skip·xfail 없음 | ✅ |
| SC5-6 | Change Budget 준수 | ✅ |
| SC5-7 | R1 스멜 1건만 수행 | ✅ |
| SC5-8 | REFACTOR Exit Criteria §7 충족 | ✅ |

---

## 11. 다음 단계

- [ ] **D-I01 RED** — entity `InputValidator` 입력 검증 (E001~E004)
- [ ] REFACTOR R2 — `ConvertResult` 도입 (`dict[str, float]` → 결과 타입)
- [ ] REFACTOR R3 — `UnitRegistry` SSOT 통합
- [ ] REFACTOR (tests) — `test_d_len_10/12` `LENGTH_UNITS` SSOT import
- [ ] U-* 확장 — CLI stdin/stdout · 오류 출력 (AC-06)

**다음 RED pytest (예상):**

```bash
python -m pytest tests/ -v
# 14 passed 유지 + D-I01 FAIL 1건 추가
```

---

## 12. 참고

| 문서 | 경로 |
|------|------|
| PRD | `docs/PRD.md` |
| Architecture | `docs/ARCHITECTURE.md` |
| REFACTOR Command | `.cursor/commands/refactor.md` |
| 이전 Report | `reports/03_Report_Green.md` |
| Transcript | `prompts/04_Prompt_Refactoring.md` |
