from unitconverter.entity.converter import Converter
from unitconverter.entity.models import Quantity


def test_d_len_03_deterministic_repeat():
    # Given
    quantity = Quantity("meter", 2.5)
    converter = Converter()

    # When
    result1 = converter.convert(quantity)
    result2 = converter.convert(quantity)

    # Then
    assert result1 == result2
