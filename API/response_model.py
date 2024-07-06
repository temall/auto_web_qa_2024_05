from typing import Optional
from pydantic import BaseModel, Field


class ResourceRequest(BaseModel):
    id_: int = Field(alias="id", strict=True)
    project_tasks_resource_id: int
    volume: float
    cost: float
    batch_number: Optional[int] = None
    batch_parent_request_id: Optional[int] = None
    is_over_budget: bool
    created_at: int
    updated_at: int
    user_id: int
    needed_at: int
    created_by: int


class ResourceRequestResponse(BaseModel):
    project_tasks: list[ResourceRequest]


class CreateResourceRequestBody(BaseModel):
    project_tasks_resource_id: int
    volume: float
    cost: float
    needed_at: int


data = [
    {
        "id": 9431736,
        "project_tasks_resource_id": 12780121,
        "volume": "1.0000000000",
        "cost": "1200.0000000000",
        "batch_number": None,
        "batch_parent_request_id": None,
        "is_over_budget": True,
        "created_at": 1719859117,
        "updated_at": 1719859117,
        "user_id": 23073,
        "needed_at": 1719859108,
        "created_by": 23073
    }
]
