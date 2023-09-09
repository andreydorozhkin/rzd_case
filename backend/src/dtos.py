from pydantic import BaseModel


class PlatformDTO(BaseModel):
    length: int
    width: int
    mass: int
    height: int
    center_of_gravity_height: int
    platform_base: int


class CargoDTO(BaseModel):
    name: str
    length: int
    width: int
    height: int
    count: int
    weight: int


class CoordinateDTO(BaseModel):
    x: int
    y: int


class PositionedCargoDTO(BaseModel):
    cargo: CargoDTO
    coordinate: CoordinateDTO


class TransformedDataDTO(BaseModel):
    platform: PlatformDTO
    cargos: list[CargoDTO]


class CalculatedDataDTO(BaseModel):
    platform: PlatformDTO
    positioned_cargos: list[PositionedCargoDTO]
