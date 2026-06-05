from unitconverter.entity.models import Quantity


class Converter:
    def convert(self, quantity: Quantity) -> dict[str, float]:
        if quantity.unit == "meter":
            return {"cm": quantity.value * 100}
        return {}
