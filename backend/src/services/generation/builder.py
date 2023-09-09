from src.dtos import PlatformDTO


class PlatformMeshBuilder:
    def __init__(self, platform: PlatformDTO):
        self._platform = platform

    def build(self):
        ...