from fastapi import FastAPI, UploadFile, File, HTTPException
import shutil
import os
from uuid import uuid4
from transcribe import transcribe_audio

app = FastAPI(title="Volga Transcription Pipeline")

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/transcribe/")
async def transcribe(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(('.mp3', '.wav', '.m4a', '.ogg', '.webm')):
        raise HTTPException(400, "Unsupported audio format")

    task_id = str(uuid4())
    file_path = f"{UPLOAD_DIR}/{task_id}_{file.filename}"
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = transcribe_audio(file_path)
    
    return {
        "task_id": task_id,
        "status": "completed",
        "filename": file.filename,
        **result
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)