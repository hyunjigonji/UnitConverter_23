from unitconverter.entity.converter import Converter
from unitconverter.entity.models import Quantity


def test_d_len_11_meter_identity_in_result():
    # Given
    quantity = Quantity("meter", 2.5)
    converter = Converter()

    # When
    result = converter.convert(quantity)

    # Then
    assert result["meter"] == 2.5
