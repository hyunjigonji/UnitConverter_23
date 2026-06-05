---
name: unit-converter-tdd
description: UnitConverter_23 Dual-Track TDD·ECB 개발 시 Agent가 따를 절차. 단위 변환, ECB(entity/control/boundary), pytest TDD, 오류 코드 E001~E007, SSOT 작업 시 사용.
---

# UnitConverter Dual-Track TDD

프로젝트 규칙 SSOT: [.cursor/rules/](../../rules/) (`unitconverter-*.mdc`)  
Domain 테스트 ID: [reference.md](reference.md)

## 언제 이 Skill을 켜는지

다음 중 **하나라도** 해당하면 이 Skill을 읽고 절차를 따른다.

- UnitConverter_23에서 **단위 변환·입력 검증·CLI** 구현 또는 수정
- 사용자가 **TDD**, **ECB**, **Dual-Track**, **RED/GREEN/REFACTOR**를 언급
- `test_d_*` / `test_u_*` 테스트 추가·수정
- entity / control / boundary 레이어 코드 작성
- 변환 계수·Base Unit·단위 문자열(SSOT) 변경
- 오류 코드 **E001~E007** 도입·매핑

**켜지 않는 경우**: README만 수정, git commit/PR만 요청, UnitConverter와 무관한 작업.

---

## 매 턴 선언 (필수)

TDD 관련 작업마다 응답 상단에 선언한다.

```
Phase: RED|GREEN|REFACTOR
Layer: boundary|control|entity
Track: Logic|UI
```

---

## Logic Track vs UI Track

| 구분 | Logic Track | UI Track |
|------|-------------|----------|
| 대상 레이어 | entity, control | boundary |
| 테스트 파일 | `test_d_*` | `test_u_*` |
| 테스트 ID | D-* | U-* |
| Domain Mock | **금지** | 해당 없음 |
| Boundary Mock | 해당 없음 | **허용** (stdin/stdout 등) |
| 검증 대상 | 변환 수치·오류·결정성·SSOT | 입출력 형식·CLI 동작 |
| 객체 | **실제 domain 객체** 사용 | boundary는 control 호출 가능 |
| skip / xfail | **금지** | **금지** |
| assert 완화·제거 | **금지** | **금지** |

---

## ECB · Mock · 오류 코드 — 금지 / 허용

### ECB 의존 방향

| 규칙 | entity | control | boundary |
|------|--------|---------|----------|
| 허용 import | entity 내부만 | entity | control |
| 금지 import | control, boundary | boundary | entity 직접 import 금지 |
| 외부 라이브러리 | entity **금지** | 프로젝트 정책 따름 | 허용 |

### Mock

| Mock 대상 | Logic Track | UI Track |
|-----------|-------------|----------|
| 변환 로직·UnitRegistry·Converter | **금지** | — |
| stdin / stdout / CLI runner | — | **허용** |
| control (UI 테스트) | — | **허용** |

### 오류 코드 E001~E007

| 코드 | 의미 | Logic에서 검증 | UI에서 검증 |
|------|------|----------------|-------------|
| E001 | InvalidInputFormat | **허용** (entity/control) | **허용** (출력/메시지 매핑) |
| E002 | UnsupportedUnit | **허용** | **허용** |
| E003 | InvalidNumericValue | **허용** | **허용** |
| E004 | EmptyInput | **허용** | **허용** |
| E005 | ConversionNotSupported | **허용** | **허용** |
| E006 | InternalConversionError | **허용** | **허용** |
| E007 | UnknownError | **허용** | **허용** |

**금지**: E001~E007 외 임의 오류 문자열, 코드 번호 재정의, Logic Track에서 Mock으로 오류만 흉내 내기.  
**허용**: boundary가 control이 반환한 오류를 사용자 출력 형식으로 변환.

### SSOT

| 항목 | 금지 | 허용 |
|------|------|------|
| 변환 계수 | 테스트·entity·control·boundary에 하드코딩 중복 | 단일 소스(예: `conversion_factors`)에서만 정의 |
| Base Unit | 카테고리별 중복 정의 | SSOT 한 곳 + 참조 |
| 단위 문자열 | `"meter"` 등 리터럴 산재 | 상수/레지스트리 단일 정의 |

---

## RED — 6단계

