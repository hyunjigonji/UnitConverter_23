from unitconverter.entity.converter import Converter
from unitconverter.entity.models import Quantity


def test_d_len_02_feet_to_inch_via_base():
    # Given
    quantity = Quantity("feet", 1.0)
    converter = Converter()

    # When
    result = converter.convert(quantity)

    # Then
    assert result["inch"] == 12
