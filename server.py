from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import asyncio

app = FastAPI()

frames = ["Frame 1 ASCII", "Frame 2 ASCII", "Frame 3 ASCII"]  # Replace with real ASCII frames

async def stream_frames():
    while True:
        for frame in frames:
            yield f"data: {frame}\n\n"
            await asyncio.sleep(0.1)

@app.get("/stream")
async def stream():
    return StreamingResponse(stream_frames(), media_type="text/event-stream")
