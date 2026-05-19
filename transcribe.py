from faster_whisper import WhisperModel
from pydub import AudioSegment
import os

model = WhisperModel("large-v3-turbo", device="cpu", compute_type="int8")

def preprocess_audio(input_path: str) -> str:
    audio = AudioSegment.from_file(input_path)
    audio = audio.set_frame_rate(16000).set_channels(1)
    output_path = input_path.rsplit('.', 1)[0] + "_processed.wav"
    audio.export(output_path, format="wav")
    return output_path

def transcribe_audio(audio_path: str):
    processed_path = preprocess_audio(audio_path)
    
    segments, info = model.transcribe(
        processed_path,
        beam_size=5,
        best_of=5,
        language=None,
        vad_filter=True,
        word_timestamps=True
    )
    
    full_text = ""
    segment_list = []
    
    for segment in segments:
        full_text += segment.text.strip() + " "
        segment_list.append({
            "start": round(segment.start, 2),
            "end": round(segment.end, 2),
            "text": segment.text.strip()
        })
    
    if os.path.exists(processed_path):
        os.remove(processed_path)
    
    return {
        "full_text": full_text.strip(),
        "language": info.language,
        "segments": segment_list
    }