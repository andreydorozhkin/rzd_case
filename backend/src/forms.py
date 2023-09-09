from pydantic import BaseModel


class PlatformForm(BaseModel):
    length: int
    width: int
    mass: int
    height: int
    center_of_gravity_height: int
    platform_base: int
    wheel_radius: int


class CargoForm(BaseModel):
    name: str
    length: int
    width: int
    height: int
    count: int
    weight: int


class CreatePlatformForm(BaseModel):
    #platform: PlatformForm
    cargo_list: list[CargoForm]
