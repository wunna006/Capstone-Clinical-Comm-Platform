from interfaces import EHRPort, AIPort

class MockEHRAdapter(EHRPort):
    # Add 'async' here
    async def get_patient_data(self, patient_id: str) -> dict:
        print(f"[EHR ADAPTER] Fetching data for {patient_id} from Mock Epic EHR...")
        return {
            "patient_id": patient_id,
            "name": "John Doe",
            "heart_rate": 90,
            "blood_pressure": "120/80",
            "status": "Stable"
        }

class MockAIAdapter(AIPort):
    # Add 'async' here
    async def generate_clinical_note(self, audio_text: str) -> dict:
        print(f"[AI ADAPTER] Processing audio text into SOAP note...")
        return {
            "Subjective": "Patient reports feeling well.",
            "Objective": "Vitals are stable.",
            "Assessment": "Routine checkup.",
            "Plan": "Continue current monitoring."
        }
    