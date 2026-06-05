import pytest


def test_d_len_12_length_category_isolation():
    # Given: Quantity("meter", 2.5)
    # When: Converter.convert() 호출
    # Then: 결과 단위가 Length 8종만 포함 (Weight/Temperature/Area/Volume 없음)
    pytest.fail(
        "RED: D-LEN-12 — 구현 없음, 의도적 실패"
    )
