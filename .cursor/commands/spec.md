# Spec — 요구사항·아키텍처 정합 확인

UnitConverter_23 **명세( Spec ) 정합**을 확인하고, 다음 TDD 작업 대상을 제안한다.  
**코드·테스트 수정 없음** — read-only 분석 + 계획만 수행.

**근거:** `docs/PRD.md` · `docs/ARCHITECTURE.md` · `.cursor/rules/unitconverter-*.mdc` · `.cursor/skills/unit-converter-tdd/reference.md`

---

## 필수 선언

응답 **첫 줄**에 반드시 출력:

```
Phase: spec | Scope: PRD·ARCHITECTURE·Rules | Mode: read-only
```

---

## 목적 (Objective)

- PRD·ARCHITECTURE·Cursor Rules 간 **요구사항·설계 일치** 확인
- 현재 코드(`src/`, `tests/`)와 명세 간 **갭** 식별
- 다음 TDD 사이클의 **Target ID · Layer · Track** 제안
- Open Item(O1~O4 등) **미확정 항목** 명시

---

## 입력 (Input)

| 입력 | 설명 | 기본값 |
|------|------|--------|
| 검토 범위 | 특정 FR/AC, 카테고리, 레이어 | PRD·ARCHITECTURE 전체 |
| Target 후보 | 사용자가 지정한 D-* / U-* ID | reference.md 미구현 ID |
| 현재 코드 | `src/`, `tests/` 존재 여부 | 저장소 실제 상태 |

사용자가 ID·범위를 지정하지 않으면 **가장 앞선 미구현 D-* ID**부터 제안한다.

---

## 출력 (Output)

```markdown
## Spec 정합 보고

- PRD AC 충족: (충족 / 미충족 / 해당 없음 — 코드 없음)
- ARCHITECTURE ECB: (준수 / 위반 N건 / 해당 없음)
- Rules SSOT: (준수 / 위반 / 해당 없음)
- 갭 요약: (한 줄)
- Open Items: (미확정 목록)
- 다음 TDD 제안:
  - Phase: red
  - Target: D-I01 (예)
  - Layer: entity
  - Track: Logic
  - 근거: (PRD AC-04, reference.md)
```

---

## 수행 절차 (Steps)

1. **문서 Read** — `docs/PRD.md`, `docs/ARCHITECTURE.md`, `.cursor/rules/` 핵심 조항 확인.
2. **코드 스캔** — `src/`, `tests/` Glob·Read — 구현·테스트 존재 여부 파악.
3. **갭 분석** — PRD FR/AC vs 코드, ARCHITECTURE 레이어 vs 디렉터리, Rules E001~E007·SSOT vs 실제.
4. **reference.md 대조** — D-* / U-* ID 중 **아직 테스트·구현 없는** 항목 목록.
5. **다음 Target 제안** — RED → GREEN → REFACTOR 순서에 맞게 **1개 ID** + Layer + Track + PRD 근거.
6. **보고** — 위 [출력](#출력-output) 형식으로 마무리. **red/green/refactor 실행하지 않음.**

---

## 성공 조건 (Success Criteria)

- [ ] PRD·ARCHITECTURE·Rules **3축** 모두 언급
- [ ] 코드/테스트 **현재 상태** 사실 기반 기술 (추측 금지)
- [ ] 다음 TDD Target **1건** — Phase/Layer/Track/Target ID 명시
- [ ] PRD AC 또는 reference ID **근거** 연결
- [ ] **코드·테스트·문서 수정 없음** (read-only)

---

## 금지 사항 (Restrictions)

| 금지 | 이유 |
|------|------|
| **`src/` · `tests/` 수정** | spec은 계획·정합 확인만 |
| **RED / GREEN / REFACTOR 수행** | 별도 Command (`/red`, `/green`, `/refactor`) |
| **pytest 실행** | 구현 검증은 TDD Phase에서 |
| **Open Item 임의 확정** | 사용자 확인 없이 O1~O4 가정 금지 |
| **PRD·Rule 재정의** | 명세 변경은 사용자 요청 시만 |
| **git commit / push** | 사용자 요청 시만 |

---

## ECB · Dual-Track (검토 기준)

| 항목 | Spec에서 확인할 것 |
|------|-------------------|
| ECB | `boundary → control → entity` 디렉터리·import 존재 여부 |
| entity 순수성 | entity에 I/O·상위 import 없음 (설계 대비) |
| Dual-Track | `test_d_*`(Logic) / `test_u_*`(UI) 분리 계획 |
| Mock | Logic Mock 금지 · UI Mock 허용 — 테스트 설계 시 반영 |
