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

## 구현 현황

| 카테고리 | Logic (D-*) | UI (U-*) | 비고 |
|----------|---------------|----------|------|
| **Length** | D-LEN-01~13 ✅ | U-OUT-01 ✅ | GREEN + REFACTOR R1 완료 |
| Weight | — | — | 후속 RED |
| Temperature | — | — | 후속 RED |
| Area | — | — | 후속 RED |
| Volume | — | — | 후속 RED |
| 입력 검증 (E001~E004) | — | — | D-I01 RED 예정 |

**테스트:** `14 passed, 0 failed` (Logic 13 + UI 1)

---

## 지원 단위

| 카테고리 | 단위 | 구현 |
|----------|------|------|
| Length | mm, cm, meter, km, inch, feet, yard, mile | ✅ |
| Weight | mg, g, kg, oz, lb | ⏳ |
| Temperature | celsius, fahrenheit, kelvin | ⏳ |
| Area | sqm, pyeong, acre, hectare | ⏳ |
| Volume | ml, liter, gallon | ⏳ |

---

## 프로젝트 구조

```
UnitConverter_23/
├── docs/
│   ├── PRD.md
│   └── ARCHITECTURE.md
├── src/unitconverter/
│   ├── entity/                # Quantity, Converter, conversion_factors (SSOT)
│   ├── control/               # ConvertInputUseCase, output_formatter, dto
│   └── boundary/              # ConvertGateway, OutputPresenter
├── tests/
│   ├── _approval.py           # Golden Master helper
│   ├── conftest.py
│   ├── golden/                # U-OUT-01 approved 출력
│   ├── entity/                # test_d_len_01.py ~ test_d_len_13.py
│   └── boundary/              # test_u_out_01.py
├── reports/                   # 01 Spec · 02 RED · 03 GREEN · 04 REFACTOR
├── prompts/                   # 세션 Transcript
├── .cursor/
│   ├── rules/
│   ├── skills/unit-converter-tdd/
│   └── commands/              # /spec · /red · /green · /refactor
├── AGENTS.md
├── UnitConverter.py           # 레거시 프로토타입 (meter/feet/yard)
├── pytest.ini
└── README.md
```

**ECB 의존 방향:** `boundary → control → entity`

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

### ECB 기반 변환 (Python)

stdin/stdout CLI(`CliApp`)는 후속 U-* Track에서 제공 예정입니다.  
현재는 boundary `OutputPresenter`로 동일 출력을 확인할 수 있습니다.

```python
from unitconverter.boundary.output_presenter import OutputPresenter

print(OutputPresenter().present("meter:2.5"))
```

### 레거시 프로토타입 (UnitConverter.py)

```bash
python UnitConverter.py
```

> meter · feet · yard 3단위만 지원하는 초기 프로토타입입니다. PRD·ARCHITECTURE 기준 `src/` 구현으로 점진 대체 중입니다.

### 테스트

```bash
# 전체 회귀 (Logic 13 + UI 1)
python -m pytest tests/ -v

# Logic Track — Length entity
python -m pytest tests/entity/ -v

# UI Track — Golden Master
python -m pytest tests/boundary/test_u_out_01.py -v
```

Golden 파일 갱신 (의도적 변경 시에만):

```powershell
# Windows PowerShell
$env:UPDATE_GOLDEN="1"; python -m pytest tests/boundary/test_u_out_01.py -v
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

| 단계 | 상태 | 산출 |
|------|------|------|
| STEP 1 Spec | ✅ | PRD · ARCHITECTURE · D-* ID |
| STEP 2 RED | ✅ | D-LEN-01~13 스켈레톤 |
| STEP 3 GREEN | ✅ | entity · control · boundary · U-OUT-01 Golden |
| STEP 4 REFACTOR | ✅ | R1 — `convert_ordered()` extract |
| STEP 5+ | ⏳ | D-I01 RED (입력 검증) · 추가 카테고리 |

---

## 오류 코드

| 코드 | 이름 | 상태 |
|------|------|------|
| E001 | InvalidInputFormat | ⏳ D-I RED 후속 |
| E002 | UnsupportedUnit | ⏳ |
| E003 | InvalidNumericValue | ⏳ |
| E004 | EmptyInput | ⏳ |
| E005 | ConversionNotSupported | ⏳ |
| E006 | InternalConversionError | ⏳ |
| E007 | UnknownError | ⏳ |

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
| GREEN Report | [reports/03_Report_Green.md](reports/03_Report_Green.md) |
| REFACTOR Report | [reports/04_Report_Refactoring.md](reports/04_Report_Refactoring.md) |

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
