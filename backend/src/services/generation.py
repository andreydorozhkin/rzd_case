from src.dtos import CalculatedDataDTO


class GenerationService:
    def __init__(self):
        pass

    def execute(self, data: CalculatedDataDTO) -> str:
        return "files/test.txt"
