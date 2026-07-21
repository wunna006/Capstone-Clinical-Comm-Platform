from pydantic import BaseModel
from typing import List
import datetime

# Data Models
class ClinicalNote(BaseModel):
    patient_id: str
    note_text: str
    timestamp: str

# Simulated Databases
COMMAND_DB_MONGO = [] # Write-heavy
QUERY_DB_POSTGRES = [] # Read-heavy

# The Event Bus (Synchronization Script)
def sync_databases(new_record: dict):
    """Simulates an event bus updating the Read DB when the Write DB changes."""
    print(f"[EVENT BUS] Syncing new record to Query DB: {new_record}")
    QUERY_DB_POSTGRES.append(new_record)

# Command (Write Operation)
def write_clinical_note(patient_id: str, text: str):
    new_note = {
        "patient_id": patient_id, 
        "note_text": text, 
        "timestamp": str(datetime.datetime.now())
    }
    COMMAND_DB_MONGO.append(new_note) # Write to Mongo
    sync_databases(new_note) # Trigger Event Bus
    return new_note

# Query (Read Operation)
def read_clinical_notes(patient_id: str) -> List[dict]:
    # Fast retrieval from Postgres
    return [note for note in QUERY_DB_POSTGRES if note["patient_id"] == patient_id]
