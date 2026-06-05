import pytest


def test_d_len_03_deterministic_repeat():
    # Given: Quantity("meter", 2.5)
    # When: Converter.convert() 2회 연속 호출
    # Then: 두 ConvertResult 완전 동일
    pytest.fail(
        "RED: D-LEN-03 — 구현 없음, 의도적 실패"
    )
