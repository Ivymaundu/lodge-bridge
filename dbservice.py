import enum
from sqlalchemy import Boolean, CheckConstraint, Enum, ForeignKey, create_engine, Column,Float, String, Integer,event, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship
from datetime import datetime 
import sqlite3

SQLALCHEMY_DATABASE_URL = "sqlite:///./lodge_api.db"

engine= create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class RoomType(Base):
    __tablename__='room_types'

    id = Column(Integer, primary_key=True, autoincrement=True)
    roomtype = Column(String, nullable=False)
    price=Column(Float, nullable=False)
    size=Column(Float,nullable=False)
    occupancy=Column(Integer,nullable=False)
    childlocc=Column(Integer,nullable=False)
    imageurl=Column(String)
    description=Column(String)

    
    availability=relationship('Availability',back_populates='roomType')
    reservations = relationship("Reservation", back_populates="room")

class Availability(Base):
    __tablename__='availability'

    id = Column(Integer, primary_key=True, autoincrement=True)
    start_date=Column(DateTime, default=datetime.utcnow, nullable=False)
    Room_type=Column(String,nullable=False)
    end_date=Column(DateTime, nullable=False)
    roomtype_id = Column(Integer, ForeignKey('room_types.id'),nullable=False)
    rooms_to_sell=Column(Integer,nullable=False)

    roomType=relationship('RoomType',back_populates='availability')

class Reservation(Base):
    __tablename__='reservations'

    id = Column(Integer, primary_key=True, autoincrement=True)
    start_date=Column(DateTime, nullable=False)
    end_date=Column(DateTime, nullable=False)
    room_id = Column(Integer, ForeignKey('room_types.id'), nullable=False)
    guest_no = Column(Integer, nullable=False)
    no_of_children = Column(Integer, nullable=False)
    address = Column(String, nullable=False)
    email_address = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    nationality = Column(String, nullable=False)
    country = Column(String, nullable=False)
    created_at=Column(DateTime, default=datetime.utcnow, nullable=False)

    room=relationship('RoomType',back_populates='reservations')





Base.metadata.create_all(bind=engine)