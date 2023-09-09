from src.dtos import TransformedDataDTO, CalculatedDataDTO


class CalculationService:

    def execute(self, data: TransformedDataDTO) -> CalculatedDataDTO:
        return data
