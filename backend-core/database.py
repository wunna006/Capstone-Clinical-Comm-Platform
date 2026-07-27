from pydantic import BaseModel
from typing import List
import datetime

<<<<<<< HEAD
# Data Models
=======
>>>>>>> 5e9711d92bcd600b862ea549fe4be57f5f3cde16
class ClinicalNote(BaseModel):
    patient_id: str
    note_text: str
    timestamp: str

<<<<<<< HEAD
# Simulated Databases
COMMAND_DB_MONGO = [] # Write-heavy
QUERY_DB_POSTGRES = [] # Read-heavy

# The Event Bus (Synchronization Script)
def sync_databases(new_record: dict):
    """Simulates an event bus updating the Read DB when the Write DB changes."""
    print(f"[EVENT BUS] Syncing new record to Query DB: {new_record}")
    QUERY_DB_POSTGRES.append(new_record)

# Command (Write Operation)
=======
COMMAND_DB_MONGO = [] 
QUERY_DB_POSTGRES = [] 

def sync_databases(new_record: dict):
    print(f"[EVENT BUS] Syncing new record to Query DB: {new_record}")
    QUERY_DB_POSTGRES.append(new_record)

>>>>>>> 5e9711d92bcd600b862ea549fe4be57f5f3cde16
def write_clinical_note(patient_id: str, text: str):
    new_note = {
        "patient_id": patient_id, 
        "note_text": text, 
        "timestamp": str(datetime.datetime.now())
    }
<<<<<<< HEAD
    COMMAND_DB_MONGO.append(new_note) # Write to Mongo
    sync_databases(new_note) # Trigger Event Bus
    return new_note

# Query (Read Operation)
def read_clinical_notes(patient_id: str) -> List[dict]:
    # Fast retrieval from Postgres
    return [note for note in QUERY_DB_POSTGRES if note["patient_id"] == patient_id]
=======
    COMMAND_DB_MONGO.append(new_note)
    sync_databases(new_note)
    return new_note
>>>>>>> 5e9711d92bcd600b862ea549fe4be57f5f3cde16
