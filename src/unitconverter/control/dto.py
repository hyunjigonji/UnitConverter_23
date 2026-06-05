from dataclasses import dataclass


@dataclass(frozen=True)
class SuccessResponse:
    lines: list[str]
