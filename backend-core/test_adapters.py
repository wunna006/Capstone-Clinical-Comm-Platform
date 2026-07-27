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

if __name__ == '__main__':
    unittest.main()
    