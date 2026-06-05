# UnitConverter_23 — RED Phase Report

**문서 ID:** 02.UnitConverter_RED_Report  
**프로젝트:** UnitConverter_23  
**단계:** STEP 3 — Logic Track RED (FR-01 Length · entity)  
**버전:** 0.2  
**일자:** 2026-06-05  
**근거:** Cursor Agent 세션 L · `/red-test-plan` · `/red-skeleton` · `/red-skeleton-all` · `/checklist-generate`

---

## 1. Executive Summary

UnitConverter_23에서 **FR-01 Length Conversion** entity Logic Track **RED 전 범위**를 완료했다.  
D-LEN-01 ~ D-LEN-13 C2C 설계·RED 스켈레톤·의도적 pytest FAIL(13건)을 확인했다.

| 항목 | 상태 |
|------|------|
| **Target** | D-LEN-01 ~ D-LEN-13 |
| **Phase** | RED |
| **Layer** | entity |
| **Track** | Logic |
| **pytest** | **13 failed** (의도적) |
| **`src/`** | 미생성 (GREEN 대기) |
| **`tests/`** | 14파일 (`conftest.py` + 13 × `test_d_len_NN.py`) |
| **GREEN 진입** | ✅ 가능 — Target: **D-LEN-01** |

---

## 2. 범위

### 2.1 In Scope (완료)

| 항목 | 산출물 |
|------|--------|
| C2C 추적 | FR-01 · AC-01/02/03/07/09 · NFR-01/02 → D-LEN-01~13 |
| RED 테스트 카탈로그 | 13건 Given-When-Then 설계 |
| RED 스켈레톤 | `tests/conftest.py` · `tests/entity/test_d_len_01.py` ~ `test_d_len_13.py` |
| pytest FAIL 확인 | 전건 `pytest.fail` 의도적 실패 |
| RED 완료 체크리스트 | 본 Report §8 |
| Export | `02_Report_Red.md` · `02_Prompt_Red.md` |

### 2.2 Out of Scope (미착수 · 후속 Track)

| 항목 | 비고 |
|------|------|
| `src/` entity 구현 | `/green` |
| assert 본문 | GREEN에서 `pytest.fail` → assert 교체 |
| D-S01 (SSOT) | 별도 RED 묶음 |
| D-I01~D-I04 (입력 검증) | entity InputValidator RED |
| AC-06 · AC-07 (출력 형식) | U-* UI Track |
| AC-05 전체 (10건×2회) | D-LEN-03 + U-* |
| REFACTOR | GREEN 이후 |
| UI Track (U-*) | 미착수 |

---

## 3. C2C 추적

### 3.1 FR → AC → D-LEN (entity Logic Track)

| FR | AC / NFR | D-LEN Test ID | entity 검증 범위 |
|----|----------|---------------|------------------|
| **FR-01-1** | **AC-01** | D-LEN-01, D-LEN-04~10, D-LEN-13 | 단위별 변환값·8단위 집합 |
| **FR-01-1** | **AC-07** | D-LEN-11 | 동일 단위 identity |
| **FR-01-1** | **NFR-02** | D-LEN-01~09, D-LEN-02, D-LEN-13 | 표준 계수 정확성 |
| **FR-01-2** | **AC-01** | D-LEN-10 | Length 8단위 전체 반환 |
| **FR-01-2** | **AC-03** (Length 행) | D-LEN-10 | 출력 단위 집합 = Length 전체 |
| **FR-01-3** | **AC-02** | D-LEN-12 | 결과 단위 ⊆ Length 8종 |
| **FR-01-4** | **AC-09** | D-LEN-02, D-LEN-13 | Base Unit(meter) 경유 |
| **FR-01-4** | **NFR-05** | D-LEN-02 | Base 경유 변환 (D-S01 별도) |
| **NFR-01** | **AC-05** (부분) | D-LEN-03 | 동일 입력 2회 동일 결과 |
| **FR-01-5** | — | *(해당 없음)* | Temperature — Length RED 제외 |

