from unitconverter.control.dto import SuccessResponse
from unitconverter.control.output_formatter import format_value
from unitconverter.entity.converter import Converter
from unitconverter.entity.models import Quantity


class ConvertInputUseCase:
    def __init__(self, converter: Converter | None = None):
        self._converter = converter or Converter()

    def execute(self, raw: str) -> SuccessResponse:
        unit, value_str = raw.split(":", 1)
        quantity = Quantity(unit, float(value_str))
        pairs = self._converter.convert_ordered(quantity)
        lines = [
            f"{name}:{format_value(value)}" for name, value in pairs
        ]
        return SuccessResponse(lines=lines)
