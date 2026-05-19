# Volga Partners - Audio Transcription Pipeline Assessment

A clean, production-ready audio transcription service built as part of the Software Engineer Assessment.

## Features
- Supports multiple audio formats (MP3, WAV, M4A, OGG, WebM)
- Uses **Faster-Whisper** (large-v3-turbo) for fast & accurate transcription
- Returns **timestamped segments**
- Audio preprocessing (16kHz mono)
- Designed with scalability in mind (FastAPI + async ready)

## Tech Stack
- Python + FastAPI
- Faster-Whisper (large-v3-turbo)
- PyDub + FFmpeg

## How to Run
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## Design Decisions
- Chose **Faster-Whisper** for best speed/accuracy balance on CPU
- Preprocessing to 16kHz mono for optimal Whisper performance
- Modular design (easy to add Celery for background jobs)
- Clear separation of concerns

Built by **Safdar Ayub**