from fastapi import Depends, FastAPI, Form
from sqlalchemy.orm import Session
from enum import Enum
import models
from database import SessionLocal, engine

from datetime import date

import time
print("Sleep for 10 sec to wait for db")
time.sleep(10)

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


class Sorting(Enum):
    Cost = 'cost'
    Date = 'date'


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/rooms/create")
def create_room(description: str = Form(...), cost: float = Form(...), db: Session = Depends(get_db)):
    db_room = models.Room(description=description, cost=cost, date_added=date.today())
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return {"room_id": db_room.id}


@app.get("/rooms/list")
def get_rooms_list(db: Session = Depends(get_db), sort_by: Sorting = Sorting.Date, ascending: bool = True):
    if sort_by == Sorting.Date:
        q = sorted(db.query(models.Room).all(), key=lambda room: room.date_added)
    else:
        q = sorted(db.query(models.Room).all(), key=lambda room: room.cost)
    if not ascending:
        q.reverse()
    return q


@app.delete("/room/delete")
def delete_room(db: Session = Depends(get_db), room_id: int = Form(...)):
    room_to_delete = db.query(models.Room).filter_by(id=room_id).first()
    db.delete(room_to_delete)
    db.commit()


@app.post("/bookings/create")
def create_booking(db: Session = Depends(get_db), room_id: int = Form(...), date_start: date = Form(...),
                   date_end: date = Form(...)):
    db_booking = models.Booking(room_id=room_id, date_start=date_start, date_end=date_end)
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return {"booking_id": db_booking.id}


@app.get("/bookings/list")
def get_bookings_list(room_id: int, db: Session = Depends(get_db)):
    return sorted(db.query(models.Booking).filter_by(room_id=room_id).all(), key=lambda booking: booking.date_start)


@app.delete("/bookings/delete")
def delete_booking(booking_id: int = Form(...), db: Session = Depends(get_db)):
    booking_to_delete = db.query(models.Booking).filter_by(id=booking_id).first()
    db.delete(booking_to_delete)
    db.commit()