### 3.2 reference.md 대응

| reference ID | D-LEN ID | Given-When-Then |
|--------------|----------|-----------------|
| D-L01 | D-LEN-01 | meter → cm 결정적 변환 |
| D-L02 | D-LEN-02 | feet → inch (Base Unit 경유) |
| D-L03 | D-LEN-03 | 동일 입력 반복 시 동일 출력 |

### 3.3 구현 결정 (To-Do T-01)

| 항목 | 결정 |
|------|------|
| assert 범위 (D-LEN-01) | **B — cm 단일 검증** (RED 1건 원칙) |
| AC-01 전체 8단위 | **D-LEN-10** 집합 검증 |
| Act 대상 | `Converter.convert(Quantity(...))` — entity API |
| 파일 구조 | 1 Test ID = 1 파일 (`test_d_len_NN.py`) |

---

## 4. RED 설계표

| Test ID | 파일 | Given → Then | PRD Trace |
|---------|------|--------------|-----------|
| **D-LEN-01** | `test_d_len_01.py` | `Quantity("meter", 1.0)` → `cm:100` | FR-01-1 · FR-01-4 · AC-01 |
| **D-LEN-02** | `test_d_len_02.py` | `Quantity("feet", 1.0)` → `inch:12` (Base 경유) | FR-01-4 · AC-09 |
| **D-LEN-03** | `test_d_len_03.py` | `Quantity("meter", 2.5)` × 2회 → 동일 결과 | NFR-01 · AC-05 |
| **D-LEN-04** | `test_d_len_04.py` | `Quantity("meter", 2.5)` → `km:0.0025` | FR-01-1 · AC-01 |
| **D-LEN-05** | `test_d_len_05.py` | `Quantity("meter", 2.5)` → `mm:2500` | FR-01-1 · AC-01 |
| **D-LEN-06** | `test_d_len_06.py` | `Quantity("meter", 2.5)` → `inch:98.4252` | FR-01-1 · NFR-02 |
| **D-LEN-07** | `test_d_len_07.py` | `Quantity("meter", 2.5)` → `feet:8.2021` | FR-01-1 · NFR-02 |
| **D-LEN-08** | `test_d_len_08.py` | `Quantity("meter", 2.5)` → `yard:2.734` | FR-01-1 · NFR-02 |
| **D-LEN-09** | `test_d_len_09.py` | `Quantity("meter", 2.5)` → `mile:0.001553` | FR-01-1 · NFR-02 |
| **D-LEN-10** | `test_d_len_10.py` | `Quantity("meter", 2.5)` → 8단위 전체 집합 | FR-01-2 · AC-01 · AC-03 |
| **D-LEN-11** | `test_d_len_11.py` | `Quantity("meter", 2.5)` → `meter:2.5` identity | AC-07 |
| **D-LEN-12** | `test_d_len_12.py` | `Quantity("meter", 2.5)` → Length 8종만 | FR-01-3 · AC-02 |
| **D-LEN-13** | `test_d_len_13.py` | `Quantity("inch", 12.0)` → `feet:1` (Base 경유) | FR-01-4 · AC-09 |

> Expected RED Failure: 전건 `pytest.fail("RED: D-LEN-NN — 구현 없음, 의도적 실패")`

---

## 5. 테스트 산출물

### 5.1 파일

