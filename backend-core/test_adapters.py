import unittest
import asyncio
from adapters import MockEHRAdapter, MockAIAdapter

class TestAdapters(unittest.IsolatedAsyncioTestCase):
    async def test_ehr_data_retrieval(self):
        adapter = MockEHRAdapter()
        result = await adapter.get_patient_data("PT-10293")
        self.assertEqual(result["patient_id"], "PT-10293")
        self.assertEqual(result["status"], "Stable")

    async def test_ai_note_generation(self):
        adapter = MockAIAdapter()
        result = await adapter.generate_clinical_note("Patient is stable.")
        self.assertIn("Subjective", result)
        self.assertIn("Plan", result)

from adapters import MockEHRAdapter, MockAIAdapter

class TestMockEHRAdapter(unittest.IsolatedAsyncioTestCase):
    
    async def test_get_patient_data_success(self):
        """Test that valid patient IDs return the correct data dictionary."""
        adapter = MockEHRAdapter()
        result = await adapter.get_patient_data("12345")
        
        # Assertions check if the output matches our expectations
        self.assertEqual(result["patient_id"], "12345")
        self.assertEqual(result["name"], "John Doe")
        self.assertEqual(result["status"], "Stable")

    async def test_get_patient_data_invalid_id(self):
        """Test that an invalid patient ID correctly raises a ValueError."""
        adapter = MockEHRAdapter()
        
        # We expect this specific block of code to raise an error
        with self.assertRaises(ValueError):
            await adapter.get_patient_data("INVALID")
            
    async def test_get_patient_data_empty_id(self):
        """Test that an empty patient ID correctly raises a ValueError."""
        adapter = MockEHRAdapter()
        with self.assertRaises(ValueError):
            await adapter.get_patient_data("")

class TestMockAIAdapter(unittest.IsolatedAsyncioTestCase):
    
    async def test_generate_clinical_note_success(self):
        """Test that valid audio text generates a structured clinical note."""
        adapter = MockAIAdapter()
        audio_input = "Patient reports feeling well today."
        result = await adapter.generate_clinical_note(audio_input)
        
        # Verify the dictionary contains the expected medical SOAP note keys
        self.assertIn("Subjective", result)
        self.assertIn("Objective", result)
        self.assertIn("Assessment", result)
        self.assertIn("Plan", result)

    async def test_generate_clinical_note_empty_audio(self):
        """Test that empty or whitespace-only audio raises a ValueError."""
        adapter = MockAIAdapter()
        with self.assertRaises(ValueError):
            await adapter.generate_clinical_note("   ")

if __name__ == '__main__':
    unittest.main()
    