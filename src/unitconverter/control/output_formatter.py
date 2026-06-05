def format_value(value: float) -> str:
    if value == int(value):
        return str(int(value))
    return format(value, "g")
