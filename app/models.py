import enum
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Enum

Base = declarative_base()


class IncidentStatus(str, enum.Enum):
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    RESOLVED = "resolved"
    CLOSED = "closed"


class IncidentSource(str, enum.Enum):
    OPERATOR = "operator"
    MONITORING = "monitoring"
    PARTNER = "partner"


class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=False)
    status = Column(Enum(IncidentStatus), default=IncidentStatus.OPEN)
    source = Column(Enum(IncidentSource), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())