| 파일 | Test ID | 함수명 |
|------|---------|--------|
| `tests/conftest.py` | — | `sample_meter_input` fixture |
| `tests/entity/test_d_len_01.py` | D-LEN-01 | `test_d_len_01_meter_to_centimeter` |
| `tests/entity/test_d_len_02.py` | D-LEN-02 | `test_d_len_02_feet_to_inch_via_base` |
| `tests/entity/test_d_len_03.py` | D-LEN-03 | `test_d_len_03_deterministic_repeat` |
| `tests/entity/test_d_len_04.py` | D-LEN-04 | `test_d_len_04_meter_to_kilometer` |
| `tests/entity/test_d_len_05.py` | D-LEN-05 | `test_d_len_05_meter_to_millimeter` |
| `tests/entity/test_d_len_06.py` | D-LEN-06 | `test_d_len_06_meter_to_inch` |
| `tests/entity/test_d_len_07.py` | D-LEN-07 | `test_d_len_07_meter_to_feet` |
| `tests/entity/test_d_len_08.py` | D-LEN-08 | `test_d_len_08_meter_to_yard` |
| `tests/entity/test_d_len_09.py` | D-LEN-09 | `test_d_len_09_meter_to_mile` |
| `tests/entity/test_d_len_10.py` | D-LEN-10 | `test_d_len_10_all_length_units_from_meter` |
| `tests/entity/test_d_len_11.py` | D-LEN-11 | `test_d_len_11_meter_identity_in_result` |
| `tests/entity/test_d_len_12.py` | D-LEN-12 | `test_d_len_12_length_category_isolation` |
| `tests/entity/test_d_len_13.py` | D-LEN-13 | `test_d_len_13_inch_to_feet_via_base` |

### 5.2 테스트 본문 (RED 스켈레톤 예시 — D-LEN-01)

```python
def test_d_len_01_meter_to_centimeter():
    # Given: Quantity("meter", 1.0)
    # When: Converter.convert() 호출
    # Then: cm:100 포함
    pytest.fail(
        "RED: D-LEN-01 — 구현 없음, 의도적 실패"
    )
```

### 5.3 pytest 결과

```bash
python -m pytest tests/entity/ -v
```

| 항목 | 값 |
|------|-----|
| collected | 13 |
| passed | 0 |
| failed | 13 (의도적) |
| FAIL 형식 | `RED: D-LEN-NN — 구현 없음, 의도적 실패` |

단일 테스트:

```bash
python -m pytest tests/entity/test_d_len_01.py::test_d_len_01_meter_to_centimeter -v
```

---

## 6. ECB · Dual-Track · TDD 준수

| 항목 | D-LEN-01~13 RED | 판정 |
|------|-----------------|------|
| Logic Track Domain Mock | 미사용 | ✅ |
| entity → control import | 없음 | ✅ |
| entity → boundary import | 없음 | ✅ |
| entity E001~E005 출력 | 검증 없음 (성공 경로만) | ✅ |
| `src/` 수정 | 없음 | ✅ |
| assert 본문 | 없음 (`pytest.fail`만) | ✅ |
| skip / xfail | 없음 | ✅ |
| 통과 더미 | 없음 | ✅ |
| RED 구조 | 1 Target = 1 파일 = 1 테스트 | ✅ |

---

## 7. RED 묶음 범위

| ID | 파일 | 함수명 | 상태 |
|----|------|--------|------|
| **D-LEN-01** | `test_d_len_01.py` | `test_d_len_01_meter_to_centimeter` | ✅ RED 완료 |
| **D-LEN-02** | `test_d_len_02.py` | `test_d_len_02_feet_to_inch_via_base` | ✅ RED 완료 |
| **D-LEN-03** | `test_d_len_03.py` | `test_d_len_03_deterministic_repeat` | ✅ RED 완료 |
| **D-LEN-04** | `test_d_len_04.py` | `test_d_len_04_meter_to_kilometer` | ✅ RED 완료 |
| **D-LEN-05** | `test_d_len_05.py` | `test_d_len_05_meter_to_millimeter` | ✅ RED 완료 |
| **D-LEN-06** | `test_d_len_06.py` | `test_d_len_06_meter_to_inch` | ✅ RED 완료 |
| **D-LEN-07** | `test_d_len_07.py` | `test_d_len_07_meter_to_feet` | ✅ RED 완료 |
| **D-LEN-08** | `test_d_len_08.py` | `test_d_len_08_meter_to_yard` | ✅ RED 완료 |
| **D-LEN-09** | `test_d_len_09.py` | `test_d_len_09_meter_to_mile` | ✅ RED 완료 |
| **D-LEN-10** | `test_d_len_10.py` | `test_d_len_10_all_length_units_from_meter` | ✅ RED 완료 |
| **D-LEN-11** | `test_d_len_11.py` | `test_d_len_11_meter_identity_in_result` | ✅ RED 완료 |
| **D-LEN-12** | `test_d_len_12.py` | `test_d_len_12_length_category_isolation` | ✅ RED 완료 |
| **D-LEN-13** | `test_d_len_13.py` | `test_d_len_13_inch_to_feet_via_base` | ✅ RED 완료 |

