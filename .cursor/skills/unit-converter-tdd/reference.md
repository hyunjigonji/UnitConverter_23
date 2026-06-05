# Domain 테스트 ID (D-*)

Logic Track · `test_d_*` 전용. U-*는 Skill 본문 UI Track 표 참고.

## 입력·오류

| ID | Given-When-Then 요약 |
|----|----------------------|
| D-I01 | 빈 입력 → E004 EmptyInput |
| D-I02 | `:` 없음 → E001 InvalidInputFormat |
| D-I03 | 숫자 아님 → E003 InvalidNumericValue |
| D-I04 | 미지원 단위 → E002 UnsupportedUnit |

## Length (Base: meter)

| ID | Given-When-Then 요약 |
|----|----------------------|
| D-L01 | meter → cm 결정적 변환 |
| D-L02 | feet → meter → inch (Base Unit 경유) |
| D-L03 | 동일 입력 반복 시 동일 출력 (deterministic) |

## Weight (Base: g)

| ID | Given-When-Then 요약 |
|----|----------------------|
| D-W01 | kg → g → oz |
| D-W02 | mg → kg (소수 정밀) |

## Temperature (Base: celsius)

| ID | Given-When-Then 요약 |
|----|----------------------|
| D-T01 | celsius → fahrenheit 공식 변환 |
| D-T02 | kelvin → celsius |
| D-T03 | 카테고리 외 단위 → E005 ConversionNotSupported |

## Area (Base: sqm)

| ID | Given-When-Then 요약 |
|----|----------------------|
| D-A01 | sqm → pyeong |
| D-A02 | acre → hectare (Base 경유) |

## Volume (Base: liter)

| ID | Given-When-Then 요약 |
|----|----------------------|
| D-V01 | liter → ml |
| D-V02 | gallon → liter |

## SSOT · Control

| ID | Given-When-Then 요약 |
|----|----------------------|
| D-S01 | 변환 계수 단일 소스에서만 로드 |
| D-C01 | control: 파싱 후 entity 변환 오케스트레이션 |
| D-C02 | entity 예외 → E006 InternalConversionError 매핑 |
