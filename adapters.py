from interfaces import EHRPort, AIPort

class MockEHRAdapter(EHRPort):
    def get_patient_data(self, patient_id: str) -> dict:
        # Simulating a call to Epic or Cerner
        print(f"[EHR ADAPTER] Fetching data for {patient_id} from Mock Epic EHR...")
        return {
            "patient_id": patient_id,
            "name": "John Doe",
            "heart_rate": 90,
            "blood_pressure": "120/80",
            "status": "Stable"
        }

class MockAIAdapter(AIPort):
    def generate_clinical_note(self, audio_text: str) -> dict:
        # Simulating a call to a Cloud Ambient AI Service
        print("[AI ADAPTER] Processing audio text into SOAP note...")
        return {
            "Subjective": "Patient reports feeling well.",
            "Objective": "Vitals are stable.",
            "Assessment": "Routine checkup.",
            "Plan": "Continue current monitoring."
        }

# Example of how to use them:
ehr = MockEHRAdapter()
patient_info = ehr.get_patient_data("PT-10293")

ai = MockAIAdapter()
soap_note = ai.generate_clinical_note("The patient says they feel fine today.")
