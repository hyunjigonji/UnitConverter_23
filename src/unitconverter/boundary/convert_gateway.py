from unitconverter.control.convert_use_case import ConvertInputUseCase
from unitconverter.control.dto import SuccessResponse


class ConvertGateway:
    def __init__(self, use_case: ConvertInputUseCase | None = None):
        self._use_case = use_case or ConvertInputUseCase()

    def convert(self, raw: str) -> SuccessResponse:
        return self._use_case.execute(raw)
