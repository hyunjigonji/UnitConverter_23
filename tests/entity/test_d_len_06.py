from unitconverter.entity.converter import Converter
from unitconverter.entity.models import Quantity


def test_d_len_06_meter_to_inch():
    # Given
    quantity = Quantity("meter", 2.5)
    converter = Converter()

    # When
    result = converter.convert(quantity)

    # Then
    assert result["inch"] == 98.4252
