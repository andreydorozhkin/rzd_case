from src.dtos import TransformedDataDTO, PlatformDTO, CargoDTO
from src.forms import CreatePlatformForm


class TransformerService:

    def execute(self, form: CreatePlatformForm) -> TransformedDataDTO:
        platform = PlatformDTO(length=2000,
                               width=300,
                               mass=21,
                               height=800,
                               center_of_gravity_height=600,
                               platform_base=1900)
        return TransformedDataDTO(platform=platform,
                                  cargos=[CargoDTO(**c.model_dump()) for c in form.cargo_list])
