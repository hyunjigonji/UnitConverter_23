from unitconverter.entity.converter import Converter
from unitconverter.entity.models import Quantity


def test_d_len_04_meter_to_kilometer():
    # Given
    quantity = Quantity("meter", 2.5)
    converter = Converter()

    # When
    result = converter.convert(quantity)

    # Then
    assert result["km"] == 0.0025
