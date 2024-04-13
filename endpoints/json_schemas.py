from pydantic import BaseModel, Field


class DataSchemasPost(BaseModel):
    year: int
    price: float
    CPU_model: str = Field('CPU model')
    Hard_disk_size: str = Field('Hard disk size')


class CheckSchemasPost(BaseModel):
    id: str
    name: str
    data: DataSchemasPost
    createdAt: str


class CheckSchemasDelete(BaseModel):
    message: str
