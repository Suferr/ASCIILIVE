from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import asyncio

app = FastAPI()

frames = [
    "Frame 1 ASCII Art",
    "Frame 2 ASCII Art",
    "Frame 3 ASCII Art"
]  # Replace with actual ASCII animation frames

async def stream_frames():
    while True:
        for frame in frames:
            yield f"data: {frame}\n\n"
            await asyncio.sleep(0.1)  # Adjust frame speed

@app.get("/stream")
async def stream():
    return StreamingResponse(stream_frames(), media_type="text/event-stream")
