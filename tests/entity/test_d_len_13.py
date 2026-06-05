from unitconverter.entity.converter import Converter
from unitconverter.entity.models import Quantity


def test_d_len_13_inch_to_feet_via_base():
    # Given
    quantity = Quantity("inch", 12.0)
    converter = Converter()

    # When
    result = converter.convert(quantity)

    # Then
    assert result["feet"] == 1
