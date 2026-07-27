<<<<<<< HEAD
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List

app = FastAPI()

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: dict):
        for connection in self.active_connections:
            await connection.send_json(message)

manager = ConnectionManager()

@app.websocket("/ws/alerts")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            # Keep connection alive
            await websocket.receive_text()
    except WebSocketDisconnect:
        manager.disconnect(websocket)

# Endpoint to trigger a critical alert (Simulating an Event-Driven trigger)
@app.post("/api/v1/trigger-alert")
async def trigger_alert(room: str, event: str):
    alert_payload = {
        "id": str(datetime.datetime.now().timestamp()),
        "room": room,
        "event": event,
        "time": "Just now"
    }
    await manager.broadcast(alert_payload)
    return {"status": "Alert Broadcasted"}
=======
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
    
>>>>>>> 5e9711d92bcd600b862ea549fe4be57f5f3cde16