---

## 8. RED 완료 체크리스트

### 8.1 C2C 추적

- [x] FR-01-1 → AC-01 → D-LEN-01, D-LEN-04~10, D-LEN-13 연결됨
- [x] FR-01-2 → AC-01, AC-03(Length 행) → D-LEN-10 연결됨
- [x] FR-01-3 → AC-02 → D-LEN-12 연결됨
- [x] FR-01-4 → AC-09 → D-LEN-02, D-LEN-13 연결됨
- [x] NFR-01(결정성) → D-LEN-03 연결됨
- [x] NFR-02(정확성) → D-LEN-01~09, D-LEN-02, D-LEN-13 연결됨
- [x] reference.md D-L01~D-L03 → D-LEN-01~D-LEN-03 대응 확인
- [x] FR-01-5(Temperature) — Length RED 범위에서 제외 확인
- [ ] D-S01(NFR-05 / AC-09 SSOT) — 본 RED 묶음 범위 외, 후속 Track
- [ ] AC-04(입력 검증) → D-I01~D-I04 — entity InputValidator, 별도 RED 묶음
- [ ] AC-06, AC-07(출력 형식·정규식) → U-* — UI Track, 별도 RED 묶음
- [ ] AC-05 전체(10건×2회) — D-LEN-03 + U-* 혼합, 본 RED 부분 커버

### 8.2 테스트 설계

- [x] D-LEN-01 ~ D-LEN-13 Test ID 13건 존재
- [x] 각 테스트에 Given / When / Then AAA 주석 존재
- [x] 파일명 `tests/entity/test_d_len_NN.py` 규칙 준수 (13파일)
- [x] 함수명 `test_d_len_NN_*` 규칙 준수
- [x] Logic Track `test_d_*` 명명 규칙 준수
- [x] Act 대상 entity API (`Converter.convert(Quantity(...))`) 주석에 명시
- [x] `pytest.fail("RED: D-LEN-NN — 구현 없음, 의도적 실패")` 형식 통일

### 8.3 RED 규칙

- [x] 전 테스트 `pytest.fail(...)` — assert 본문 없음
- [x] `python -m pytest tests/entity/ -q` → 13 failed, 0 passed 확인
- [x] `@pytest.mark.skip` 없음
- [x] `@pytest.mark.xfail` 없음
- [x] `assert True` 및 통과 더미 없음
- [x] RED 1 Target = 1 파일 = 1 테스트 함수 구조

### 8.4 ECB 규칙

- [x] 테스트 코드 entity → boundary import 없음
- [x] 테스트 코드 entity → control import 없음
- [x] boundary → entity 직접 import 없음 (테스트 해당 없음)

### 8.5 Mock 규칙

- [x] Logic Track Domain Mock 없음 (`unittest.mock`, Converter/Registry patch 없음)
- [x] stdin/stdout Mock 없음 (entity Logic Track)

### 8.6 구현 코드

- [x] `src/**/*.py` 프로덕션 코드 생성·수정 없음
- [x] 변경 범위 = `tests/`만 (13 × `test_d_len_NN.py` + `conftest.py`)
- [x] GREEN 선행 구현 없음

