from typing import List
from fastapi import FastAPI,Depends
from models import RoomTypeCreate,RoomTypeResponse,AvailabilityOut,AvailabilityCreate,AvailabilityBase
from dbservice import Availability,Reservation,RoomType,SessionLocal
from fastapi.middleware.cors import CORSMiddleware  
from sqlalchemy.orm import Session

app=FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Add CORS middleware
origins = [
    '*'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
)

@app.post('/room_types')
def create_room_type(room:RoomTypeCreate,db: Session = Depends(get_db)):
    new_room_type=RoomType(
        roomtype=room.roomtype,
        price=room.price,
        size=room.size,
        occupancy=room.occupancy,
        childlocc=room.childlocc,
        imageurl=room.imageurl,
        description=room.description
    )
    db.add(new_room_type)
    db.commit()
    db.refresh(new_room_type)
    return new_room_type


@app.get('/room_types', response_model=list[RoomTypeResponse])
def get_room_types(db: Session = Depends(get_db)):

    room_types=db.query(RoomType).all()
    return room_types


@app.post("/availability", response_model=List[AvailabilityOut])
def get_availability(available: AvailabilityCreate, db: Session = Depends(get_db)):
    availability = db.query(Availability).filter(Availability.roomtype_id == available.roomtype,
    Availability.start_date <= available.end_date,Availability.end_date >= available.start_date).all()
    return availability