# UnitConverter_23

![unit-converter](./unit-converter.jpg)

단위와 값을 한 줄로 입력하면, **같은 카테고리의 모든 지원 단위**로 변환 결과를 출력하는 CLI 프로그램입니다.

**아키텍처:** ECB (Entity — Control — Boundary)  
**개발 방식:** Dual-Track TDD (Logic `test_d_*` · UI `test_u_*`)

---

## 개요

| 항목 | 내용 |
|------|------|
| 입력 | `<unit>:<value>` (예: `meter:2.5`) |
| 출력 | `<unit>:<converted_value>` — 한 줄에 한 단위 |
| 오류 | E001~E007 코드 |
| Base Unit | Length→meter · Weight→g · Temperature→celsius · Area→sqm · Volume→liter |

**예시**

입력:

```
meter:2.5
```

출력 (Length 카테고리 전 단위):

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

## 지원 단위

| 카테고리 | 단위 |
|----------|------|
| Length | mm, cm, meter, km, inch, feet, yard, mile |
| Weight | mg, g, kg, oz, lb |
| Temperature | celsius, fahrenheit, kelvin |
| Area | sqm, pyeong, acre, hectare |
| Volume | ml, liter, gallon |

---

## 프로젝트 구조

```
UnitConverter_23/
├── docs/
│   ├── PRD.md                 # 제품 요구사항
│   └── ARCHITECTURE.md        # ECB·SOLID 설계
├── src/                       # (GREEN 단계에서 구현 예정)
│   └── unitconverter/
│       ├── entity/
│       ├── control/
│       └── boundary/
├── tests/
│   ├── conftest.py
│   └── entity/
│       └── test_d_len_01.py   # D-LEN-01 RED
├── reports/                   # 단계별 보고서
├── prompts/                   # 세션 Transcript
├── .cursor/
│   ├── rules/                 # 개발 규칙 (SSOT)
│   ├── skills/unit-converter-tdd/
│   └── commands/              # /spec · /red · /green · /refactor
├── AGENTS.md
├── UnitConverter.py           # 레거시 프로토타입 (meter/feet/yard)
└── README.md
```

---

## 설치 및 실행

### 가상환경

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

pip install pytest
```

### 레거시 프로토타입 (UnitConverter.py)

```bash
python UnitConverter.py
```

> ECB 기반 CLI(`src/unitconverter/boundary/`)는 GREEN 단계 이후 제공 예정입니다.

### 테스트

```bash
# D-LEN-01 RED (현재: 의도적 FAIL)
python -m pytest tests/entity/test_d_len_01.py::test_d_len_01_meter_to_centimeter -v

# Logic Track 전체 (추가 후)
python -m pytest tests/ -v
```

---

## TDD 워크플로

```
/spec  →  /red  →  /green  →  /refactor  →  /red  → ...
```

| Track | 대상 | 테스트 | Mock |
|-------|------|--------|------|
| Logic | entity, control | `test_d_*` | Domain Mock **금지** |
| UI | boundary | `test_u_*` | stdin/stdout Mock **허용** |

**현재 진행:** STEP 3 — D-LEN-01 RED 완료 (entity · meter→cm) · GREEN 대기

---

## 오류 코드

| 코드 | 이름 |
|------|------|
| E001 | InvalidInputFormat |
| E002 | UnsupportedUnit |
| E003 | InvalidNumericValue |
| E004 | EmptyInput |
| E005 | ConversionNotSupported |
| E006 | InternalConversionError |
| E007 | UnknownError |

---

## 참고 문서

| 문서 | 경로 |
|------|------|
| PRD | [docs/PRD.md](docs/PRD.md) |
| Architecture | [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) |
| Agent 역할 | [AGENTS.md](AGENTS.md) |
| TDD Skill | [.cursor/skills/unit-converter-tdd/SKILL.md](.cursor/skills/unit-converter-tdd/SKILL.md) |
| Domain 테스트 ID | [.cursor/skills/unit-converter-tdd/reference.md](.cursor/skills/unit-converter-tdd/reference.md) |
| Spec Report | [reports/01_Report_Spec.md](reports/01_Report_Spec.md) |
| RED Report | [reports/02_Report_Red.md](reports/02_Report_Red.md) |

---

## 실습 맥락 (생성형 AI 활용, 6시간)

| 단계 | 내용 | 시간 |
|------|------|------|
| 1 | 문제 코드·요구사항 분석 | 0.5h |
| 2 | OCP·SRP 기반 기본 구현 | 2h |
| 3 | TC 작성 (단위 변환·입력 검증) | 0.5h |
| 4 | 추가 요구사항 (설정 외부화·동적 등록·출력 포맷) | 2h |
| 5 | 회고·발표 | 1h |

> 본 저장소는 위 실습을 **ECB + Dual-Track TDD**로 재구성한 UnitConverter_23 버전입니다. 레거시 `UnitConverter.py`는 초기 프로토타입이며, PRD·ARCHITECTURE 기준 구현으로 점진 대체합니다.
