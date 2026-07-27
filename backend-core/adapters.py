from interfaces import EHRPort, AIPort
# Optional: import dataclasses or pydantic for strict typing
from typing import Dict, Any

class MockEHRAdapter(EHRPort):
    async def get_patient_data(self, patient_id: str) -> Dict[str, Any]:
        # Simulate an error case for testing resilience
        if not patient_id or patient_id == "INVALID":
            raise ValueError(f"Patient ID {patient_id} not found in EHR.")
            
        return {
            "patient_id": patient_id,
            "name": "John Doe",
            "heart_rate": 90,
            "status": "Stable"
        }

class MockAIAdapter(AIPort):
    async def generate_clinical_note(self, audio_text: str) -> Dict[str, str]:
        # Simulate a failure if no audio is provided
        if not audio_text.strip():
            raise ValueError("Audio text stream is empty. Cannot generate note.")
            
        return {
            "Subjective": "Patient reports feeling well.",
            "Objective": "Vitals are stable.",
            "Assessment": "Routine checkup.",
            "Plan": "Continue current monitoring."
        }