# TDD GREEN — 최소 구현으로 테스트 통과

UnitConverter_23 Dual-Track TDD **GREEN 단계만** 수행한다.  
**전제:** 직전 `/red`에서 **FAILED** 확인된 Target 테스트가 있어야 한다.

**근거:** `.cursor/rules/unitconverter-*.mdc` · `.cursor/skills/unit-converter-tdd/SKILL.md`

---

## 필수 선언

응답 **첫 줄**에 반드시 출력:

```
Phase: green | Layer: entity|control|boundary | Track: Logic|UI | Target: D-*|U-*
```

Target은 **직전 RED와 동일 ID**여야 한다.

---

## 목적 (Objective)

- RED에서 실패한 **Target 테스트 1개**를 통과시키는 **최소 코드**만 작성한다.
- ECB 레이어 경계·SSOT·E001~E007을 준수한다.
- REFACTOR·추가 기능은 **하지 않는다**.

---

## 입력 (Input)

| 입력 | 설명 | 필수 |
|------|------|------|
| Target ID | RED와 동일한 `D-*` / `U-*` | ✅ |
| Layer | 구현 대상 레이어 | ✅ |
| RED 보고 | FAIL 요약·변경 tests 파일 | ✅ |
| Track | Logic / UI | ✅ |

**구현 허용 범위 (Layer별):**

| Layer | 수정 허용 경로 | ECB |
|-------|----------------|-----|
| entity | `src/unitconverter/entity/` | 외부 I/O·상위 import 금지 |
| control | `src/unitconverter/control/` | entity만 import |
| boundary | `src/unitconverter/boundary/` | control만 import (entity 직접 금지) |

---

## 출력 (Output)

```markdown
## GREEN 완료

- Target: D-L01 — PASS
- 변경 파일: src/unitconverter/entity/converter.py
- Layer: entity
- pytest (단일): 1 passed
- pytest (Track): N passed, 0 failed
- ECB: 위반 없음
- SSOT: 계수·단위 — UnitRegistry만 추가
- Mock: Logic Track — 없음
- 다음: /refactor 또는 새 Target /red
```

---

## 수행 절차 (Steps)

1. **RED 확인** — Target 테스트가 **FAILED** 상태였는지 RED 보고·pytest로 확인. PASS면 RED부터 재수행.
2. **Phase 선언** — 필수 선언 (Target = RED와 동일).
3. **최소 구현** — Target 1개 통과에 필요한 **최소** 코드만 해당 Layer에 추가.
   - entity → control → boundary 순 (의존 방향)
   - 변환 계수·단위 문자열 → **SSOT** (`UnitRegistry`, `ConversionFactors`)에만 추가
4. **Logic Track** — Domain Mock **금지**, 실객체로 통과.
5. **pytest 단일** — Target 테스트 → **PASS**.
6. **pytest Track** — `test_d_*.py` 또는 `test_u_*.py` 전체 → **0 failed**.
7. **ECB·E001~E007·출력 형식** — Rule·PRD와 일치 확인.
8. **보고** — [출력](#출력-output). **REFACTOR는 `/refactor`에서.**

---

## pytest 예시 (bash)

단일 (GREEN 확인):

```bash
pytest tests/test_d_length.py::test_d_l01_meter_to_cm -q
```

Track 회귀:

```bash
pytest tests/test_d_*.py -q
pytest tests/test_u_*.py -q
```

---

## 성공 조건 (Success Criteria)

- [ ] Target 테스트 **PASS**
- [ ] 동일 Track **전체 PASS** (회귀 없음)
- [ ] RED 테스트 **삭제·완화 없음**
- [ ] 구현 = Target 통과 **최소 범위** (범위 밖 리팩터 없음)
- [ ] ECB import 방향 **위반 없음**
- [ ] SSOT — 계수·단위 **중복 하드코딩 없음**
- [ ] Logic Track — Domain Mock **없음**
- [ ] GREEN 완료 보고 출력

---

## 금지 사항 (Restrictions)

| 금지 | 이유 |
|------|------|
| **RED 테스트 삭제·assert 완화** | TDD 원칙 |
| **skip / xfail** | GREEN 우회 |
| **Logic Track Domain Mock** | Dual-Track 규칙 |
| **entity I/O · 상위 import** | ECB·entity 순수성 |
| **boundary → entity 직접 import** | ECB |
| **REFACTOR·구조 개편** | `/refactor` Phase |
| **Target 외 기능 추가** | 최소 구현 원칙 |
| **RED 없이 GREEN** | RED → GREEN 순서 |
| **tests/ assert 변경으로 통과** | 프로덕션 구현으로 통과 |

---

## ECB · Dual-Track

| Track | 구현 | Mock |
|-------|------|------|
| Logic | entity/control **실코드** | Domain Mock **금지** |
| UI | boundary + control 연동 | stdin/stdout Mock **허용** |

오류·변환은 **E001~E007** 및 PRD 출력 형식(`<unit>:<value>`) 준수.
