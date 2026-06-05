from unitconverter.entity.converter import Converter
from unitconverter.entity.models import Quantity


def test_d_len_09_meter_to_mile():
    # Given
    quantity = Quantity("meter", 2.5)
    converter = Converter()

    # When
    result = converter.convert(quantity)

    # Then
    assert result["mile"] == 0.001553
