from unitconverter.entity.converter import Converter
from unitconverter.entity.models import Quantity


def test_d_len_08_meter_to_yard():
    # Given
    quantity = Quantity("meter", 2.5)
    converter = Converter()

    # When
    result = converter.convert(quantity)

    # Then
    assert result["yard"] == 2.734