### 8.7 RED Exit Criteria

- [x] FR-01 Length entity RED 스켈레톤 전건(D-LEN-01~13) 작성 완료
- [x] 의도적 FAIL 상태 확정 (`pytest.fail`)
- [x] ECB · Mock · TDD RED 규칙 위반 0건
- [x] **GREEN 진입 가능** — `/green` Target: **D-LEN-01** (`tests/entity/test_d_len_01.py`)

---

## 9. 갭 분석 (RED 직후)

| 항목 | RED 전 | RED 후 |
|------|--------|--------|
| `tests/` | D-LEN-01만 | D-LEN-01~13 스켈레톤 ✅ |
| `src/` | 없음 | 없음 (GREEN 필요) |
| `Converter.convert()` | 미구현 | 미구현 |
| assert 본문 | — | 전건 `pytest.fail` placeholder |
| C2C | D-LEN-01 부분 | FR-01 Length 전체 entity 매핑 ✅ |
| 체크리스트 | 없음 | §8 통합 ✅ |

---

## 10. Open Items

| ID | 항목 | 상태 |
|----|------|------|
| O1 | 출력 범위 — 같은 카테고리만? | PRD AC-02 · D-LEN-12 entity 검증 |
| O2 | Temperature 비선형 전략 | ARCHITECTURE · 확인 권장 |
| O3 | pyeong ↔ sqm | 미확정 |
| O4 | Length first | **D-LEN-01~13 RED ✅** · GREEN ⏳ |
| O8 | src/ + RED | **RED 전 범위 ✅** · GREEN ⏳ |
| O9 | T-01 assert 범위 | **B(cm 단일) 확정** · D-LEN-10에서 8단위 집합 |

---

## 11. 성공 기준

| ID | 기준 | 판정 |
|----|------|------|
| SC3-1 | D-LEN-01~13 RED 테스트 13건 추가 | ✅ |
| SC3-2 | pytest 의도적 FAIL 13건 확인 | ✅ |
| SC3-3 | 변경 파일 = `tests/`만 | ✅ |
| SC3-4 | Logic Track Mock 미사용 | ✅ |
| SC3-5 | skip/xfail/assert/통과더미 없음 | ✅ |
| SC3-6 | `src/` 무변경 | ✅ |
| SC3-7 | C2C FR-01 · AC · NFR → D-LEN 추적 | ✅ |
| SC3-8 | RED 완료 체크리스트 §8 충족 | ✅ |
| SC3-9 | GREEN 진입 가능 | ✅ |

---

## 12. 다음 단계

- [ ] `/green` — `src/unitconverter/entity/` 최소 구현 (D-LEN-01)
  - `models.py` (`Quantity`, `ConversionLine`, `ConvertResult`)
  - `converter.py` (`Converter.convert`)
  - `unit_registry.py` · `conversion_factors.py` (Length SSOT)
- [ ] `test_d_len_01.py` — `pytest.fail` → assert 본문 교체 (`cm:100`)
- [ ] GREEN pytest PASS 확인
- [ ] D-LEN-02 ~ D-LEN-13 순차 GREEN (TDD 1건씩)

**GREEN pytest (예상):**

```bash
python -m pytest tests/entity/test_d_len_01.py::test_d_len_01_meter_to_centimeter -v
```

---

## 13. 참고

| 문서 | 경로 |
|------|------|
| PRD | `docs/PRD.md` |
| Architecture | `docs/ARCHITECTURE.md` |
| D-* ID | `.cursor/skills/unit-converter-tdd/reference.md` |
| RED Command | `.cursor/commands/red.md` |
| Transcript | `prompts/02_Prompt_Red.md` |
| 이전 Report | `reports/01_Report_Spec.md` |

> **통합 이력:** v0.2 — `03_Report_RED_Checklist.md` 내용을 §8 RED 완료 체크리스트로 본 문서에 통합. `03_Report_RED_Checklist.md` 삭제.
