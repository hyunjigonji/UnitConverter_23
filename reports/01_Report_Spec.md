# UnitConverter_23 — Governance · Spec · TDD Report

**문서 ID:** 01.UnitConverter_Governance_Report  
**프로젝트:** UnitConverter_23  
**단계:** STEP 1~2 — 거버넌스 · 명세 · TDD Command 완성  
**버전:** 0.3  
**일자:** 2026-06-05  
**근거:** Cursor Agent 세션 A~K (Rule · Skill · Command · Docs · Export)

---

## 1. Executive Summary

UnitConverter_23에서 **AI·개발 거버넌스**와 **제품·아키텍처 명세**를 프로젝트 파일로 고정했다.

| 계층 | 산출물 | 상태 |
|------|--------|------|
| **Rule** | `.cursor/rules/*.mdc` (6파일) | ✅ |
| **Skill** | `unit-converter-tdd` (SKILL.md + reference.md) | ✅ |
| **Command** | `/spec` · `/red` · `/green` · `/refactor` (4파일) | ✅ |
| **Agent** | `AGENTS.md` (4 Agent 역할) | ✅ |
| **Spec** | `docs/PRD.md` | ✅ |
| **Architecture** | `docs/ARCHITECTURE.md` (ECB·SOLID) | ✅ |

**아직 없는 것:** `src/` ECB 코드, `tests/` pytest, `/review-ecb` Command, `hooks.json`, U-* ID 카탈로그, Open Item O1~O4 사용자 최종 확인.

---

## 2. 범위

### 2.1 In Scope (완료)

| 항목 | 산출물 |
|------|--------|
| Rule SSOT | `.cursor/rules/unitconverter-*.mdc` |
| TDD Skill | `.cursor/skills/unit-converter-tdd/` |
| TDD Commands | `spec.md`, `red.md`, `green.md`, `refactor.md` |
| Agent 정의 | `AGENTS.md` |
| 제품 요구사항 | `docs/PRD.md` |
| 아키텍처 설계 | `docs/ARCHITECTURE.md` |
| 거버넌스 보고 · Transcript | `reports/01_Report_Spec.md`, `prompts/01_Prompt_Spec.md` |

### 2.2 Out of Scope (미착수)

| 항목 | 비고 |
|------|------|
| `src/` entity/control/boundary 구현 | STEP 3+ |
| `tests/` RED/GREEN/REFACTOR 코드 | STEP 3+ |
| `/review-ecb` Command | 선택 |
| `UnitConverter.py` 리팩터 | 프로토타입 유지 |
| git push (최종) | 사용자 요청 시 |

---

## 3. 8계층 ↔ UnitConverter_23 매핑

| 계층 | 역할 | 상태 |
|------|------|------|
| **Model** | LLM 추론 | Cursor 제공 |
| **Agent** | `AGENTS.md` 4역할 + Cursor Agent | ✅ |
| **Harness** | Cursor IDE | ✅ |
| **Rule** | `.cursor/rules/*.mdc` | ✅ |
| **Skill** | `unit-converter-tdd` | ✅ |
| **Command** | `/spec` `/red` `/green` `/refactor` | ✅ |
| **Tool / MCP** | Read/Grep/Shell, pytest | ✅ |
| **Test Loop** | Skill + Command 문서화 | ⏳ 코드 미구현 |
| **Hook** | — | ❌ |

---

## 4. Rule — `.cursor/rules/*.mdc`

