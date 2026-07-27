from abc import ABC, abstractmethod

class EHRPort(ABC):
    @abstractmethod
    def get_patient_data(self, patient_id: str) -> dict:
        pass

class AIPort(ABC):
    @abstractmethod
    def generate_clinical_note(self, audio_text: str) -> dict:
        pass
<<<<<<< HEAD
    
=======
        
>>>>>>> 5e9711d92bcd600b862ea549fe4be57f5f3cde16
