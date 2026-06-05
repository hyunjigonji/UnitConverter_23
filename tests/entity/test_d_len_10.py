from unitconverter.entity.converter import Converter
from unitconverter.entity.models import Quantity

LENGTH_UNITS = {"mm", "cm", "meter", "km", "inch", "feet", "yard", "mile"}


def test_d_len_10_all_length_units_from_meter():
    # Given
    quantity = Quantity("meter", 2.5)
    converter = Converter()

    # When
    result = converter.convert(quantity)

    # Then
    assert len(result) == 8
    assert set(result.keys()) == LENGTH_UNITS
