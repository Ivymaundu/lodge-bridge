from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class RoomTypeCreate(BaseModel):
    roomtype:str
    price:float
    size:float
    occupancy:int
    childlocc:int
    imageurl:str | None
    description:str


class RoomTypeResponse(RoomTypeCreate):
    id:int
    


class AvailabilityBase(BaseModel):
    roomtype: str
    start_date: datetime
    end_date: datetime



class AvailabilityCreate(AvailabilityBase):
    pass


class AvailabilityOut(AvailabilityBase):
    id: int
    price: float
    size: float
    occupancy: int
    childocc: int
    imageurl: Optional[str] = None
    description: Optional[str] = None
    roomstosell: int

    class Config:
        from_attributes = True