1. `.cursor/rules/`와 [reference.md](reference.md)에서 **D-* 또는 U-* ID**를 정한다.
2. **Phase/Layer/Track** 선언.
3. **실패할 테스트 하나**만 작성 (`test_d_*` 또는 `test_u_*`, Given-When-Then 권장).
4. 아직 **프로덕션 코드는 최소·미구현** 상태를 유지한다.
5. **해당 테스트만** pytest 실행 → **반드시 FAIL** 확인.
6. RED 완료 보고: 테스트 ID, 실패 메시지, 다음 GREEN 범위.

**금지**: GREEN용 구현 선행, skip/xfail, assert 완화, Logic Track Mock.

---

## GREEN — 6단계

1. **Phase/Layer/Track** 선언.
2. **RED에서 실패한 테스트 하나**를 통과시키는 **최소 코드**만 해당 Layer에 추가.
3. **해당 테스트** pytest 실행 → PASS.
4. **같은 Track 전체** pytest 실행 → 기존 테스트 회귀 없음 확인.
5. 오류·변환은 **E001~E007** 및 `unitconverter-domain.mdc` 출력 형식과 일치시킨다.
6. GREEN 완료 보고: 통과한 테스트 ID, 변경 파일(Layer), pytest 결과 요약.

**금지**: RED 테스트 삭제, assert 제거, 범위 밖 리팩터, Logic Track Mock.

---

## REFACTOR — 6단계

1. **Phase/Layer/Track** 선언.
2. **동작 변경 없이** 구조·이름·중복 제거만 수행 (SSOT·ECB 경계 정리 포함).
3. entity → control/boundary 역방향 import 없는지 확인.
4. 변환 계수·단위 문자열 **중복 없음** 확인.
5. **전체 pytest** (`pytest`) 실행 → 전부 PASS.
6. REFACTOR 완료 보고: 변경 요약, 회귀 없음 확인, 다음 RED 후보(있으면).

**금지**: 테스트 assert 완화, 공개 동작·오류 코드 변경, REFACTOR 중 새 기능 추가.

---

## Test / Review Loop

| 시점 | 실행 명령 | 기대 결과 |
|------|-----------|-----------|
| RED 직후 | `pytest tests/test_d_<area>.py::test_<id> -q` 또는 `pytest tests/test_u_<area>.py::test_<id> -q` | **FAIL** (새 테스트 1개) |
| GREEN 직후 | 동일 `-q` 단일 테스트 | **PASS** |
| GREEN 검증 | `pytest tests/test_d_*.py -q` (Logic) 또는 `pytest tests/test_u_*.py -q` (UI) | Track 전체 **PASS** |
| REFACTOR 전·후 | `pytest -q` | **전체 PASS** |
| Layer 변경 후 | 해당 Layer + 인접 Layer 테스트 재실행 | 회귀 **없음** |
| SSOT·오류 코드 변경 후 | `pytest -q` | **전체 PASS** |

**Review Loop (한 사이클 종료 조건)**

1. 선언한 Phase 목표 달성 (RED=실패 확인, GREEN=통과, REFACTOR=구조만 변경).
2. 해당 Track pytest green.
3. `.cursor/rules/` ECB·SSOT·Dual-Track 위반 없음.
4. 다음 작업이 있으면 **RED부터** 다시 시작 (REFACTOR 다음에 GREEN으로 새 기능 넣지 않음).

---

## 완료 보고 항목

작업 턴 또는 TDD 사이클 종료 시 아래를 포함한다.

- [ ] **Phase / Layer / Track** 선언값
- [ ] **테스트 ID** (D-* 또는 U-*)
- [ ] **변경 파일** 및 Layer
- [ ] **pytest 명령**과 결과 (FAIL/ PASS, scope)
- [ ] **ECB** 위반 여부 (import 방향)
- [ ] **Mock** 사용 여부 (Logic Track이면 반드시 "없음")
- [ ] **SSOT** 준수 여부 (계수·Base Unit·단위 문자열 중복 없음)
- [ ] **오류 코드** 매핑 (해당 시 E001~E007)
- [ ] **다음 단계** (예: "D-L05 GREEN", "REFACTOR 후 D-W01 RED")

---

## TDD 사이클 순서 (엄수)

```
RED → GREEN → REFACTOR → (새 요구) RED → ...
```

한 번에 **하나의 실패 테스트**만 RED. GREEN은 그 테스트만 통과시키는 최소 구현. REFACTOR는 전체 green 상태에서만.

---

## 추가 자료

- Domain 테스트 ID 목록: [reference.md](reference.md)
- Slash Command: `.cursor/commands/` — `/spec`, `/red`, `/green`, `/refactor`
