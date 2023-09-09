from src.dtos import TransformedDataDTO, PlatformDTO, CargoDTO
from src.forms import CreatePlatformForm


class TransformerService:
    def __init__(self):
        pass

    def execute(self, form: CreatePlatformForm) -> TransformedDataDTO:
        return TransformedDataDTO(platform=PlatformDTO(**form.platform.model_dump()),
                                  cargos=[CargoDTO(**c.model_dump()) for c in form.cargo_list])
