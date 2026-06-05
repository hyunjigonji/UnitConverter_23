from unitconverter.boundary.convert_gateway import ConvertGateway


class OutputPresenter:
    def __init__(self, gateway: ConvertGateway | None = None):
        self._gateway = gateway or ConvertGateway()

    def present(self, raw: str) -> str:
        response = self._gateway.convert(raw)
        return "\n".join(response.lines)