| 파일 | 내용 | 적용 |
|------|------|------|
| `unitconverter-domain.mdc` | 도메인, 5카테고리, E001~E007 | alwaysApply |
| `unitconverter-architecture.mdc` | ECB, Dual-Track | alwaysApply |
| `unitconverter-testing.mdc` | D-*/U-*, pytest | globs: tests/** |
| `unitconverter-tdd.mdc` | RED→GREEN→REFACTOR | alwaysApply |
| `unitconverter-ssot.mdc` | 변환 계수·Base Unit SSOT | globs: src/** |
| `unitconverter-ai-behavior.mdc` | 한국어, git commit 규칙 | alwaysApply |

루트 `.cursorrules` → **삭제**, `.mdc`로 완전 이전.

---

## 5. Skill — `unit-converter-tdd`

| 파일 | 역할 |
|------|------|
| `SKILL.md` | RED/GREEN/REFACTOR, Dual-Track, ECB·Mock·E001~E007, pytest Loop |
| `reference.md` | D-* ID 18건 (D-I/L/W/T/A/V/S/C) |

**Phase 선언:**

```
Phase: RED | GREEN | REFACTOR | spec
Layer: entity | control | boundary
Track: Logic | UI
```

---

## 6. Command — TDD Slash 워크플로

| 파일 | 슬래시 | Phase | 수정 허용 | 핵심 |
|------|--------|-------|-----------|------|
| `spec.md` | `/spec` | spec | **없음** (read-only) | PRD·ARCHITECTURE·Rules 정합, 다음 Target 제안 |
| `red.md` | `/red` | RED | `tests/`만 | AAA 테스트 1건, pytest **FAIL** |
| `green.md` | `/green` | GREEN | `src/` (해당 Layer) | RED Target 최소 구현, Track PASS |
| `refactor.md` | `/refactor` | REFACTOR | `src/`·`tests/` (동작 불변) | SSOT·ECB 정리, `pytest -q` |

**TDD 순서:** `/spec` → `/red` → `/green` → `/refactor` → `/red` …

**공통 Command 구조:** Objective · Input · Output · Steps · Success Criteria · Restrictions

**삭제:** `tdd-red.md` → `red.md`로 통합·보강

**Dual-Track:**

| Track | Mock |
|-------|------|
| Logic (`test_d_*`) | Domain Mock **금지** |
| UI (`test_u_*`) | stdin/stdout·control Mock **허용** |

---

## 7. Agent — `AGENTS.md`

| Agent | 역할 |
|-------|------|
| Architect Agent | ECB·SSOT·Base Unit 설계 |
| TDD Coach Agent | RED→GREEN→REFACTOR 사이클 총괄 |
| Test Engineer Agent | `test_d_*` / `test_u_*` 작성·실행 |
| Code Reviewer Agent | ECB·TDD·Rule read-only 리뷰 |

각 Agent: Role · Responsibilities · Output · Restrictions 정의.

---

## 8. Spec · Architecture 문서

### 8.1 `docs/PRD.md`

| 섹션 | 내용 |
|------|------|
| 기능 | `<unit>:<value>` → **동일 카테고리 전 단위** 출력 |
| 비기능 | 결정성, SSOT, 검증 가능성 |
| 오류 | E001~E007 |
| AC | AC-01~AC-09 체크리스트 |

**PRD와 Open Item:** AC-02에서 카테고리 격리 명시 → O1은 PRD 초안 반영, **사용자 최종 확인 권장**.

### 8.2 `docs/ARCHITECTURE.md`

| 섹션 | 내용 |
|------|------|
| ECB | boundary → control → entity |
| SOLID | 계층·클래스별 적용 |
| 클래스 | UnitRegistry, Converter, InputValidator, ConvertInputUseCase, CliApp 등 |
| 흐름 | 입력 · 변환 · 오류 (sequence/flowchart) |
| 테스트 | Dual-Track 전략 |
| 디렉터리 | `src/unitconverter/{entity,control,boundary}/` |

**entity 원칙:** 외부 I/O·상위 레이어 import **없음**.

---

## 9. D-* ID (reference.md)

| 접두 | ID | 주제 |
|------|-----|------|
| D-I* | D-I01~I04 | 입력·오류 |
| D-L* | D-L01~L03 | Length |
| D-W* | D-W01~W02 | Weight |
| D-T* | D-T01~T03 | Temperature |
| D-A* | D-A01~A02 | Area |
| D-V* | D-V01~V02 | Volume |
| D-S/C* | D-S01, D-C01~C02 | SSOT, control |

---

## 10. 갭 분석

| 항목 | 현재 | 목표 |
|------|------|------|
| `UnitConverter.py` | 3단위 프로토타입 | PRD 5카테고리 + ECB |
| `src/` | 없음 | ARCHITECTURE 디렉터리 |
| `tests/` | 없음 | `test_d_*` / `test_u_*` |
| Command | 4 Phase 완비 | `/review-ecb` 선택 추가 |
| U-* ID | Skill만 언급 | reference 또는 별도 카탈로그 |

---

## 11. Open Items

| ID | 항목 | 상태 |
|----|------|------|
| O1 | 출력 범위 — 같은 카테고리만? | PRD AC-02 반영 · **사용자 확인 권장** |
| O2 | Temperature 비선형 전략 | ARCHITECTURE `TemperatureConverter` · **계수 확인 권장** |
| O3 | pyeong ↔ sqm (3.305785?) | **미확정** |
| O4 | 구현 우선순위 (Length first?) | **미확정** |
| O5 | U-* ID 카탈로그 | ⏳ STEP 3 |
| O6 | `/green`, `/refactor` Command | ✅ **완료** |
| O7 | `/review-ecb` Command | ⏳ 선택 |
| O8 | `src/` + 첫 `/red` (D-I01 등) | ⏳ STEP 3 |

---

## 12. 성공 기준

| ID | 기준 | 판정 |
|----|------|------|
| SC1-1 | Rule `.mdc` 6파일, `.cursorrules` 제거 | ✅ |
| SC1-2 | Skill 전 Phase · Dual-Track · pytest Loop | ✅ |
| SC1-3 | reference.md D-* 18건 | ✅ |
| SC1-4 | Command 4종 (`spec`/`red`/`green`/`refactor`) | ✅ |
| SC1-5 | Skill·Command ↔ Rule 정합 | ✅ |
| SC2-1 | `docs/PRD.md` (요구사항만) | ✅ |
| SC2-2 | `docs/ARCHITECTURE.md` (ECB·SOLID) | ✅ |
| SC2-3 | `AGENTS.md` (4 Agent) | ✅ |
| SC2-4 | 01_Report · 01_Prompt 최신화 | ✅ |

---

## 13. 다음 단계 (STEP 3+)

- [ ] Open Item O1~O4 사용자 확인
- [ ] `/spec` → `/red` D-I01 또는 D-L01 — `tests/test_d_*.py` 생성
- [ ] `src/unitconverter/` ECB 스켈레ton (ARCHITECTURE §10)
- [ ] (선택) `/review-ecb` Command
- [ ] U-* reference · `test_u_*`

---

## 14. 참고

| 문서 | 경로 |
|------|------|
| PRD | `docs/PRD.md` |
| Architecture | `docs/ARCHITECTURE.md` |
| Agents | `AGENTS.md` |
| Rules | `.cursor/rules/unitconverter-*.mdc` |
| Skill | `.cursor/skills/unit-converter-tdd/SKILL.md` |
| D-* ID | `.cursor/skills/unit-converter-tdd/reference.md` |
| Commands | `.cursor/commands/{spec,red,green,refactor}.md` |
| Transcript | `prompts/01_Prompt_Spec.md` |
| 프로토타입 | `UnitConverter.py`, `README.md` |
