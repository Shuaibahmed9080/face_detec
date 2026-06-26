from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database import Base

class Attendance(Base):
    __tablename__ = "attendance_logs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    age = Column(Integer)
    gender = Column(String(50))
    status = Column(String(50))
    time = Column(DateTime, default=datetime.utcnow)