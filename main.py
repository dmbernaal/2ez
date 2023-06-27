import argparse
import os
from src.audio import url2mp4, split_audio, load_file_as_bytes, wget
from src.whisper import transcribe_audio_chunks
from src.vtt import VTT
from src.prints import Print

print = Print()

def main(args):
    if not args.local:
        print.download()
        if args.wget: file_path = wget(args.url_or_path)
        else: file_path = url2mp4(args.url_or_path)
    else: print.local(); file_path = args.url_or_path
    print.tobytes(); bytes_file = load_file_as_bytes(file_path)
    print.split(); audio_chunks = split_audio(bytes_file, input_audio_format="mp4", output_audio_format="mp3", chunk_duration=60, min_duration_for_chunking=300)
    print.transcribe(); transcription = transcribe_audio_chunks(audio_chunks)
    if args.save_vtt:
        vtt = VTT.from_transcription(transcription)
        transcription = vtt.parse()
    with open(args.output, "w") as f: print.save(); f.write(transcription)
    print.remove(); os.remove(file_path)

if __name__ == "__main__":
    argparse = argparse.ArgumentParser()
    argparse.add_argument("--url-or-path", type=str, required=True)
    argparse.add_argument("--local", default=False, type=bool, required=False)
    argparse.add_argument("--output", default="output.txt", type=str, required=True)
    argparse.add_argument("--save-vtt", default=False, type=bool, required=False)
    argparse.add_argument("--wget", default=False, type=bool, required=False)
    args = argparse.parse_args()
    main(args)