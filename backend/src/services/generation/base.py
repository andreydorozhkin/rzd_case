from src.dtos import CalculatedDataDTO
from src.services.generation.builder import PlatformMeshBuilder


class GenerationService:
    _builder = PlatformMeshBuilder

    def execute(self, data: CalculatedDataDTO) -> str:
        self._builder(platform=data.platform).build()
        return "files/test.pdf"
