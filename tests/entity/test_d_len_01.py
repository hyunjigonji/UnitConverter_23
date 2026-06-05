from unitconverter.entity.converter import Converter
from unitconverter.entity.models import Quantity


def test_d_len_01_meter_to_centimeter():
    # Given
    quantity = Quantity("meter", 1.0)
    converter = Converter()

    # When
    result = converter.convert(quantity)

    # Then
    assert result["cm"] == 100
