import asyncio
from adapters import MockEHRAdapter, MockAIAdapter

async def run_tests():
    print("--- Starting System Architecture Tests ---\n")
    
    # Initialize our adapters
    ehr_adapter = MockEHRAdapter()
    ai_adapter = MockAIAdapter()

    # TEST 1: Successful EHR Data Retrieval
    print("Test 1: Fetching valid patient data...")
    try:
        patient_data = await ehr_adapter.get_patient_data("12345")
        print(f"SUCCESS: {patient_data}\n")
    except Exception as e:
        print(f"FAILED: {e}\n")

    # TEST 2: Simulated EHR Failure (Invalid ID)
    print("Test 2: Fetching invalid patient data (Testing Error Handling)...")
    try:
        error_data = await ehr_adapter.get_patient_data("INVALID")
        print(f"SUCCESS: {error_data}\n")
    except Exception as e:
        print(f"EXPECTED ERROR CAUGHT: {e}\n")

    # TEST 3: Successful AI Note Generation
    print("Test 3: Generating AI clinical note from audio...")
    try:
        audio_stream = "Patient complains of mild headache and fatigue."
        clinical_note = await ai_adapter.generate_clinical_note(audio_stream)
        print(f"SUCCESS: {clinical_note}\n")
    except Exception as e:
        print(f"FAILED: {e}\n")

    # TEST 4: Simulated AI Failure (Empty Audio)
    print("Test 4: Generating AI note with empty audio (Testing Error Handling)...")
    try:
        empty_note = await ai_adapter.generate_clinical_note("   ")
        print(f"SUCCESS: {empty_note}\n")
    except Exception as e:
        print(f"EXPECTED ERROR CAUGHT: {e}\n")

    print("--- All Tests Completed ---")

# Run the async event loop
if __name__ == "__main__":
    asyncio.run(run_tests())
    