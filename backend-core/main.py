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
