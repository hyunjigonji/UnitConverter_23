# UnitConverter_23 — RED Phase Report

**문서 ID:** 02.UnitConverter_RED_Report  
**프로젝트:** UnitConverter_23  
**단계:** STEP 3 — 첫 Logic Track RED (D-LEN-01)  
**버전:** 0.1  
**일자:** 2026-06-05  
**근거:** Cursor Agent 세션 L · `/red-test-plan` · `/red-skeleton`

---

## 1. Executive Summary

UnitConverter_23에서 **첫 Logic Track RED**를 완료했다.  
entity 레이어 **D-LEN-01** (meter → cm 변환)에 대한 C2C 설계·RED 스켈레톤·의도적 pytest FAIL을 확인했다.

| 항목 | 상태 |
|------|------|
| **Target** | D-LEN-01 |
| **Phase** | RED |
| **Layer** | entity |
| **Track** | Logic |
| **pytest** | **1 failed** (의도적) |
| **`src/`** | 미생성 (GREEN 대기) |
| **`tests/`** | 2파일 생성 |

---

## 2. 범위

### 2.1 In Scope (완료)

| 항목 | 산출물 |
|------|--------|
| C2C 추적 | FR-01-1 · FR-01-4 · AC-01 → D-LEN-01 |
| RED 설계표 | Track B — `Converter.convert()` · cm:100 |
| RED 스켈레톤 | `tests/conftest.py` · `tests/entity/test_d_len_01.py` |
| pytest FAIL 확인 | `pytest.fail` 의도적 실패 |
| Export | `02_Report_Red.md` · `02_Prompt_Red.md` |

### 2.2 Out of Scope (미착수)

| 항목 | 비고 |
|------|------|
| `src/` entity 구현 | `/green` |
| assert 본문 | GREEN에서 `pytest.fail` → assert 교체 |
| D-LEN-02 ~ D-LEN-03 | 동일 RED 묶음 · 후속 RED |
| REFACTOR | GREEN 이후 |
| UI Track (U-*) | 미착수 |

---

## 3. C2C 추적

### 3.1 PRD → Test ID

| PRD ID | 요구사항 요약 | D-LEN-01 매핑 |
|--------|--------------|---------------|
| **FR-01-1** | 지원 단위 간 변환 수행 | meter → cm (Length 지원 단위) |
| **FR-01-4** | Base Unit(meter) 경유 변환 | 1 meter = 100 cm |
| **AC-01** | Length 정상 변환 (8단위·결정성) | **부분** — cm 단일 assert (T-01 = B) |

### 3.2 reference.md 대응

| reference ID | D-LEN ID | Given-When-Then |
|--------------|----------|-----------------|
| D-L01 | D-LEN-01 | meter → cm 결정적 변환 |

### 3.3 구현 결정 (To-Do T-01)

| 항목 | 결정 |
|------|------|
| assert 범위 | **B — cm 단일 검증** (RED 1건 원칙) |
| AC-01 전체 8단위 | 후속 D-LEN 또는 control/UI Track으로 분리 |

---

## 4. RED 설계표 (Track B)

| Test ID | 대상 함수 | Given → Then | PRD Trace | Expected RED Failure |
|---------|-----------|--------------|-----------|----------------------|
| **D-LEN-01** | `convert()` | Given: `meter:1` · When: 길이 변환 · Then: `cm:100` | FR-01-1 · FR-01-4 · AC-01 | `pytest.fail` (의도적) |

> 설계 단계 예상 실패: `ModuleNotFoundError` (`src/` 미존재).  
> 스켈레ton 단계: `pytest.fail`로 **명시적 RED FAIL** 확정.

---

## 5. 테스트 산출물

### 5.1 파일

| 파일 | 역할 |
|------|------|
| `tests/conftest.py` | `sample_meter_input` → `"meter:1"` |
| `tests/entity/test_d_len_01.py` | `test_d_len_01_meter_to_centimeter` |

### 5.2 테스트 본문 (RED 스켈레톤)

```python
def test_d_len_01_meter_to_centimeter(sample_meter_input):
    # Given: meter:1 입력
    # When: convert(sample_meter_input) 호출
    # Then: cm:100 포함
    pytest.fail(
        "RED: D-LEN-01 — meter→centimeter 변환 미구현, 의도적 실패"
    )
```

### 5.3 pytest 결과

