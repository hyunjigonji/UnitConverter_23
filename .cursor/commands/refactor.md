# TDD REFACTOR — 동작 불변 구조 개선

UnitConverter_23 Dual-Track TDD **REFACTOR 단계만** 수행한다.  
**전제:** Target Track **전체 pytest green** (직전 `/green` 완료).

**근거:** `.cursor/rules/unitconverter-*.mdc` · `.cursor/skills/unit-converter-tdd/SKILL.md`

---

## 필수 선언

응답 **첫 줄**에 반드시 출력:

```
Phase: refactor | Layer: entity|control|boundary | Track: Logic|UI | Scope: (리팩터 범위 한 줄)
```

---

## 목적 (Objective)

- **공개 동작·테스트 결과 불변** 상태에서 구조·이름·중복을 정리한다.
- ECB 경계·SSOT 위반을 **제거**한다.
- **새 기능·새 테스트**는 추가하지 않는다.

---

## 입력 (Input)

| 입력 | 설명 | 필수 |
|------|------|------|
| Scope | 리팩터 대상 (파일·모듈·중복 제거 등) | ✅ |
| Layer / Track | 주로 수정하는 레이어 | ✅ |
| GREEN 상태 | Track 전체 PASS | ✅ (전제) |

**리팩터 허용 예:**

- 중복 계수·단위 문자열 → SSOT 통합
- 네이밍·파일 분리·dead code 제거
- import 정리 (ECB 방향 유지)
- 테스트 코드 **구조** 정리 (assert·ID·의미 **불변**)

---

## 출력 (Output)

```markdown
## REFACTOR 완료

- Scope: entity/converter.py 중복 제거 → UnitRegistry SSOT
- 변경 파일: src/unitconverter/entity/converter.py, unit_registry.py
- pytest (전체): N passed, 0 failed
- 동작 변경: 없음
- ECB: 위반 없음
- SSOT: 중복 제거 확인
- 다음: 새 Target → /red
```

---

## 수행 절차 (Steps)

1. **전제 확인** — `pytest -q` 또는 Track suite **전부 PASS**. 실패 있으면 REFACTOR **중단** → `/green` 먼저.
2. **Phase 선언** — Scope 포함.
3. **동작 동결** — 변환 결과·ErrorCode·공개 API 시그니처 **변경 금지**.
4. **리팩터 수행** — 구조·SSOT·ECB 경계만 개선.
5. **ECB 검사** — entity → control/boundary 역방향 import 없음.
6. **SSOT 검사** — 계수·Base Unit·단위 문자열 중복 없음.
7. **pytest 전체** — `pytest -q` → **0 failed**.
8. **보고** — [출력](#출력-output). 새 기능은 **`/red`부터**.

---

## pytest 예시 (bash)

REFACTOR 전·후 (동일 결과 기대):

```bash
pytest -q
pytest tests/test_d_*.py -q
pytest tests/test_u_*.py -q
```

---

## 성공 조건 (Success Criteria)

- [ ] REFACTOR **전·후** pytest 전체 **PASS**
- [ ] 테스트 assert **삭제·완화 없음**
- [ ] 공개 동작·E001~E007 매핑 **불변**
- [ ] ECB import 방향 **위반 없음**
- [ ] SSOT **개선 또는 유지** (중복 없음)
- [ ] **새 기능·새 RED 테스트 없음**
- [ ] REFACTOR 완료 보고 출력

---

## 금지 사항 (Restrictions)

| 금지 | 이유 |
|------|------|
| **동작·API·오류 코드 변경** | REFACTOR ≠ 기능 변경 |
| **assert 완화·skip·xfail** | 테스트 의미 보존 |
| **RED 없이 새 기능** | REFACTOR 후 → `/red` |
| **REFACTOR 중 GREEN 범위 구현** | Phase 혼합 금지 |
| **Logic Track Domain Mock 도입** | Dual-Track |
| **entity I/O 추가** | entity 순수성 |
| **실패 상태에서 REFACTOR** | GREEN 선행 필수 |

---

## ECB · Dual-Track · TDD 순서

```
RED → GREEN → REFACTOR → (새 요구) RED → ...
```

| Track | REFACTOR 시 Mock |
|-------|------------------|
| Logic | Domain Mock **금지** (기존과 동일) |
| UI | boundary Mock **허용** (기존과 동일) |

REFACTOR 종료 후 다음 작업은 **항상 `/red`** (또는 `/spec`)부터 시작한다.
