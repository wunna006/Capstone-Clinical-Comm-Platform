from pydantic import BaseModel
from typing import List
import datetime

class ClinicalNote(BaseModel):
    patient_id: str
    note_text: str
    timestamp: str

COMMAND_DB_MONGO = [] 
QUERY_DB_POSTGRES = [] 

def sync_databases(new_record: dict):
    print(f"[EVENT BUS] Syncing new record to Query DB: {new_record}")
    QUERY_DB_POSTGRES.append(new_record)

def write_clinical_note(patient_id: str, text: str):
    new_note = {
        "patient_id": patient_id, 
        "note_text": text, 
        "timestamp": str(datetime.datetime.now())
    }
    COMMAND_DB_MONGO.append(new_note)
    sync_databases(new_note)
    return new_note
