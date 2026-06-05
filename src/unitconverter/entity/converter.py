from unitconverter.entity.conversion_factors import (
    LENGTH_UNITS,
    METERS_PER_UNIT,
    OUTPUT_PRECISION,
)
from unitconverter.entity.models import Quantity


class Converter:
    def convert(self, quantity: Quantity) -> dict[str, float]:
        base_meters = quantity.value * METERS_PER_UNIT[quantity.unit]
        result = {}
        for unit in LENGTH_UNITS:
            value = base_meters / METERS_PER_UNIT[unit]
            precision = OUTPUT_PRECISION.get(unit)
            if precision is not None:
                value = round(value, precision)
            result[unit] = value
        return result
