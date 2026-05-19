# Volga Partners - Audio Transcription Pipeline Assessment

## Overview
A clean, scalable, and production-ready audio transcription service that converts audio files into timestamped text using state-of-the-art open-source technology.

## Design Decisions & Architecture

### 1. Choice of Technology Stack
- **Faster-Whisper (large-v3-turbo)**: Selected for the best balance of **speed, accuracy, and resource efficiency** on CPU. It is significantly faster than original Whisper while maintaining high accuracy.
- **FastAPI**: Chosen for its modern async capabilities, automatic Swagger UI, and excellent performance.
- **PyDub + FFmpeg**: Used for robust audio preprocessing and format conversion.

### 2. Core Design Principles
- **Modularity**: Separated concerns (`main.py` for API, `transcribe.py` for core logic).
- **Reliability**: Automatic audio preprocessing to 16kHz mono WAV (optimal for Whisper).
- **Scalability**: Designed with background task processing (Celery) in mind for future concurrent uploads.
- **Clean Code**: Proper error handling, file cleanup, and structured output.

### 3. How the Pipeline Works
1. User uploads audio file via `/transcribe/` endpoint
2. File is saved with unique `task_id`
3. Audio is converted to 16kHz mono WAV
4. Faster-Whisper transcribes with VAD filter and word timestamps
5. Returns full text + per-segment timestamps
6. Temporary files are cleaned up

### 4. Handling Real-World Scenarios
- **Multiple Formats**: PyDub handles MP3, WAV, M4A, OGG, WebM etc.
- **Long Audio**: Ready for chunking implementation (can be added easily)
- **Concurrency**: Architecture supports Celery + Redis for background processing
- **Failure Recovery**: Designed to support retries and task status tracking

### 5. Future Improvements
- Celery + Redis for true async background processing
- Speaker Diarization
- Noise reduction
- Summarization & action items

## How to Run Locally
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

**Test Endpoint**:  
`POST http://127.0.0.1:8000/transcribe/` (multipart file upload)

Built by **Safdar Ayub** for Volga Partners Software Engineer Assessment