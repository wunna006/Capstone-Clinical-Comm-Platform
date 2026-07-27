from interfaces import EHRPort, AIPort
<<<<<<< HEAD

class MockEHRAdapter(EHRPort):
    # Add 'async' here
    async def get_patient_data(self, patient_id: str) -> dict:
        print(f"[EHR ADAPTER] Fetching data for {patient_id} from Mock Epic EHR...")
=======
# Optional: import dataclasses or pydantic for strict typing
from typing import Dict, Any

class MockEHRAdapter(EHRPort):
    async def get_patient_data(self, patient_id: str) -> Dict[str, Any]:
        # Simulate an error case for testing resilience
        if not patient_id or patient_id == "INVALID":
            raise ValueError(f"Patient ID {patient_id} not found in EHR.")
            
>>>>>>> 5e9711d92bcd600b862ea549fe4be57f5f3cde16
        return {
            "patient_id": patient_id,
            "name": "John Doe",
            "heart_rate": 90,
<<<<<<< HEAD
            "blood_pressure": "120/80",
=======
>>>>>>> 5e9711d92bcd600b862ea549fe4be57f5f3cde16
            "status": "Stable"
        }

class MockAIAdapter(AIPort):
<<<<<<< HEAD
    # Add 'async' here
    async def generate_clinical_note(self, audio_text: str) -> dict:
        print(f"[AI ADAPTER] Processing audio text into SOAP note...")
=======
    async def generate_clinical_note(self, audio_text: str) -> Dict[str, str]:
        # Simulate a failure if no audio is provided
        if not audio_text.strip():
            raise ValueError("Audio text stream is empty. Cannot generate note.")
            
>>>>>>> 5e9711d92bcd600b862ea549fe4be57f5f3cde16
        return {
            "Subjective": "Patient reports feeling well.",
            "Objective": "Vitals are stable.",
            "Assessment": "Routine checkup.",
            "Plan": "Continue current monitoring."
<<<<<<< HEAD
        }
    
=======
        }
>>>>>>> 5e9711d92bcd600b862ea549fe4be57f5f3cde16
