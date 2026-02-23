from fastapi import FastAPI, WebSocket
import asyncio
import random
import json

app = FastAPI()

@app.websocket("/ws/fleet-updates")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            # Simulate AI calculating new metrics
            data = {
                "efficiency": f"+{random.uniform(20, 25):.1f}%",
                "reroutes": random.randint(1000, 1500),
                "activeAnomalies": random.randint(1, 5),
                "newLog": {
                    "unit": f"TRK-{random.randint(100, 999)}",
                    "action": "Route optimized for fuel",
                    "delta": f"-{random.randint(2, 15)} min"
                }
            }
            await websocket.send_text(json.dumps(data))
            await asyncio.sleep(3) # Update every 3 seconds
    except Exception as e:
        print(f"Connection closed: {e}")