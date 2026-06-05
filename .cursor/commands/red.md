# TDD RED — 실패 테스트 먼저

UnitConverter_23 Dual-Track TDD **RED 단계만** 수행한다.  
**근거:** `.cursor/rules/unitconverter-*.mdc` · `.cursor/skills/unit-converter-tdd/reference.md`

---

## 필수 선언

응답 **첫 줄**에 반드시 출력:

```
Phase: red | Layer: entity|control|boundary | Track: Logic|UI | Target: D-*|U-*
```

---

## 목적 (Objective)

- **하나의** 실패 테스트를 `tests/`에 먼저 작성한다.
- pytest로 **의도된 FAIL**을 확인한다.
- 프로덕션 코드(`src/`)는 **수정하지 않는다**.
- GREEN은 **별도 Phase** (`/green`)에서 수행한다.

---

## 입력 (Input)

| 입력 | 설명 | 필수 |
|------|------|------|
| Target ID | `D-*` (Logic) 또는 `U-*` (UI) | ✅ (미지정 시 reference.md 다음 ID) |
| Layer | `entity` · `control` · `boundary` | ✅ |
| Track | `Logic` · `UI` | ✅ |
| `/spec` 결과 | Spec 정합 보고의 다음 Target | 선택 |

**Track · Layer · 파일 매핑:**

| Track | Layer | 테스트 파일 | Mock |
|-------|-------|-------------|------|
| Logic | entity, control | `tests/test_d_*.py` | Domain Mock **금지** |
| UI | boundary | `tests/test_u_*.py` | stdin/stdout·control Mock **허용** |

---

## 출력 (Output)

```markdown
## RED 완료

- Target: D-L01
- pytest: FAILED — AssertionError: expected 250, got None
- 변경 파일: tests/test_d_length.py (tests/만)
- ECB: (해당 없음 / 위반 없음)
- Mock: Logic Track — 없음
- 다음: /green — src/entity 최소 구현
```

---

## 수행 절차 (Steps)

1. **선행 확인** — `/spec` 또는 reference.md에서 **Target ID** 확정. 중복 ID 금지.
2. **Phase 선언** — 필수 선언 형식 출력.
3. **AAA 테스트 1건 작성** — `tests/`만 수정.
   - **Arrange:** Given 입력·실제 domain 객체 (Logic: Mock 금지)
   - **Act:** 검증 대상 API 호출
   - **Assert:** 기대값 **엄격** 검증 (Given-When-Then docstring 권장)
4. **프로덕션 미수정** — `src/`, `UnitConverter.py` **변경 금지**.
5. **pytest 단일 실행** — Target 테스트 1개만.
6. **FAIL 확인** — FAILED 필수. PASS면 assert·기대값 재검토.
7. **보고** — [출력](#출력-output) 형식. **GREEN 하지 않음.**

---

## pytest 예시 (bash)

Logic Track:

```bash
pytest tests/test_d_length.py::test_d_l01_meter_to_cm -q
```

UI Track:

```bash
pytest tests/test_u_cli.py::test_u_c01_output_format -q
```

Track 확인 (새 테스트만 FAIL):

```bash
pytest tests/test_d_*.py -q
pytest tests/test_u_*.py -q
```

---

## 성공 조건 (Success Criteria)

- [ ] Target 테스트 **1개**만 추가·수정
- [ ] 지정 pytest 명령 결과 = **FAILED** (AssertionError 등)
- [ ] 변경 파일 = **`tests/`만**
- [ ] Logic Track → Domain Mock **미사용**
- [ ] skip / xfail / assert 완화 **없음**
- [ ] `src/` **무변경**
- [ ] RED 완료 보고 출력

> ImportError·collection error: RED로 인정 가능하나 보고에 명시하고, 테스트·import 경로 정정 후 **FAILED** 재확인 권장.

---

## 금지 사항 (Restrictions)

| 금지 | 이유 |
|------|------|
| **`src/` · 프로덕션 코드 수정** | RED = 테스트만 |
| **Logic Track Domain Mock** | `unittest.mock`, Converter·Registry patch 금지 |
| **assert 완화·제거** | GREEN 우회 |
| **skip / xfail / 테스트 삭제** | TDD 원칙 위반 |
| **GREEN / REFACTOR** | `/green`, `/refactor`에서 수행 |
| **한 턴에 여러 RED 테스트** | 1 FAIL = 1 RED |
| **RED 없이 구현** | RED → GREEN 순서 |

---

## ECB · Dual-Track

- Logic 테스트는 **entity/control 실객체**로 Act·Assert.
- UI 테스트는 boundary만 대상; control Mock **허용**, entity **직접 import 금지** (boundary 규칙).
- 오류 검증 시 **E001~E007** 코드만 사용 (Rule SSOT).
