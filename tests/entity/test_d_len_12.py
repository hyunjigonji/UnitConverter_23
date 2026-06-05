from unitconverter.entity.converter import Converter
from unitconverter.entity.models import Quantity

LENGTH_UNITS = {"mm", "cm", "meter", "km", "inch", "feet", "yard", "mile"}


def test_d_len_12_length_category_isolation():
    # Given
    quantity = Quantity("meter", 2.5)
    converter = Converter()

    # When
    result = converter.convert(quantity)

    # Then
    assert set(result.keys()) == LENGTH_UNITS
