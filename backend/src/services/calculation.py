from src.dtos import TransformedDataDTO, CalculatedDataDTO


class CalculationService:
    def __init__(self):
        pass

    def execute(self, data: TransformedDataDTO) -> CalculatedDataDTO:
        ...
