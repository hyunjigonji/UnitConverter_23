from unitconverter.entity.converter import Converter
from unitconverter.entity.models import Quantity


def test_d_len_07_meter_to_feet():
    # Given
    quantity = Quantity("meter", 2.5)
    converter = Converter()

    # When
    result = converter.convert(quantity)

    # Then
    assert result["feet"] == 8.2021
