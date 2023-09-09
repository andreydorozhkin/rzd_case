from typing import Annotated

from fastapi import APIRouter, Depends
from starlette.responses import FileResponse

from src.forms import CreatePlatformForm
from src.services.calculation import CalculationService
from src.services.generation import GenerationService
from src.services.transformer import TransformerService

v1_router = APIRouter(prefix="/api/v1")


@v1_router.post("/generator/platform")
def create_3d_model(form: CreatePlatformForm,
                    transformer_service: Annotated[TransformerService, Depends()],
                    calculation_service: Annotated[CalculationService, Depends()],
                    generation_service: Annotated[GenerationService, Depends()],
                    ) -> FileResponse:
    objects_dto = transformer_service.execute(form)
    data = calculation_service.execute(objects_dto)
    file_path = generation_service.execute(data)
    return FileResponse(file_path)
