from interfaces import EHRPort, AIPort

class MockEHRAdapter(EHRPort):
    def get_patient_data(self, patient_id: str) -> dict:
        return {
            "patient_id": patient_id,
            "name": "John Doe",
            "heart_rate": 90,
            "status": "Stable"
        }

class MockAIAdapter(AIPort):
    def generate_clinical_note(self, audio_text: str) -> dict:
        return {
            "Subjective": "Patient reports feeling well.",
            "Objective": "Vitals are stable.",
            "Assessment": "Routine checkup.",
            "Plan": "Continue current monitoring."
        }
    