import openai
from tqdm.auto import tqdm
import io, os
from typing import List
from dotenv import load_dotenv

### LOAD ENV FOR OPENAIR API KEY
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

### TRANSCRIBE AUDIO
def transcribe_audio_chunk(audio_chunk: io.BytesIO) -> str:
    audio_chunk.seek(0)
    txt = openai.Audio.transcribe('whisper-1', audio_chunk)
    transcription = txt['text'].strip()
    return transcription

def transcribe_audio_chunks(audio_chunks: List[io.BytesIO]) -> str:
    transcriptions = []    
    for audio_chunk in tqdm(audio_chunks, desc="Transcribing audio chunks", unit="chunk"):
        transcription = transcribe_audio_chunk(audio_chunk)
        transcriptions.append(transcription)
    full_transcription = "\n".join(transcriptions)
    return full_transcription