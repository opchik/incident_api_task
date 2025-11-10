from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional

from . import models, schemas
from .database import get_db

app = FastAPI(
    title="Incident API",
    description="API для учета инцидентов",
    version="1.0.0"
)

@app.post("/incidents/", response_model=schemas.IncidentResponse)
def create_incident(incident: schemas.IncidentCreate, db: Session = Depends(get_db)):
    db_incident = models.Incident(**incident.dict())
    db.add(db_incident)
    db.commit()
    db.refresh(db_incident)
    return db_incident

@app.get("/incidents/", response_model=List[schemas.IncidentResponse])
def get_incidents(
    status: Optional[schemas.IncidentStatus] = None,
    db: Session = Depends(get_db)
):
    query = db.query(models.Incident)
    if status:
        query = query.filter(models.Incident.status == status)
    return query.all()

@app.get("/incidents/{incident_id}", response_model=schemas.IncidentResponse)
def get_incident(incident_id: int, db: Session = Depends(get_db)):
    incident = db.query(models.Incident).filter(models.Incident.id == incident_id).first()
    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")
    return incident

@app.patch("/incidents/{incident_id}", response_model=schemas.IncidentResponse)
def update_incident_status(
    incident_id: int, 
    incident_update: schemas.IncidentUpdate, 
    db: Session = Depends(get_db)
):
    incident = db.query(models.Incident).filter(models.Incident.id == incident_id).first()
    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")
    
    incident.status = incident_update.status
    db.commit()
    db.refresh(incident)
    return incident

@app.get("/")
def root():
    return {"message": "Incident API is running"}