```bash
python -m pytest tests/entity/test_d_len_01.py::test_d_len_01_meter_to_centimeter -v
```

| 항목 | 값 |
|------|-----|
| collected | 1 |
| passed | 0 |
| failed | 1 |
| duration | 0.11s |
| FAIL 한 줄 | `Failed: RED: D-LEN-01 — meter→centimeter 변환 미구현, 의도적 실패` |

---

## 6. ECB · Dual-Track · TDD 준수

| 항목 | D-LEN-01 RED | 판정 |
|------|--------------|------|
| Logic Track Domain Mock | 미사용 | ✅ |
| entity → control import | 없음 | ✅ |
| entity → boundary import | 없음 | ✅ |
| entity E001~E005 출력 | 검증 없음 (성공 경로만) | ✅ |
| `src/` 수정 | 없음 | ✅ |
| assert 본문 | 없음 (`pytest.fail`만) | ✅ |
| skip / xfail | 없음 | ✅ |
| 통과 더미 | 없음 | ✅ |
| RED 1건 | D-LEN-01 단독 | ✅ |

---

## 7. RED 묶음 범위

| ID | 파일 (예상) | 함수명 (예상) | 상태 |
|----|-------------|---------------|------|
| **D-LEN-01** | `test_d_len_01.py` | `test_d_len_01_meter_to_centimeter` | ✅ RED 완료 |
| D-LEN-02 | `test_d_len_02.py` | `test_d_len_02_feet_to_inch_via_base` | ⏳ |
| D-LEN-03 | `test_d_len_03.py` | `test_d_len_03_deterministic_repeat` | ⏳ |

---

## 8. 갭 분석 (RED 직후)

| 항목 | RED 전 | RED 후 |
|------|--------|--------|
| `tests/` | 없음 | D-LEN-01 스켈레톤 ✅ |
| `src/` | 없음 | 없음 (GREEN 필요) |
| `Converter.convert()` | 미구현 | 미구현 |
| assert (cm:100) | — | `pytest.fail` placeholder |

---

## 9. Open Items

| ID | 항목 | 상태 |
|----|------|------|
| O1 | 출력 범위 — 같은 카테고리만? | PRD AC-02 · 사용자 확인 권장 |
| O2 | Temperature 비선형 전략 | ARCHITECTURE · 확인 권장 |
| O3 | pyeong ↔ sqm | 미확정 |
| O4 | Length first | **진행 중** (D-LEN-01 RED 완료) |
| O8 | src/ + 첫 RED | **D-LEN-01 RED ✅** · GREEN ⏳ |
| O9 | T-01 assert 범위 | **B(cm 단일) 확정** |

---

## 10. 성공 기준

| ID | 기준 | 판정 |
|----|------|------|
| SC3-1 | D-LEN-01 RED 테스트 1건 추가 | ✅ |
| SC3-2 | pytest 의도적 FAIL 확인 | ✅ |
| SC3-3 | 변경 파일 = `tests/`만 | ✅ |
| SC3-4 | Logic Track Mock 미사용 | ✅ |
| SC3-5 | skip/xfail/assert/통과더미 없음 | ✅ |
| SC3-6 | `src/` 무변경 | ✅ |
| SC3-7 | C2C FR-01-1 · FR-01-4 · AC-01 추적 | ✅ |

---

## 11. 다음 단계

- [ ] `/green` — `src/unitconverter/entity/` 최소 구현
  - `models.py` (`Quantity`, `ConversionLine`, `ConvertResult`)
  - `converter.py` (`Converter.convert`)
  - `unit_registry.py` · `conversion_factors.py` (Length SSOT)
- [ ] `test_d_len_01.py` — `pytest.fail` → assert 본문 교체 (`cm:100`)
- [ ] GREEN pytest PASS 확인
- [ ] D-LEN-02 RED (feet → inch Base 경유)

**GREEN pytest (예상):**

```bash
python -m pytest tests/entity/test_d_len_01.py::test_d_len_01_meter_to_centimeter -v
```

---

## 12. 참고

| 문서 | 경로 |
|------|------|
| PRD | `docs/PRD.md` |
| Architecture | `docs/ARCHITECTURE.md` |
| D-* ID | `.cursor/skills/unit-converter-tdd/reference.md` |
| RED Command | `.cursor/commands/red.md` |
| Transcript | `prompts/02_Prompt_Red.md` |
| 이전 Report | `reports/01_Report_Spec.md` |
